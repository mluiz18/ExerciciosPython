nota = float(input("Digite a nota do aluno: "))

if nota >= 9 and nota <= 10:
    print("Conceito A")
else:
    if nota >= 7 and nota <= 8:
        print("Conceito B")
    else:
        if nota >= 5 and nota <= 6:
            print("Conceito C")
        else:
            print("conceito D")