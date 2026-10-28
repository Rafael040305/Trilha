i = 1
lista = []

def analise(indice, numero, lista_numeros):
    while indice <= numero:
        if ((indice % 3 == 0) and (indice % 5 == 0)):
            lista_numeros.append("FizzBuzz")
        elif (indice % 3 == 0):
            lista_numeros.append("Fizz")
        elif (indice % 5 == 0):
            lista_numeros.append("Buzz")
        else:
            lista_numeros.append(f"{indice}")
        indice += 1 
    return lista_numeros

n = int(input())
print(analise(i, n, lista))