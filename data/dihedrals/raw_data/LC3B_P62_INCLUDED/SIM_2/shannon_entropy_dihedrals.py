import pandas as pd
import seaborn as sns
import numpy as np
import re
import matplotlib.pyplot as plt
import numpy as np
import sys

def entropy(array):
    _, counts = np.unique(array, return_counts=True)
    probabilities = counts / len(array)
    shannon_entropy = -np.sum(probabilities * np.log2(probabilities))
    
    return shannon_entropy

def num_ext(DF, angle):
    FORM_dih_sel_col=[]
    for i in DF.columns:
        j=i.split('.')[0].replace(angle,'')
        t_ls=re.findall(r'\d+', j)
        t=int(''.join(t_ls))
        FORM_dih_sel_col.append(t)
    return(FORM_dih_sel_col)

def entropy_ret(rot_dat,angle_):
    rot_dat_ent_df=pd.DataFrame()
    rot_dat_ent=[]
    for i in rot_dat.columns:

        ls=rot_dat[i].to_numpy()
        rot_dat_ent.append(entropy(ls))
    
    rot_dat_ent_df['Residues']=num_ext(rot_dat, angle_)
    rot_dat_ent_df[angle_]= rot_dat_ent   
    return rot_dat_ent_df

def net_ent_calc(state_df):
    net_entropy_norm_state=[]
    for a,i,j,k,l,m,n in zip(state_df['Residues'],
                    state_df['psi'],# chi entropy
                    state_df['phi'],
                    state_df['chi1'],state_df['chi2'],state_df['chi3'],state_df['chi4']):

        ent_ls=[i,j,k,l,m,n]
        ent_ls=ent_ls[:-3] # avoiding chi2 chi3 and chi4
        val=sum(ent_ls)
        if val ==0:
            net_entropy_norm_state.append(0)
        else:
            net_entropy_norm_state.append(val/max(ent_ls))

    return net_entropy_norm_state




chi1_rotamer_file=sys.argv[1]
chi2_rotamer_file=sys.argv[2]
chi3_rotamer_file=sys.argv[3]
chi4_rotamer_file=sys.argv[4]

psi_rotamer_file=sys.argv[5]
phi_rotamer_file=sys.argv[6]

op_file_name=sys.argv[7]

sys_chi1_rotamers_df=pd.read_csv(chi1_rotamer_file,
                                 index_col=0)
sys_chi2_rotamers_df=pd.read_csv(chi2_rotamer_file,
                                 index_col=0)
sys_chi3_rotamers_df=pd.read_csv(chi3_rotamer_file,
                                 index_col=0)
sys_chi4_rotamers_df=pd.read_csv(chi4_rotamer_file,
                                 index_col=0)

sys_psi_rotamers_df=pd.read_csv(psi_rotamer_file,
                                 index_col=0)
sys_phi_rotamers_df=pd.read_csv(phi_rotamer_file,
                                 index_col=0)


sys_psi_entropy=entropy_ret(sys_psi_rotamers_df, 'psi')
sys_phi_entropy=entropy_ret(sys_phi_rotamers_df, 'phi')


sys_chi1_entropy=entropy_ret(sys_chi1_rotamers_df, 'chi1')
sys_chi2_entropy=entropy_ret(sys_chi2_rotamers_df, 'chi2')
sys_chi3_entropy=entropy_ret(sys_chi3_rotamers_df, 'chi3')
sys_chi4_entropy=entropy_ret(sys_chi4_rotamers_df, 'chi4')


sys_entropy_merger1=pd.merge(sys_psi_entropy, sys_phi_entropy, on='Residues', how='outer')
sys_entropy_merger2=pd.merge(sys_entropy_merger1, sys_chi1_entropy, on='Residues', how='outer')
sys_entropy_merger2=pd.merge(sys_entropy_merger2, sys_chi2_entropy, on='Residues', how='outer')
sys_entropy_merger2=pd.merge(sys_entropy_merger2, sys_chi3_entropy, on='Residues', how='outer')
sys_entropy_merger2=pd.merge(sys_entropy_merger2, sys_chi4_entropy, on='Residues', how='outer')

sys_entropy_merger2=sys_entropy_merger2.fillna(0)

sys_entropy_merger2['NET_ENTROPY']=net_ent_calc(sys_entropy_merger2)


sys_entropy_merger2.to_csv(op_file_name)






