def gen_r(k):
 import pandas as pd
 if  k==1:
   d=   pd.read_excel  ( r'D:\papers\GCC\prg_every_row_4_2020\for_platform\python_less_matrix\real_data\d_1.xls',   sheet_name='s1', usecols='c:e');
 elif  k==2:
   d=   pd.read_excel  ( r'D:\papers\GCC\prg_every_row_4_2020\for_platform\python_less_matrix\real_data\d_2_2.xls', sheet_name='s1', usecols='a:c');
 elif k==3:
   d=   pd.read_excel  ( r'D:\papers\GCC\prg_every_row_4_2020\for_platform\python_less_matrix\real_data\d_2_3.xls', sheet_name='s1', usecols='a:c');
 elif k==4:
   d=   pd.read_excel  ( r'D:\papers\GCC\prg_every_row_4_2020\for_platform\python_less_matrix\real_data\d_4.xls',   sheet_name='s1', usecols='b:d');
 elif  k==5:
   d=   pd.read_excel  ( r'D:\papers\GCC\prg_every_row_4_2020\for_platform\python_less_matrix\real_data\d_5.xls',   sheet_name='s2', usecols='b:d');
 elif  k==6:
   d=   pd.read_excel  ( r'D:\papers\GCC\prg_every_row_4_2020\for_platform\python_less_matrix\real_data\d_6.xls',   sheet_name='Sheet2', usecols='b:d');
 elif  k==7:
   d=   pd.read_excel  ( r'D:\papers\GCC\prg_every_row_4_2020\for_platform\python_less_matrix\real_data\d_7.xls',   sheet_name='Sheet1', usecols='c:d');
 elif  k==8:
   d=   pd.read_excel  ( r'D:\papers\GCC\prg_every_row_4_2020\for_platform\python_less_matrix\real_data\d_8.xls',   sheet_name='s1', usecols='a:h');
 return(d);
