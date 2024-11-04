lista = []

for cont in range(0,5):
    lista.append(int(input('Digite um número: ')))
    

for cont, numero in enumerate(lista):
    print(f"Na posição {cont} encontrei o valor {numero}! ")