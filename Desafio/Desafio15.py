senha = str(input("Digite sua senha: "))

if len(senha) < 8:
    print("Digite uma senha com pelo menos 8 caracteres!")
else:
    if senha.islower():
        print("Digite uma senha com pelo menos 1 letra maiúscula!")
    else:
        if senha.isalpha():
            print("Digite uma senha com pelo menos 1 número!")
        else:
            print("Senha aprovada com sucesso!")