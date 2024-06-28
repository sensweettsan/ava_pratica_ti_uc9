'''
Questão 2: Implementar uma Calculadora com Loop
Escreva uma função chamada calculadora que recebe três argumentos: dois números (a e b) e uma string representando a operação (operacao). 
A função deve retornar o resultado da operação aplicada aos dois números. As operações suportadas são:

    + para adição
    - para subtração
    * para multiplicação
    / para divisão

A função deve lidar com a divisão por zero e retornar uma mensagem apropriada nesse caso.

Segue um trecho mostrando como deve ser implementada a função:
    def calculadora(a, b, operacao):
        if operacao == '+':
            return a + b


Na entrada dos números deve ser feito o tratamento de exceções, para que seja tratado os casos que não sejam digitados números.

O programa deve ficar em loop, solicitando ao usuário os valores e a operação até que o usuário digite s para sair.

Os números digitados devem ser armazenados em uma lista e depois de encerrar, mostrar a lista, o maior número, o menor número e a média dos números.

'''

def calculadora(a, b, operacao):
    if operacao == '+':
        return a + b
    elif operacao == '-':
        return a - b
    elif operacao == '*':
        return a * b
    elif operacao == '/':
        if b == 0:
            return "Erro: divisão por zero!"
        else:
            return a / b
    else:
        return "Operação inválida!"


numeros = []
    
while True:
    try:
            num1 = float(input("Digite o primeiro número (ou 's' para sair): "))
            if num1 == 's':
                break
            num2 = float(input("Digite o segundo número: "))
            operacao = input("Digite a operação (+, -, *, /): ")

            resultado = calculadora(num1, num2, operacao)
            print(f"Resultado: {resultado}")

            numeros.append(num1)
            numeros.append(num2)
        
    except ValueError:
            print("Entrada inválida. Por favor, digite um número válido.")
        
    except Exception as e:
            print(f"Ocorreu um erro: {e}")
    
    if numeros:
        print("\n=== Estatísticas dos números ===")
        print(f"Números digitados: {numeros}")
        print(f"Maior número: {max(numeros)}")
        print(f"Menor número: {min(numeros)}")
        print(f"Média dos números: {sum(numeros) / len(numeros)}")
