#MI_net_SC.py DIHEDRAL_MI.csv ROTAMER_MI.csv ORDERNESS_MI.csv output_net_mi_mat_SC.csv
import numpy as np
import pandas as pd
import MDAnalysis
import seaborn as sns
import matplotlib.pyplot as plt
import tqdm
import sys

LC3BII_chi1_MI=pd.read_csv('%s'%sys.argv[1],
                          index_col=0)


in_pick=[38,72,74,80,101,107,112]
in_pick_added=[]
counter=0
for i in in_pick:
    counter=counter+1
    in_pick_added.append(i+counter)

col_val=[0 for i in range(len(LC3BII_chi1_MI))]
resid_=[40, 75, 78, 85, 107, 114, 120]
for i,j in zip(in_pick_added,resid_):
    LC3BII_chi1_MI.insert(loc=i, column='res%d'%j, value=col_val)

LC3BII_chi1_MI=LC3BII_chi1_MI.transpose()

#ROTAMER
col_val=[0 for i in range(len(LC3BII_chi1_MI))]
resid_=[40, 75, 78, 85, 107, 114, 120]
for i,j in zip(in_pick_added,resid_):
    LC3BII_chi1_MI.insert(loc=i, column='res%d'%j, value=col_val)
LC3BII_chi1_rotamer_MI=pd.read_csv('%s'%sys.argv[2],
                          index_col=0)
in_pick=[38,72,74,80,101,107,112]
in_pick_added=[]
counter=0
for i in in_pick:
    counter=counter+1
    in_pick_added.append(i+counter)

col_val=[0 for i in range(len(LC3BII_chi1_rotamer_MI))]
resid_=[40, 75, 78, 85, 107, 114, 120]
for i,j in zip(in_pick_added,resid_):
    LC3BII_chi1_rotamer_MI.insert(loc=i, column='res%d'%j, value=col_val)

LC3BII_chi1_rotamer_MI=LC3BII_chi1_rotamer_MI.transpose()

col_val=[0 for i in range(len(LC3BII_chi1_rotamer_MI))]
resid_=[40, 75, 78, 85, 107, 114, 120]
for i,j in zip(in_pick_added,resid_):
    LC3BII_chi1_rotamer_MI.insert(loc=i, column='res%d'%j, value=col_val)

#ORDERNESS
LC3BII_chi1_ORDERNESS_MI=pd.read_csv('%s'%sys.argv[3],
                          index_col=0)
in_pick=[38,72,74,80,101,107,112]
in_pick_added=[]
counter=0
for i in in_pick:
    counter=counter+1
    in_pick_added.append(i+counter)

col_val=[0 for i in range(len(LC3BII_chi1_ORDERNESS_MI))]
resid_=[40, 75, 78, 85, 107, 114, 120]
for i,j in zip(in_pick_added,resid_):
    LC3BII_chi1_ORDERNESS_MI.insert(loc=i, column='res%d'%j, value=col_val)

LC3BII_chi1_ORDERNESS_MI=LC3BII_chi1_ORDERNESS_MI.transpose()

col_val=[0 for i in range(len(LC3BII_chi1_ORDERNESS_MI))]
resid_=[40, 75, 78, 85, 107, 114, 120]
for i,j in zip(in_pick_added,resid_):
    LC3BII_chi1_ORDERNESS_MI.insert(loc=i, column='res%d'%j, value=col_val)

MI_net_np=LC3BII_chi1_MI.to_numpy()+LC3BII_chi1_rotamer_MI.to_numpy()+LC3BII_chi1_ORDERNESS_MI.to_numpy()
MI_net_normalised=MI_net_np/np.max(MI_net_np)
MI_net_normalised=pd.DataFrame(MI_net_normalised)
MI_net_normalised.to_csv('%s'%sys.argv[4])