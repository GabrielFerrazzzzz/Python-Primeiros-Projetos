# Gabriel Araújo Ferraz de Melo (Gabriel.afm81@gmail.com)
# RM: 553011


# Minhas variaveis:

cliente = ["Basic", "Silver", "Gold", "Platinium"]
Valor = float(input("Digite o seu faturamento mensal: "))
print("1 - Menos de 6 meses / 2 - 6 meses a 1 ano / 3 - 1 a 10 anos / 4 - Mais de 10 anos.")
tipo_assinatura = int(input("Quanto tempo você faz parte deste projeto?: "))
meses = 0

# Separando tipo do cliente por Valores e assinatura conosco:

if Valor > 5000:
    cliente = [cliente[3]]
elif Valor >= 3000 and Valor <= 5000:
    if tipo_assinatura == 4:
        cliente = [cliente[3]]
    else:
        cliente = [cliente[2]]
elif Valor >= 1000 and Valor < 3000:
    if tipo_assinatura == 3:
        cliente = [cliente[2]]
    else:
        cliente = [cliente[1]]
elif Valor >= 1000:
    if tipo_assinatura == 2:
        cliente = [cliente[1]]
    else:
        cliente = [cliente[0]]

# Separando o tipo do cliente independente do valor faturado, mas por tempo conosco: (FIDELIDADE)

    if tipo_assinatura == 3:
        [cliente[0]] = [cliente[1]]
    if tipo_assinatura == 4:
        [cliente[0]] = [cliente[2]]

# Lógica de mensagens por tipo de cliente:

if tipo_assinatura == 1:
    meses = int(input("Quantos meses você está com a gente?: "))
    print("Você é um cliente", cliente[0], f" e seu faturamente total é de {Valor * meses}R$")
    print(f"O valor a pagar de bonús é de {((Valor * meses) * 0.30):.2f}R$")
    print(f"O valor a receber é de {((Valor * meses) * 0.70):.2f}R$")
    print("Aumente o seu nivel para melhores recompensas")
elif tipo_assinatura == 2:
    meses = int(input("Quantos meses você está com a gente?: "))
    print("Você é um cliente", cliente[0], f" e seu faturamente total é de {Valor * meses}R$")
    print(f"O valor a pagar de bonús é de {((Valor * meses) * 0.20):.2f}R$")
    print(f"O valor a receber é de {((Valor * meses) * 0.80):.2f}R$")
    print("Aumente o seu nivel para melhores recompensas")
elif tipo_assinatura == 3:
    anos = int(input("Quantos anos você está com a gente?: "))
    print("Você é um cliente", cliente[0], f" e seu faturamente total é de {Valor * (anos * 12)}R$")
    print(f"O valor a pagar de bonús é de {((Valor * anos * 12) * 0.10):.2f}R$")
    print("Caro cliente", cliente[0], f"O valor a receber é de {((Valor * (anos * 12)) * 0.90):.2f}R$")
    print("Você está próximo ao nivel máximo, aumente o seu nivel para melhores recompensas")
elif tipo_assinatura == 4:
    anos = int(input("Quantos anos você está com a gente?: "))
    print(f"O seu faturamente total é de {Valor * (anos * 12)}R$")
    print(f"O valor a receber é de {((Valor * (anos * 12)) * 0.95):.2f}R$")
    print("Caro cliente ", cliente[0], f"O valor a pagar de bonús é de {((Valor * anos * 12) * 0.05):.2f}R$")
    print("Você é um cliente nivel máximo", cliente[0], ", continue assim")
else:
    print("Junte-se ao nosso time hoje mesmo. Seja Tech!")
