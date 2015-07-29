metrosQuadrados=int(input("Quantos metros quadrados serão pintados: "))
if metrosQuadrados % 54 != 0 :
	numeroLatas = int ( metrosQuadrados / 54) + 1
else:
	numeroLatas = int(metrosQuadrados / 54)

valorTotal =  numeroLatas * 80


print("Numero  de latas: {:d} . Preco total: {:.2f}".format(numeroLatas, valorTotal))
