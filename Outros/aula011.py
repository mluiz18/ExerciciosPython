#Modularização
#A Fim de manter minha sanidade mental, eu criei um novo projeto e testei a modularização lá
#Básicamente o que eu fiz foi: criar uma função em um arquivo e importar ela para outro com o import
#vale ressaltar que o recomendado é importar o modulo inteiro, mas caso os nomes não conflitem eu posso usar "from x import y"

#Pacotes = Bibliotecas que você baixa (tipo: pandas, numpy, matplot)
#quando você "instala" essas libs na verdade você está baixando um arquivo com todas essas funções ja feitas, ai e so importar

#outra coisa:
#arquivo (em python) = potencial modulo
#pasta (em python) = potencial pacotes
#ou seja, as pastas "Outros" ou "Faculdade", para o python são potenciais pacotes

#funções que eu tenho que importar nos exercicios futuros

def aumentar(n, a=0):
    novo_valor = n + (n * a)/100
    return novo_valor

def diminuir(n, d=0):
    novo_valor = n - (n * d) / 100
    return novo_valor

def dobro(n):
    return n * 2

def metade(n):
    return n / 2

def moeda(valor=0, moeda="R$", f=True):
    if f:
        return f"{moeda}{valor}"
    else:
        return valor