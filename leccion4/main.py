# 1. Haciendo uso de comprensión de listas realice un programa que, dado 
#   una  lista  de  listas  de  números  enteros,  devuelva  el  máximo  de  cada 
#   lista. Por ejemplo, suponga la siguiente listas de listas: 
#    [[2, 4, 1], [1,2,3,4,5,6,7,8], [100,250,43]] 
#   El programa debe  devolver el mayor elemento de  cada sublista 
#    
#   Ahora, haciendo uso del pdb, inserte puntos de parada justo en la línea 
#   donde ha implementado la compresión de listas. Haga pruebas 
#   mostrando el contenido de las variables y continuar con la ejecución 
#   línea a línea. ¿Qué conclusiones obtiene?.

# import pdb
# pdb.set_trace()

# lista = [[2, 4, 1], [1,2,3,4,5,6,7,8], [100,250,43]] 
# poner el punto de interrupcion en PDB
# for l in lista:
#     print(max(l))

# mList=[max(l) for l in lista]
# print(mList)
# 2. Haga  uso  de  la  función  filter  para  construir  un  programa  que,  dado 
#   una lista de n números devuelva aquellos que  son primos. Por 
#   ejemplo, dada la lista [3, 4, 8, 5, 5, 22, 13], el programa que implemente 
#   debe devolver como resultado [3, 5, 5, 13]

lista = [3, 4, 8, 5, 5, 22, 13,20 ,66, 230, 95, 63]

# mLista = list(filter(lambda x: x == i for i in lista if i))

for l in lista:
    mLista = list( filter(lambda x: x % l, lista)
)
print(mLista)