"""

This script returns the information about peak flow, time of peak flow and volume of two check- points, and plots hydrographs.

An example of the information returned:

Hidrograma de entrada Embalse de Puentes
Peak flow : 1063.59 m3/s
Time of peak flow : 2012-09-28 17:00
Volume : 24.38 Hm3 

"""

from py4j.java_gateway import JavaGateway, get_field
import os
import pandas as pd
import numpy as np
import matplotlib.pylab as pylab
import matplotlib.pyplot as plt
%matplotlib inline
gateway = JavaGateway()
jhec = gateway.jvm.hec

#Function:
extractDATA(pathDss,TituloDSS,model):#############
# this function has three arguments:
# 1. path of DSS record
# 2. name of the data type to display
# 3. Name of the meteorological model
#
# Function returns all necessary data to conduct model calibration:
# 1. Inflow volume
# 2. Peak flow
# 3. Time to peak flow
# 4. Hydrograph
def extractDATA(pathDss,TituloDSS,model):
 #getting data
 record = theFile.get(pathDss, True)
 values = [p for p in get_field(record,"values")]
 times = pd.DatetimeIndex(data=[np.datetime64(int(t)*60-2208988800,
's' )/
 for t in get_field(record, "times")], name="Time")
 
 #printing the most important data to calibrate a model
 print(model)
 print(TituloDSS)*
 print('Peak flow : ', max(values), ' m3/s')
 print('Time of peak flow : ',times[values.index(max(values))] )
 #Integral approximation with trap method
 volume = np.trapz(values)*60/10**6
 print("Volume :", volume,' Hm3')
 print('')
 #Plotting graphs
 f, ax = plt.subplots()
 ts=pd.TimeSeries(values, index=times)
 ts.plot()
 plt.ylabel('Flow m3/s')
 plt.gca().set_ylim([0,1500])
 ax.set_title(TituloDSS)

# file opening APERTURA DEL ARCHIVO
theFile = jhec.heclib.dss.HecDss.open("C:/Thesis.dss")

# rain data entry ENTRADA DE LOS DATOS DE LLUVIA
os.system("C:/RunDSS2.bat ")

# hec-hms calculation CALCULO CON HEC-HMS
os.system("C:/thesis.bat")

# results display VISUALIZACIÓN DE RESULTADOS
extractDATA('//OUTLET/FLOW/28SEP2012/1MIN/RUN:RUN 3 THIESSEN/','Hidrograma de entrada Embalse de Puentes', 'Thiessen')
extractDATA('//VALDEINFIENRO/FLOW-COMBINE/28SEP2012/1MIN/RUN:RUN THIESSEN/','Hidrograma de entrada Embalse de Valdeinfienro', 'Thiessen ')

# file closing
theFile.done()
