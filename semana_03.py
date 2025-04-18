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
#aca definido el album A me devolverá si es True cuando existan ceros en ese album, es decir que hay que seguir comprando figuritas. 
#hasta que devuelva false; en ese caso el album estará completo

def album_incompleto(A):
    return 0 in A


#Ejercicio 3: Comprar
#Implementá una función comprar_figu(figus_total) que reciba el número total de figuritas que tiene el álbum (dado por el parámetro figus_total) y 
#devuelva un número entero aleatorio que representa la figurita que nos tocó.

def comprar_figu(figus_total):
    figuritas=list(range(figus_total))
    return random.choice(figuritas)


#Ejercicio 4: Cantidad de compras
#Implementá la función cuantas_figus(figus_total) que, dado el tamaño del álbum (figus_total), 
#genere un álbum nuevo, simule su llenado y devuelva la cantidad de figuritas que se debieron 
# comprar para completarlo


def cuantas_figus(figus_total):
    A = crear_album(figus_total)
    compras=0   
    while album_incompleto(A):
        figu=comprar_figu(figus_total)
        A [figu]=1
        compras=compras+1
    return compras


#EJERCICIO N°5 
#Ejecutá n_repeticiones = 1000 veces la función anterior utilizando figus_total = 6 y guardá en una lista los resultados obtenidos en cada repetición. 
#Con los resultados obtenidos estimá cuántas figuritas hay que comprar, en promedio, para completar el álbum de seis figuritas.

n_repeticiones=1000
figus_total=6
resultados = []

for i in range (n_repeticiones):
    compras= cuantas_figus(figus_total)
    resultados.append(compras)
promedio= sum(resultados) / n_repeticiones    


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

#CONCLUSION: 
# EL PROMEDIO DE FIGURITAS A COMPRAR ES DE 6278, PARA ALBUM DE 860 FIGURITAS. PARA 100 REPETICIONES
# EL PROMEDIO DE FIGURITAS A COMPRAR ES DE 6242, PARA ALBUM DE 860 FIGURITAS. PARA 200 REPETICIONES
# EL PROMEDIO DE FIGURITAS A COMPRAR ES DE 6283, PARA ALBUM DE 860 FIGURITAS. PARA 500 REPETICIONES
# ENTONCES A MAYOR CANTIDAD DE REPETICIONES (PERSONAS QUE QUIEREN LLENAR ESE ALBUM), VOY A ACERCARME A UN 
# PROMEDIO MAS PRECISO. 


'''
#DEF
#print (crear_album(50))
#print (comprar_figu(800))
#print(cuantas_figus(860))
#print (resultados)
#print(promedio)
#promediopara860= experimento_figus (100, 860)
#print ("El promedio de figuritas a comprar es de:  ", promediopara860)
'''


#CON PAQUETE DE FIGURITAS

#Ejercicio 7:
#Simulá la generación de un paquete con cinco figuritas, sabiendo que el álbum es de 860. 
#Tené en cuenta que, como en la vida real, puede haber figuritas repetidas en un paquete
import random

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

#EJERCICIO9:
#Implementá una función cuantos_paquetes(figus_total, figus_paquete) que dado el tamaño del álbum y la cantidad de figus por paquete, 
#genere un álbum nuevo, simule su llenado y devuelva cuántos paquetes se debieron comprar para completarlo.

def cuantos_paquetes (figus_total,figus_paquete):
    A = [0]* figus_total
    paquetes_comprados=0

    while 0 in A:
        paquete=comprar_paquete(figus_total,figus_paquete)
        for figu in paquete:
            A [figu]=1
        paquetes_comprados=paquetes_comprados+1
    return paquetes_comprados


#CONCLUSIÓN: PARA ALBUM DE 860 FIGURITAS, Y PAQUETES DE 5 FIGURITAS, DAL ALREDEDOR DE 1200 PAQUETES NECESARIOS A COMPRAR.


#EJERCICIO 10:
#Calculá n_repeticiones = 100 veces la función cuantos_paquetes, utilizando figus_total = 860, 
# figus_paquete = 5. Guarda los resultados obtenidos en una lista y calculá su promedio. 
# #Si los recursos de la computadora lo permiten, hacelo con 1000 repeticiones.
# No olvides guardar todo en un archivo semana_03.py. Tené en cuenta que el archivo que entregues 
# debe poder ser importado para testear la función experimento_figus() sin que se ejecuten comandos 
# no deseados.

figus_paquete=5

def experimento_paquetes (n_repeticiones, figus_total):
    resultados = []
    for i in range (n_repeticiones):
        compras = cuantos_paquetes(figus_total,figus_paquete)
        resultados.append(compras)
    promedio= sum(resultados) / n_repeticiones
    return promedio



#CONCLUSIÓN: 
# CON n=100: PARA ALBUM DE 860 FIGURITAS, Y PAQUETES DE 5 FIGURITAS, DA ALREDEDOR DE 1215/1274/1240/1220 PAQUETES NECESARIOS A COMPRAR
# CON n=1000: PARA ALBUM DE 860 FIGURITAS, Y PAQUETES DE 5 FIGURITAS, DA ALREDEDOR DE 1264/1270/1260/1263 PAQUETES NECESARIOS A COMPRAR
# es decir, a mayor cantidad de REPETICIONES (n), la DISPERSIÓN ES MENOR, Y EL PROMEDIO TIENDE A UN INTERVALO MAS CHICO DE GAP.

n_repeticiones=10
figus_total=860


if __name__== "__main__":
    experimento_paquetes (n_repeticiones, figus_total)
    experimento_figus (n_repeticiones, figus_total)


'''
#print (comprar_paquete(figus_total))
#paquete=comprar_paquete(860,5)
#print (paquete)
#figus_total=860
#figus_paquete=5
#paquetes_acomprar= cuantos_paquetes(figus_total,figus_paquete)
#print("la cantidad de paquetes a comprar es de:  ", paquetes_acomprar)
#promediopaquetes860= experimento_paquetes (1000, 860)
#print ("El promedio de paquetes a comprar es de:  ", promediopaquetes860)
'''

