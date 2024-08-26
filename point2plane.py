
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

def estimate_normal(pcd):
    # estimate normals if point cloud does not have normals
    pcd.estimate_normals(
        search_param=o3d.geometry.KDTreeSearchParamHybrid(radius=10000, max_nn=30))
    normals = np.asarray(pcd.normals)
    return normals

def match_point_compute_error(src,tar,normals):
    # Calculates the one way matching distortion from src -> target
    # building kdtree
    tar_pc = o3d.geometry.PointCloud()
    tar_pc.points = o3d.utility.Vector3dVector(tar)
    kdtree = o3d.geometry.KDTreeFlann(tar_pc)
    # matching points
    point_size_src = src.shape[0]
    error_list = np.zeros(point_size_src)
    for i in range(point_size_src):
        [_,idx,dis] = kdtree.search_knn_vector_3d(src[i],1)
        normal = normals[i] # get the src normal
        error_vector = tar[idx[0]] - src[i] # compute the error vector
        error_list[i] = (np.dot(normal,error_vector))**2 # get the square of vector projection
    return error_list.sum()/point_size_src

def match_point_compute_error_hausdorf(src,tar,normals):
    # Calculates the one way matching distortion from src -> target
    # building kdtree
    tar_pc = o3d.geometry.PointCloud()
    tar_pc.points = o3d.utility.Vector3dVector(tar)
    kdtree = o3d.geometry.KDTreeFlann(tar_pc)
    # matching points
    point_size_src = src.shape[0]
    error_list = np.zeros(point_size_src)
    for i in range(point_size_src):
        [_,idx,dis] = kdtree.search_knn_vector_3d(src[i],1)
        normal = normals[i] # get the src normal
        error_vector = tar[idx[0]] - src[i] # compute the error vector
        error_list[i] = (np.dot(normal,error_vector))**2 # get the square of vector projection
    return np.max(error_list)**0.5


#MSE P2PLANE
def p2plane(ref_name,dis_name, no_normals = 'True'):
    ref = o3d.io.read_point_cloud(ref_name)
    dis = o3d.io.read_point_cloud(dis_name)
    if no_normals:
        ref_normals = estimate_normal(ref)
    else:
        ref_normals = np.array(ref.normals)
    ref_points = pc_normalize(np.array(ref.points))
    dis_points = pc_normalize(np.array(dis.points))
    return match_point_compute_error(ref_points,dis_points,ref_normals)

#HAUSDORF P2PLANE
def p2plane_hausdorf(ref_name,dis_name, no_normals = 'True'):
    ref = o3d.io.read_point_cloud(ref_name)
    dis = o3d.io.read_point_cloud(dis_name)
    if no_normals:
        ref_normals = estimate_normal(ref)
    else:
        ref_normals = np.array(ref.normals)
    ref_points = pc_normalize(np.array(ref.points))
    dis_points = pc_normalize(np.array(dis.points))
    return match_point_compute_error_hausdorf(ref_points,dis_points,ref_normals)\
#

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
    #             score1 = p2plane(ref_path,dis_path)
    #             score2 = p2plane_hausdorf(ref_path,dis_path)
    #             mos1.append(score1)
    #             mos2.append(score2)
    #
    # with open('mos1.txt', 'w') as f:
    #     f.write(str(mos1))
    # with open('mos2.txt', 'w') as f:
    #     f.write(str(mos2))

    with open('mos1.txt', 'r') as f:
        mos1 = f.read()
    mos1_list = mos1.split(',')
    mos1 = np.array(mos1_list, dtype=float)
    # print(mos1.shape)
    with open('mos2.txt', 'r') as f:
        mos2 = f.read()
    mos2_list = mos2.split(',')
    mos2 = np.array(mos2_list, dtype=float)
    mos_book = xlrd.open_workbook('D:\PCQA\CL\data\SJTU-PCQA\MOS.xlsx')
    mos_book = mos_book.sheet_by_index(0)
    mos = []
    for i in range(9):
        mos.append(mos_book.col_values(i))

    mos = np.array(mos, dtype=float)
    mos = mos.reshape(-1, 1).squeeze(1)

    predict_mos = np.array(mos1, dtype=float)
    PLCC, SRCC, KRCC, RMSE = corr_value(mos, predict_mos, True)
    print('PLCC: {:4f}, SRCC: {:4f}, KRCC: {:4f}, RMSE: {:4f}\n'.format(PLCC, SRCC, KRCC, RMSE))

    predict_mos = np.array(mos2, dtype=float)
    PLCC, SRCC, KRCC, RMSE = corr_value(mos, predict_mos, True)
    print('PLCC: {:4f}, SRCC: {:4f}, KRCC: {:4f}, RMSE: {:4f}\n'.format(PLCC, SRCC, KRCC, RMSE))
