num1 = int(input("Digite um número: "))
num2 = int(input("Digite um número: "))
soma = num1 + num2


if num1 > 10 or num2 > 10:
    print("Escreva números maiores que 1 e menores que 10!")
else:
    if num1 < 1 or num2 < 1:
        print("Escreva números maiores que 1 e menores que 10!")
    else:
        if soma < 8:
            print((soma)/2)
        else:
            if soma == 8:
                print(num1*num2)
            else:
                if soma > 8:
                    if num1 > num2:
                        print(num1/num2)
                    else:
                        print(num2/num1)