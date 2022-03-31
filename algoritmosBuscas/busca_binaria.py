from random import randint

n = 3
lista = []
for i in range(0, 16):
    lista.append(randint(1, 15))

lista.sort()
# inicio = 0
# fim = len(lista) - 1
# meio = (inicio + fim) // 2
# pos = 0
# print(lista)
# while (inicio < fim) and (n != lista[meio]):
#     if lista[meio] > n:
#         fim = meio -1
#     else:
#         inicio = meio +1
#     meio = (inicio + fim) // 2
#     if n == lista[meio]:
#         pos = meio
#
# if pos !=0:
#     print(f"valor encontrado na posição {pos}")
# else:
#     print('valor n encontrado!')


def busca_binaria(valores, procurado):
    inicio = 0
    fim = len(valores) - 1
    meio = (inicio + fim) // 2
    pos = 0
    while (inicio < fim) and (procurado != valores[meio]):
        if valores[meio] > procurado:
            fim = meio - 1
        else:
            inicio = meio + 1
        meio = (inicio + fim) // 2

    if procurado != valores[meio]:
        return -1
    else:
        return meio

print(lista)
print(busca_binaria(lista, n))




