# -*- coding: utf-8 -*-
"""
Created on Thu Mar  4 10:10:31 2021

@author: wolf_florian
@work: multicore translate .xyz files to tiff
"""

from multiprocessing import Pool
from glob import glob
import os

def main(file):
    """translate .xyz file to tiff
    input is full path to file"""
    
    try:
        os.system('gdal_translate -a_srs EPSG:32632 \"{}\" \"{}\"'.format(file, file[:-3]+'tif'))
    except:
        print('error: ', file)

# set in path to folder with .xyz files        
path = r'R:\Rh_Rasterdaten\DGM_Raster\He\DGM_Hessen\DGM 1\*.xyz'
# change directory to folder
os.chdir(r'R:\Rh_Rasterdaten\DGM_Raster\He\DGM_Hessen\DGM 1')

# get all files as list
files = glob(path)

# run main definition on 4 cores for all files
if __name__ == "__main__":
    pool = Pool(4)
    for bar in pool.imap_unordered(main, files):
        foo = bar
    pool.terminate()
    pool.join()
