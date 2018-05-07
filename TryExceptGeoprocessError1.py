import arcpy
arcpy.env.workspace = "F:\MarshallJ_EPA_SEEPosition\SEE_PugetSound\Research\HecGeoRAS\TerrainTiles10\TerrainTiles10\terraintiles.mdb\Layers"
in_feature = "River"
out_feature = "River"
try:
    arcpy.CopyFeatures_management(in_feature, out_feature)
except arcpy.ExecuteError:
    print arcpy.GetMessage(2)
except:
    print "A nontool error has occurred."

import arcpy
arcpy.env.workspace = "C:\EsriPress\Python\Data\Exercise05\Facilities.gdb"
in_feature = "hospitals"
out_feature = "hospitals"
try:
    arcpy.CopyFeatures_management(in_feature, out_feature)
except arcpy.ExecuteError:
    print arcpy.GetMessage(2)
except:
    print "A nontool error has occurred."

try:
    import arcpy
    import sys
    import traceback
    arcpy.env.workspace = "C:\EsriPress\Python\Data\Exercise05\Facilities.gdb"
    in_feature = "hospitals"
    out_feature = "hospitals"
    arcpy.CopyFeatures_management(in_feature, out_feature)
except:
    tb = sys.exc_info()[2]
    tbinfo = traceback.format_tb(tb)[0]
    pymsg = "PYTHON ERRORS:\nTraceback info:\n" + tbinfo + "\nError Info:\n" + str(sys.exc_type) + ":" + str(sys.exc_value) + "\n"
    arcpy.AddError(pymsg)
    msgs = "ArcPy ERRORS:\n" + arcpy.GetMessages(2) + "\n"
    arcpy.AddError(msgs)
    print pymsg + "\n"
    print msgs
    
    