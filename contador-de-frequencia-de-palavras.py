#Crie um programa que leia um arquivo de texto
# e conte a frequência de cada palavra no arquivo.
def iniciar():
    contando_palavras_repetidas()

def contando_palavras_repetidas():
    escreve_frase = input("Escreva alguma frase: ").upper()
    frase_list = escreve_frase.split()
    frequencia = {}

    for palavra in frase_list:
        if palavra in frequencia:
            frequencia[palavra] += 1
        else:
            frequencia[palavra] = 1

    for palavra, quantidade in frequencia.items():
        print(f"{palavra}: {quantidade}")

iniciar()