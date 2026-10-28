inteiro = int(input())

if inteiro % 2 == 0:
    inteiro += 1

for i in range(6):
    print(inteiro + 2 * i)

# outro metodo

x = int(input())
impressos = 0
while impressos < 6:
    if x % 2 != 0:
        print(x)
        impressos += 1
    x += 1