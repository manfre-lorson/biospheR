# -*- coding: utf-8 -*-
"""
Created on Wed Mar  3 11:09:36 2021

@author: wolf_florian
"""

from osgeo import gdal, osr
from glob import glob


path = r'R:\Rh_Datenmanagement\Geodaten\Annex2\Orthoimagery\1997\**\*.TIF'

files = glob(path, recursive=True)


srs = osr.SpatialReference()
srs.ImportFromEPSG(31468)

for f in files:
    try:
        file = gdal.Open(f, gdal.GA_Update)
        file.SetProjection(srs.ExportToWkt())

        print(f, 'successfully updated')
        band=file.GetRasterBand(1)
        band.SetNoDataValue(255)
        band.FlushCache()
        band = None
        file = None
    except:
        print(f, 'ERROR')


