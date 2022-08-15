def nnlg(data,result,max_all,rang1):
 from scipy.spatial import distance
 import numpy as np ;
 every_row = np.empty([1, rang1]);
 j=np.where(result==0)[0]; 
 if len(j)>0:
  for i in range(len(j)):
   q=1;
   if result[j[i]] == 0:
    every_row[0][:]=distance.cdist(data.iloc[j[i]:j[i]+1:].values, data.iloc[:,:].values, 'euclidean');
    while q==1:
     every_row[0,j[i]] =max_all;
     w= np.argmin(every_row);
     if result[int(w) ][ 0] !=0: 
        result[j[i]][0] =  result[int(w)][0];
        q=0;
     else:
        every_row[0][int(w)]=max_all;
 every_row=[]; j=[]; 
 return(result); 
