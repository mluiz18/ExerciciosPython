s = 0
c = 0
for x in range(1,501,2):
    if x % 3 == 0:
        print(x)
        c += 1
        s = s + x

print(f"A Soma dos {c} números são {s}")