qtcompetidores, qtvoltas = input().split(' ')
qtcompetidores = int(qtcompetidores)
qtvoltas = int(qtvoltas)

corrida = []
ganhador = 1

for competidor in range(qtcompetidores):
    tempo = input().split(' ')
    for i in range(len(tempo)):
        tempo[i] = int(tempo[i])
    corrida.append([competidor, sum(tempo)])
    menortempo = sum(tempo)

for i in corrida:
    if(i[1] < menortempo):
        menortempo = i[1]
        ganhador = i[0] + 1
        
print(ganhador)