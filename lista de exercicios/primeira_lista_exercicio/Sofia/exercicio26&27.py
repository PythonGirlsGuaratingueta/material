hora=float(input("Valor por hora: R$ "))
horario=int(input("Quantidade de horas trabalhadas: "))

salarioBruto=hora*horario

impostoRenda=(salarioBruto*11)/100

inss=(salarioBruto*8)/100

sindicato=(salarioBruto*5)/100


salarioLiquido=salarioBruto-impostoRenda-inss-sindicato



print("Salario Bruto: R$ {:.2f}.\nImposto de Renda: {:.2f}.\nINSS: R$ {:.2f}.\nSindicato: R$ {:.2f}.\nSalario Final:{:.2f}".format(salarioBruto,impostoRenda,inss,sindicato,salarioLiquido))
