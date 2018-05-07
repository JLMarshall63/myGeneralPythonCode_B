try:
    import arcpy
    from arcpy import env
    env.workspace = "F:\MarshallJ_EPA_SEEPosition\SEE_PugetSound\Research\PSPIMStage4\PSPIM2\PSPIM2\PSPIM.gdb\Biota_NMFS_TE"
    fclist = arcpy.ListFeatureClasses()
    for fc in fclist:
        count = arcpy.GetCount_management(fc)
        print count

except Exception , e:
    str(e)
    

import exceptions
dir(exceptions)