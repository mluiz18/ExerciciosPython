nota_um = float(input("Digite a primeira nota: "))
nota_dois = float(input("Digite a segunda nota: "))
media = (nota_um + nota_dois)/2

if media < 5:
    print(f"A Sua média é {media}, e você está REPROVADO!")
elif media >= 5 and media <= 6.9:
    print(f"A Sua média é {media}, e você está de RECUPERAÇÃO!")
else:
    print(f"A Sua média é {media}, e você está APROVADO!")