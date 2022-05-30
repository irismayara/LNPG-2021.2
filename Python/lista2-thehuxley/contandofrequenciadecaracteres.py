# Escreva um programa que receba um texto em uma única linha e imprima cada caractere e o número de vezes que ocorre no texto, na ordem inversa à alfabética.

# ENTRADA: Uma linha contendo qualquer caractere, que pode incluir letras, números, pontuação e caracteres especiais.

# SAIDA: Uma sequência linhas onde cada linha contém um caractere e seu respectivo número de ocorrências no texto. A sequência de caracteres segue a ordem alfabética decrescente.

txt = input()
texto = []
for caracter in txt:
    texto.append(caracter)

texto.sort()

unicos = []
for c in texto:
    if(c not in unicos):
        unicos.append(c)

unicos= unicos[::-1]
for c in unicos:
    print(c, texto.count(c))