% Define the logistic function
function yhat = logistic_func(params, X)
    bayta1 = params(1);
    bayta2 = params(2);
    bayta3 = params(3);
    bayta4 = params(4);
    
    logisticPart = 1 + exp(-(X - bayta3) ./ abs(bayta4));
    yhat = bayta2 + (bayta1 - bayta2) ./ logisticPart;
end
