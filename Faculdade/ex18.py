salario = float(input("Digite seu salário: "))
financiamento = float(input("Digite o valor do financiamento pretendido: "))

if financiamento <= (salario*5):
    print("Financiamento Concecido")
else:
    print("Financiamento Negado")