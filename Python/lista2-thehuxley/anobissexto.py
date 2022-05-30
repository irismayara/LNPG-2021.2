#Estamos no ano de 2152.
# Você foi contratado(a) para criar um programa que utilize funções para indicar se um determinado ano é ou não bissexto. Para cada ano fornecido ao programa, faz-se necessário, primeiro, identificar se o ano fornecido é um valor inteiro de 4 dígitos e, segundo, dado que o ano é um número válido, informar se é ou não um ano bissexto. 
# Um ano é bissexto se ele satisfaz as seguintes condições:
# É divisível por 4 e,
# Não é divisível por 100 ou é divisível por 400.
# Seu programa deve ter na solução três funções (3): contarDigitos, ehBissexto e Mensagem. A quantidade de parâmetros e retornos das funções ficam a critério do(a) programador(a).
# 
# A entrada consiste numa lista de valores por linha. A entrada -1 indica o fim do programa.


# from datetime import date

def contarDigitos(valor):
    if(valor/1000 > 1 and valor//1000 < 10):
        return True
    else:
        return False

def ehBissexto(ano):
    if((ano % 4 == 0) and ((ano % 100 != 0) or (ano % 400 == 0))):
        return True
    else:
        return False

def Mensagem(ano, anoValido, anoBissexto):
    #anoAtual = int(date.today().strftime('%Y'))
    anoAtual = 2152
    if(anoValido):
        if(anoBissexto):
            if(ano == anoAtual):
                print("O ano", ano, "eh bissexto")
            elif(ano < anoAtual):
                print("O ano", ano, "foi bissexto")
            else:
                print("O ano", ano, "serah bissexto")
        else:
            print("O ano", ano, "NAO eh bissexto")
    else:
        print("Ano invalido")

while True:
    ano = int(input())
    if(ano == -1):
        break
    anoValido = contarDigitos(ano)
    anoBissexto = ehBissexto(ano)
    Mensagem(ano, anoValido, anoBissexto)