"""
This script plots flow data which is already recorded in HEC-DSSVue. The script returns a hydrograph from a selected record.
"""


#module importation
from py4j.java_gateway import *
from pandas import *
from numpy import *
from matplotlib.pylab import *
%matplotlib inline

#creation of a bridge between Java and Python
j = JavaGateway().jvm.hec.heclib.dss.HecDss.open

#file opening
dssFile = j("C:/Project1.dss")

#geting data from the record
record = dssFile.get("//JUNCTION/FLOW/28SEP2002/5MIN/RUN:RUN 1/", True)

#geting flow vales from the record
parameter = [p for p in get_field(record,"values")

#geting date&time of flow vales from the record
times = DatetimeIndex(data=[datetime64(int(t*60), 's' ) \
 for t in get_field(record, "times")],
name="Time")
ts=TimeSeries(values, index=times)

#data plotting
ts.plot()
