carcteres = ["a", "z", "g", "y", "e", "h", "p", "o", "q","n"] 
i = 0
soma = 0
consoantes = []
while i < len(carcteres):
    if carcteres[i] != "a" and carcteres[i] != "e" and carcteres[i] != "i" and carcteres[i] != "o" and carcteres[i] != "u":
        soma = soma + 1
        consoantes.append(carcteres[i])
    i += 1
print("numero de consoantes {}".format(soma)) 
i = 0
while i < len(consoantes):
    #imprimindo na mesma linha
    #print(consoantes[i], end=" ")
    #ou
    print consoantes[i],
    i = i + 1
