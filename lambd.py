def lamb(rang1,data_n):
 from scipy.spatial import distance;
 import numpy as np; 
 p2p_sm=(np.random.rand(1,rang1));
 evry_dist=distance.cdist(data_n.iloc[1:1+1:].values, data_n.iloc[:,:].values, 'euclidean');
 max_all=np.amax(evry_dist);
 for i in range(rang1):
     evry_dist=distance.cdist(data_n.iloc[i:i+1:].values, data_n.iloc[:,:].values, 'euclidean');
     evry_dist[0,i] =max_all;
     p2p_sm[0][i]= np.nanmin(evry_dist);
 return(np.nanmax(p2p_sm[0,:]),max_all); 