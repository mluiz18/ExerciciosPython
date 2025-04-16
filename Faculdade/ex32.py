salario = float(input("Digite seu salário: "))
filhos = int(input("Digite quantos filhos: "))
somasalario = salario
quantidadesalario = 1
somafilhos = filhos
quantidadefilhos = 1
maior_salario = salario

while salario >= 0:
    salario = float(input("Digite seu salário: "))
    filhos = int(input("Digite quantos filhos: "))
    somasalario += salario
    quantidadesalario += 1
    somafilhos += somafilhos
    quantidadefilhos += 1
    if salario > maior_salario:
        maior_salario = salario

print(f"A Média salarial da população é {somasalario+1/quantidadesalario}")
print(f"A Média de filhos da população é {somafilhos/quantidadefilhos}")
print(f"O Maior salário é {maior_salario}")
