import locale
locale.setlocale(locale.LC_MONETARY,"pt-pt.UTF-8")


def converta_real_em_euro(valor_em_real):
    euro_hoje = 0.18 #que é equivalente a 1 (R$) real
    valor_em_euro = valor_em_real * euro_hoje
    return valor_em_euro

valor_em_real = float(input("Digite o valor em reais que deseja converte em Euro: "))
valor_convertido = converta_real_em_euro(valor_em_real)
valor_convertido_formato = locale.currency(valor_convertido)
print(valor_convertido_formato)