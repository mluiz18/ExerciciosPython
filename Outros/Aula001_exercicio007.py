a = float(input("Digite um lado do triângulo: "))
b = float(input("Digite outro lado do triângulo: "))
c = float(input("Digite outro lado do triângulo: "))

if a + b > c and b + c > a and a + c > b:
    if a == b and a == c:
        print("Você pode formar um triângulo equilátero")
    elif a == b and a != c or a == c and a != b:
        print("Você pode formar um triângulo isósceles")
    else:
        print("Você pode formar um triângulo escaleno")
else:
    print("Você não pode formar um triângulo com esses segmentos!")

