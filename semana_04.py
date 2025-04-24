
#Ejercicio 1:
#Crear la función arboles_parque(nombre_archivo, nombre_parque) que dado el archivo 'arbolado-en-espacios-verdes.csv' nos genere una lista 
#con un diccionario para cada árbol (identificado por su id) de ese parque (cada fila del csv) y los nombres de las columnas correspondientes como claves de un diccionario interno.
#
# ZIP: COMBINA ELEMENTOS CREANDO PARES O GRUPOS DE DATOS
# nombres = ['Ana', 'Luis', 'Sofía']
#edades = [25, 30, 22]
#combinado = zip(nombres, edades)
#print(list(combinado))
#[('Ana', 25), ('Luis', 30), ('Sofía', 22)]


#LA FUNCION DICTREADER DEL MODULO CSV: El módulo csv de Python trae varias funciones, clases y constantes:
#csv.DictReader(file, ...) Devuelve un iterador que lee cada fila como un diccionario, usando la primera fila como nombres de las claves.
#csv.reader(file, ...) Devuelve un iterador que lee cada fila como una lista de valores. Ideal si no necesitás los encabezados como claves


import csv

def arboles_parque(nombre_archivo, nombre_parque):
    lista_total_arboles = []

    with open(nombre_archivo, encoding='utf-8') as f:
        lectura = csv.DictReader(f)
        for fila in lectura:
            if fila['espacio_ve'] == nombre_parque:
                lista_total_arboles.append(fila)
    
    return lista_total_arboles

#arbol_parque_irlanda = arboles_parque(r'C:\Users\Usuario\Desktop\Proyectos\arbolado-en-espacios-verdes.csv','IRLANDA')
#print(arbol_parque_irlanda[:3])

#USANDO ZIP: DictReader ya hace internamente lo que zip haría, asociando cada valor de fila con su respectivo encabezado
#dictreader es mucho más directo

#Ejercicio 2:
#Crear una función que aprovechando la anterior, nos indique el árbol más popular de ese parque: arbol_mas_popular(nombre_parque)

def arbol_mas_popular(nombre_archivo, nombre_parque):
    lista_total_arboles = arboles_parque(nombre_archivo, nombre_parque)
    
    if not lista_total_arboles:
        return "No se encontraron árboles en ese parque."
    
    especies = []
    for fila in lista_total_arboles:
        especie = fila['nombre_com']
        especies.append(especie)
    
    max=0
    nombre_mas_comun = None

    for especie in especies: 
        cantidad = especies.count(especie)
        if cantidad > max:
            max= cantidad
            nombre_mas_comun=especie
        return nombre_mas_comun

#HACIENDO PRUEBAS EN PARQUE IRLANDA, EL MAS POPULAR ES EL CEDRO DEL HIMALAYA.

#arbol_popular = arbol_mas_popular(r'C:\Users\Usuario\Desktop\Proyectos\arbolado-en-espacios-verdes.csv','IRLANDA')
#print (arbol_popular)   

#Ejercicio 3:
#Indicar los n árboles más altos de ese parque n_mas_altos(nombre_parque, n)

def n_altos (nombre_archivo, nombre_parque,n):
    lista_total_arboles = arboles_parque(nombre_archivo, nombre_parque)

    arboles_altos = []

    for arbol in lista_total_arboles: 
        altura= float (arbol['altura_tot'])
        especie = arbol ['id_arbol']
        arboles_altos.append((altura,especie))
    return arboles_altos[:n]

#arboles_mas_altos = n_altos(r'C:\Users\Usuario\Desktop\Proyectos\arbolado-en-espacios-verdes.csv','IRLANDA',5)
#print (arboles_mas_altos)
 
#Ejercicio 4:
#Dado un parque y una especie, indicar la altura promedio de esa especie altura_promedio(nombre_parque, especie)

def arboles_parque(nombre_archivo, nombre_parque):
    lista_total_arboles = []
    with open(nombre_archivo, encoding='utf-8') as f:
        lectura = csv.DictReader(f)
        for fila in lectura:
            if fila['espacio_ve'] == nombre_parque:
                lista_total_arboles.append(fila)
    
    return lista_total_arboles

def altura_promedio (nombre_archivo,nombre_parque, especie_n):
    lista_total_arboles = arboles_parque(nombre_archivo, nombre_parque)
    totalalturas = []

    for arbol in lista_total_arboles: 
        especie = arbol ['nombre_com']
        if especie == especie_n:
            altura=float (arbol['altura_tot'])
            totalalturas.append(altura)
    if totalalturas:
        promedio = sum(totalalturas)/len(totalalturas)
        return promedio
    else: 
        return "no existe dicha especie en tal parque"

#promedioalturas= altura_promedio(r'C:\Users\Usuario\Desktop\Proyectos\arbolado-en-espacios-verdes.csv','IRLANDA','Jacarandá')
#print(promedioalturas)

#el promedio de altura de jacaranda en parque IRLANDA, es de 13.48 metros. 


















 










    
