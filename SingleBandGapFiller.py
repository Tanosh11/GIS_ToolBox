#-------------------------------------------------------------------------------
# Name:        module1
# Purpose:
#
# Author:      qgeddes
#
# Created:     12/04/2013
# Copyright:   (c) qgeddes 2013
# Licence:     <your licence>
#-------------------------------------------------------------------------------
#Change
import arcpy
arcpy.CheckOutExtension("Spatial")
arcpy.env.overwriteOutput=True
##FirstScene=     arcpy.Raster(arcpy.GetParameterAsText(0))
##CloudMask1= arcpy.Raster(arcpy.GetParameterAsText(1))
##SecondScene=    arcpy.Raster(arcpy.GetParameterAsText(2))
##CloudMask2=arcpy.Raster(arcpy.GetParameterAsText(3))
##
##OutputFolder=arcpy.GetParameterAsText(4)

FirstScene=     arcpy.Raster("C:\\Users\\qgeddes\\Downloads\\Landsat\\Cloudtest\\Alabama\\LE70190392012129EDC00_B1.tif")
CloudMask1= arcpy.Raster("C:\\Users\\qgeddes\\Downloads\\Landsat\\Cloudtest\\Alabama\\Reflectance\\masktest3.tif")
SecondScene=    arcpy.Raster("C:\\Users\\qgeddes\\Downloads\\Landsat\\Cloudtest\\Alabama\\Reflectance\\LE70190392012129EDC00_B1_TOA_Reflectance.tif")
CloudMask2=arcpy.Raster("C:\\Users\\qgeddes\\Downloads\\Landsat\\Cloudtest\\Alabama\\Reflectance\\masktest3.tif")

GapMask1=FirstScene>0
GapMask2=SecondScene>0

FinalMask1=GapMask1*CloudMask1
FinalMask2=GapMask2*CloudMask2

#where nodata is present for first scene and data is present for second
FillMask=(FinalMask1==0)*FinalMask2
FinalImage=(FirstScene*FinalMask1)+(SecondScene*FillMask)


FinalImage.save("C:\\Users\\qgeddes\\Downloads\\Landsat\\Cloudtest\\Alabama\\Reflectance\\GapFillTest\\test2.tif")
