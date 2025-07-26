#Fatorial (de novo)

fatorial = int(input("Fatorial: "))

f = 1
for i in range(1,fatorial+1):
    f *= i

print(f"{fatorial}! = {f}")