salario = int(input("Digite seu salário: "))
aumento = int(input("Digite a porcentagem de aumento: "))
newSal = salario + (salario*aumento/100)
print(f"O Seu novo salário será de {newSal}! Você terá um aumento de {newSal - salario} reais.")