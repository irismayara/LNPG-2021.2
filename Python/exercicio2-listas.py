# Marilda é bem desorganizada, mas muito festeira. Por isso toda festa que Marilda organiza é uma confusão. Não sabe direito quem convidou. Você pode ajudar Marilda. Escreva um programa para registrar os convidados da festa. O programa só precisa receber um número com a quantidade de convidados e depois deixar o usuários digitar os nomes dos convidados.Por último o programa deve imprimir a lista de convidados em ordem alfabética

quantidade_convidados = int(input("Digite a quantidade de convidados da festa: "))
convidados = []

for i in range(quantidade_convidados):
    convidado = input()
    convidados.append(convidado)

convidados.sort()
print(convidados)