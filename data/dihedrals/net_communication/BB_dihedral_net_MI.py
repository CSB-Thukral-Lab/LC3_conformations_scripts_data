#dihedral_MI_net.py BB_DIHEDRAL.csv BB_ROTAMER.csv BB_ORDERNESS.csv output_net_mi_mat.csv
import numpy as np
import pandas as pd
import MDAnalysis
import seaborn as sns
import matplotlib.pyplot as plt
import tqdm
import sys

LC3BII_bb_dihedral_MI=pd.read_csv('%s'%sys.argv[1],
                          index_col=0)

LC3BII_rotamer_MI=pd.read_csv('%s'%sys.argv[2],
                          index_col=0)
LC3BII_orderness_MI=pd.read_csv('%s'%sys.argv[3],
                          index_col=0)
MI_net_np=LC3BII_bb_dihedral_MI.to_numpy()+LC3BII_rotamer_MI.to_numpy()+LC3BII_orderness_MI.to_numpy()
MI_net_normalised=MI_net_np/np.max(MI_net_np)
MI_net_normalised=pd.DataFrame(MI_net_normalised)
MI_net_normalised.to_csv('%s'%sys.argv[4])