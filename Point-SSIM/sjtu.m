clear all;
close all;
clc;

load('Final_MOS.mat')
%% Configurations
PARAMS.ATTRIBUTES.GEOM = false;
PARAMS.ATTRIBUTES.NORM = true;
PARAMS.ATTRIBUTES.CURV = true;
PARAMS.ATTRIBUTES.COLOR = true;

PARAMS.ESTIMATOR_TYPE = {'VAR', 'Mean'};
PARAMS.POOLING_TYPE = {'Mean'};
PARAMS.NEIGHBORHOOD_SIZE = 12;
PARAMS.CONST = eps(1);
PARAMS.REF = 0;

FITTING.SEARCH_METHOD = 'rs';
if strcmp(FITTING.SEARCH_METHOD, 'rs')
    ratio = 0.01;
elseif strcmp(FITTING.SEARCH_METHOD, 'knn')
    knn = 12;
end
FITTING.SEARCH_SIZE = [];

QUANT.VOXELIZATION = false;
QUANT.TARGET_BIT_DEPTH = 9;


%% Load point clouds
stimuli_path='D:\PCQA\data\sjtu-database\data';
refer_path='D:\PCQA\data\sjtu-database\reference';
% model = {'redandblack','ULB Unicorn','loot','soldier','Romanoillamp','longdress','statue','shiva','hhi'};
model = {'hhi'};
t=0;
result=zeros(378,1);
for i=1:9
    ref_model = fullfile(refer_path,model{i});
    ref_model = strcat(ref_model, '.ply');
    dis_model_path = fullfile(stimuli_path,model{i});
    dis_models = dir(fullfile(dis_model_path,'*.ply'));
    for j=1:length(dis_models)
        t=t+1;
        dis_model = fullfile(dis_model_path,strcat(model{i},'_',num2str(j-1),'.ply'));
        disp(['ref_model:',ref_model,' dis_model: ',dis_model])

        A = pcread(ref_model);
        B = pcread(dis_model);


        %% Sort geometry
        [geomA, idA] = sortrows(A.Location);
        if ~isempty(A.Color)
            colorA = A.Color(idA, :);
            A = pointCloud(geomA, 'Color', colorA);
        else
            A = pointCloud(geomA);
        end
        
        [geomB, idB] = sortrows(B.Location);
        if ~isempty(B.Color)
            colorB = B.Color(idB, :);
            B = pointCloud(geomB, 'Color', colorB);
        else
            B = pointCloud(geomB);
        end
        
        
        %% Point fusion
        A = pc_fuse_points(A);
        B = pc_fuse_points(B);
        
        
        %% Voxelization
        if QUANT.VOXELIZATION
            A = pc_vox_scale(A, [], QUANT.TARGET_BIT_DEPTH);
            B = pc_vox_scale(B, [], QUANT.TARGET_BIT_DEPTH);
        end
        
        
        %% Normals and curvatures estimation
        if PARAMS.ATTRIBUTES.NORM || PARAMS.ATTRIBUTES.CURV
            if strcmp(FITTING.SEARCH_METHOD, 'rs')
                FITTING.SEARCH_SIZE = round(ratio * double(max(max(A.Location) - min(A.Location))));
            else
                FITTING.SEARCH_SIZE = knn;
            end
            [normA, curvA] = pc_estimate_norm_curv_qfit(A, FITTING.SEARCH_METHOD, FITTING.SEARCH_SIZE);
            [normB, curvB] = pc_estimate_norm_curv_qfit(B, FITTING.SEARCH_METHOD, FITTING.SEARCH_SIZE);
        end
        
        
        %% Set custom structs with required fields
        sA.geom = A.Location;
        sB.geom = B.Location;
        if PARAMS.ATTRIBUTES.NORM
            sA.norm = normA;
            sB.norm = normB; 
        end
        if PARAMS.ATTRIBUTES.CURV
            sA.curv = curvA;
            sB.curv = curvB;
        end
        if PARAMS.ATTRIBUTES.COLOR
            sA.color = A.Color;
            sB.color = B.Color;
        end
        
        
        %% Compute structural similarity scores
        [pssim] = pointssim(sA, sB, PARAMS);
        result(t)=asSym;
    end
end
MOS = Final_MOS(:);

result1 =result(:);


[popt, PredictMos2]= fit_function(MOS,result);
plot(PredictMos2,MOS,'o')
[srocc,krocc,plcc,rmse,or] = verify_performance(MOS,PredictMos2);
