clear;
fid = fopen('listwise_test_10level.txt');
fout = fopen('test_pmos.txt', 'wt');
temp = [];
cnt = 0;
while ~feof(fid)
    disp([num2str(cnt), '/4200'])
    str = string(fgetl(fid));
    S = regexp(str,  ' ', 'split');
    str = S(1);
    temp = [temp; str];
    if mod(cnt, 11) == 0
        fprintf(fout, "1\n");
        pc_or = pcread(str);
        pc_or.Normal = pcnormals(pc_or);
    else
        pc_dvg = pcread(str);
        pc_dvg.Normal = pcnormals(pc_dvg);
        pmos = angularSimilarity(pc_dvg, pc_or,'mse');
        fprintf(fout, "%f\n", pmos);
        % fprintf(fout, '\n');
    end

    cnt = cnt + 1;
    
end
fclose(fid);
fclose(fout);