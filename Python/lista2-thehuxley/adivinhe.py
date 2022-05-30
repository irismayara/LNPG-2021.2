def jogo():
    qtd_caractere = int(input())
    senha = input()
    parada = ''
    for i in range(qtd_caractere):
        parada += '0'

    while True:
        chute = input()
        E = 0
        B = 0
        if(chute == parada):
            break

        for i in range(qtd_caractere):
            if(chute[i] == senha[i]):
                E += 1
            elif(chute[i] in senha):
                B += 1

        print("({},{})".format(E, B))

        if(E == qtd_caractere):
            break

qtd_jogos = int(input())

while qtd_jogos != 0:
    jogo()
    qtd_jogos -= 1