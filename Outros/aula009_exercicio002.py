def mostrar_tela(txt):
    print("-" * (len(txt) + 6))
    print(f"{txt:>{len(txt) + 3}}")
    print("-" * (len(txt) + 6))

texto = str(input("Texto: "))
mostrar_tela(texto)