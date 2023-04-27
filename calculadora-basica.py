#Crie um programa que simule uma calculadora básica. O usuário deve digitar dois números
#e a operação que deseja realizar (+, -, *, /) e o programa deve retornar o resultado da operação.

print("*******************")
print("****CALCULADORA****")
print("*******************")

def calculadora():
    numero_entrada = int(input("Digite o primeiro valor: "))
    numero_entrada2 = int(input("Digite o segundo valor: "))
    tipo_operacao = input("Digite a operação que deseja para realizar o calculo (+, -, *, /): ")
    if tipo_operacao == "+":
        calculo = numero_entrada + numero_entrada2
    elif tipo_operacao == "-":
        calculo = numero_entrada - numero_entrada2
    elif tipo_operacao == "*":
        calculo = numero_entrada * numero_entrada2
    elif tipo_operacao == "/":
        calculo = numero_entrada / numero_entrada2
    print(round(calculo))

calculadora()

