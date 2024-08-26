%clear;

MOS = importdata('test_pmos.txt');
size = length(MOS);
originalArray = MOS;

    % 获取原始数组的长度  
    lengthOriginal = length(originalArray);  
      
    % 创建一个逻辑索引数组，初始化为true（保留所有元素）  
    logicalIdx = true(1, lengthOriginal);  
      
    % 计算需要删除的元素数量（每隔11个）  
    numToDelete = floor(lengthOriginal / 11);  
      
    % 每隔11个元素，将对应的逻辑索引设置为false（删除该元素）  
    % 但不要超出numToDelete的范围  
    for i = 1:numToDelete  
        idxToDelete = (i-1)*11 + 1; % 计算要删除的元素的索引  
        if idxToDelete <= lengthOriginal  
            logicalIdx(idxToDelete) = false;  
        end  
    end  
      
    % 使用逻辑索引数组来过滤原始数组  
    newArray = originalArray(logicalIdx);  

MOS = newArray;
% pcqm = POINTSSIM;
pcqm = pcqm * 10^15;
[srocc3,krocc3,plcc3,rmse3,or3] = verify_performance(MOS,pcqm);



F = @(P,x) P(1).*(1/2 - 1./(1+exp(P(2).*(x-P(3)))))+P(4).*x+P(5);
% 因为使用数值解法，需要给系数的初始值（根据参数的意义设，或者随意），matlab会从初始值开始寻找局部最优解。
p0 = [1,10,0.0001,5,0];

% 然后使用lsqcurvefit函数进行拟合，将拟合得到的系数存在p中，元素排列顺序跟前面定义函数的时候是相同的
% [p,resnorm,~,exitflag,output] = lsqcurvefit(F,p0,PredictMos1,GroundTruth);
% % 首先根据拟合后的参数获得函数值
% PredictMos1=F(p,PredictM os1);
% % 绘制拟合数据的折线图
% plot(PredictMos1,GroundTruth,'o')
% [srocc,krocc,plcc,rmse,or] = verify_performance(GroundTruth,PredictMos1);


[p,resnorm,~,exitflag,output] = lsqcurvefit(F,p0,pcqm,MOS);
PredictMos2=F(p,pcqm);
plot(PredictMos2,MOS,'o')
[srocc,krocc,plcc,rmse,or] = verify_performance(MOS,PredictMos2);
