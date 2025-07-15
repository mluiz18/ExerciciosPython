from time import sleep
def contador(i,f,p):
    for x in range(i,f+p,p):
        print(f"{x}", end=" ")
        sleep(0.5)
    print()

print("Contagem de 1 até 10 de 1 em 1:", end=" ")
contador(1,10,1)

print("Contagem de 10 até 0 de 2 em 2:", end=" ")
contador(10,0,-2)

inicio = int(input("Inicio: "))
fim = int(input("Fim: "))
passo = int(input("Passo: "))
print("C)", end=" ")
contador(inicio,fim,passo)