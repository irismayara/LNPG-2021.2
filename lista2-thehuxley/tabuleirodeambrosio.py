#Ambrósio comprou um novo jogo de tabuleiro que veio com peças faltando e decidiu joga-lo de outro jeito: Cada rodada o jogador deve rolar o dado para definir o número de casas que irá se mover, porém o dado está viciado e sempre dá o resultado na sequência 1, 2, 3, 4, 5, 6, 1, 2, ...
#O jogador começa na casa 1 (um), e se ultrapassar a ultima casa, deve retornar à primeira e continuar a andar o número de casas restantes, até parar exatamente na ultima.
#Supondo que o número de casas seja 8 (oito), o jogador ocupará as seguintes posições:
#1>2>4>7>3>8
#Como em alguns casos o número de jogadas pode ser grande, você deve ajudar Ambrósio a descobri-lo.

#ENTRADA: Um inteiro N que representa a ultima casa do tabuleiro. (4 <= N < 10000)

#SAIDA: O número necessário de jogadas para conseguir chegar à ultima casa.