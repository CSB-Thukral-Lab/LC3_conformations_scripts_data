#python phi_table_maker.py output_filename_prefix.csv
import pandas as pd
import os
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np
import re
import sys

def num_sort(test_string):
    return list(map(int, re.findall(r'\d+', test_string)))[0]


# path=r"/Users/jesucastin/Documents/LC3B/Chi_Analysis/LC3B_II/"
# os.chdir(path)
file_names=[]
for file in os.listdir():
    if file.endswith('.xvg'):
        file_names.append(file)



resids=[i.replace('phi','') for i in file_names]
resids.sort(key=num_sort)

resids_file_n=['phi%s'%i for i in resids]

file_no=0
# path=r"/Users/jesucastin/Documents/LC3B/Chi_Analysis/LC3B_II/"
# os.chdir(path)

df_list=[]
file_names=[]

for file in resids_file_n:
    
    # Create the filepath of particular file
    file_path =f"{file}"
    file_names.append(file)
    file_no=file_no+1


    temp_df=pd.read_csv(file_path,skiprows=17,delim_whitespace=True,header=None,engine='python')
    df_list.append(temp_df[1])
fin_df_r1=pd.concat(df_list,axis=1)

fin_df_r1.columns=resids_file_n


fin_df_r1_360=pd.DataFrame()
for i in fin_df_r1:
    transformed_angles=[]
    for j in fin_df_r1['%s'%i]:
        if j<0:
            transformed_angles.append(j+360)
        else:
            transformed_angles.append(j)
    fin_df_r1_360['%s'%i]=transformed_angles

fin_df_r1_360.to_csv('%s.csv'%sys.argv[1])
