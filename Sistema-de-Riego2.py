"""
Programa que controla el funcionamiento de un sistema de riego automático para plantas de cultivo.

Autor: Marco Vinicio Esparza

Versión: v2.1
"""

import random
import time

# Definición del grafo
grafo = {
    'Planta 1': ['Planta 2'],
    'Planta 2': ['Planta 3'],
    'Planta 3': ['Planta 4'],
    'Planta 4': ['Planta 5'],
    'Planta 5': ['Planta 6'],
    'Planta 6': ['Planta 7'],
    'Planta 7': ['Planta 8'],
    'Planta 8': ['Planta 9'],
    'Planta 9': ['Planta 10'],
    'Planta 10': ['Planta 11'],
    'Planta 11': ['Planta 12'],
    'Planta 12': ['Planta 13'],
    'Planta 13': ['Planta 14'],
    'Planta 14': ['Planta 15'],
    'Planta 15': ['Planta 16'],
    'Planta 16': ['Planta 17'],
    'Planta 17': ['Planta 18'],
    'Planta 18': ['Planta 19'],
    'Planta 19': ['Planta 20'],
    'Planta 20': []
}

# Definición de la humedad del suelo para cada planta (0 = seco, 1 = húmedo)
humedad = {
    'Planta 1': random.randint(0, 1),
    'Planta 2': random.randint(0, 1),
    'Planta 3': random.randint(0, 1),
    'Planta 4': random.randint(0, 1),
    'Planta 5': random.randint(0, 1),
    'Planta 6': random.randint(0, 1),
    'Planta 7': random.randint(0, 1),
    'Planta 8': random.randint(0, 1),
    'Planta 9': random.randint(0, 1),
    'Planta 10': random.randint(0, 1),
    'Planta 11': random.randint(0, 1),
    'Planta 12': random.randint(0, 1),
    'Planta 13': random.randint(0, 1),
    'Planta 14': random.randint(0, 1),
    'Planta 15': random.randint(0, 1),
    'Planta 16': random.randint(0, 1),
    'Planta 17': random.randint(0, 1),
    'Planta 18': random.randint(0, 1),
    'Planta 19': random.randint(0, 1),
    'Planta 20': random.randint(0, 1)
}

# Definición del umbral de humedad (0 = totalmente seco, 1 = completamente húmedo)
umbral = random.randint(0, 1)

def regar(planta):
    """
    Proceso que simula la activación del riego de una planta en particular.
    Parámetros:
    --------------
    Si, reciebe un parámetro planta, que es un string con el nombre de la planta a regar.

    Retorna:
    --------------
    No retorna parámetros
    """
    print(f"Activando el riego para la planta {planta}")

def buscar_camino(grafo, inicio, final, umbral_humedad):
    """
    Proceso para buscar el camino más corto desde la planta inicial hasta la planta final.
    Parámetros:
    --------------
    Si, recibe cuatro parámetros: 
    grafo, que es un diccionario que representa el grafo de conexiones entre las plantas.
    inicio y final, que son las plantas de inicio y fin, respectivamente.
    umbral_humedad, que es el umbral de humedad del suelo.

    Retorna:
    --------------
    Retorna el camino.
    """
    # Inicialización de variables
    cola = [[inicio]]
    visitados = set()
    humedad_suelo = {nodo: random.randint(0, 100) for nodo in grafo}  # Inicializa la humedad del suelo aleatoriamente

    # Realizar la búsqueda BFS
    while cola:
        # Sacar el primer camino de la cola
        camino = cola.pop(0)
        nodo_actual = camino[-1]

        # Comprobar si se ha llegado al nodo final
        if nodo_actual == final:
            return camino

        # Comprobar si el nodo actual ha sido visitado
        if nodo_actual in visitados:
            continue

        # Añadir el nodo actual a la lista de visitados
        visitados.add(nodo_actual)

        # Comprobar los vecinos del nodo actual y añadirlos a la cola
        for vecino in grafo[nodo_actual]:
            if vecino not in visitados:
                # Comprobar si la humedad del suelo del vecino es menor que el umbral establecido
                if humedad_suelo[vecino] < umbral_humedad:
                    # Si la humedad del suelo es menor que el umbral, regar el suelo
                    print(f"Regando el suelo en {vecino}...")
                    time.sleep(2)  # Simula el tiempo de riego
                    humedad_suelo[vecino] = random.randint(60, 100)  # Actualiza la humedad del suelo después del riego
                cola.append(camino + [vecino])

    # Si no se encuentra un camino desde el nodo de inicio al nodo final, regresa None
    return None

# programa principal
if __name__ == '__main__':

    # inicializar el programa
    print("********* SISTEMA DE RIEGO AUTOMÁTICO *********")
    # iniciar bucle para repetir el proceso las veces que el usuario quiera
    while(True): 

        inicio = input("Ingrese la planta inicio: ")
        # validar que la entrada sea válida
        while inicio not in ["Planta 1", "Planta 2", "Planta 3", "Planta 4", "Planta 5", "Planta 6", "Planta 7", "Planta 8", "Planta 9", "Planta 10", "Planta 11", "Planta 12", "Planta 13", "Planta 14", "Planta 15", "Planta 16", "Planta 17", "Planta 18", "Planta 19", "Planta 20"]:
                inicio = input("Entrada inválida. Ingrese el número de la planta a regar (1-4): ")
        final = input("Ingrese la planta final: ")
        while final not in ["Planta 1", "Planta 2", "Planta 3", "Planta 4", "Planta 5", "Planta 6", "Planta 7", "Planta 8", "Planta 9", "Planta 10", "Planta 11", "Planta 12", "Planta 13", "Planta 14", "Planta 15", "Planta 16", "Planta 17", "Planta 18", "Planta 19", "Planta 20"]:
                final = input("Entrada inválida. Ingrese el número de la planta a regar (1-4): ")
        umbral_humedad = 50
        camino = buscar_camino(grafo, inicio, final, umbral_humedad)
        print("Humedad controlada en la ruta: ", camino)

        # Se pregunta al usuario si quiere volver a usar el programa  
        repetirProceso = input("¿Repetir proceso? (si/no): ")
        if repetirProceso.lower() != "si":
            print("********** FIN DEL PROCESO **********")
            # detener el bucle por completo
            break
