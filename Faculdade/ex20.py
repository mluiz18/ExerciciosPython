tempo = int(input("Digite o tempo que o investimento ficou rendendo: "))

if tempo < 1:
    print("A Taxa de juros é de 0,55")
elif tempo >= 1 and tempo < 2:
    print("A Taxa de juros é de 0,65")
elif tempo >= 2 and tempo < 3:
    print("A Taxa de juros é de 0,75")
elif tempo >= 3 and tempo < 4:
    print("A Taxa de juros é de 0,85")
elif tempo >= 4 and tempo < 5:
    print("A Taxa de juros é de 0,90")
elif tempo >= 5:
    print("A Taxa de juros é de 0,95")