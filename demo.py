import pandas as pd
import hdfdict
import numpy as np
import h5py,time
import re


dfd = {}

#{1:df1,5:df2,113:df3<-add col} 

def print_attrs(name, obj):
    global dfd
    if '<class \'h5py._hl.dataset.Dataset\'>' == str(type(obj)):
        k= str(len(obj))
        if k not in dfd.keys():
            df = pd.DataFrame()
            #print(name,"Adding new key for len ", k)
        else:
            df = dfd[k]
        df[name] = obj
        df = pd.concat([pd.DataFrame(df[name].tolist()).add_prefix(name) for name in df.columns], axis=1)
        dfd[k] = df   
        l = len(obj[0])
        print(name,"Adding col to dfd index ", k)
        

f = h5py.File('walking5.h5', 'r')
f.visititems(print_attrs)


writer = pd.ExcelWriter('hd5excelout5.xlsx', engine = 'xlsxwriter')
for k, df in dfd.items():
    print(k,len(df))
    df.to_excel(writer, sheet_name = 'sheet_len_'+k)
writer.save()
writer.close()