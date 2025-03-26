ano_nascimento = int(input("Digite o ano de nascimento: "))
idade = 2025 - ano_nascimento
print(f"O Atleta tem {idade} anos")
if idade <= 9:
    print("Você está na categoria MIRIN")
elif idade > 9 and idade <= 14:
    print("Você está na categoria INFANTIL")
elif idade > 14 and idade <= 19:
    print("Você está na categoria JUVENIL")
elif idade > 19 and idade<= 20:
    print("Você está na categoria SÊNIOR")
else:
    print("Você está na categoria MASTER")