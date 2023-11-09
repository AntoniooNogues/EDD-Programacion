#Representar matrices
def actividad_6():
    a = ((3, 2, 3),
         (4, 5, 6))
    b = ((-1, 0),
         (0, 1),
         (1, 1))
    resultado = [[0, 0], [0, 0]]
    for x in range(len(a)):
        for j in range(len(b[0])):
            for k in range(len(b)):
                resultado[i][j] += a[i][k]*b[k][j]
    for x in range(len(resultado)):
        resultado[i]= tuple(resultado[i])
    resultado = tuple(resultado)
    for x in range(len(resultado)):
        print(resultado[i])

