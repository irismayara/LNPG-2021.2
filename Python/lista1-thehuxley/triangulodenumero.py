#Faça um programa que dado um número inteiro n, imprima n linhas, onde cada linha deve seguir o seguinte padrão:
#1
#22
#333
#4444
#55555
#666666
#7777777
#…
#nnnnnnnnnn

n = int(input())

for i in range(1, n + 1): 
    for j in range(1, i + 1):
        print(i, end="")
    print("")