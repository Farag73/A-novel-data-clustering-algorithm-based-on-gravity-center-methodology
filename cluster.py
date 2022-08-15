def clus(data,max_all,tshold_p,rang1,n):
 from scipy.spatial import distance
 import numpy as np ;
 import cluster_p; 
 import pandas as pd 
 import pdb;
 i=0;k=1;
 gc = np.empty([20,1]);
 result = np.empty([rang1,1]);
 result[:,0]=0;
 dis_b_a = np.empty([1, rang1]);
 for l in range(rang1):
  m = np.nanmin(tshold_p[:,0]);
  if  not( (np.isnan(m)) or  pd.isnull(tshold_p[:,0]).all()):
   tshold_p2=tshold_p[np.where(tshold_p[:,0] == int(m))];
   m_gc = np.nanmin(tshold_p2[:,1]);
   gc_pos=np.where(tshold_p[:,0]== int(m))  and np.where(tshold_p[:,1] == m_gc)[0][0];
   gc[k-1,0]=gc_pos;
   if  not (np.isnan(gc_pos)): 
    points_pos = cluster_p.clus_p(data,max_all,gc_pos,rang1);
    vist=0; pn=0;
    for j in range(int(m)):
      q=int(points_pos[j])-1;
      if result[q][0]== 0:
         pn=pn+1;
    if pn>n:
      if result[gc_pos,0]==0:
        result[gc_pos,0]=k; l=l+1;  i=i+1; vist=1; tshold_p[gc_pos,0]=np.NaN;
      for j in range(int(m)+1):
        q=int(points_pos[j]);
        if int(result[q,0])== 0:
          result[q,0]=k;
          l=l+1;   i=i+1;vist=1; 
          tshold_p[q,0]=np.NaN;
      if vist==1:
              k=k+1;
    else:
       tshold_p[gc_pos,0]=np.NaN;
 points_pos=[]; dis_b_a=[];    
 return(result,gc);