def remover_especiais(palavra):
    especiais = ['.', '"', '(', '*', '$', '#', ':']
    for caracter in palavra:
        if(caracter not in especiais):
            palavra += caracter
        else:
            return palavra

while True:
    texto = input()
    if(texto == '-1'):
        break
    texto = texto.lower()