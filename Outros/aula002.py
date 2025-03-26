i = int(input("Digite o ínicio: "))
f = int(input("Digite o fim: "))
p = int(input("Digite o passo: "))

s = 0
for x in range(i , f+1, p):
    n = int(input("Digite um número: "))
    s += n
print(f"O Somátorio é {s}")
print("Fim")

#25:45