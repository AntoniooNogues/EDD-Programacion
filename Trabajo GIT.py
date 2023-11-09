#Representar matrices
def actividad_6():
    a = ((1, 2, 3),
         (4, 5, 6))
    b = ((-1, 0),
         (0, 1),
         (1, 1))
    resultado = [[0, 0], [0, 0]]
    for i in range(len(a)):
        for l in range(len(b[0])):
            for k in range(len(b)):
                resultado[i][l] += a[i][k]*b[k][l]
    for i in range(len(resultado)):
        resultado[i]= tuple(resultado[i])
    resultado = tuple(resultado)
    for i in range(len(resultado)):
        print(resultado[i])


def ejercicio3_(palabra):
    #Crea una función que reciba una cadena y cuente cuántas letras "a" contiene.
    palabra_mayusculas = palabra.upper()

    contador_a = palabra.count("a")
    contador_A = palabra.count ("A")
    contador_total = contador_a + contador_A

    return contador_total