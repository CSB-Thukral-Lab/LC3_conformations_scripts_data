import pandas as pd 
import numpy as np
import scipy.special
import sys
import os
from itertools import combinations
import tqdm

#FUNCTION

def std_scaler(y,y_val):
    mean=np.mean(y)
    std_=np.std(y)
    return((y_val)/(std_))

def manhattan_dist_1d(p1,p2):
    manhattan_dist=abs(p1-p2)
    return(manhattan_dist)

def chebyshev_dist(p1,p2):
    return(max(np.abs(p1[0]-p2[0]),np.abs(p1[1]-p2[1])))

def digamma_func(z):
    digamma_value = scipy.special.digamma(z)
    return(digamma_value)

def MI_CC(RES1,RES2,df_name):
    '''
    Mutual Information between two continuous variables 
    calculated based on Kraskov et al., 2004 [1]
    
    [1] Kraskov, A., Stögbauer, H., &amp; Grassberger, P. (2004).
    Estimating mutual information. Physical Review E, 69(6). https://doi.org/10.1103/physreve.69.066138 
    
    PARAMETERS TO PASS
    ------------------
    RES1: Eg., LYS51
    RES2: Eg., PHE52
    df_name: DataFrame of the chi1 angles of residues across time frames
    
    RETURNS
    -------
    MI between two continuous variable
    
    NOTE: This function should not be used to calculate two sets of 
    discrete variables or one set of discrete and another set of continuous 
    variable
    '''
    R1=df_name['%s'%RES1].to_list()
    R2=df_name['%s'%RES2].to_list()
    N=len(R1)
    k=3
    
    x_scaled=[]
    y_scaled=[]
    
    for i in R1:
        x_scaled.append(std_scaler(R1,i))
        
    for i in R2:
        y_scaled.append(std_scaler(R2,i))
    
    x_scaled=np.array(x_scaled)
    y_scaled=np.array(y_scaled)
    
    rng = np.random.default_rng(seed=1)
    y_scaled += (
            1e-10
            * np.maximum(1, np.mean(np.abs(y_scaled)))
            * rng.standard_normal(size=len(y_scaled))
        )
    
    x_scaled += (
            1e-10
            * np.maximum(1, np.mean(np.abs(x_scaled)))
            * rng.standard_normal(size=len(x_scaled))
        )
        
    xy=[]
    for i,j in zip(x_scaled,y_scaled):
        xy.append([i,j])
    
    K3_radius=[]
    for i in xy:
        ref_point=i
        radius=[]
        for j in xy:
            if j!=ref_point:
                radius.append(chebyshev_dist(ref_point,j))
        radius.sort()
        K3_radius.append(radius[2])
    
    x_point_radius=[]
    y_point_radius=[]
    for i,j in zip(xy,K3_radius):
        x_point_radius.append([i[0],j])
        y_point_radius.append([i[1],j])
    
    # Find nxi
    nx_i_ls=[]
    for i in x_point_radius:
        val=i[0]
        dist=i[1]
        nx_i=0
        for j in x_point_radius:
            if j[0]!=val:
                if manhattan_dist_1d(val,j[0])<dist:
                    nx_i=nx_i+1

        nx_i_ls.append(nx_i)
    
    # Find nyi
    ny_i_ls=[]
    for i in y_point_radius:
        val=i[0]
        dist=i[1]
        ny_i=0
        for j in y_point_radius:
            if j[0]!=val:
                if manhattan_dist_1d(val,j[0])<dist:
                    ny_i=ny_i+1

        ny_i_ls.append(ny_i)
    
    nx_i_ls=np.array(nx_i_ls)
    ny_i_ls=np.array(ny_i_ls)
    
    mi = (digamma_func(N)+ digamma_func(k)- np.mean(digamma_func(nx_i_ls + 1))- np.mean(digamma_func(ny_i_ls + 1)))
    
    if mi<0:
        return 0
    else:
        return mi

#code begins
fin_df_r1_360=pd.read_csv('%s'%sys.argv[1],index_col=0)
file_name=sys.argv[1].split('.')[0]

def rSubset(arr, r):
    return list(combinations(arr, r))

arr = fin_df_r1_360.columns
r = 2
comb=rSubset(arr, r)

df_cols=[i for i in fin_df_r1_360.columns]
mi_chi1= np.zeros((fin_df_r1_360.shape[1],fin_df_r1_360.shape[1]))

for i in tqdm.tqdm(comb):
    r1=i[0]
    r2=i[1]
    mi=MI_CC(r1,r2,fin_df_r1_360)
    mi_chi1[df_cols.index('%s'%i[0]),df_cols.index('%s'%i[1])]=mi
    mi_chi1[df_cols.index('%s'%i[1]),df_cols.index('%s'%i[0])]=mi

mi_chi1_norm=mi_chi1/np.max(mi_chi1)

mi_chi1_DF=pd.DataFrame(mi_chi1)
mi_chi1_DF.to_csv('%s_MI_MATRIX.csv'%file_name)

mi_chi1_DF_normalised=pd.DataFrame(mi_chi1_norm)
mi_chi1_DF_normalised.to_csv('%s_MI_MATRIX_NORMALISED.csv'%file_name)
