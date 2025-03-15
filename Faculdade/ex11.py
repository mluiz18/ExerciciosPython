nota = float(input("Digite uma nota: "))

if nota >= 60 and nota <= 100:
    print("Aprovado")
elif nota >= 0 and nota < 60:
    print("Reprovado")
else:
    print("Nota inválida")