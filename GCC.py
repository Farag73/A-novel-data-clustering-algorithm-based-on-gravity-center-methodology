# A new data clustering algorithm based on Gravity center methodology
# Expert system waith application journal Elsevier puplisher
# First and corrosponding auther "Farag hamed Kuwil" 00905454426352 
# All rights reserved
from scipy.spatial import distance;
import pandas as pd ; 
import matplotlib.pyplot as plt
import numpy as np; 
import Normal;
import graph; 
import lambd;
import NN_alg;
import cohesion;  
import cluster; 
import gen_data; 
import gen_data_r; 
n=2; # second coefficient 
#data=gen_data.gen(6); # unread dataset
data = gen_data_r.gen_r(1);# realdataset
#*****************************************************************
data = data.dropna(how='any')
data = data.drop_duplicates()
data=data.drop([np.argmin(data.applymap(np.isreal).all(1))]);
data=Normal.normalize(data);# some experiments need to ignore this line
#*****************************************************************
rang1=len(data); dim=data.size/len(data);
tshold_p=np.empty([rang1,2]);
#*****************************************************************
(lam,max_all)=lambd.lamb(rang1,data);
#*****************************************************************
#lam=lam/6;  # first coefficient 
tshold_p=cohesion.tshold_p(data,max_all,lam,rang1,tshold_p);
#*****************************************************************
(result,gc)=cluster.clus(data,max_all,tshold_p,rang1,n);
#*****************************************************************
result=NN_alg.nnlg(data,result,max_all,rang1);
#****************************************************************************
data=np.append(data, np.empty([rang1, 1]), axis=1);
#****************************************************************************
graph.g(dim,rang1,data,result);