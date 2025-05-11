
# **Análisis Parques Ciudad Buenos Aires**

## **Alcance**:

### En esta investigación, se realizó un análisis sobre la base de datos de Parques de CABA. 
### Para este análisis vamos a mostrar la manera de poder expresar un código, para gestionar datos con archivo .csv. Y poder mostrar conclusiones acerca de:

* El/los parques con más cantidad de árboles
* El/los parques con los árboles más altos en promedio
* El/los parques con más variedad de especies
* La especie que más ejemplares tiene en la ciudad
* La razón entre especies exóticas y autóctonas

## 1. El/los parques con más cantidad de árboles

#### Para dicho análisis se ha confeccionado el siguiente código en Python: 

```python
import csv

def arboles_parque(nombre_archivo, nombre_parque):
    lista_total_arboles = []

    with open(nombre_archivo, encoding='utf-8') as f:
        lectura = csv.DictReader(f)
        for fila in lectura:
            if fila['espacio_ve'] == nombre_parque:
                lista_total_arboles.append(fila)
    
    return lista_total_arboles

# Ejemplo de uso:
# arbol_parque_irlanda = arboles_parque(
#     r'C:\Users\Usuario\Desktop\Proyectos\arbolado-en-espacios-verdes.csv',
#     'IRLANDA'
# )
# print(arbol_parque_irlanda[:3])

```
#### USANDO ZIP: DictReader ya hace internamente lo que zip haría, asociando cada valor de fila con su respectivo encabezado. Dictreader es mucho más directo




## 2. Crear una función que aprovechando la anterior, nos indique el árbol más popular de ese parque: arbol_mas_popular(nombre_parque)

```python

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
```
### HACIENDO PRUEBAS EN PARQUE IRLANDA, EL MAS POPULAR ES EL CEDRO DEL HIMALAYA.
### Ejemplo de Uso:
### arbol_popular = arbol_mas_popular(r'C:\Users\Usuario\Desktop\Proyectos\arbolado-en-espacios-verdes.csv','IRLANDA')
### print (arbol_popular)   


## 3. Indicar los n árboles más altos de ese parque n_mas_altos(nombre_parque, n)

```python
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
```

## 4. Dado un parque y una especie, indicar la altura promedio de esa especie altura_promedio(nombre_parque, especie)

```python

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
```
#### Ejemplo de uso: 
#### promedioalturas= altura_promedio(r'C:\Users\Usuario\Desktop\Proyectos\arbolado-en-espacios-verdes.csv','IRLANDA','Jacarandá')
#### print(promedioalturas)

#### El promedio de altura de jacaranda en parque IRLANDA, es de 13.48 metros. 


## 5. Probar el código creado y definir las funciones extra necesarias para decidir:

### a. El/los parques con más cantidad de árboles.
### b. El/los parques con los árboles más altos en promedio.
### c. El/los parques con más variedad de especies.
### d. La especie que más ejemplares tiene en la ciudad.
### e. La razón entre especies exóticas y autóctonas.

### a:_
#### Creamos un diccionario para contar árboles por parque. Recorremos cada fila del archivo. Si el parque ya está en el diccionario, sumamos 1. Si no está, lo agregamos con valor 1.
#### Busco la cantidad máxima de árboles en un parque. Busco todos los parques que tengan esa cantidad máxima

```python
def parques_con_mas_arboles(nombre_archivo):
    
    conteo_parques = {}

    
    with open(nombre_archivo, encoding='utf-8') as f:
        lector = csv.DictReader(f)

        for fila in lector:
            parque = fila['espacio_ve']  

            if parque in conteo_parques:
                conteo_parques[parque] += 1
            else:
                
                conteo_parques[parque] = 1

    maximo = 0
    for cantidad in conteo_parques.values():
        if cantidad > maximo:
            maximo = cantidad

    
    parques_maximos = []
    for parque, cantidad in conteo_parques.items():
        if cantidad == maximo:
            parques_maximos.append(parque)

    return parques_maximos, maximo

```

#### b. El/los parques con los árboles más altos en promedio.

Aquí los pasos tomados son: 
Suma las alturas de todos los árboles por parque.

Calcula el promedio por parque. 

Encuentra el promedio más alto. 

Devuelve el o los parques que tienen ese valor.

```python

def parque_altura_promedio(nombre_archivo):
    suma_alturas = {}
    cantidad_arboles = {}

    with open(nombre_archivo, encoding='utf-8') as f:
        lector = csv.DictReader(f)
        for fila in lector:
            parque = fila['espacio_ve']
            altura = float(fila['altura_tot'])

            
            if parque in suma_alturas:
                suma_alturas[parque] += altura
                cantidad_arboles[parque] += 1
            else:
                suma_alturas[parque] = altura
                cantidad_arboles[parque] = 1

    
    promedios = {}
    for parque in suma_alturas:
        promedio = suma_alturas[parque] / cantidad_arboles[parque]
        promedios[parque] = promedio

    max_promedio = max(promedios.values())

    parques_maximos = [p for p, prom in promedios.items() if prom == max_promedio]

    return parques_maximos, max_promedio
```

### c. El/los parques con más variedad de especies.

```python

def parque_mas_variedad(nombre_archivo):
    conteo = {}

    with open(nombre_archivo, encoding='utf-8') as f:
        lector = csv.DictReader(f)

        for fila in lector:
            parque = fila['espacio_ve']
            especie = fila['nombre_com']

            if parque not in conteo:
                conteo[parque] = []
            if especie not in conteo[parque]:
                conteo[parque].append(especie)

    max_cantidad = 0
    parques_max = []

    for parque in conteo:
        cantidad = len(conteo[parque])
        if cantidad > max_cantidad:
            max_cantidad = cantidad
            parques_max = [parque]
        elif cantidad == max_cantidad:
            parques_max.append(parque)

    return parques_max, max_cantidad
```

### d. La especie que más ejemplares tiene en la ciudad

```python
def especie_mas_comun(nombre_archivo):
    especies = []

    with open(nombre_archivo, encoding='utf-8') as f:
        lector = csv.DictReader(f)

        
        for fila in lector:
            especie = fila['nombre_com']
            especies.append(especie)

    max_cantidad = 0
    especie_mas_frecuente = None

    for especie in especies:
        cantidad = especies.count(especie)
        if cantidad > max_cantidad:
            max_cantidad = cantidad
            especie_mas_frecuente = especie

    return especie_mas_frecuente, max_cantidad   
```

### e. La razón entre especies exóticas y autóctonas

```python
def razon_exoticas_autoctonas(nombre_archivo):
    exoticas = []
    autoctonas = []

    with open(nombre_archivo, encoding='utf-8') as f:
        lector = csv.DictReader(f)

        for fila in lector:
            especie = fila['nombre_com'].strip().lower()
            origen = fila['origen'].strip().lower()

            if origen == 'exótica' and especie not in exoticas:
                exoticas.append(especie)
            elif origen == 'autóctona' and especie not in autoctonas:
                autoctonas.append(especie)

    if len(autoctonas) > 0:
        razon = len(exoticas) / len(autoctonas)
    else:
        razon = "No hay especies autóctonas"

    return len(exoticas), len(autoctonas), razon

```


---


*Documento creado por David Tobares - Master AI - Mayo 2025

