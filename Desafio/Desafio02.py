#Fatorial

n = int(input("Numero: "))
f = 1
for i in range(1,n+1):
    f *= i

print(f"{n}! = {f}")