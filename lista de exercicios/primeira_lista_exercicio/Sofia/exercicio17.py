alt=float(raw_input("Insira seu tamanho: "))
sexo=raw_input("Qual seu Sexo: ").lower()

if sexo =="f" or sexo=="feminino" :
	ideal=(62.1*alt)-44.7
	print("Seu peso ideal e: %.2f"%ideal)
elif sexo=="m" or sexo=="masculino":
	ideal(72.7*h)-58
	print("Seu peso ideal e: %.2f"%ideal)
else:
	print("Invalido!")
