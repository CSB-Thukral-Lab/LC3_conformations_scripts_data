#python fast_cont_mat.py <pdb_traj_file> <state: PRE/UNB/BND> <output_file_name>
import MDAnalysis
from mpi4py import MPI
import numpy as np
import os
import tqdm
from itertools import combinations
import sys



comm = MPI.COMM_WORLD
rank = comm.Get_rank() # get your process ID
size = comm.Get_size()
print(rank)

if rank == 0:
    Traj=MDAnalysis.Universe('%s'%sys.argv[1])
    lc3_state=sys.argv[2] 
    f_name=sys.argv[3]
    os.mkdir('%s_cont_mat'%f_name)
	# os.mkdir('%s_dist_mat'%f_name)
 
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
        break

    
    start=0
    timestep = 1
    # total_frames=1001
    max_distance=5
    def rSubset(arr, r):
        return list(combinations(arr, r))
    arr = LC3_resid
    r = 2
    comb=rSubset(arr, r)
    total_frames=Traj.trajectory.n_frames
    
else:
    comb = None
    LC3_resid = None
    Traj = None
    f_name= None
    total_frames= None
    start=None
    timestep =None
    max_distance=None


comb = comm.bcast(comb,root=0)
LC3_resid = comm.bcast(LC3_resid,root=0)
Traj = comm.bcast(Traj,root=0)
total_frames = comm.bcast(total_frames,root=0)
f_name = comm.bcast(f_name,root=0)
start=comm.bcast(start,root=0)
timestep =comm.bcast(timestep,root=0)
max_distance=comm.bcast(max_distance,root=0)

local_comb = comb[rank::size]
res_cont_mat_UNB= np.zeros((len(LC3_resid),len(LC3_resid)))

for resn in tqdm.tqdm(local_comb):
    for t in Traj.trajectory:
        sel1=Traj.select_atoms('resid %d and not type H'%resn[0])
        sel1.universe.trajectory[t.frame]
        sel2=Traj.select_atoms('resid %d and not type H'%resn[1])
        sel2.universe.trajectory[t.frame]

        cont_count=0
        for i in sel1.atoms:
            for j in sel2.atoms:

                pos_1=np.array(i.position)  
                pos_2=np.array(j.position)
                
                dist=np.linalg.norm(pos_1 - pos_2)

                if dist<=max_distance:
                    cont_count=cont_count+1
                    if cont_count==1:
                        res_cont_mat_UNB[resn[0]-1,resn[1]-1]+=1
                        continue

res_cont_mat_UNB_prob=res_cont_mat_UNB/total_frames
np.savetxt("%s_cont_mat/%s_CONT_MAT_%d.csv"%(f_name,f_name,rank),res_cont_mat_UNB_prob,delimiter=",")
