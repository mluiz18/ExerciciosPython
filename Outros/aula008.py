#Dicionários são indentificados por chaves {} ou dict()
dados = {"nome": "Pedro", "idade": 25}
print(dados["nome"])
print(dados["idade"])

#Para criar um novo elemento dentro de um dicionario basta eu declarar ele no parenteses
dados["sexo"] = "Masculino"
print(dados)

#Para remover elementos, se usa o comando "del"
del dados["sexo"]
print(dados)

#Para mudar o valor e igual variável
dados["nome"] = "Miguel"
print(dados)
print(dados["nome"])

#Existe um diferença entre itens, chaves e valores, por exemplo:
#o comando .values() me retorna todos os valores de um dicionario

filme = {
    "Titulo": "Star Wars",
    "Ano": 1977,
    "Diretor": "George Lucas"
}

print(f"os valores do dicionário Filme são: {filme.values()}")

#As "Keys" me retornam quais os indices eu tenho no dicionario
print(f"as keys do dicionário Filme são: {filme.keys()}")

#Os itens são as Keys e os Values
print(f"os itens do dicionário Filme são: {filme.items()}")

#Eu posso usar isso em loops
for k, v in filme.items():
    print(f"O {k} é {v}")

#Eu posso colocar essa lista, em um vetor por exemplo.

dados = {"nome": "Pedro", "idade": 25}
#Se eu quiser colocar um dicionario dentro de um print formatado eu tenho que colocar em aspas simples ''
print(f"O {dados['nome']} tem {dados['idade']} anos.")

#Para copiar um dicionario eu utilizo o metodo .copy(), ja que não posso fazer o fatimento [:]
ser = []
ser.append(dados.copy())
print(ser)

#Para ordenar um dicionario eu, crio outra lista e uso a função sorted + uma função importada chamada itemgetter (from operator import itemgetter)
# o comando fica assim:
# lista = sorted(lista_original.items(), key = itemgetter(coluna que eu quero usar como parametro))
# o resultado fica igual a uma lista