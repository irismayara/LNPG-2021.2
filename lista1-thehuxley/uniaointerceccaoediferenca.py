#Faça um programa que receba os elementos de 2 vetores e imprima na saída a união, a interseção e a diferença entre os 2 vetores.

#No começo o usuário informa 2 inteiros que determinam a quantidade de elementos dos 2 vetores. Em seguida, o usuário informa os elementos do vetor.

#As saídas são os conjuntos união, interseção e diferença entre os vetores de acordo com os exemplos.

lenvetor1 = int(input())
lenvetor2 = int(input())

v1 = []
v2 = []
uniao = []
interceccao = []
diferenca = []

for i in range(lenvetor1):
    v1.append(input())

for i in range(lenvetor2):
    v2.append(input())

for i in v2:
    if (i not in uniao):
        uniao.append(i)
for i in v1:
    if (i not in uniao):
        uniao.append(i)
    else:
        interceccao.append(i)     

for i in v1:
    if(i not in interceccao):
        diferenca.append(i)

print(uniao)
print(interceccao)
print(diferenca)