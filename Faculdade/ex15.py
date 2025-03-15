salario = float(input("Digite seu salário atual: "))
tempodeservico = int(input("Digite o tempo em que você trabalha: "))

if tempodeservico <= 1:
    print(f"Seu novo salário será R${(salario + (salario*10)/100)}")
else:
    print(f"Seu novo salário será R${salario + (salario*20)/100}")