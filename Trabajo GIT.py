#Representar matrices
def actividad_6():
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
        resultado[i]= tuple(resultado[i])
    resultado = tuple(resultado)
    for i in range(len(resultado)):
        print(resultado[i])
    #Este comentario se tiene que eliminar

    numero = random.randint(1, 10)

    intentos = 0

    while intentos < 3:
        intento = int(input("¡Bienvenido/a! Introduce el número que pienses que es:  "))
        # Si el número es igual al número secreto. Gana.
        if intento == numero:
            print("¡Enhorabuena!, Adivinaste el número secreto.", numero)
            break
        elif intento < numero:
            print("El número es mayor.")
        else:
            print("El número es menor.")

        intentos += 1
    # Si en el número de intentos no lo adivinas, se dice la solución.
    if intentos == 3 and intento != numero:
        print("Has agotado tus 3 intentos. El número secreto era:", numero)
