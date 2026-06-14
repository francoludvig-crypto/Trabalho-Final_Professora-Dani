#Lista de itens
produtos = ["eNodeB 4G-LTE Banda-28 700MHz", "Antena Setorial", "Core Software", "Cabo Coaxial", "Antena UHF", "Serviço de Instalação"]

#Price list Cliente Final
valorFinal = [59890.90, 6850.72, 4690.00, 3240.90, 5450.70, 5000.00]

#Price list Integrador
valorIntegrador = [42830.90, 4550.72, 3600.00, 2940.90, 4320.70, 4500.00]

#Price list Distribuidor
valorDistribuidor = [36450.90, 3650.72, 2990.00, 1880.90, 3740.70, 3200.00]

#PO do Cliente
pedido = []

# Variáveis globais
customerType = None
prices = None
isRunning = True


# Aqui escolhe a categoria de cliente
def chooseCustomer():
    print("\n\nQual a categoria do Cliente?\n")
    print("1 - Distribuidor")
    print("2 - Integrador")
    print("3 - Consumidor Final\n")
    print("Pressione qualquer número maior para finalizar\n")

    escolhaT = int(input("Escolha uma das opções: "))

    #MATCH CASE (EQUIVALENTE AO SWITCH CASE DO C++)
    #Esse trecho para tipo de cliente já se atribui a ele a sua price list correta
    match escolhaT: # Tipo Cliente / Price List
        case 1:
            return "Distribuidor", valorDistribuidor
        case 2:
            return "Integrador", valorIntegrador
        case 3:
            return "Consumidor Final", valorFinal
        case _:
            return None,None
        
def showCatalog():                      #pega tipo de cliente e imprime em letras de caixa alta
    print(f"====MOSTRANDO CATÁLOGO PARA {customerType.upper()}====\n")

    for i in range(len(produtos)): #corre a lista de produtos considerando o tamanho da lista com 6 itens
        print(f"{i+1} - {produtos[i]}") #Imprime os nomes dos itens no catálogo seguindo a corrida da lista
        print(f"    R${prices[i]}\n") #Imprime os preços dos itens no catálogo seguindo a corrida da lista


customerType, prices = chooseCustomer()

#Implmentação do meu menu do sistema
while isRunning == True:
    print("\n=== BEM VINDO À KHOMP ===")
    print("=== MENU PRINCIPAL ===")
    print("1 - Ver catálogo")
    print("2 - Adicionar item ao pedido")
    print("3 - Remover item do pedido")
    print("4 - Consultar pedido")
    print("5 - Finalizar Orçamento")
    print("6 - Finalizar Sistema")

    opcao = int(input("Escolha uma opção: "))

    if opcao == 1:
        showCatalog()
    elif opcao == 2:
        showCatalog()
        #adiciona-se itens à lista "pedido"
        item = int(input("\nDigite o número do item desejado: ")) -1 #Internamente o Python começa a ler pelo índice 0, mas o usuário verá 1
        if item >=0 and item < len(produtos):
            pedido.append(item)
            print("Produto adicionado ao pedido!\n")
        else:
            print("Produto inválido!")

    elif opcao == 3:
        if len(pedido) == 0:
            print("Pedido está vaziu!")
        else:
            print("\n=== ITENS DO PEDIDO ===")
            for i in range(len(pedido)):
                print(f"{i+1} - {produtos[pedido[i]]}")
            
            remover = int(input("\n Digite o número do item que deseja remover: ")) - 1 #Internamente o Python começa a ler pelo índice 0, mas o usuário verá 1
            
            #Remove-se itens da lista "pedido"
            if remover >= 0 and remover < len(pedido):
                pedido.pop(remover)
                print("Item removido com sucesso!")

            else:
                print("Item inválido!")

    elif opcao == 4:
        if len(pedido) == 0:
            print("Pedido vaziu!")

        else:
            total = 0
            print("\n== PEDIDO ATUAL ==")
            for item in pedido:
                print(f"{produtos[item]}")
                print(f"R${prices[item]}\n")

                total = total + prices[item]

            print(f"VALOR TOTAL: R${total}")

    elif opcao == 5:
        if len(pedido) == 0:
            print("Não existem produtos no orçamento atual!")

        else:
            total = 0
            print("\n== ORÇAMENTO FINAL ==")
            print(f"Cliente: {customerType}\n")

            for item in pedido:
                print(f"{produtos[item]}")
                print(f"R${prices[item]}\n")

                total = total + prices[item]

            print(f"VALOR TOTAL: R${total}")
            print("\nKHOMP INDUSTRIA E COMERCIO LTDA!")
            isRunning = False
    elif opcao == 6:
        print("Encerrando sistema...")
        isRunning = False
        break
    else:
        print("opção inválida!")
        break
