# Uma agência de publicidade cria anúncios para candidatos em vários meios de comunicação. Os preços são calculados em função das mídias escolhidas, que podem ser: internet, rádio, tv, revista e outdoor.

# Anúncios para Internet custam R$ 3.000, para revista R$ 750 e para outdoor R$ 1.500;
# Anúncios para rádio custam R$ 500 se for para FM, e R$ 300 se for para AM;
# Anúncios para tv custam R$ 1.200 em horário regular (até 20h) e R$ 2000 em horário nobre (depois de 20h).

# Escreva um programa que calcule qual será o custo total da propaganda escolhida pelos candidatos.

# ENTRADA: O programa deve receber como entrada o primeiro nome do candidato junto com a quantidade de mídias em que deseja ter sua propaganda eleitoral divulgada. Nas linhas seguintes serão lidas as informações sobre os tipos de mídia que podem ser: internet, radio, tv, revista e outdoor. Quando houver informação adicional, esta será fornecida na linha seguinte (como no caso da rádio que pode ser fm ou am). O programa faz isso até que seja informado um candidato com

# SAIDA: A saída consiste de uma linha para cada candidato, contendo seu nome seguido do caractere dois pontos (:), um espaço em branco e o custo da propaganda (ponto flutuante com 2 casas decimais).

def calcMidia(midia):
    if(midia == 'internet'):
        custo = 3000
    elif(midia == 'radio'):
        tipo = input()
        if(tipo == 'am'):
            custo = 300
        elif(tipo == 'fm'):
            custo = 500
    elif(midia == 'tv'):
        horario = int(input())
        if(horario < 21):
            custo = 1200
        else:
            custo = 2000
    elif(midia == 'revista'):
        custo = 750
    elif(midia  == 'outdoor'):
        custo = 1500

    return custo

while True:
    n = input()
    if(n == 'FIM'):
        break

    candidato, qtdemidia = n.split(' ')
    qtdemidia = int(qtdemidia)
    custo = 0

    for i in range(qtdemidia):
        midia = input()
        custo += calcMidia(midia)

    print("{}: {:.2f}".format(candidato, custo))