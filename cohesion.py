def tshold_p(data,max_all,lam,rang1,tshold_p):
 from scipy.spatial import distance
 import numpy as np  
 every_row = np.empty([1, rang1]);
 dis_b_a = np.empty([1, rang1]);
 for i in range(rang1): 
   every_row[0][:]=distance.cdist(data.iloc[i:i+1:].values, data.iloc[:,:].values, 'euclidean');
   every_row[0][i]=max_all;
   every_row = every_row [ :, every_row[0].argsort()];
   for j in range(rang1-3): 
     dis_b_a[0][j]=every_row[0,j+1]-every_row[0,j];
   if np.amax(dis_b_a)>lam: 
      test_exit=np.where(dis_b_a[0,:]>lam)[0][0];
      if not (np.isnan(test_exit)):
        tshold_p[i][0]=test_exit;
        tshold_p[i][1]=dis_b_a[0,test_exit];
   else: 
       tshold_p[i][0]=rang1-1;
       tshold_p[i][1]=0;
 every_row=[]; dis_b_a=[];  
 return(tshold_p); 
