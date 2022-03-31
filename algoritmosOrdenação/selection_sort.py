#subprogramas
from random import randint


def preenche(valores):
    for i in range(len(valores)):
        valores[i] = randint(1, 20)


def trocar(vals, posX, posY):
    temp = vals[posX]
    vals[posX] = vals[posY]
    vals[posY] = temp
    return None


def selecionarMenor(vals, pos):
    menor_valor = pos
    for i in range(pos+1, len(vals)):
        if vals[i] < vals[menor_valor]:
            menor_valor = i

    return menor_valor


def ordenar(valores):
    for ind in range(len(valores)-1):
        menor = selecionarMenor(valores, ind)
        trocar(valores, ind, menor)



lista = [0]*15
print(lista)
preenche((lista))
print(lista)
ordenar(lista)
print(lista)