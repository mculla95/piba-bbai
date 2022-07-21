from numpy import var
from numpy import sqrt
fileObj = open("offset", "r") #opens the file in read mode
lines = fileObj.read().splitlines() #puts the file into an array
fileObj.close()
offset = []
for line in lines:
	offs = line.strip().split()
	if (offs[1] == 'master') & (offs[2] == 'offset'):
		midv= int(offs[3])
		offset.append(midv)
intoffset=[]
for element in offset:
	intoffset.append(int(element))
media = 0
suma = 0
for offi in intoffset:
	suma = suma + abs(offi)
longitud=len(intoffset)

varianza = var(intoffset)
media = suma/longitud
print("El numero de elementos es ", longitud)
print("La suma de elementos es ", suma)
print("La media es ", media)
print("La varianza es ", sqrt(varianza))
