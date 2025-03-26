n = int(input("Digite um numero: "))

print("---------------------------------")
print("  Escolha a Base para Conversão  ")
print("[1] - para Binário")
print("[2] - para Octal")
print("[3] - para Hexadecimal")
r = int(input(""))

if r == 1:
    print(f"{n} convertido para binário é igual à {bin(n)[2:]}")
elif r == 2:
    print(f"{n} convertido para octal é igual à {oct(n)[2:]}")
elif r == 3:
    print(f"{n} convertido para hexadecimal é igual à {hex(n)[2:]}")
else:
    print("Opção Inválida")

