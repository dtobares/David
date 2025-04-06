'''
Ejercicio 1: Invertir una lista
Escribir una función invertir_lista(lista) que dada una lista devuelva otra que tenga los mismos elementos pero en el orden inverso. 
Es decir, el que era el primer elemento de la lista de entrada deberá ser el último de la lista de salida y análogamente con los demás elementos
'''

listaautos = ['corolla','sierrita','citroen','ram']
def invertir_lista (listaautos):
    return listaautos [::-1]


listacompu = ['HP','MAC','DELL','LENOVO']
def invertir_lista (listacompu):
    return list (reversed(listacompu))


#comentarios de clase sobre como se ejecutó:
#el ::1, va bien. Sino for i in range (len(l))
# res.append (l[-i-1]). Pensarlo mejor así (no con el reversed)
#para agregar un elemento adelante de una lista [6]+l



'''
Ejercicio 2: Conjetura de Collatz
Escribir una función que compute la conjetura de Collatz para un número entero dado. La misma se puede enunciar como:

Empezamos con un número entero positivo,
Lo evaluamos, si el número es par entonces lo dividimos entre 2. Si es impar, entonces se multiplica por 3 y se le suma 1.
Al resultado lo volvemos a evaluar y nuevamente aplicamos las operaciones correspondientes hasta que obtengamos un 1.
Retornar la cantidad de pasos realizados
'''
# funciones recursivas: para resolverlo voy a usar algo mas chico, algo mas chico, y hasta que se hace tan chico que se resuelve. 
#es como factorear. 
#el factorial de 6: 6!, se calcula como 6*5*4*3*2*1
# o tambien como 6!= 6. 5!........
# def factorial (n):
#    if n==1:
#    resultado=1
#    else: 
#      resultado = n*factorial(n-1)
# return resultado
# ITERATIVA: 
# resultado=1
# while n>1 VER COMO ES FACTORIAL ITERATIVA


#OPCIÓN CON LA FUNCIÓN COLLATZ

def collatz (nro):
    pasos=0
    while nro != 1:
        if nro %2 ==0:
            nro=nro/2
        else:
            nro=nro*3+1
        pasos=pasos+1
    return pasos


#LA VERSION RECURSIVA COMO SERÍA:
#ESTA ES LA MANERA RECURSIVA
'''
def collatz (n):
    if n==1:
        return 0
    else:
        if n%2==0:
            n=n/2
        else:
            n=n*3+1
        respuesta=collatz(n)
        return 1+respuesta
collatz(4)
print(collatz(4))
'''
'''
def collatz (n):
    if n==1:
        return 0
    else:
        if n%2==0:
            n=n/2
        else:
            n=n*3+1
        respuesta=collatz(n)
        return 1+respuesta
'''
#
#
#
'''
Ejercicio 3: Diccionarios
Dado un diccionario que dadas ciertas claves (que serán strings) tiene ciertas definiciones (lista de strings), dar dos funciones:

contar_definiciones(d) que dado un diccionario devuelve otro diccionario con las mismas claves y para cada una de ellas la cantidad de definiciones que tiene.
cantidad_de_claves_letra(d, l) que dado el diccionario d devuelve la cantidad de entradas (claves) que comienzan con la letra l.
'''

diccionario={
    "gas" : ["se usa para cocinar", "combustible para auto", "se transporta en garrafas", "se transporta en gasoducto", "combustible explosivo"],
    "nafta" : ["combustible liviano", "tiene distintos octanajes", "tiene distintos colores","se usa en autos y motos"],
    "auto" : ["es un medio de transporte", "hay de diferentes marcas y fabricantes", "tiene 4 ruedas", "son a motor naftero o electrico"],
    "edificio" : ["puede servir para habitarlo", "construcción de varios pisos en altura", "puede servir de oficina laborales", "pueden ser inteligentes y ecologicos"],
    }

def contar_definiciones(diccionario):
    return {clave: len(definiciones) for clave, definiciones in diccionario.items()}
    

def cantidad_de_claves_letra(diccionario,l):
    cont=0
    for clave in diccionario:
        if clave.startswith(l):
            cont=cont+1
    return cont



'''
Ejercicio 4: Propagación
Vamos a modelar una fila con varios fósforos uno al lado del otro. Los fósforos pueden estar en tres estados: nuevos, prendidos fuego o ya gastados (carbonizados). 
Representaremos esta situación con una lista L con un elemento por fósforo, que en cada posición tiene un 0 (nuevo), un 1 (encendido) o un -1 (carbonizado). 
El fuego se propaga inmediatamente de un fósforo encendido a cualquier fósforo nuevo que tenga a su lado. Los fósforos carbonizados no se encienden nuevamente.
Escribir una función llamada propagar que reciba una lista con 0’s, 1’s y -1’s y devuelva la lista en la que los 1’s se propagaron a sus vecinos con 0
'''

L= [0,0,0,-1,1,0,0,0,-1,0,1,0,0]
def propagar(L): 
    fosforos = L.copy()
    for i in range(1, len(fosforos)):
        if fosforos[i] == 0 and fosforos[i - 1] == 1:
            fosforos[i] = 1
    
    for i in range (len (fosforos)-2,-1,-1):
        if fosforos [i]==0 and fosforos [i+1] ==1:
            fosforos[i]=1
    
    return fosforos


L= [0, 0, 0, 1, 0, 0]
def propagar(L): 
    fosforos = L.copy()
    for i in range(1, len(fosforos)):
        if fosforos[i] == 0 and fosforos[i - 1] == 1:
            fosforos[i] = 1  

    for i in range (len(fosforos)-2,-1,-1):
        if fosforos [i]==0 and fosforos [i+1] ==1:
            fosforos [i]=1
            
    return fosforos














