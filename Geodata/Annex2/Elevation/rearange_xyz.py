# -*- coding: utf-8 -*-
"""
Created on Tue Mar  9 13:24:46 2021

@author: wolf_florian
"""

import os
from multiprocessing import Pool
import pandas as pd
from glob import glob

# path to data
path = r'R:\Rh_Rasterdaten\DGM_Raster\Th\dgm1_2017'

# get list of all files
files = glob(path + os.sep + '*.xyz')


def main(fi):
    # read data
    df = pd.read_csv(fi, header=None, sep = ' ')
    # sort values 
    dfs = df.sort_values(by =[1,0], ascending=[False,True] )  
    # create out path
    out= r'R:\Rh_Rasterdaten\DGM_Raster\Th\dgm1_2017_xyz_clip\{}'
    # write data to file
    dfs.to_csv(out.format(fi.split(os.sep)[-1]), sep=' ', index=False, header=False)
    

if __name__=="__main__":
    # create pool of workers
    pool = Pool(4)
    # run main function in parallel
    for bar in pool.imap_unordered(main, files):
        foo = bar
    # close pool
    pool.terminate()
    pool.join()
   




