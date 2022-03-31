n = 7
lista = [10,15,7,3,5]
lista.append(7)
for i in range(len(lista)):
    if lista[i] == n:
        if i == len(lista)-1:
            print("valor n encontrado")
        else:
            print(f"valor encontrado na posicao {i}")
            break
# print(lista[len(lista)-1])

#algoritmo adciona o valor procurado na ultima posição da lista
