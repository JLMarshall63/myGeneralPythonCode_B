import arcpy
import random
arcpy.CreatePersonalGDB_management("C:/temp", "Circles.mdb")
arcpy.env.workspace = r'C:\temp\Circles.mdb'
mygeodatabase = r'C:\temp\Circles.mdb'
arcpy.CreateRandomPoints_management
(arcpy.env.workspace,'three_points',",",3)
arcpy.Buffer_analysis("three_points", "three_polys", "10")