% %clear;
% fid = fopen('listwise_test_10level.txt');
% data = textscan(fid,'%s %f %s','Delimiter',' ');
% MOS = importdata('test_pmos.txt');
% size = length(MOS);
% t=0;
% result=zeros(size,1);
% for i=1:size
%     disp([num2str(i), '/5520'])
%     if mod(i,11)==1
%         t=t+1;
%         model = data{1,1}{i,1};
%         result(t)=0;
%     else
%         t=t+1;
%         model1 = data{1,1}{i,1};
%         A=pcread(model);
%         B=pcread(model1);
%         A.Normal=pcnormals(A);
%         B.Normal=pcnormals(B);
%         [asBA, asAB, asSym] = point_to_plane(A, B, 'max');
%         result(t)=asSym;
%     end 
% end



[srocc3,krocc3,plcc3,rmse3,or3] = verify_performance(MOS,result);
