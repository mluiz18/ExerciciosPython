expressao = str(input("Digite sua expressão: "))
parenteses = []

for x in expressao:
    if x == "(":
        parenteses.append("(")
    else:
        if x == ")":
            if len(parenteses) > 0:
                parenteses.pop()
            else:
                parenteses.append(")")
                break

if len(parenteses) == 0:
    print("Sua expressão é válida!")
else:
    print("Sua expressão é inválida!")