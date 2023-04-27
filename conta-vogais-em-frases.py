#Crie um programa que leia uma frase e retorne a quantidade de vogais na frase.

def conta_vogais():
    frase = input("Digite uma frase: ").lower()
    vogais = "aeiou".lower()
    count = 0
    for letra in frase:
        if letra in vogais:
            count += 1
    print("Tem {} vogais na frase {}".format(count, frase))

conta_vogais()


