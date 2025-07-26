#soma de 1 a n

n = int(input("Número: "))

while n < 1:
    print("O Número precisa ser maior que 1!")
    n = int(input("Número: "))

s = 0
for i in range(1,n+1):
    s += i

print(f"A Soma de 1 até {n} é igual á {s}")