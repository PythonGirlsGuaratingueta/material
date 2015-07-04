alt=float(input("Insira seu tamanho: "))
sexo=input("Qual seu Sexo: ").lower()
peso=float(input("Qual seu peso: "))

if sexo =="f" or sexo=="feminino" :
	ideal=int((62.1*alt)-44.7)
	
elif sexo=="m" or sexo=="masculino":
	ideal=int((72.7*h)-58)
    
else:
    print("Invalido!")

if peso==ideal:
    print("Voce esta dentro do peso ideal.")
elif peso>ideal:
    print ("Voce esta acima do peso ideal.Seu peso ideal é: {:.d}".format(ideal))
else:
    print ("Voce esta abaixo do peso ideal.Seu peso ideal é: {:.d}".format(ideal))
	
