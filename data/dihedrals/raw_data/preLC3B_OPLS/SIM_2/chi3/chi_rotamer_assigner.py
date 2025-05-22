import pandas as pd
import os
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np
import sys

def rotamer_state(chi_angle):
    '''
    returns the rotameric state for the chi
    if 0 ---> gauche-
    if 1 ---> trans
    if 2 ---> gauche+
    else ---> reassigns to any one of the above core states
    '''
    hard_boundaries = [0, 120, 240, 360]

    if chi_angle >= 15 and chi_angle < 106:
        return(0)
    elif chi_angle >= 135 and chi_angle < 226:
        return(1)
    elif chi_angle >= 255 and chi_angle < 346:
        return(2)
    else:
        return(np.digitize(chi_angle,hard_boundaries)-1)

fin_df_r1_360=pd.read_csv('%s'%sys.argv[1],index_col=0)
rotameric_states=pd.DataFrame()

for i in fin_df_r1_360.columns:
    chi1_ls=fin_df_r1_360[i].to_list()
    rotamer_state_ls=[]
    for j in chi1_ls:
        rotamer_state_ls.append(rotamer_state(j))
    rotameric_states[i]=rotamer_state_ls

rotameric_states.to_csv('%s'%sys.argv[2])