peso = float(input("Digite seu peso (em Kg): "))
altura = float(input("Digite sua altura (em metros): "))
IMC = peso / ( altura ** 2 )

print(f"Seu IMC é {IMC:.1f}")

if IMC < 18.5:
    print("Você está abaixo do peso!")
elif IMC >= 18.5 and IMC < 25:
    print("Você está no peso ideal!")
elif IMC >= 25 and IMC < 30:
    print("Você está sobrepeso!")
elif IMC >= 30 and IMC < 40:
    print("Você está obeso!")
else:
    print("Você com obesidade mórbida!")