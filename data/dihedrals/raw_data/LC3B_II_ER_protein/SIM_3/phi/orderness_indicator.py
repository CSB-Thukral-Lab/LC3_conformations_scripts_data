import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
import tqdm
import sys

total_frames=1000
def transition_indicator(corrected_rotamer_list):
    transition_indicator_ls=[]
    counter=-1
    for i in range(len(corrected_rotamer_list)):
        if i==total_frames:
            break
        else:
            if corrected_rotamer_list[i]==corrected_rotamer_list[i+1]:
                transition_indicator_ls.append(0)
            else:
                transition_indicator_ls.append(1)
    return(transition_indicator_ls)

LC3B_rotameric_states_corrected=pd.read_csv('%s'%sys.argv[1],index_col=0)

LC3B_transition_states=pd.DataFrame()
for cols in LC3B_rotameric_states_corrected:
    # print(cols)
    transition_indicator_ls=transition_indicator(LC3B_rotameric_states_corrected[cols].to_list())
    
    LC3B_transition_states[cols]=transition_indicator_ls


frames=[]
for i in range(0,total_frames):
    frames.append(i)


m=3
val_ls=[]
k_ls=[]
value_sets=[]
for i in frames:
    val=i
    k=0
    values_=[]
    for j in frames:
        if j!=val:
            if j >= val-m and j <= val+m:
                values_.append(j)
                k=k+1
    # print('K-Nearest values of %f is %d'%(val,k))
#     values_=[j]+values_
    value_sets.append(values_)
    val_ls.append(val)
    k_ls.append(k)

counter=-1
value_sets_v_added=[]
for i in value_sets:
    counter=counter+1
    value_sets_v_added.append([counter]+i)

def entropy(array):
    _, counts = np.unique(array, return_counts=True)
    probabilities = counts / len(array)
    shannon_entropy = -np.sum(probabilities * np.log2(probabilities))
    
    return (shannon_entropy)
def orderness_indicator(transition_indicator_ls):
    entropy_time_point=[]
    for i in value_sets_v_added:
        transition_indicator_val=[]
        for val in i:
            transition_indicator_val.append(transition_indicator_ls[val])

        transition_indicator_val=np.array(transition_indicator_val)
        en=entropy(transition_indicator_val)
        entropy_time_point.append(en)

    orderness_state=[]
    for i in entropy_time_point:
        if i >0.5:
            orderness_state.append(1)
        else:
            orderness_state.append(0)   
    
    return(orderness_state)

LC3B_ORDERNESS_states=pd.DataFrame()
for cols in LC3B_transition_states:
    # print(cols)
    ORDERNESS_S=orderness_indicator(LC3B_transition_states[cols].to_list())
    LC3B_ORDERNESS_states[cols]=ORDERNESS_S
    

LC3B_ORDERNESS_states.to_csv('%s'%sys.argv[2])