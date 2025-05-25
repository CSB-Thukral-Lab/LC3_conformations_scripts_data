# python NET_COMM_MAT.py structure.pdb MI_mat.csv output_MI_mat.csv

from itertools import combinations
import numpy as np
import pandas as pd
import MDAnalysis
import seaborn as sns
import matplotlib.pyplot as plt
import tqdm
import sys

def net_comm(structure,MI_mat,source,sink):
    scaling_factor=100
    LC3B_II=MDAnalysis.Universe(structure)
    LC3B_II_SOURCE_vicinity=LC3B_II.select_atoms('not resid 120-125 and around 3 resid %d'%source)
    LC3B_II_TARGET_vicinity=LC3B_II.select_atoms('not resid 120-125 and around 3 resid %d'%sink)

    source_vicinity=[i.resnum for i in LC3B_II_SOURCE_vicinity.residues]
    target_vicinity=[i.resnum for i in LC3B_II_TARGET_vicinity.residues]
    
    source_resid=[source]
    target_resid=[sink]
    source_vicinity=source_vicinity+source_resid
    target_vicinity=target_vicinity+target_resid
    
    resid_all=LC3B_II.select_atoms('resid 1-119')
    resid_all_resno=[i.resnum for i in resid_all.residues]
#     alanines=LC3B_II.select_atoms('resname ALA or resname GLY')
#     alanine_resno=[i.resnum for i in alanines.residues]
    
#     non_alanines=LC3B_II.select_atoms('protein and not(resname ALA or resname GLY)')
#     non_alanines_resno=[i.resnum for i in non_alanines.residues]
    
#     source_vicinity_n=[]
#     for i in source_vicinity:
#         if i not in alanine_resno:
#             source_vicinity_n.append(i)
    
#     target_vicinity_n=[]
#     for i in target_vicinity:
#         if i not in alanine_resno:
#             target_vicinity_n.append(i)
    
    mi_mat=pd.read_csv(MI_mat,
                  index_col=0)
    mi_mat_np=mi_mat.to_numpy()
    
    mi_select=[]
    for i in source_vicinity:
        for j in target_vicinity:
            a=resid_all_resno.index(i)
            b=resid_all_resno.index(j)
#             print(i,j,mi_mat_np[a,b])
            mi_select.append(mi_mat_np[a,b])
    net_comm_score=np.average(mi_select)*scaling_factor
    
    return(net_comm_score)


def rSubset(arr, r):
    return list(combinations(arr, r))
arr = [i for i in range(1,120)]
r = 2
comb=rSubset(arr, r)

structure='%s'%sys.argv[1]
MI_mat='%s'%sys.argv[2]


net_comm_mat= np.zeros((len(arr),len(arr)))
for i in tqdm.tqdm(comb):
    net_comm_mat[i[0]-1,i[1]-1]=net_comm(structure,MI_mat,i[0],i[1])

net_comm_mat_df=pd.DataFrame(net_comm_mat)
net_comm_mat_df.to_csv('%s'%sys.argv[3])