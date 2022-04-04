#Seu objetivo é escrever um programa que calcule a soma dos elementos dados na entrada.

#A entrada consiste de um número inteiro n indicando a quantidade de elementos a serem lidos seguidos de n elementos, um em cada linha.

#A saída consiste de um número inteiro indicando a soma, seguido de um final de linha.


n = int(input()) #quantidade de valores a serem lidos e somados
soma = 0

for i in range(n):
    soma += int(input())

print(soma)