# Leet é uma maneira de escrever palavras na qual algumas letras, sílabas ou palavras são substituídas por números ou símbolos. Isso é muito usado no contexto da informática para confundir leitores "não iniciados” ou escrever de forma resumida (por exemplo, na escrita de tweets). Dentro desse contexto, você vai escrever um programa que que transforma palavras na grafia comum em palavras na escrita Leet de forma invertida. Ao final, o programa deve informar a quantidade de substituições realizadas.

# Use a seguinte codificação:
# a, A: @
# e, E: 3
# i, I: 1
# o, O: 0
# t, T: 7
# s, S: 5

# Não haverão palavras acentuadas.
# Se o usuário informar uma string vazia, o programa emitirá uma mensagem de erro e a quantidade 0 (zero).
# Se o usuário informar uma string que contém pelo menos um número, o programa escreverá uma mensagem de erro e a quantidade 0 (zero).
# O código deve fazer uso de funções sempre que necessário, observando os princípios da modularização e separação de objetivos.

def codificar(string, codigos):
    for i in range(len(string)):
        for codigo in codigos:
            if(string[i] in codigo):
                string = string.replace(string[i], codigo[2])
    string = inverter(string)
    return string

def contarSubstituicoes(string, codigos):
    substituicoes = 0
    for i in range(len(string)):
        for codigo in codigos:
            if(string[i] in codigo):
                substituicoes += 1
    return substituicoes

def stringValida(string):
    if(isEmpty(string)):
        print("vazio")
        print("0")
    elif(hasNumber(string)):
        print("numeros")
        print("0")
    else:
        return True

def isEmpty(string):
    if(string == ''):
        return True

def hasNumber(string):
    numeros = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    for caracter in string:
        if(caracter in numeros):
            return True

def inverter(txt):
  return txt[::-1]

a = ['a','A', '@']
e = ['e', 'E', '3']
i = ['i', 'I', '1']
o = ['o', 'O', '0']
t = ['t', 'T', '7']
s = ['s', 'S', '5']
codigos = [a, e, i , o, t, s]

string = input()
if(stringValida(string)):
    leet = codificar(string, codigos)
    substituicoes = contarSubstituicoes(string, codigos)
    print(leet)
    print(substituicoes)