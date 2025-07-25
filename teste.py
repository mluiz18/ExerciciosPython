n = int(input("Digite um número: "))
s = 0

if n < 1:
    for i in range(n,1):
        s += i
else:
    for i in range(1,n+1):
        s += i

print(f"A Soma de todos os número de 1 até {n} é {s}")