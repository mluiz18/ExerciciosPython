numero = int(input("Digite um valor: "))
n_pares = 0
n_impares = 0
q_pares = 0
n_lidos = 0
q_numero = 0

if numero < 0:
    print("Número inválido")

while numero > 0:
    q_numero += 1
    n_lidos += numero
    if numero % 2 ==0 :
        n_pares += numero
        q_pares += 1
    else:
        if numero % 3 == 0:
            n_impares += numero
    numero = int(input("Digite um valor: "))

print(n_pares)
print(n_impares)
print(n_pares/q_pares)
print(n_lidos/q_numero)