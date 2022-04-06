# Mega Sena – Crie duas listas com números de 0 a 9, embaralheas listas, e sorteie um número de cada uma para formar uma dezena, repita a operação mais 5 vezes, assim como na mega sena. Caso a dezena caia como 00 (zero, zero) faça o sorteio dela novamente até sair outra combinação. Depois disso exiba as dezenas sorteadas.
import random

unidade = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
dezena = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']

for i in range(6):
    random.shuffle(unidade)
    random.shuffle(dezena)
    sorteado = dezena[0] + unidade[0]
    if(sorteado == '00'):
        i -= 1
    print(sorteado, end=' ')