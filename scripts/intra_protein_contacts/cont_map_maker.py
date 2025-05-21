#python contact_map_maker.py <path to the raw contact directory> <state>
import pandas as pd
import numpy as np
import os
import sys



path=r"%s"%sys.argv[1]
lc3_state=sys.argv[2]

if lc3_state.upper()=="UNB":
    print("considering membrane-bound Apo state")
    LC3_resid=[i for i in range(1,120)] #range for membrane-bound LC3 (GLP 120 is not considered)
    
elif lc3_state.upper()=="BND":
    print("considering membrane-bound p62 LIR state")
    LC3_resid=[i for i in range(1,120)]+[i for i in range(338,345)] #LC3 (resi 1 to 119) and p62 LIR peptide (resi 338 to 344)
    
elif lc3_state.upper()=="PRE":
    print("considering cytosolic state state")
    LC3_resid=[i for i in range(1,126)] # considering extended C-terminal 
    
else:
    raise ValueError("Incorrect LC3 state definition. Select one of three options: PRE/UNB/BND")

#os.chdir(path)
dist_mat_state= np.zeros((len(LC3_resid),len(LC3_resid)))
# dist_mat_df=pd.DataFrame(dist_mat)
for file in os.listdir(path):
    if file.endswith('.csv'):
        t_dist=pd.read_csv('%s/%s'%(path,file),header=None)
        t_dist_np=t_dist.to_numpy()
        dist_mat_state=dist_mat_state+t_dist_np

dist_mat_state_df=pd.DataFrame(dist_mat_state)
dist_mat_state_df.to_csv('%s.csv'%sys.argv[1])