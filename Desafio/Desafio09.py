# Número primo (de novo, sim!)

primo = int(input("Número: "))
c = 0
for i in range(1,primo+1):
    if primo % i == 0:
        c += 1

if c == 2 or primo == 1:
    print("É Primo")
else:
    print("Não é primo")