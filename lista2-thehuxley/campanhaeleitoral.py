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
        custo = 1.500

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