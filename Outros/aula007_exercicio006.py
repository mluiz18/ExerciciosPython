alunos = []
resp = "S"
while True:
    aluno = []
    nome = str(input("Nome: "))
    nota1 = float(input("Nota 1: "))
    nota2 = float(input("Nota 2: "))
    aluno.append(nome)
    aluno.append(nota1)
    aluno.append(nota2)
    alunos.append(aluno[:])
    resp = str(input("Quer continuar? [S/N] "))
    if resp in "Nn":
        break

print("-=" * 3, "Boletim Geral", "-=" * 3)
print("No.   Nome         Média")
for n, a in enumerate(alunos):
    print(f" {n}   ",   f"{a[0]}         ",f"{(a[1]+a[2])/2}")

mostrar_notas = int(input("Mostrar notas de qual aluno [999 interrompe]: "))
while mostrar_notas != 999:
    print(f"Notas de {alunos[mostrar_notas][0]}:\nNota 1: {alunos[mostrar_notas][1]}\nNota 2: {alunos[mostrar_notas][2]}")
    mostrar_notas = int(input("Mostrar notas de qual aluno [999 interrompe]: "))