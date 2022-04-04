#Periodicamente as crianças brasileiras devem tomar vacinas que as protegem de diversas doenças. Escrever um programa para ler o ano em que a criança toma a 1a dose e a periodicidade (intervalo em anos) da vacina e exibir em que outros anos a criança deve tomar as próximas doses desta vacina, sabendo que são 4(quatro) doses ao total.

dose1 = int(input())
periodicidade = int(input())

dose2 = dose1 + periodicidade
dose3 = dose2 + periodicidade
dose4 = dose3 + periodicidade

print(dose2,  dose3, dose4)