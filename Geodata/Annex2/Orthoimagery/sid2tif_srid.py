# -*- coding: utf-8 -*-
"""
Created on Mon Mar  8 10:40:33 2021

@author: wolf_florian
"""

from multiprocessing import Pool
from glob import glob
import os


path = r'R:\Rh_Rasterdaten\Orthofotos\2012'

os.chdir(path)

files = glob(path +os.sep + '*.tif')

out = r'R:\Rh_Datenmanagement\Geodaten\Annex2\Orthoimagery\rgb\thueringen\2012'

def main(file):
    try:
        os.system('gdal_translate -a_srs EPSG:31468 -co compress=deflate  \"{}\" \"{}\"'.format(file, out + os.sep + file.split(os.sep)[-1][:-3]+'tif'))
    except:
        print('error: ', file)
        
if __name__ == "__main__":
    pool = Pool(4)
    for bar in pool.imap_unordered(main, files):
        foo = bar
    pool.terminate()
    pool.join()
