# Import the modules needed to run the script.
from hec.script import *
from hec.heclib.dss import *
from hec.io import TimeSeriesContainer
from hec.heclib.util import HecTime
from os import*

# Function to get forecast of precipitation: getForecast()
# This is an empty function which should be filled in the future when the
# information about source of forecast will be provided.
def getForecast():
 return()
 
# Function to actualize precipitation
def newGage(sciezka,lokalizacja):
watershed = ''

loc = lokalizacja
param = 'PRECIP-INC'
ver = 'GAGE'
startTime = '27Sep2012 1200'
lines= [ line.rstrip('\n') for line in open(sciezka)]
values = [float(string) for string in lines]
hecTime = HecTime()
tsc = TimeSeriesContainer()
tsc.watershed = watershed
tsc.location = loc
tsc.parameter = param
tsc.version = ver
tsc.fullName = '/%s/%s/%s//1HOUR/%s/' % (watershed, loc, param, ver)
tsc.interval = 60
hecTime.set(startTime)
times = []
for value in values :
 times.append(hecTime.value())
 hecTime.add(tsc.interval)
tsc.values = values
tsc.times = times
tsc.startTime = times[0]
tsc.endTime = times[-1]
tsc.numberValues = len(values)
tsc.units = 'MM'
tsc.type = 'PER-CUM' #inst-cum, per-aver,per-cum
dssFile = HecDss.open('/home/dorota/prueba/prueba.dss')
dssFile.put(tsc)
dssFile.done()
return


################################ MAIN SCRIPT ############################
# get/download rainfall data into text file
getForecast()
# actualize precipitation of all gages stations
newGage('/home/dorota/prueba/INES.txt','INES')
newGage('/home/dorota/prueba/VALDEINFIENRO.txt', Valdeinfierno')
newGage('/home/dorota/prueba/PUENTES.txt', 'Embalse de Puentes')
newGage('/home/dorota/prueba/MARIA.txt', 'Maria')
newGage('/home/dorota/prueba/CASTILLO.txt', 'Venta del Castillo')

# hec-hms calculation 
system("bash /usr/local/hec-dssvue201/HecDssVue/scripts/run-hms.sh")

# CREATE ALERT 
#matrix with junctions of studied basin
uniones= ['J445', 'J450', 'J455', 'J460', 'J465', 'J472', 'J477', 'J480',
'J487', 'J497', 'J500', 'J507', 'J510', 'VALDEINFIENRO', 'OUTLET']
#open the DSS file
dssFile = HecDss.open("/home/nowiczka/basin.dss")

#matrix with peak flow limits of all junctions of studied basin
LIMITS =[200,200,200,20,20,20, 200, 200, 200, 200, 200, 300, 400, 1500, 3000]

#create empty list
maxValor, path=[], []

# getting peak flow from all junctions #############
for i in range(len(uniones)):
 path.append("//"+uniones[i]+"/FLOW/28SEP2012/1MIN/RUN:RUN 1/")
 valores = dssFile.get(path[i])
 maxValor.append(max(valores.values))
 
#creating new text file 
file = open("/home/nowiczka/alerta.txt", "w") # open the file
file.write("ALERTA")
file.write("\n")
file.write("Guandalentin Basin")
file.write("\n")
file.write("\n")
for i in range(len(uniones)):
 for j in range(1):
 x= str(uniones[i])+ ' '+str(maxValor[i])+ ' m3/s'
 file.write("%s\n" % x)
# close the text file
file.close()

# sending alert if there is a need 
if maxValor>limites:
 system("bash /home/nowiczka/sendmail.sh")
 
#close the DSS file
dssFile.done()
