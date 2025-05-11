

#Retomar el ejercicio de Figus
#Hacer las clases:
# ○ Álbum: constructor (¿qué toma?) y métodos: pegar_figu, esta_completo
# ○ Figu: constructor (¿qué toma?)
# ○ Paquete: constructor(¿qué toma?), método dame_figus


class Figu:
    def __init__(self, numero):
        self.numero = numero


import random

class Paquete:
    def __init__(self, figus_total, figus_por_paquete):
        self.figuras = [Figu(random.randint(0, figus_total - 1)) for _ in range(figus_por_paquete)]

    def dame_figus(self):
        return self.figuras
    
class Album:
    def __init__(self, figus_total):
        self.figus_total = figus_total
        self.figus_pegadas = [0] * figus_total

    def pegar_figu(self, figu):
        self.figus_pegadas[figu.numero] = 1

    def esta_completo(self):
        return 0 not in self.figus_pegadas
    


def llenar_album_con_paquetes(figus_total, figus_por_paquete):
    album = Album(figus_total)
    paquetes_comprados = 0

    while not album.esta_completo():
        paquete = Paquete(figus_total, figus_por_paquete)
        for figu in paquete.dame_figus():
            album.pegar_figu(figu)
        paquetes_comprados += 1

    return paquetes_comprados

#figus_total = 860
#figus_por_paquete = 5
#repeticiones = 100

#resultados = [llenar_album_con_paquetes(figus_total, figus_por_paquete) for _ in range(repeticiones)]
#promedio = sum(resultados) / repeticiones

#print (promedio)

