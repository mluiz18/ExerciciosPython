num1 = int(input("Digite um número: "))
num2 = int(input("Digite um número: "))
num3 = int(input("Digite um número: "))
num4 = int(input("Digite um número: "))

if num1 < num2 and num1 < num3 and num1 < num4:
    print(f"O número {num1} é o menor")
elif num2 < num1 and num2 < num3 and num2 < num4:
    print(f"O número {num2} é o menor")
elif num3 < num1 and num3 < num2 and num3 < num4:
    print(f"O número {num3} é o menor")
else:
    print(f"O número {num4} é o menor")