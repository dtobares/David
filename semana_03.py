'''
Álbum con 860 figuritas.
Cada figurita se imprime en cantidades iguales y se distribuye aleatoriamente.
Cada paquete trae cinco figuritas.
'''
# CON FIGUS SUELTAS
# Ejercicio 1: Crear
# Implementá la función crear_album(figus_total) que devuelve un álbum (vector) vacío con figus_total espacios para pegar figuritas

import random


def crear_album(figus_total):
    return [0]*figus_total

# Ejercicio 2: Incompleto
# ¿Cuál sería el comando de Python que nos dice si hay al menos un cero en el vector que representa el álbum? ¿Qué significa que haya al menos un cero en nuestro vector?

def album_incompleto(A):
    return 0 in A

def comprar_figu(figus_total):
    figuritas=list(range(figus_total))
    return random.choice(figuritas)

#Ejercicio 4: Cantidad de compras
#Implementá la función cuantas_figus(figus_total) que, dado el tamaño del álbum (figus_total), 
#genere un álbum nuevo, simule su llenado y devuelva la cantidad de figuritas que se debieron 
# comprar para completarlo


def cuantas_figus(figus_total):
    album=crear_album(figus_total)
    compras=0   
    while album_incompleto(album):
        figu=comprar_figu(figus_total)
        album[figu]=1
        compras=compras+1
    return compras

#EJERCICIO N°5 
'''
n_repeticiones=1000
figus_total=6
resultados = []

for i in range (n_repeticiones):
    compras= cuantas_figus(figus_total)
    resultados.append(compras)

promedio= sum(resultados) / n_repeticiones

print(promedio)
'''

#EJERCICIO 6:
#Escribí una función llamada experimento_figus(n_repeticiones, figus_total) que simule el llenado 
#de n_repeticiones álbums de figus_total figuritas y devuelva el número estimado de figuritas que 
#hay que comprar, en promedio, para completar el álbum.

#Para esto, una posibilidad es que la función experimento_figus() llame a la función cuantas_figus()
#tantas veces como lo indica el parámetro n_repeticiones y guarde los resultados parciales en una lista, 
#a partir de la cual luego realice el promedio.

def experimento_figus (n_repeticiones, figus_total):
    resultados = []
    for i in range (n_repeticiones):
        compras = cuantas_figus(figus_total)
        resultados.append(compras)
    promedio= sum(resultados) / n_repeticiones
    return promedio

promediopara860= experimento_figus (100, 860)
print ("El promedio de figuritas a comprar es de:  ", promediopara860)

#CON PAQUETE DE FIGURITAS

#
#Ejercicio 7:
#Simulá la generación de un paquete con cinco figuritas, sabiendo que el álbum es de 860. 
#Tené en cuenta que, como en la vida real, puede haber figuritas repetidas en un paquete

def comprar_paquete (figus_total):
    paquete=[]
    for i in range (5):
        paquete.append (random.choice(range(figus_total)))
    return paquete

#Ejercicio 8:
#Implementá una función comprar_paquete(figus_total, figus_paquete) que, dado el tamaño del 
#álbum (figus_total) y la cantidad de figuritas por paquete (figus_paquete), genere un paquete (lista) de
#figuritas al azar

def comprar_paquete(figus_total, figus_paquete):
    paquete=[]
    for i in range (figus_paquete):
        paquete.append (random.choice(range(figus_total)))
    return paquete

paquete=comprar_paquete(860,5)
print (paquete)

#EJERCICIO9:

def cuantos_paquetes (figus_total,figus_paquete):
    album= [0]* figus_total
    paquetes_comprados=0

    while 0 in album:
        paquete=comprar_paquete(figus_total,figus_paquete)
        for figu in paquete:
            album[figu]=1
            paquetes_comprados=paquetes_comprados+1
    return paquetes_comprados

figus_total=860
figus_paquete=5
paquetes_acomprar= cuantos_paquetes(figus_total,figus_paquete)

print("la cantidad de paquetes a comprar es de:  ", paquetes_acomprar)

#EJERCICIO 10

#Calculá n_repeticiones = 100 veces la función cuantos_paquetes, utilizando figus_total = 860, 
# figus_paquete = 5. Guarda los resultados obtenidos en una lista y calculá su promedio. 
# #Si los recursos de la computadora lo permiten, hacelo con 1000 repeticiones.
# No olvides guardar todo en un archivo semana_03.py. Tené en cuenta que el archivo que entregues 
# debe poder ser importado para testear la función experimento_figus() sin que se ejecuten comandos 
# no deseados.

def experimento_paquetes (n_repeticiones, figus_total):
    resultados = []
    for i in range (n_repeticiones):
        compras = cuantos_paquetes(figus_total,figus_paquete)
        resultados.append(compras)
    promedio= sum(resultados) / n_repeticiones
    return promedio

promediopaquetes860= experimento_figus (100, 860)
print ("El promedio de paquetesva comprar es de:  ", promediopaquetes860)


       