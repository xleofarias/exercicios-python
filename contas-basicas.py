#Crie um programa que peça ao usuário para digitar dois números e mostre a soma,
# a subtração, a multiplicação e a divisão desses números.

def inicia():
    primeiro_input = primeiro_valor()
    segundo_input = segundo_valor()
    calculos(primeiro_input, segundo_input)

def calculos(primeiro_input, segundo_input):
    soma = print("A soma de {} mais {} é = {} ".format(primeiro_input, segundo_input, primeiro_input + segundo_input))
    subtracao = print("A subtração de {} menos {} é = {} ".format(primeiro_input, segundo_input, primeiro_input - segundo_input))
    multiplicacao = print("A multiplicação de {} vezes {} é = {} ".format(primeiro_input, segundo_input, primeiro_input * segundo_input))
    divisao = print("A divisão de {} por {} é = {} ".format(primeiro_input, segundo_input, round(primeiro_input / segundo_input, 2)))
    return soma, subtracao, multiplicacao, divisao

def primeiro_valor():
    primeiro_input = int(input("Digite o primeiro valor: "))
    return primeiro_input

def segundo_valor():
    segundo_input = int(input("Digite o segundo valor: "))
    return segundo_input

inicia()
