"""
The code below creates text file with peak flow values for all junctions of the specified basin model
"""

#  junction matrix creation 
uniones= ['J445', 'J450', 'J455', 'J460', 'J465', 'J472', 'J477', 'J480', 'J487', 'J497', 'J500', 'J507', 'J510', 'VALDEINFIENRO', 'OUTLET']


# Open the file
dssFile = HecDss.open("/home/dorota/prueba/prueba.dss")


# getting flow peak from all junctions 
maxValor, path=[], []
for i in range(len(uniones)):
 path.append("//"+uniones[i]+"/FLOW/28SEP2012/1MIN/RUN:RUN 1/")
 valores = dssFile.get(path[i])
 print(max(valores.values))
 maxValor.append(max(valores.values))

# creating new alert file 
file = open("/home/nowiczka/alerta.txt", "w")
file.write("---ALERTA---- ")
file.write("\n")
file.write("Guandalentin Basin")
file.write("\n")
file.write("\n")
for i in range(len(uniones)):
 for j in range(1):
 x= str(uniones[i])+ ' '+str(maxValor[i])+ ' m3/s'
 file.write("%s\n" % x)
# Close the file
file.close()
