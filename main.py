# CREADO NDD Sept 2020
import random
import numpy as np

# FUNCIONES PARA OPERADORES


def evalua(n, x, poblIt, utilidad):
    suma = 0
    total = 0
    for i in range(0, n):
        for j in range(0, x):
            suma += poblIt[i, j] * utilidad[j]
        fitness[i] = suma
        total += suma
        suma = 0
    return fitness, total


def imprime(n, total, fitness, poblIt):
    # Tabla de evaluación de la Población
    acumula = 0
    print("\n", 'Tabla Iteración:', "\n")
    for i in range(0, n):
        probab = fitness[i] / total
        acumula += probab
        print([i + 1], " ", poblIt[i], "  ", fitness[i], " ",
              "{0:.3f}".format(probab), " ", "{0:.3f}".format(acumula))
        acumulado[i] = acumula
    print("Total Fitness:      ", total)
    return acumulado


def seleccion(acumulado):
    Alescoje = np.random.rand()
    print("escoje:      ", Alescoje)

    for i in range(0, n):
        if acumulado[i] > Alescoje:
            padre = poblIt[i]
            break
    return (padre)


def cruce(a1, p1, p2):
    tempMatriz = np.empty((n-1,2), dtype=object)
    if a1 < Pcruce:
        print("Mas grande", Pcruce, "que ", a1, "-> Si Cruzan")

        rangoPuntosCorte = np.zeros((n-1,), dtype=float)

        rangoPuntosCorte[0] = (1/(n-1))
        for i in range(1, n-1):
            rangoPuntosCorte[i] = rangoPuntosCorte[i-1] + (1/(n-1))

        print("\nRango de puntos de corte: ",rangoPuntosCorte,"\n")

        a = np.random.rand()
        for i in range(0,2):
            indice = np.searchsorted(rangoPuntosCorte, a)
            tempMatriz[i,0] = vars()['p{}'.format(i+1)][:indice+1]
            tempMatriz[i,1] = vars()['p{}'.format(i+1)][indice+1:]
            print("Aleatorio: {:.2f}\nTempMatriz[{},0]: {}\nTempMatriz[{},1]: {}\n".format(a, i, tempMatriz[i,0], i, tempMatriz[i,1]))

        hijo1 = list(tempMatriz[0,0])
        hijo1.extend(list(tempMatriz[1,1]))
        hijo2 = list(tempMatriz[1,0])
        hijo2.extend(list(tempMatriz[0,1]))
        
        print("hijo1: ", hijo1)
        print("hijo2: ", hijo2)

    else:
        print("Menor", Pcruce, "que ", a1, "-> NO Cruzan")
        hijo1 = p1
        hijo2 = p2

    return hijo1, hijo2


def crear(n, x):
    suma = 0
    ejemplo = np.random.randint(0, 2, (n, x))

    for i in range(n):
        for j in range(x):
            suma += ejemplo[i, j] * pesos[j]

        while suma > 15:
            ejemplo[i] = np.random.randint(0, 2, (1, x))
            suma = 0
            for j in range(x):
                suma += ejemplo[i, j] * pesos[j]

        suma = 0

    return ejemplo


#### Parametros #####
x = 4  # numero de variables de decision - Elementos diferentes: x
n = 4  # numero de individuos en la poblacion - cromosomas: n
Pcruce = 0.98  # Probabilidad de Cruce
Pmuta = 0.1  # Probabilidad de Mutación

fitness = np.empty((n))
acumulado = np.empty((n))
suma = 0
total = 0

# Ingresar los datos del Problema de la Mochila - Peso y Utilidad de los Elementos
pesos = [7, 6, 8, 2]
utilidad = [4, 5, 6, 3]

# Individuos, soluciones o cromosomas
poblInicial = crear(n, x)


print("Poblacion inicial Aleatoria:", "\n", poblInicial)
print("\n", "Utilidad:", utilidad)
print("\n", "Pesos", pesos)
poblIt = poblInicial

# FIN DE LOS DATOS INICIALES

# Llama función evalua, para calcular el fitness de cada individuo
fitness, total = evalua(n, x, poblIt, utilidad)
# print("\n","Funcion Fitness por individuos",  fitness)
# print("\n","Suma fitness: ",  total)

# imprime la tabla de la iteracion
imprime(n, total, fitness, poblIt)

# ***************************************
# Inicia Iteraciones

# Crear vector de 5x2 vacio  a = numpy.zeros(shape=(5,2))
for iter in range(2):
    print("\n", "Iteración ", iter + 1)

    for i in [0, 2]:  # Para el bloque de 2 hijos cada vez
        papa1 = seleccion(acumulado)  # Padre 1
        print("padre 1:", papa1)
        papa2 = seleccion(acumulado)  # Padre 2
        print("padre 2:", papa2)

        hijoA, hijoB = cruce(np.random.rand(), papa1, papa2)
        print("hijo1: ", hijoA)
        poblIt[i] = hijoA
        print("hijo2: ", hijoB)
        poblIt[i + 1] = hijoB

        # POBLACION INTERMEDIA!!!!!

    print("\n", "Poblacion Iteración ", iter + 1, "\n", poblIt)
    fitness, total = evalua(n, x, poblIt, utilidad)
    # print("\n","Funcion Fitness por individuos",  fitness)
    # print("\n","Suma fitness: ",  total)

    # imprime la tabla de la iteracion
    imprime(n, total, fitness, poblIt)
    # pobIt=pobIntermedia
