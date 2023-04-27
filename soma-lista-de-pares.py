#Crie um programa que leia uma lista de números
# e retorne a soma de todos os números pares na lista.

lista_numeros = [10,4,3,13,2,8,5]
pares = []

print("Lista sem filtro")
print(lista_numeros)

print("Lista com filtro só de pares")
for numero in lista_numeros:
    if numero % 2 == 0:
        pares.append(numero)

print(pares)

print("A soma dos pares")
soma = print(sum(pares))