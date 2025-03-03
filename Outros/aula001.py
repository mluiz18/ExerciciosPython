name = str(input("Digite seu nome: ")).title().strip()

if name == "Miguel":
    print("Um belo nome!")
elif name == "Theo" or name == "Ravi":
    print("Seu nome é bem popular no Brasil.")
elif name == "Arthur":
    print("Pague o que me deve.")
else:
    print("Um bom nome.")

print(f"Prazer em te conhecer, {name}!")