try:
    fileName = 'C:\University of Washington GIS\UOWSummer2017\GEOG565\TextDocs\myTestB.txt'
    with open(fileName, 'w') as fWrite:
        fWrite.write("My new test is now setting the stage for much more information to be acquired! arcpy.DefineProjection_management(x, PROJCS['NAD_1983_2011_StatePlane_Washington_North_FIPS_4601_Ft_US',GEOGCS['GCS_NAD_1983_2011',DATUM['D_NAD_1983_2011',SPHEROID['GRS_1980',6378137.0,298.257222101]],PRIMEM['Greenwich',0.0],UNIT['Degree',0.0174532925199433]],PROJECTION['Lambert_Conformal_Conic'],PARAMETER['False_Easting',1640416.666666667],PARAMETER['False_Northing',0.0],PARAMETER['Central_Meridian',-120.8333333333333],PARAMETER['Standard_Parallel_1',47.5],PARAMETER['Standard_Parallel_2',48.73333333333333],PARAMETER['Latitude_Of_Origin',47.0],UNIT['Foot_US',0.3048006096012192]] ")

except Exception , e:
    str(e)
    