while True:
    idade = int(input())
    if(idade == 0):
        break
    elif(idade < 0):
        print("Pessoa ainda não nasceu")
    elif(idade < 12):
        print("Você é uma criança")
    elif(idade < 18):
        print("Você é um adolescente")
    elif(idade < 36):
        print("Você é um jovem")
    elif(idade < 65):
        print("Você é um adulto")
    elif(idade > 64):
        print("Você é um idoso")
