#Interactive Help -> comando "help()" no terminal, possui toda a documentação das funções nativas, ou não, do python.
#Se eu quiser saber o que um comando faz eu posso colocar ele dentro do parenteses do help:
help(print)

#Docstrings -> Para funções que você criou, você precisa criar uma docstring para especificar o que ela faz, para isso e so colocar """ documentação """

def contador(i,f,p):
    '''
    Função que conta e mostra na tela
    :param i: Inicio
    :param f: Fim
    :param p: Passo
    :return: sem retorno
    '''

    c = i
    while c <= f:
        print(f"{c}", end="..")
        c += p
    print("FIM!")

help(contador)

#Paramêtros Opcionais -> Caso as vezes você precise definir um valor, e as vezes não, você pode usar isso
def soma(a,b,c=0):
    #se c não receber nenhum valor ele vai valer 0. Eu posso fazer isso tambem para a e b (a=0,b=0,c=0), assim chamadas sem parametros funcionariam.
    soma = a+b+c
    print(soma)

soma(3,6,9)
soma(8,4)

#Se eu quiser declarar um variavel global em um lugar que ela seria declarada como local eu coloco (global nome da variavel)
