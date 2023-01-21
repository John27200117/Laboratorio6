#Diferencia simetrica de conjuntos
con1   = {3,5,7,9,11,13,5,18,2}
con2 = {1,2,4,7,8,10,13,15,17,20}
print("Conjunto A: ",con1)
print("Cantidad de elementos del conjunto A: ",len(con1))
print(type(con1))
print()
print("Conjunto B: ",con2)
print("Cantidad de elementos del conjunto B: ",len(con2))
print(type(con2))
print()
print("Conjunto diferencia simetrica de los conjuntos A y B: ")
print(con1 ^ con2)