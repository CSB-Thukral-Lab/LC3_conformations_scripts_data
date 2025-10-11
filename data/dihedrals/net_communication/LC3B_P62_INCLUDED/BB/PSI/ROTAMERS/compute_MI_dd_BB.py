import numpy as np
import pandas as pd
import os
import tqdm
import sys
from itertools import combinations

LC3B_rotameric_states=pd.read_csv('%s'%sys.argv[1],index_col=0)

def rSubset(arr, r):
    return list(combinations(arr, r))


def MI_dd(x,y):
    N=len(x)
    discrete_states=[0,1]
    r = 2
    comb=rSubset(discrete_states, r)
    comb_re=[]
    for i in comb:
        comb_re.append((i[1],i[0]))
    add_on=[(0,0),(1,1)]
    comb=comb+add_on+comb_re

    MI_UV=0
    for i in comb:
        U_i=0
        U_j=0
        R_i_R_j=0
        for xi,yi in zip(x,y):
            if xi==i[0]:
                U_i=U_i+1
            if yi==i[1]:
                U_j=U_j+1
            if xi==i[0] and yi==i[1]:
                R_i_R_j=R_i_R_j+1
        p_ij=R_i_R_j/N
        pi=U_i/N
        pj=U_j/N
        if pi==0 or pj ==0:
            mi_i_j=0
        else:
    #     mi_i_j=(R_i_R_j/N)*np.log((N*(R_i_R_j))/U_i*U_j)
            mi_i_j=p_ij*np.log(p_ij/(pi*pj))

            if str(mi_i_j)=='nan':
                mi_i_j=0
            else:
                mi_i_j=mi_i_j
    #     print(mi_i_j)
        MI_UV=MI_UV+mi_i_j
        
    return(MI_UV)



arr = LC3B_rotameric_states.columns
r = 2
comb=rSubset(arr, r)
df_cols=[i for i in LC3B_rotameric_states.columns]
mi_chi1= np.zeros((LC3B_rotameric_states.shape[1],LC3B_rotameric_states.shape[1]))

for i in tqdm.tqdm(comb):
    r1=LC3B_rotameric_states[i[0]].to_list()
    r2=LC3B_rotameric_states[i[1]].to_list()
    mi=MI_dd(r1,r2)
    mi_chi1[df_cols.index('%s'%i[0]),df_cols.index('%s'%i[1])]=mi
    mi_chi1[df_cols.index('%s'%i[1]),df_cols.index('%s'%i[0])]=mi


mi_chi1_DF_LC3B_II_norm=mi_chi1/np.max(mi_chi1)

mi_chi1_df=pd.DataFrame(mi_chi1)
mi_chi1_DF_LC3B_II_norm_df=pd.DataFrame(mi_chi1_DF_LC3B_II_norm)

mi_chi1_df.to_csv('%s_MI_rotameric_states.csv'%sys.argv[2])
mi_chi1_DF_LC3B_II_norm_df.to_csv('%s_MI_rotameric_states_normalised.csv'%sys.argv[2])