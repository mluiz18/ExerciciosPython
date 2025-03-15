anonascimento = int(input("Digite o ano de nascimento: "))
anoatual = int(input("Digite em que ano estamos: "))
idade = anoatual - anonascimento

if idade >= 0 and idade <= 3:
    print(f"A Pessoa é um bebê com {idade} anos.")
elif idade > 3 and idade <= 11:
    print(f"A Pessoa é uma criança com {idade} anos.")
elif idade > 11 and idade <= 17:
    print(f"A Pessoa é um adolescente com {idade} anos.")
elif idade > 17 and idade <= 64:
    print(f"A Pessoa é um adulto com {idade} anos.")
elif idade > 65:
    print(f"A Pessoa é um idoso com {idade} anos.")