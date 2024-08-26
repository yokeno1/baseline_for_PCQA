clear;
stimuli_path='D:\PCQA\data\sjtu-database\data';
refer_path='D:\PCQA\data\sjtu-database\reference';
% model=[];
% types = ['Octree','ColorNoise','Downsample','Downsample+ColorNoise','Downsample+GaussNoise','GaussNoise','ColorNoise+GaussNoise'];
% levels = ['level1','level2','level3','level4','level5','level6'];
model = {'redandblack','UBL_unicorn','loot','soldier','Romanoillamp','longdress','statue','shiva','hhi'};
% MOS=mean(subjdesktopdsis,2);
t=0;
result=zeros(378);
for i=1:length(model)
    ref_model = fullfile(refer_path,model{i});
    ref_model = strcat(ref_model, '.ply');
    dis_model_path = fullfile(stimuli_path,model{i});
    dis_models = dir(fullfile(dis_model_path,'*.ply'));
    for j=1:length(dis_models)
        disp(['model:',num2str(i),' num: ',num2str(j)])
        t=t+1;
        dis_model = fullfile(dis_model_path,strcat(model{i},'_',num2str(j-1),'.ply'));
   
        A=pcread(ref_model);
        B=pcread(dis_model);
        A.Normal=pcnormals(A);
        B.Normal=pcnormals(B);

        [asBA, asAB, asSym] = point_to_point(A, B, 'mse');
        result(t)=asSym;
    end
end


[srocc,krocc,plcc,rmse,or] = verify_performance(MOS,result);
