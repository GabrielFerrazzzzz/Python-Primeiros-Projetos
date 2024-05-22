# Gabriel Araújo Ferraz de Melo (Gabriel.afm81@gmail.com)
# RM: 553011


# Minhas variaveis

turma = int(input("Quantos alunos tem na sua sala?: "))
alunos_pares = 0
alunos_impares = 0
Nota_par = 0
Nota_Impar = 0
media_impar = 0
media_par = 0
nota_total_impar = 0
nota_total_par = 0

# Calculo para saber se o aluno é um aluno impar ou par :

for numero in range(1, turma + 1):
    if numero % 2 == 1:
        Nota_Impar = float(input("Este aluno é um aluno impar! Por favor, digite a nota deste aluno: "))  # True
        if Nota_Impar > 10 or Nota_Impar < 0:
            print("Nota invalida, tente novamente!")
            break
        nota_total_impar += Nota_Impar
        alunos_impares += 1
    else:
        Nota_par = float(input("Este aluno é um aluno par! Por favor, digite a nota deste aluno: "))  # False
        if Nota_par > 10 or Nota_par < 0:
            print("Nota invalida, tente novamente!")
            break
        nota_total_par += Nota_par
        alunos_pares += 1

# Calculo de média:

media_impar = nota_total_impar / alunos_impares
print(f"A média dos alunos ímpares é de {media_impar:.2f}")
media_par = nota_total_par / alunos_pares
print(f"A media dos alunos pares é de {media_par:.2f}")

# Logica para a média:

if media_impar > media_par:
    print("Os alunos impares são os vencedores")
elif media_impar < media_par:
    print("Os alunos pares são os vencedores")
elif media_impar == media_par:
    print("Houve um empate!")
