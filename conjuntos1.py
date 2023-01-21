con1   = {1,3,6,8,12,17,23,11}
con2 = {2,5,6,8,10,11,14,16,18,21}
con3 = {1,3,6,9,11,13,23,30}
print("Conjunto A: ",con1)
print("Cantidad de elementos del conjunto A: ",len(con1))
print(type(con1))
print()
print("Conjunto B: ",con2)
print("Cantidad de elementos del conjunto B: ",len(con2))
print(type(con2))
print()
print("Conjunto C: ",con3)
print("Cantidad de elementos del conjunto C: ",len(con3))
print(type(con3))
print()
#Union de conjuntos
print("Union de los conjuntos A u B u C: ")
print("Union: ",con1|con2|con3)
print()
#Interseccion de conjuntos
print("Interseccion de los conjuntos A ∩ B ∩ C:")
print("Conjunto interseccion: ",con1 & con2 & con3)
print()
#Diferencia de conjuntos A - B
print("Conjunto diferencia A - B:")
print("Conjunto diferencia: ",con1 - con2)
