import arcpy
from arcpy import env
env.workspace = "C:\EsriPress\Python\Data\Exercise07"
fc = "airports.shp"
cursor = arcpy.da.SearchCursor(fc, ["NAME"], '"TOT_ENP" > 100000')
for row in cursor:
    print row[0]
del row
del cursor