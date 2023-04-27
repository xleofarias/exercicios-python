import locale

def menu():
    print("número", "código_moeda", "tipo_moeda", sep="     ")
    print("  1. ","    en-US", "     Dólar", sep="     ")
    print("  2. ","    ja-JP","     Iene", sep="     ")
    print("  3. ","    pt-PT", "     Euro", sep="     ")

def valor_moedas():
    dolar_hoje = 0.2
    euro_hoje = 0.18
    iene_hoje = 26.91
    return dolar_hoje, euro_hoje, iene_hoje

def escolha_moeda(dolar_hoje, iene_hoje, euro_hoje):
    moeda_escolhida = float(input("Digite o tipo de moeda que deseja usando o número acima: "))
    while moeda_escolhida < 1 or moeda_escolhida > 3:
        moeda_escolhida= float(input("Digite um número de 1 a 3, como mostrado no menu: "))

    if moeda_escolhida == 1:
        moeda_escolhida = dolar_hoje
        locale.setlocale(locale.LC_MONETARY, "en-US.UTF-8")
        print("A moeda escolhida foi Dolar")
    elif moeda_escolhida == 2:
        moeda_escolhida = iene_hoje
        locale.setlocale(locale.LC_MONETARY, "ja-JP.UTF-8")
        print("O tipo de moeda escolhida foi Iene")
    elif moeda_escolhida == 3:
        moeda_escolhida = euro_hoje
        locale.setlocale(locale.LC_MONETARY, 'pt-PT.UTF-8')
        print("O tipo de moeda escolhida foi Euro")

    return moeda_escolhida

def valor_convertido(moeda_escolhida):
    valor_em_real = float(input("Quantos reais você deseja converte? "))
    converte_moeda_em_real = moeda_escolhida * valor_em_real
    valor_formatado = locale.currency(converte_moeda_em_real, grouping= True)
    print(valor_formatado)

menu()
dolar_hoje, euro_hoje, iene_hoje = valor_moedas()
moeda_escolhida = escolha_moeda(dolar_hoje, iene_hoje, euro_hoje)
valor_convertido(moeda_escolhida)