numero = int(input("Digite o número que você quer saber a tabuada: "))

print(f"Tabuada do {numero}")
print("---------------")
for x in range(1,11):
    print(f"{numero} x {x} = {numero*x}")

print("---------------")