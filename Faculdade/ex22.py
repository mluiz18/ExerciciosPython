nome = str(input("Digite o nome do aluno: "))
nota1 = float(input("Digite uma nota do aluno: "))
nota2 = float(input("Digite uma nota do aluno: "))
nota3 = float(input("Digite uma nota do aluno: "))
frequencia = int(input("Digite a frequencia do aluno: "))
media = (3*nota1)+(5*nota2)+(2*nota3)/3

if frequencia < 15:
    print("Aluno reprovado!")
else:
    if media >= 6:
        print("Aluno Aprovado")
    else:
        print("O Aluno devera fazer prova final.")