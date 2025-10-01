#Daily challenge freeCodeCamp
#Binary to Decimal

def to_decimal(binary):
    vetor = []
    for i in range(len(binary)):
        vetor.append(binary[i])

    vetor = vetor[::-1]
    s = 0

    for i in range(len(vetor)):
        x = int(vetor[i])*(2**i)
        s += x

    return s

print(to_decimal("101"))
print(to_decimal("1010"))
print(to_decimal("10010"))
print(to_decimal("1010101"))
