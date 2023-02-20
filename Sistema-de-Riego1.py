"""
Programa que controla el funcionamiento de un sistema de riego automático para plantas de cultivo.

Autor: Marco Vinicio Esparza

Versión: v2.3
"""

def ejecutar_sistema_riego():
    """
    Proceso que se utiliza para controlar el riego de las plantas de cultivo en un sistema de riego automático.
    Parámetros:
    --------------
    No recibe parámetros

    Retorna:
    --------------
    No retorna parámetros
    """

    # definir el grafo del sistema de riego
    grafo = {
        "bomba": ["valvula1", "valvula2"],
        "valvula1": ["planta1", "planta2", "planta5", "planta6", "planta9", "planta10", "planta13", "planta14"],
        "valvula2": ["planta3", "planta4", "planta7", "planta8", "planta11", "planta12", "planta15", "planta16"],
        "planta1": [],
        "planta2": [],
        "planta3": [],
        "planta4": [],
        "planta5": [],
        "planta6": [],
        "planta7": [],
        "planta8": [],
        "planta9": [],
        "planta10": [],
        "planta11": [],
        "planta12": [],
        "planta13": [],
        "planta14": [],
        "planta15": [],
        "planta16": [],
        "planta17": [],
        "planta18": [],
        "planta19": [],
        "planta20": []
    }

    # definir el costo de cada arista
    costo = {
        ("bomba", "valvula1"): 1,
        ("bomba", "valvula2"): 1,
        ("valvula1", "planta1"): 1,
        ("valvula1", "planta2"): 1,
        ("valvula1", "planta5"): 1,
        ("valvula1", "planta6"): 1,
        ("valvula1", "planta9"): 1,
        ("valvula1", "planta10"): 1,
        ("valvula1", "planta13"): 1,
        ("valvula1", "planta14"): 1,
        ("valvula2", "planta3"): 1,
        ("valvula2", "planta4"): 1,
        ("valvula2", "planta7"): 1,
        ("valvula2", "planta8"): 1,
        ("valvula2", "planta11"): 1,
        ("valvula2", "planta12"): 1,
        ("valvula2", "planta15"): 1,
        ("valvula2", "planta16"): 1
    }

    # solicitar al usuario la planta a regar
    planta_a_regar = input("Ingrese el número de la planta a regar (1-20): ")

    # validar que la entrada sea válida
    while planta_a_regar not in ["1", "2", "3", "4", "5", "6", "7", "8", "9", "10", "11", "12", "13", "14", "15", "16", "17", "18", "19", "20" ]:
        planta_a_regar = input("Entrada inválida. Ingrese el número de la planta a regar (1-20): ")

    # definir la meta
    meta = "planta" + planta_a_regar

    # encontrar el camino más corto desde la bomba hasta la planta a regar
    cola = [("bomba", ["bomba"])]
    while cola:
        (nodo, camino) = cola.pop(0)
        if nodo == meta:
            break
        for vecino in grafo[nodo]:
            cola.append((vecino, camino + [vecino]))

    # mostrar el camino encontrado y su costo
    print("Camino desde la bomba hasta la planta {}: {}".format(planta_a_regar, "->".join(camino)))
    print("Costo del camino: {}".format(sum([costo[(camino[i], camino[i+1])] for i in range(len(camino) - 1)])))

    # encender las válvulas en el orden del camino encontrado
    for nodo in camino[1:]:
        # código para encender la válvula
        print("Moviendose a la {}...".format(nodo))

    # mostrar un mensaje de éxito
    print("La planta {} ha sido regada.".format(planta_a_regar))


# programa principal
if __name__ == '__main__':
    # inicializar el programa
    print("********* SISTEMA DE RIEGO AUTOMÁTICO *********")
    # iniciar bucle para repetir el proceso las veces que el usuario quiera
    while(True):    
        print("Ingrese el número de la opción que desea ejecutar:")
        print("1. Regar una planta")
        print("2. Salir")

        opcion = input()

        while opcion == "1":
            ejecutar_sistema_riego()
            print("\nIngrese el número de la opción que desea ejecutar:")
            print("1. Regar una planta")
            print("2. Salir")
            opcion = input()

        print("¡Hasta luego!")
        # Se pregunta al usuario si quiere volver a usar el programa  
        repetirProceso = input("¿Repetir proceso? (si/no): ")
        if repetirProceso.lower() != "si":
            print("********** FIN DEL PROCESO **********")
            # detener el bucle por completo
            break