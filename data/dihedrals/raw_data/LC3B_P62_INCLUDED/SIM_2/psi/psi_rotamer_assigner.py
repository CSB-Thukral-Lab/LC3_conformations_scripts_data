import pandas as pd
import os
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np
import sys

def rotamer_state(psi_angle):
    hard_boundaries=[0,160,360]
    '''
    returns the rotameric state for the chi
    if 0 ---> cis
    if 1 ---> trans
    if 2 ---> transitioning b/w two rotamer
    '''
    
    if psi_angle >= 15 and psi_angle < 146:
        return(0)
    elif psi_angle >= 175 and psi_angle < 346:
        return(1)
    else:
        return(np.digitize(psi_angle,hard_boundaries)-1)


fin_df_r1_360=pd.read_csv('%s'%sys.argv[1],index_col=0)
rotameric_states=pd.DataFrame()

for i in fin_df_r1_360.columns:
    chi1_ls=fin_df_r1_360[i].to_list()
    rotamer_state_ls=[]
    for j in chi1_ls:
        rotamer_state_ls.append(rotamer_state(j))
    rotameric_states[i]=rotamer_state_ls

rotameric_states.to_csv('%s'%sys.argv[2])