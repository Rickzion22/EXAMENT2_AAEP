#Nombre: Ricardo Adolfo Lopez Arquiñigo
import random

def coordenadasGeneradas(cantidad):
    matriz = []
    for i in range(cantidad):
        X = random.randint(-81, 81)
        Y = random.randint(-81, 81)
        matriz.append([X, Y])
    return matriz

def distanciaCuadrada(x, y):
    return x * x + y * y

def coordenadaMasLejana(coordenadas):
    if len(coordenadas) == 1:
        X = coordenadas[0][0]
        Y = coordenadas[0][1]
        if X > 0 and Y < 0:
            return coordenadas[0]
        else:
            return [0, 0]  
    else:
        mitad = len(coordenadas) // 2
        Izquierda = coordenadaMasLejana(coordenadas[:mitad])
        Derecha = coordenadaMasLejana(coordenadas[mitad:])

        distanciaIzquierda = distanciaCuadrada(Izquierda[0], Izquierda[1])
        distanciaDerecha = distanciaCuadrada(Derecha[0], Derecha[1])

        if distanciaIzquierda > distanciaDerecha:
            return Izquierda
        else:
            return Derecha


def main():
    cantidad = int(input("Ingrese la cantidad de coordenadas a generar: "))
    coordenadas = coordenadasGeneradas(cantidad)

    print("\nCoordenadas generadas:")
    for pares in coordenadas:
        print(pares)
    resultado = coordenadaMasLejana(coordenadas)

    if resultado[0] == 0 and resultado[1] == 0:
        print("\nNo se encontró ninguna coordenada que cumpla con las condiciones")
    else:
        print("\nLa coordenada más del origen (0,0) con X positivo e Y negativo es:", resultado)

if __name__ == "__main__":
    main()
