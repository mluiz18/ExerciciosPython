from datetime import datetime

def verificador_de_voto(nasc):
    """
    Função que retorna se a pessoa é obrigada a votar, tem o voto opcional ou não pode votar
    :param nasc: ano de nascimento
    :return: valor literal
    """
    idade = datetime.now().year - nasc
    if idade < 16:
        return False
    else:
        if idade >= 16 and idade < 18:
            return True
        else:
            return True

nascimento = int(input("Ano de nascimento: "))

if not verificador_de_voto(nascimento):
    print(f"A sua idade ({datetime.now().year - nascimento} anos) não está apta a votar!")
else:
    if verificador_de_voto(nascimento) and datetime.now().year - nascimento < 18:
        print(f"A Sua idade ({datetime.now().year - nascimento} anos) tem o voto opcional")
    else:
        if verificador_de_voto(nascimento) and datetime.now().year - nascimento >= 18:
            print(f"A Sua idade ({datetime.now().year - nascimento} anos) tem voto obrigatório")