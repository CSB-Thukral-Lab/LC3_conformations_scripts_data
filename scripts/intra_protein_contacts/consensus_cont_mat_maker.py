#python consensus_cont_mat_maker.py <cont_mat_replica1> <cont_mat_replica2> <cont_mat_replica3> <output_cont_mat_overall> 
import pandas as pd
import sys

cont_mat_s1=pd.read_csv('%s'%sys.argv[1],index_col=0)
cont_mat_s2=pd.read_csv('%s'%sys.argv[2],index_col=0)
cont_mat_s3=pd.read_csv('%s'%sys.argv[3],index_col=0)

cont_mat_s=cont_mat_s1+cont_mat_s2+cont_mat_s3
cont_mat_s=cont_mat_s/3
cont_mat_s.to_csv('%s'%sys.argv[4])