import os
os.environ["KMP_DUPLICATE_LIB_OK"] = "TRUE"
import numpy as np
from scipy import stats,optimize
from scipy.optimize import curve_fit



def func_for_nlinfit(x,bayta1,bayta2,bayta3,bayta4,bayta5):   # 非线性拟合函数
    """
    \
    :param x: 自变量
    :param bayta: 待拟合参数
    :return:  因变量
    """
    logisticPart = 0.5 - 1.0/(1 + np.exp(bayta2 * (x - bayta3)))
    yhat = bayta1 * logisticPart + bayta4 * x + bayta5
    return yhat

def f_err(p, y, x):
    return (y - func_for_nlinfit(x, *p)) * (y - func_for_nlinfit(x, *p))

# def nlinfit(mos,predict_mos):
#     beta1 = 10
#     beta2= 0
#     beta3 = np.mean(predict_mos)
#     beta4= 0.1
#     beta5= 0.1
#     beta =np.array([beta1,beta2,beta3,beta4,beta5],dtype=float)
#     c=optimize.leastsq(f_err,beta,args=(mos,predict_mos),maxfev=1000000)    # c包含系数与一个判别值，判别值在1-4代表求解成功，例如(array([ 1.45249006e+03,  1.18588625e-02, -4.76070521e+01, -3.29286136e+00,-1.98160616e+02]), 1)
#     return c
#
# def nlinfit2(mos,predict_mos):
#     p_est, err_est = optimize.curve_fit(func_for_nlinfit, predict_mos,mos)
#     return p_est

def logistic_func(X, bayta1, bayta2, bayta3, bayta4):
    logisticPart = 1 + np.exp(np.negative(np.divide(X - bayta3, np.abs(bayta4))))
    yhat = bayta2 + np.divide(bayta1 - bayta2, logisticPart)
    return yhat


def fit_function(y_label, y_output):
    beta = [np.max(y_label), np.min(y_label), np.mean(y_output), 0.5]
    popt, _ = curve_fit(logistic_func, y_output, \
                        y_label, p0=beta, maxfev=100000000)
    y_output_logistic = logistic_func(y_output, *popt)

    return y_output_logistic

def corr_value(mos,predict_mos,fit_flag=True):
    if fit_flag:
        # c = nlinfit(mos,predict_mos)
        # yhat = func_for_nlinfit(predict_mos,*c[0])
        yhat= fit_function(mos,predict_mos)
        PLCC,l1=stats.pearsonr(mos,yhat)
        SROCC,l1 = stats.spearmanr(mos,predict_mos)
        KROCC,l2 = stats.kendalltau(mos,predict_mos)
        RMSE = np.sqrt(np.sum((yhat-predict_mos)**2)/len(mos))

    else:
        PLCC, l1 = stats.pearsonr(mos, predict_mos)
        SROCC, l1 = stats.spearmanr(mos, predict_mos)
        KROCC, l2 = stats.kendalltau(mos, predict_mos)
        RMSE = np.sqrt(np.sum((mos - predict_mos) ** 2)/len(mos))
    return abs(PLCC),abs(SROCC),abs(KROCC),RMSE