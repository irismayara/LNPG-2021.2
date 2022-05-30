#A Entidade ganhou vários blocos de encaixar, mas infelizmente, os blocos só se encaixam quando têm exatamente o mesmo tamanho. Ela quer encaixar os blocos de forma que consiga a menor quantidade de torres possível. Faça um programa que preveja o tamanho da maior torre e a quantidade de torres no final.

#A primeira linha da entrada terá um inteiro n (1 <= n <= 1000) indicando a quantidade de blocos a Entidade ganhou. Na linha seguinte, terão n inteiros h_i  (1 <= h_i <= 1000), representando o tamanho do i-ésima bloco.

#A saída deverá conter dois inteiros t e k, representando respecitvamente o tamanho da maior torre e quantas torres ficaram no final.

qtdeblocos = int(input())
blocos = input().split(' ')
blocos.sort()

torres = list()
torre = list()

maiortorre = 0

for i in range(qtdeblocos):
    torre.append(blocos[i])
    if(i < qtdeblocos - 1):
        if(blocos[i+1] != blocos[i]):
            torres.append(torre)
            torre = []
    elif(i == qtdeblocos - 1):
        torres.append(torre)

for i in torres:
    if(len(i) > maiortorre):
        maiortorre = len(i)

qtdetorres = len(torres)

print(torres)
print(maiortorre, qtdetorres)