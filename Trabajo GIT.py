#Todo el proyecto a cambiado "Realizado por Antonio"
def actividad_6():
<<<<<<< HEAD
    a = ((1, 2, 3),
         (4, 5, 6))
    b = ((-1, 0),
         (0, 1),
         (1, 1))
    resultado = [[0, 0], [0, 0]]
    for i in range(len(a)):
        for j in range(len(b[0])):
            for k in range(len(b)):
                resultado[i][j] += a[i][k]*b[k][j]
    for i in range(len(resultado)):
        resultado[i] = tuple(resultado[i])
    resultado = tuple(resultado)
    for i in range(len(resultado)):
        print(resultado[i])
    print("Todo es un éxito")
    #Este comentario se tiene que eliminar
=======
    a = 2+2
    resultado = a**(9*a)
    print(resultado)
actividad_6()

>>>>>>> 729f971e471341c304cb982b8ac571fedce0e3bf
