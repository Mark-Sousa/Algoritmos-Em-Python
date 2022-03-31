def preencher(valores):
    for ind in range(len(valores)):
        valores[ind] = int(input(f"Elemento de indice {ind}: "))


# def buscaElemento(numeros, dado):#não é um bom algoritmo visto que percorre toda lista
#     local = -1
#     for ind in range(len(numeros)):
#         if numeros[ind] == dado:
#             local = ind
#     return local

def buscaElemento(numeros, dado):
    local = -1
    for i in range(len(numeros)):
        if numeros[i] == dado:
            return i
    return local


def escreverResposta(valor, pos):
    if pos < 0:
        print(f"{valor} não foi encontrado")
    else:
        print(f"{valor} foi encotrado na posição {pos}")

#programa principal


numeros = [0]*10
print("------------------------------------------")
preencher(numeros)
print("------------------------------------------")
dado = int(input("escolha um numero: "))
onde = buscaElemento(numeros, dado)
escreverResposta(dado, onde)