valCasa = float(input("Qual o valor da casa? "))
salario = float(input("Qual o seu salário? "))
tempo =  float(input("Em quantos anos pretende quitar a casa? "))
parcelaMensal = valCasa/(tempo*12)
pMaxima = (salario*30/100)

if parcelaMensal > pMaxima:
    print("Empréstimo Negado!")
else:
    print("Empréstimo Aprovado!")

