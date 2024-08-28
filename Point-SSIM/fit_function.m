% Define the fitting function
function [popt, y_output_logistic] = fit_function(y_label, y_output)
    % Initial parameters
    beta0 = [max(y_label), min(y_label), mean(y_output), 0.5];
    
    % Define the function to fit
    fit_func = @(params, X) logistic_func(params, X);
    
    % Use lsqcurvefit to perform the fitting
    options = optimoptions('lsqcurvefit', 'Display', 'off');
    [popt, ~] = lsqcurvefit(fit_func, beta0, y_output, y_label, [], [], options);
    
    % Predict using the fitted parameters
    y_output_logistic = logistic_func(popt, y_output);
end