from random import randint
#subprogramas


def preencher(vals):
    for ind in range(len(vals)):
        vals[ind] = randint(1, 15)

    return None


def troca(vals, posX, posY):
    temp = vals[posX]
    vals[posX] = vals[posY]
    vals[posY] = temp

    return None


def ordenar(valores):
    for ind in range(len(valores)-1, 0, -1):
        for j in range(ind):
            if valores[j] > valores[j+1]:
                troca(valores, j, j+1)

    return None


def ordenar_saida_rapida(valores): #caso a lista estiver ordenada o loop encerra sem precisar comparar tudo
    ultima_pos = len(valores)-1
    troquei = True
    while troquei:
        troquei = False
        for ind in range(ultima_pos):
            if valores[ind] > valores[ind+1]:
                troca(valores, ind, ind+1)
                troquei = True

        ultima_pos -= 1
    return None


listagem = [0]*10
preencher(listagem)
print(listagem)
ordenar_saida_rapida(listagem)
print(listagem)