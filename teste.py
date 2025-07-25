n = int(input("Digite um número: "))
f = 1
for i in range(n):
    f *= i+1

print(f"{n}! = {f}")