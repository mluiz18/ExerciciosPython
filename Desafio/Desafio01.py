#Sequencia de Fibonacci

c = 0
primeiro = 0
segundo = 1
terceiro = primeiro + segundo
print(1)
print(1)
for i in range(c,10):
    primeiro = segundo
    segundo = terceiro
    terceiro = primeiro + segundo
    print(terceiro)
