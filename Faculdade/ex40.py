n = int(input("Digite um valor: "))
menor_que_25 = 0
menor_que_50 = 0
menor_que_75 = 0
menor_que_100 = 0

while n > 0:
    if n > 0 and n <= 25:
        menor_que_25 += 1
    else:
        if n > 26 and n <= 50:
            menor_que_50 += 1
        else:
            if n > 50 and n <= 75:
                menor_que_75 += 1
            else:
                if n > 75 and n <= 100:
                    menor_que_100 += 1
    n = int(input("Digite um valor: "))

print(menor_que_25)
print(menor_que_50)
print(menor_que_75)
print(menor_que_100)