#!Python3
# Lista de Produtos
produtos = []

categorias = {
    "1": "Bebidas",
    "2": "Prato Principal",
    "3": "Sobremesas",
}

# Dicionário do Produto
produto = {
    "category": "",
    "item": "",
    "name": "",
    "price": ""
}

# Impressão do Menu de seleção
def printMenu():
    print("-------------------------------------")
    print("Seja bem vindo ao Cardápio")
    print("")
    print("Selecione uma das opções:")
    print("1) Adicionar itens ao cardápio")
    print("2) Excluir itens do cardápio")
    print("3) Alterar Itens do cardápio")
    print("4) Buscar itens no cardápio")
    print("5) Listar todos os itens do cardápio")
    print("6) Salvar e sair")
    print("-------------------------------------")

# Adicionando Item
def addItem():
    # Escolha a Categoria
    print("Qual Categoria?")
    # Percorre as categorias exibindo cada uma delas
    for key, value in categorias.items():
        print(f"{key}) {value}")
    option = input("Digite o número da categoria: ")
    
    # Verificar se a categoria escolhida é válida
    if option in categorias:
        produto["category"] = categorias[option]
    else:
        print("Categoria inválida. Item não adicionado.")
        return
    # Tipo/item
    produto["item"] = input("Digite o Tipo de Produto: ")
    # Nome
    produto["name"] = input("Digite o Nome do Produto: ")
    # Preço
    produto["price"] = input("Digite o Preço do Produto: ")
    # Adiciona o produto à lista de produtos
    produtos.append(produto.copy())
    print("Item adicionado com sucesso!\n")

def removeItem():
    # TO DO
    # Ana Paula Alves
    pass

def editItem():
    # TO DO
    # Bruno Reich
    pass

def searchItem():
    # TO DO
    # Ryan Lucas
    pass

def printItens():
    # TO DO
    # Bernardo Plottegher
    pass

def saveAndClose():
    # Cria ou abre o arquivo chamado "cardápio.txt"
    with open("cardapio.txt", "w") as file:
        # Percorre a lista de Produtos
        for produto in produtos:
            file.write(f"Categoria: {produto['category']}\n")
            file.write(f"Tipo: {produto['item']}\n")
            file.write(f"Nome: {produto['name']}\n")
            file.write(f"Preço: {produto['price']}\n")
            file.write("\n")

    print("Cardápio salvo em 'cardapio.txt'. Programa encerrado.")

# Looping de execução do programa
while True:
    printMenu()
    option = int(input("Escolha uma das opções: "))
    # Adicionar Item
    if(option == 1):
        addItem()

    # Remover item
    elif(option == 2):
        removeItem()

    # Editar Item
    elif(option == 3):
        editItem()

    # Buscar Item
    elif(option == 4):
        searchItem()

    # Exibir Itens
    elif(option == 5):
        printItens()

    # Salvar em txt e Sair
    elif(option == 6):
        saveAndClose()
        break

    else:
        print("Opção inválida, digite novamente.")
