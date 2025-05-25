#backbone_dihedral_MI.py psi_MI.csv phi_MI.csv output_net_mi_mat.csv
import numpy as np
import pandas as pd
import MDAnalysis
import seaborn as sns
import matplotlib.pyplot as plt
import tqdm
import sys

# LC3BII_chi1_MI=pd.read_csv('%s'sys.argv[1],
#                           index_col=0)
# in_pick=[38,72,74,80,101,107]
# in_pick_added=[]
# counter=0
# for i in in_pick:
#     counter=counter+1
#     in_pick_added.append(i+counter)

# col_val=[0 for i in range(len(LC3BII_chi1_MI))]
# resid_=[40, 75, 78, 85, 107, 114]
# for i,j in zip(in_pick_added,resid_):
#     LC3BII_chi1_MI.insert(loc=i, column='res%d'%j, value=col_val)

# LC3BII_chi1_MI=LC3BII_chi1_MI.transpose()

# col_val=[0 for i in range(len(LC3BII_chi1_MI))]
# resid_=[40, 75, 78, 85, 107, 114]
# for i,j in zip(in_pick_added,resid_):
#     LC3BII_chi1_MI.insert(loc=i, column='res%d'%j, value=col_val)

LC3BII_psi_MI=pd.read_csv('%s'%sys.argv[1],
                          index_col=0)
LC3BII_phi_MI=pd.read_csv('%s'%sys.argv[2],
                          index_col=0)
MI_net_np=(LC3BII_psi_MI.to_numpy()/np.max(LC3BII_psi_MI.to_numpy()))+(LC3BII_phi_MI.to_numpy()/np.max(LC3BII_phi_MI.to_numpy()))
MI_net_normalised=MI_net_np/np.max(MI_net_np)
MI_net_normalised=pd.DataFrame(MI_net_normalised)
MI_net_np_df=pd.DataFrame(MI_net_np)
MI_net_np_df.to_csv('%s.csv'%sys.argv[3])
MI_net_normalised.to_csv('%s_normalised.csv'%sys.argv[3])