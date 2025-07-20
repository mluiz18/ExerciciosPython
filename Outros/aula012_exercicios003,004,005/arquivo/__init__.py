from os import write


def arqExiste(doc):
    try:
        a = open(doc, "rt")
        a.close()
    except FileNotFoundError:
        return False
    else:
        return True

def criarArquivo(nome):
    try:
        a = open(nome, "wt+")
        a.close()
    except:
        print("Houve um erro ao criar o arquivo!")
    else:
        print("Arquivo Criado com sucesso!")

def lerArquivo(nome):
    try:
        a = open(nome, "rt")
    except:
        print("Erro ao ler o arquivo!")
    else:
        print(f"{"NOME":<33} {"IDADE":>1}")
        for linha in a:
            dados = linha.split(";")
            dados[1] = dados[1].replace("\n", "")
            print(f"{dados[0]:<30} {dados[1]:>3} anos")
    finally:
        a.close()

def cadastroArq(arq, nome="", idade=0):
    try:
        a = open(arq, "at")
    except:
        print("Erro ao abrir o arquivo!")
    else:
        try:
            a.write(f"{nome};{idade}\n")
        except:
            print("Erro ao cadastrar a pessoa!")
        else:
            print(f"Registro de {nome} confirmado!")
    finally:
        a.close()