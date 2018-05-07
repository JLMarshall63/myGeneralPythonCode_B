try:
    import arcpy
    arcpy.env.workspace = "C:\EsriPress\Python\Data\Exercise06"
    fc = "railroads.shp"
    desc = arcpy.Describe(fc)
    sr = desc.SpatialReference
    print "Dataset type: " + desc.datasetType
    print "Spatial Reference: " + sr.name

except Exception, e:
     print str(e)