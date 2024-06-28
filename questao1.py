'''
Questão 1: Escreva uma função chamada classificar_idade que recebe um número inteiro representando a idade de uma pessoa e 
retorna uma string que classifica a pessoa em uma das seguintes categorias:

1- "Criança" se a idade for menor que 12 anos.
2- "Adolescente" se a idade for entre 12 e 17 anos.
3- "Adulto" se a idade for entre 18 e 64 anos.
4- "Idoso" se a idade for 65 anos ou mais.


# Teste a função
print(classificar_idade(10))  # Saída esperada: Criança
print(classificar_idade(15))  # Saída esperada: Adolescente
print(classificar_idade(30))  # Saída esperada: Adulto
print(classificar_idade(70))  # Saída esperada: Idoso

'''

idade = int(input('Digite sua idade: '))

def classificar_idade(idade):
    if idade < 12:
        return 'criança'
    elif idade <= 17:
        return 'Adolesente'
    elif idade <= 64:
        return 'Adulto'
    else:
        return 'idoso'

print(classificar_idade(idade))





