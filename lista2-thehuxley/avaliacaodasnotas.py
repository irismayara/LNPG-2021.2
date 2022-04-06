# Escreva um programa para ler as resposta de uma turma em uma prova com 5 questões e, a partir do gabarito fornecido ao final, obter a maior nota, a menor nota e a média das notas da turma.

# Para cada aluno pode haver mais de uma resposta, prevalecendo a última,ou seja, a(s) resposta(s) anterior(es) devem ser desconsideradas, não entrando portando no cálculo da maior/menor nota e média da turma. Para isso, é fornecido o primeiro nome do aluno junto com sua resposta, separados por um espaço em branco.

# Para efeito de cálculo da nota do aluno, deve ser definida uma função chamada calcular_nota, a qual deve receber 2 parâmetros: a resposta do aluno e o gabarito da prova. Esta função deve retornar um valor inteiro que representa a nota do aluno (de 0 a 5).

# ENTRADA: O programa deve os dados das respostas dos alunos (Primeiro Nome e Respostas). O primeiro nome e as respostas às 5 questões são informadas na mesma linha e separadas por um espaço em branco. A leitura dos dados dos alunos se encerra quando é encontrado o caractere *. Na linha seguinte é fornecido o gabarito das 5 questões.

# SAIDA: A saída consiste de 3 linhas contendo, respectivamente: a maior nota (de 0 a 5), a menor menor nota (de 0 a 5) e a média das notas da turma (0.00 a 5.00). Observe que a média possui 2 casas decimais.


def calcular_nota(respostaAluno, gabarito):
    nota = 0
    i = 0
    for resposta in respostaAluno:
        if (resposta == gabarito[i]):
            nota += 1
        i += 1
    return nota

caderneta = []
while True:
    n = input()

    if (n == '*'):
        gabarito = input()

        for aluno in caderneta:
            respostaAluno = aluno[1]
            nota = calcular_nota(respostaAluno, gabarito)
            aluno.append(nota)
        
        maiornota = 0
        menornota = 5
        somanotas = 0

        for aluno in caderneta:
            if(aluno[2] > maiornota):
                maiornota = aluno[2]
            if(aluno[2] < menornota):
                menornota = aluno[2]
            
            somanotas += aluno[2]
        
        media = float(somanotas)/float(len(caderneta))
        print("Maior:", maiornota)
        print("Menor:", menornota)
        print("Media {:.2f}".format(media))

        break
    else:
        aluno = n.split()
        for a in caderneta:
            if(aluno[0] in a):
                caderneta.remove(a)
        caderneta.append(aluno)