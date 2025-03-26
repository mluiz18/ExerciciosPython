ano_nascimento = int(input("Digite o ano em que você nasceu: "))
alistamento = 2025 - ano_nascimento

if alistamento > 18:
    print(f"Você tem {alistamento} anos, e ja passou {alistamento - 18} anos de se alistar.")
    print(f"Seu alistamento deveria ter sido em {ano_nascimento + 18}")
elif alistamento == 18:
    print(f"Você tem {alistamento} anos, e está na hora de se alistar.")
else:
    print(f"Você tem {alistamento} anos, e ainda faltam {(18 - alistamento)} ser alistar.")
    print(f"Seu alistamento deverá ser em {ano_nascimento + 18}")