#Ester está programando suas férias e decidiu viajar gastando no máximo R$ 300 de passagens (ida e volta). Para usar bem seu dinheiro, ela quer ir para a cidade mais longe possível sem extrapolar seu orçamento. Escreva um programa que receba como entrada o nome, a distância (em quilômetros) e o valor da passagem (só ida) de várias cidades, até que ela informe a cidade FIM, e exiba o nome do melhor destino para ela.

#Obs: Considere que as passagens de ida e de volta tenham o mesmo valor

#ENTRADA: Um String (que pode estar escrito de qualquer forma), um inteiro (km) e um real para cada cidade. Para encerrar a entrada, será informado o String FIM (escrito de qualquer forma) como nome da cidade

#SAIDA: Um String com as letras todas maiúsculas. Se nenhuma cidade for informada, deverá ser exibida a mensagem SEM DESTINO
opcoes = []
while True:
    destino = input()
    destino = destino.upper()
    if(destino == "FIM"):
        for opcao in opcoes:
            if(opcao[2] * 2 <= 300):
                if(opcao[1] > maiordistancia):
                    maiordistancia = opcao[1]
                    destinoescolhido = opcao[0]      
        print(destinoescolhido)      
        break
    distancia = int(input())
    passagem = int(input())
    opcoes.append([destino, distancia, passagem])
    maiordistancia = distancia
