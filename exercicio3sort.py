numeros = input()
lista_numeros = numeros.split()
nova_lista = []

for x in lista_numeros:
    nova_lista.append(int(x))

nova_lista.sort()

for x in nova_lista:
    print(x)