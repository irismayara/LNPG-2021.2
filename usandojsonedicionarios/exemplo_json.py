import json

with open('instituicoes-AL.json') as json_file:
    data = json.load(json_file)
    instituicoes = data['instituicoes']

    #print('Número de instituições: ', len(instituicoes))

    #for instituicao in instituicoes:
    #    print('NOME:', instituicao['nome'])
    #   if('telefone1' in instituicao):
    #        print('TELEFONE:', instituicao['telefone1'], '/', instituicao['telefone2'])
    #    if('email' in instituicao):
    #        print('E-MAIL:', instituicao['email'])
    #    print('CIDADE:', instituicao['endereco']['municipio'])
    #    print('----------------------------------------------------------')

    #exemplo 2 - digitar cidade e imprimir cursos desta

    municipio = input('Digite um municipio:')

    cursos = []
    for instituicao in instituicoes:
        if(municipio == instituicao['endereco']['municipio']):
            for curso in instituicao['cursos']:
                if(curso['nome'] not in cursos):
                    cursos.append(curso['nome'])

    for curso in cursos:
        print(curso)

    #exemplo 3 - digitar cep e imprimir curso e modalidade
        