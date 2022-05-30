# Uma determinada professora quer treinar as pessoas para que elas saibam em que faixa etária elas estão. Para isso ela lhe pede que faça um programa que leia a idade das pessoas e indiquem qual sua faixa etária. O programa deve parar quando é feita a leitura da idade 0. 

# Para as demais idades a saída deve ser: 
# Idade: de 01 a 11 anos - Saída: "Você é uma criança" 
# Idade: de 12 a 17 anos - Saída: "Você é um adolescente" 
# Idade: de 18 a 35 anos - Saída: "Você é um jovem"
# Idade: de 36 a 64 anos - Saída: "Você é um adulto"
# Idade: acima de 65 anos - Saída: "Você é um idoso"

#obs: Quando for digitado uma idade negativa, é preciso informar que a pessoa ainda não nasceu.  

# ENTRADA: Idades aleatórias, termina a digitação com 0.
# SAIDA: Faixa etária de acordo com a idade da entrada.

while True:
    idade = int(input())
    if(idade == 0):
        break
    elif(idade < 0):
        print("Você ainda não nasceu.")
    elif(idade < 12):
        print("Você é uma criança.")
    elif(idade < 18):
        print("Você é um adolescente.")
    elif(idade < 36):
        print("Você é um jovem.")
    elif(idade < 65):
        print("Você é um adulto.")
    elif(idade > 64):
        print("Você é um idoso.")