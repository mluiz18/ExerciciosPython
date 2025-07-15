#Funções
def mensagem(msg):
    print("-"*(len(msg)+6))
    print(f"{msg:>{len(msg)+3}}")
    print("-"*(len(msg)+6))

mensagem(str(input("Digite sua mensagem: ")))

#Empacotar paramentros (*num), básicamente, quando que tenho um tamanho diferente de parametros para uma mesma função eu uso isso
def contador(*num):
    return len(num)

print(contador(3,2,4,1,5))
print(contador(3,2,4))
