peso=int(input("Insira o peso do peixe: "))
excedente=0
multa=0
if peso>50:
	excedente=peso-50
	multa=excedente*4

if peso>50:
	print("\n\nPeso excedente: {:d}.\n".format(excedente))
	print("Multa por Peso excedente: R$ {:d},00."
	.format(multa))
else:
	print("Peso excedente: {:d}.\n".format(excedente))
	print("Multa por Peso excedente: R$ {:d},00."
	.format(multa))
