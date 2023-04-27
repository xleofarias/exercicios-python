#Tabuada
numero_tabuada = int(input("Qual tabuada que deseja?(digite o número) \n"))
tamanho_tabuada = int(input("Qual é o tamanho da tabuada? \n"))

print("TABUADA COMPLETA")

for multiplicacao in range(1,tamanho_tabuada + 1):
    resultado = numero_tabuada * multiplicacao
    print("{} vezes {} é {}".format(numero_tabuada, multiplicacao, resultado))

