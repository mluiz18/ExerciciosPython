#Número Primo

def numero_primo(n):
    c = 0
    for i in range(1,n+1):
        if n % i == 0:
            c+=1

    if c == 2:
        print(f"O Número {n} É primo!")
    else:
        print(f"O Número {n} NÃO é primo!")

numero_primo(4)