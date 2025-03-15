horastrabalhadas = float(input("Digite a quantidade de horas que você trabalhou essa semana: "))

if horastrabalhadas <= 40:
    salario = 15*horastrabalhadas
    print(f"Seu salário é de R$ {salario}")
else:
    salario = 600+(21*horastrabalhadas)
    print(f"Seu salário é de R$ {salario}")