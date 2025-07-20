#Tratamento de Erros e Exceções
#chamamos esses erros em vermelho de excessão

#print(x)
#NameError: name 'x' is not defined -> a variavel não foi inicializada!

#n = int(input("N: ")) # -> se eu digitar qualquer valor diferente de um inteiro ele me retorna um ValueError
#ValueError: invalid literal for int() with base 10: 'oito'

#a = int(input("Numerador: "))
#r = a/0 # Divisão por zero não existe no campo dos inteiros ou reais
#ZeroDivisionError: division by zero

b = "2"
#z = 2/b # Divisão de um número inteiro por uma string
#TypeError: unsupported operand type(s) for /: 'int' and 'str'

lst = [3,2,4]
#print(lst[3]) #Indice fora de alcance
#IndexError: list index out of range

#import uteis #Não existe o módulo uteis
#ModuleNotFoundError: No module named 'uteis'

#Essas são só algumas excessões, na documentação do python existe um monte
#Python docs: https://docs.python.org/3/library/exceptions.html

#Para tratar essas quantidades enormes de erros temos os comandos try e except

try: #um try pode ter varios except
    x = int(input("Numerador: "))
    y = int(input("Denominador: "))
    z = x/y
except Exception as erro: #se o try der errado | o exception ali vai ser tipo uma lib
    print(f"Erro: {erro}")
except (TypeError, ValueError):
    print(f"Tivemos um problema!")
#parte opcional:
else: #se o try der certo
    print(z)
finally: #independe se o try der certo ou errado, ele vai executar esse bloco de código
    print(":)")

