"""
Agenda exemplo
"""
agenda = {}
while(True):
    print()
    print("*****************************")
    print("g >> gravar um novo contato")
    print("r >> resgatar um contato")
    print("x >> Sair da agenda")
    print()
    print("*****************************")
    controle = input("Qual a opção que deseja fazer?: ")
    if controle == "g":
        nome = input("Digite o nome: ")
        agenda[nome] = input("Digite o telefone: ")
        print()
        print("*****************************")
        print("Cadastro realizado com sucesso!")
    elif controle == "r":
        busca = input("Para busca digite um nome: ")
        if (busca in agenda):
            print(busca, "telefone: ",agenda[busca])
        else:
            print("Nome não encontrado na agenda!!!")
        print()
        print("*****************************")
    elif controle == "x":
        break
    else:
        print()
        print("*****************************")
        print("Opção inválida")
print()
print("*****************************")
print("Agenda encerrada!")
print("Obrigado!!")
