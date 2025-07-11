boletim = {}
boletim["Nome"] = str(input("Nome: "))
boletim["Média"] = float(input("Média: "))


if boletim["Média"] >= 7:
    boletim["status"] = "Aprovado"
else:
    if boletim["Média"] >= 5:
        boletim["status"] = "Recuperação"
    else:
        if boletim["Média"] >= 0:
            boletim["status"] = "Reprovado"
        else:
            boletim["Média"] = "Média Inválida"
            boletim["status"] = "Média Inválida"

print("-="*3, f"Boletim do {boletim['Nome']}", "-="*3)
for k, v in boletim.items():
    print(f"{k}: {v}")