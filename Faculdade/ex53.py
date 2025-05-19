def receber_vetore(vetor):
    negativos = 0
    for i in range(len(vetor)):
        if vetor[i] < 0:
            negativos += 1
    return negativos

lingangu = [10,-1,0,-9,4,-18,-18,81]

print(receber_vetore(lingangu))