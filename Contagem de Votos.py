# Gabriel Araújo Ferraz de Melo (Gabriel.afm81@gmail.com)
# RM: 553011


# Minhas variaveis:

Dias_da_semana = ["segunda-feira", "terça-feira", "quarta-feira", "quinta-feira", "sexta-feira"]
Alunos = int(input("Quantos alunos irão votar?: "))
contagem = [0, 0, 0, 0, 0]
dia1 = 0
dia2 = 0
Votos1 = 0
Votos2 = 0

# Escolha do dia:

for Semana in range(Alunos):
    print("1 - Segunda / 2 - Terça / 3 - Quarta / 4 - Quinta / 5 - Sexta")
    voto = int(input("Escolha um dia da semana: "))

    if voto == 1:
        contagem[0] += 1
    elif voto == 2:
        contagem[1] += 1
    elif voto == 3:
        contagem[2] += 1
    elif voto == 4:
        contagem[3] += 1
    elif voto == 5:
        contagem[4] += 1

# Lógica da contagem, caso haja um dia vencedor:

print("Contagem final:")
for i in range(len(Dias_da_semana)):
    if contagem[i] > Votos1:
        Votos1 = contagem[i]
        dia1 = Dias_da_semana[i]
        print(Dias_da_semana[i], ":", contagem[i])
    elif contagem[i] > Votos2:
        Votos2 = contagem[i]
        dia2 = Dias_da_semana[i]
        print(Dias_da_semana[i], ":", contagem[i])
        print("Os outros dias não alcançaram votos suficientes para contabilizarmos!")
if Votos1 == Votos2:
    print("Empate! Dois dias empataram com", Votos1, "votos, tente novamente!.")
else:
    print(f"O dia em que ocorrerá as aulas será na {dia1} com {Votos1} votos. Obrigado por participar!")
