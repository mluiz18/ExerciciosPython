lanche = ["Hamburguer", "Suco", "Pizza", "Pudim"]
lanche[3] = "Picole"
print(lanche)

# .append("Oq vc quiser adicionar") adiciona um valor a lista
lanche.append("Batata Frita")
print(lanche)

# .insert("Posição que você quer adicionar", "O que vc quer adicionar") adiciona um valor a lista na posição que você quiser
lanche.insert(2, "Cachorro Quente")
print(lanche)

# Formas de remover um valor de uma lista:

# del lanche["Posição do valor que você quer apagar"]
del lanche[2]
print(lanche)

# lanche.pop("Posição do valor que você quer apagar") remove um valor de uma posição
lanche.pop() # O comando .pop() sem paramêtro remove o ultimo elemento, mas você pode passar dentro dos () a posição do item que quer remover
print(lanche)

# lanche.remove("O Item que você quer remover")
lanche.remove("Suco")
print(lanche)

if "Picole" in lanche:
    lanche.remove("Picole")
    print(lanche)

# Você pode criar listas com o range():
# nome_da_lista = list(range(4,11))

valores = list(range(4,11))
print(f"Lista com valores gerados pelo range(): {valores}")

# Para ordernar uma lista eu posso usar o metodo .sort()
val = [8,2,4,3,1,0,9,6,5,7]
val.sort()
print(val)

# Se eu quiser ordenar de forma decrescente eu uso o .sort(reverse=True)
val.sort(reverse=True)
print(val)

# Se eu quiser saber o tamanho de uma lista, eu uso o comando len()
print(len(val))

# Se eu quiser mostrar os valores de forma bonitinha, eu crio um loop com o for
for v in val:
    if v == len(val):
        print(v)
    else:
        print(v, end=", ")

# Se eu quiser mostrar os indices, eu uso o enumerate
for c, v in enumerate(val):
    print(f"Indice: {c}, Valor = {v}")

# Para passa todos os valores de uma lista para outra, eu posso, ou criar um for, ou simplismente b = a[:]
a = [[2,0,1,9], [0,2,1,2]]
b = a[:]
print(b)
# Eu não posso fazer b = a, por que o python vai fazer uma ligação entre as duas listas me impedindo de modificar somente uma
