#Todo el proyecto a cambiado "Realizado por Antonio"
def actividad_6():
<<<<<<< HEAD
<<<<<<< HEAD


=======
    a = ((1, 2, 3),
         (4, 5, 6))
    b = ((-1, 0),
         (0, 1),
         (1, 1))
    resultado = [[0, 0], [0, 0]]
    for i in range(len(a)):
        for j in range(len(b[0])):
>>>>>>> d3d391369ebe55fda606d5658644f62e8b0b8372
            for k in range(len(b)):
                resultado[i][l] += a[i][k]*b[k][l]
    for i in range(len(resultado)):
        resultado[i] = tuple(resultado[i])
    resultado = tuple(resultado)
    for i in range(len(resultado)):
        print(resultado[i])
<<<<<<< HEAD


def ejercicio3_(palabra):
    #Crea una función que reciba una cadena y cuente cuántas letras "a" contiene.
    palabra_mayusculas = palabra.upper()

    contador_a = palabra.count("a")
    contador_A = palabra.count ("A")
    contador_total = contador_a + contador_A

    return contador_total
=======
    print("Todo es un éxito")
    #Este comentario se tiene que eliminar
>>>>>>> d3d391369ebe55fda606d5658644f62e8b0b8372
=======
    a = 2+2
    resultado = a**(9*a)
    print(resultado)
actividad_6()

>>>>>>> 729f971e471341c304cb982b8ac571fedce0e3bf
