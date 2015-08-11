notas = [8.0, 7.0, 9.0, 8.0]
i = 0
soma = 0
while i < len(notas):
    print("Nota {}: {}".format(i+1, notas[i]))
    soma = soma + notas[i]
    i += 1
print("media: ", soma/len(notas))
