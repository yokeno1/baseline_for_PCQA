import open3d as o3d
import numpy as np
import os
from PLCC import *
import xlrd
from tqdm import tqdm
def pc_normalize(pc):
    l = pc.shape[0]
    centroid = np.mean(pc, axis=0)
    pc = pc - centroid
    m = np.max(np.sqrt(np.sum(pc**2, axis=1)))
    pc = pc / m
    return pc


def d_rms(src,tar):
    # Calculates the one way matching distortion from src -> target
    # building kdtree
    tar_pc = o3d.geometry.PointCloud()
    tar_pc.points = o3d.utility.Vector3dVector(tar)
    kdtree = o3d.geometry.KDTreeFlann(tar_pc)
    # matching points and caculate distance    
    point_size_src = src.shape[0]
    distance_list = np.zeros(point_size_src)
    for i in range(point_size_src):
        [_,idx,dis] = kdtree.search_knn_vector_3d(src[i],1)
        distance_list[i] = dis[0] # get the square of the closest point's distance
    return (distance_list.sum()/point_size_src)**0.5

def d_hausdorf(src,tar):
    # Calculates the one way matching distortion from src -> target
    # building kdtree
    tar_pc = o3d.geometry.PointCloud()
    tar_pc.points = o3d.utility.Vector3dVector(tar)
    kdtree = o3d.geometry.KDTreeFlann(tar_pc)
    # matching points and caculate distance    
    point_size_src = src.shape[0]
    distance_list = np.zeros(point_size_src)
    for i in range(point_size_src):
        [_,idx,dis] = kdtree.search_knn_vector_3d(src[i],1)
        distance_list[i] = dis[0] # get the square of the closest point's distance
    return np.max(distance_list)**0.5

def d_symmetric_rms(pc1,pc2,mode = 'max'):
    # p2point see Evaluation criteria for PCC (Point Cloud Compression)
    if mode == 'max':
        return max(d_rms(pc1,pc2),d_rms(pc2,pc1))
    else:
    # see See `"Dynaamic Polygon Clouds: Representation and Compression for VR/AR" <https://arxiv.org/abs/1610.00402>` pper.
        return (d_rms(pc1,pc2)+d_rms(pc2,pc1))/2 

def d_symmetric_hausdorf(pc1,pc2):
    # haudorf p2point see Evaluation criteria for PCC (Point Cloud Compression)
    return max(d_hausdorf(pc1,pc2),d_hausdorf(pc2,pc1))

# MSE P2POINT
def p2point(ref_name,dis_name):
    ref = o3d.io.read_point_cloud(ref_name)
    dis = o3d.io.read_point_cloud(dis_name)
    ref_points = pc_normalize(np.array(ref.points))
    dis_points = pc_normalize(np.array(dis.points))
    return d_symmetric_rms(ref_points,dis_points)

# HAUSDORF P2POINT
def p2point_hausdorf(ref_name,dis_name):
    ref = o3d.io.read_point_cloud(ref_name)
    dis = o3d.io.read_point_cloud(dis_name)
    ref_points = pc_normalize(np.array(ref.points))
    dis_points = pc_normalize(np.array(dis.points))
    return d_symmetric_hausdorf(ref_points,dis_points)

if __name__ == '__main__':

    # data_path = 'D:\PCQA\CL\data\SJTU-PCQA\data'
    # models = os.listdir(data_path)
    # types = ['Octree','ColorNoise','Downsample','Downsample+ColorNoise','Downsample+GaussNoise','GaussNoise','ColorNoise+GaussNoise']
    # levels = ['level1','level2','level3','level4','level5','level6']
    # mos1 = []
    # mos2 = []
    # pbar = tqdm(total=len(models) * len(types) * len(levels))
    # for model in models:
    #     ref_path = data_path + '/' + model + '/' + model + '.ply'
    #     for typ in types:
    #         for level in levels:
    #             pbar.update()
    #             dis_path = data_path + '/' + model + '/' + typ + '/' + level + '.ply'
    #             score1 = p2point(ref_path,dis_path)
    #             score2 = p2point_hausdorf(ref_path,dis_path)
    #             mos1.append(score1)
    #             mos2.append(score2)
    #
    # with open('./result/p2po_mos1.txt', 'w') as f:
    #     f.write(str(mos1))
    # with open('./result/p2po_mos2.txt', 'w') as f:
    #     f.write(str(mos2))

    # with open('./result/p2po_mos1.txt','r') as f:
    #     mos1 = f.read()
    # mos1_list = mos1.split(',')
    # mos1 = np.array(mos1_list,dtype=float)
    # # print(mos1.shape)
    # with open('./result/p2po_mos2.txt', 'r') as f:
    #     mos2 = f.read()
    # mos2_list = mos2.split(',')
    # mos2 = np.array(mos2_list, dtype=float)
    # mos_book = xlrd.open_workbook('D:\PCQA\CL\data\SJTU-PCQA\MOS.xlsx')
    # mos_book = mos_book.sheet_by_index(0)
    # mos = []
    # for i in range(9):
    #     mos.append(mos_book.col_values(i))
    #
    # mos = np.array(mos, dtype=float)
    # mos = mos.reshape(-1,1).squeeze(1)
    # # print(mos)
    #
    # predict_mos = np.array(mos1, dtype=float)
    # PLCC, SRCC, KRCC, RMSE = corr_value(mos, predict_mos, True)
    # print('PLCC: {:4f}, SRCC: {:4f}, KRCC: {:4f}, RMSE: {:4f}\n'.format(PLCC, SRCC, KRCC, RMSE))
    #
    #
    # predict_mos = np.array(mos2, dtype=float)
    # PLCC, SRCC, KRCC, RMSE = corr_value(mos, predict_mos, True)
    # print('PLCC: {:4f}, SRCC: {:4f}, KRCC: {:4f}, RMSE: {:4f}\n'.format(PLCC, SRCC, KRCC, RMSE))

#PLCC: 0.775843, SRCC: 0.715329, KRCC: 0.536786, RMSE: 5.599031

# PLCC: 0.700806, SRCC: 0.671430, KRCC: 0.495518, RMSE: 5.527702

    data_path = 'D:\PCQA\data\sjtu-database\data'
    ref_path = r'D:\PCQA\data\sjtu-database\reference'
    models = os.listdir(data_path)
    mos1 = []
    mos2 = []
    pbar = tqdm(total=len(models) * 42)
    for model in models:
        ref_model = ref_path + '/' + model + '.ply'
        for i in range(42):
                pbar.update()
                dis_path = data_path + '/' + model + '/' + model + '_%d.ply' %i
                score1 = p2point(ref_model,dis_path)
                score2 = p2point_hausdorf(ref_model,dis_path)
                mos1.append(score1)
                mos2.append(score2)

    with open('./p2po_mos1.txt', 'w') as f:
        f.write(str(mos1))
    with open('./p2po_mos2.txt', 'w') as f:
        f.write(str(mos2))
