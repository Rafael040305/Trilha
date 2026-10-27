numeros = input()
lista_numeros = numeros.split()
nova_lista = []

for x in lista_numeros:
    x = int(x)
    nova_lista.append(x)

for j in range(len(nova_lista) - 1):
    i = 0
    while i < len(nova_lista) - 1:
        if nova_lista[i] > nova_lista[i+1]:
            nova_lista[i], nova_lista[i+1] = nova_lista[i+1], nova_lista[i]
        i += 1

for x in nova_lista:
    print(x)


