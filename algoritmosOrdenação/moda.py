from random import randint

#subprogramas
def preencher(valores):
    for i in range(len(valores)):
        valores[i] = randint(1, 10)


def busca_moda(valores):
    auxiliar = [0]*len(valores)
    for i in range(len(valores)):
        auxiliar[i] = 1
        for j in range(i+1, len(valores)):
            if valores[j] == valores[i]:
                auxiliar[i] += 1
    moda = 0
    for i in range(1, len(auxiliar)):
        if auxiliar[i] > auxiliar[moda]:
            moda = auxiliar[i]

    return valores[moda]

#programa principal
numero = [0]*10
preencher(numero)
print(numero)
print(busca_moda(numero))
