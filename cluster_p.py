def clus_p(data,max_all,pos,rang1):
 from scipy.spatial import distance
 import numpy as np ;
 every= np.empty([2, rang1]);
 every[0][:]=np. linspace(0,rang1-1,rang1);
 every[1][:]=distance.cdist(data.iloc[pos:pos+1:].values, data.iloc[:,:].values, 'euclidean');
 every[1][pos]=max_all;
 every = every [ :, every[1].argsort()];
# every_row = every_row [ :, every_row[0].argsort()];
 #every=(sortrows(every',2))';
 return(every[0][:]); 
 