"""
This script update rainfall data records in HEC-DSS database.

Firstly, we create Main Window. Secondly, we open the DSS file Project.dss, and we read data from the specified record. Then, a new matrix
with actual rainfall data is generated. With set_field function, the data is updated. Finally, save function saves the data container in 
the opened DSS file
"""

# modules importation 
from py4j.java_gateway import JavaGateway, get_field, set_field
gateway = JavaGateway()
jhec = gateway.jvm.hec

# main script
mainWindow = jhec.dssgui.ListSelection.createMainWindow()
mainWindow.openDSSFile("C:/Project.dss")
record=mainWindow.read("//GAGE 1/PRECIP-INC/01JAN2000/30MIN/GAGE/")
temp=get_field(record,"values")
newTemp = [newTemp.rstrip('\n') for newTemp in open('C:/rainfall.txt')]
newTemp=[float(string) for string in newTemp]

# new matrix creation 
for i in range(len(newTemp)):
 temp[i]=newTemp[i]
set_field(record,"values",temp)
mainWindow.save(record)
