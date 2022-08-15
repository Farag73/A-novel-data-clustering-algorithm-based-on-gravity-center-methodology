def g(dim,rang1,data_n,result):
 if dim==2:
  data_n[:,2]=result[:,0];
  import matplotlib.pyplot as plt
  for i in range(rang1):
    if data_n[i,2]==1:
      plt.plot(data_n[i, 0],     data_n[i,1] ,c='b',marker='.');
    elif data_n[i,2]==2:
      plt.plot(data_n[i, 0],     data_n[i,1] ,c='g',marker='.');
    elif data_n[i,2]==3:
      plt.plot(data_n[i, 0],     data_n[i,1] ,c='r',marker='+');
    elif data_n[i,2]==4:
      plt.plot(data_n[i, 0],     data_n[i,1] ,c='c',marker='*');
    elif data_n[i,2]==5:
      plt.plot(data_n[i, 0],     data_n[i,1] ,c='m',marker='.');
    elif data_n[i,2]==6:
      plt.plot(data_n[i, 0],     data_n[i,1] ,c='y',marker='o');
    elif data_n[i,2]==7:
      plt.plot(data_n[i, 0],     data_n[i,1] ,c='k',marker='o');
    elif data_n[i,2]==8:
      plt.plot(data_n[i, 0],     data_n[i,1] ,c='m',marker='.');
    elif data_n[i,2]==9:
      plt.plot(data_n[i, 0],     data_n[i,1] ,c='y',marker='.');
    elif data_n[i,2]==10:
      plt.plot(data_n[i, 0],     data_n[i,1] ,c='r',marker='.');  
    elif data_n[i,2]==11:
      plt.plot(data_n[i, 0],     data_n[i,1] ,c='g',marker='.');
 else:
  data_n[:,3]=result[:,0];
  from matplotlib import pyplot
  from mpl_toolkits.mplot3d import Axes3D
  import matplotlib.pyplot as plt
  fig = pyplot.figure()
  ax = Axes3D(fig)
  ax = fig.add_subplot(111, projection='3d');
  for i in range(rang1):
    if data_n[i,3]==0:
      ax.scatter(data_n[i, 0], data_n[i,1] ,data_n[i,2] ,c='b',marker='o');
    elif data_n[i,3]==1:
      ax.scatter(data_n[i, 0], data_n[i,1] ,data_n[i,2] ,c='b',marker='o');
    elif data_n[i,3]==2:
      ax.scatter(data_n[i, 0], data_n[i,1] ,data_n[i,2] ,c='g',marker='o');
    elif data_n[i,3]==3:
      ax.scatter(data_n[i, 0], data_n[i,1] ,data_n[i,2] ,c='r',marker='o');
    elif data_n[i,3]==4:
      ax.scatter(data_n[i, 0], data_n[i,1] ,data_n[i,2] ,c='c',marker='o');
    elif data_n[i,3]==5:
      ax.scatter(data_n[i, 0], data_n[i,1] ,data_n[i,2] ,c='m',marker='o');
    elif data_n[i,3]==6:
      ax.scatter(data_n[i, 0], data_n[i,1] ,data_n[i,2] ,c='y',marker='o');
    elif data_n[i,3]==7:
      ax.scatter(data_n[i, 0], data_n[i,1] ,data_n[i,2] ,c='k',marker='o');
    elif data_n[i,3]==8:
      ax.scatter(data_n[i, 0], data_n[i,1] ,data_n[i,2] ,c='m',marker='.');
    elif data_n[i,3]==9:
      ax.scatter(data_n[i, 0], data_n[i,1] ,data_n[i,2] ,c='y',marker='.');
    elif data_n[i,3]==9:
      ax.scatter(data_n[i, 0], data_n[i,1] ,data_n[i,2] ,c='r',marker='.');
 return