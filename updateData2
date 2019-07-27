"""
This script update rainfall data records in HEC-DSS database using TimeSeriesContainer class.

The script is build on a example 20 "Using a TimeSeriesContainer Object" from HEC-DSS manual (2009):
It aims to update forecast rainfall from text files into the HEC-DSSVue database.
"""

from hec.script import *
from hec.heclib.dss import *
from hec.io import TimeSeriesContainer
from hec.heclib.util import HecTime

# function
def newGage(pathTxt,locGage):
 watershed = ''
 loc =locGage
 param = 'RAINFALL'
 ver = 'GAGE'
 startTime = '27SEP2012, 1200'
 lines= [ line.rstrip('\n') for line in open(pathTxt)]
 values = [float(string) for string in lines]
 hecTime = HecTime()
 tsc = TimeSeriesContainer()
 tsc.watershed = watershed
 tsc.location = loc
 tsc.parameter = param
 tsc.version = ver
 tsc.fullName = '/%s/%s/%s//1HOUR/%s/' % \
 (watershed, loc, param, ver)
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
 tsc.type = 'PRECIP-INC'
 dssFile = HecDss.open("C:/Thesis.dss")
 dssFile.put(tsc)
 dssFile.done()
 
 
# main code 
newGage('C:/INES.TXT','Dona Ines')
newGage('C:/VALDEINFIENRO.TXT', 'Embalse de Valdeinfierno')
newGage('C:/PUENTES.TXT', 'Embalse de Puentes')
newGage('C:/MARIA.TXT', 'Maria')
newGage('C:/CASTILLO.TXT', 'Venta del Castillo')
