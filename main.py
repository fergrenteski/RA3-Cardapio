#!Python3

#Importações
import os

# Lista de Produtos
produtos = []

# Contagem para limpar console
contagem =  0

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
    print("6) Sair")
    print("-------------------------------------")

# Limpa Console
def clearConsole():
    input("\n Pressione Enter para continuar...")
    # Verifica o Sistema
    if os.name == 'nt':
        # Windows
        os.system('cls')
    else:
        # Linux, Mac
        os.system('clear')

# Carrega itens do arquivo "cardapio.txt"
def loadItems():
     # Verifica se existe arquivo "cardapio.txt"
     if os.path.exists("cardapio.txt"):
        # Abre o arquivo com modo leitura "r"
        with open("cardapio.txt", "r") as file:
            # Lê todas as linhas do arquivo
            lines = file.readlines()
            # Contador de linhas
            i = 0
            while i < len(lines):
                # Verifica se ainda há linhas suficientes para processar um produto completo
                if i + 4 <= len(lines):
                    # Popula Categoria do Produto
                    produto["category"] = lines[i].strip().split(": ")[1]
                    # Popula Tipo do Produto
                    produto["item"] = lines[i+1].strip().split(": ")[1]
                    # Popula Nome do Produto
                    produto["name"] = lines[i+2].strip().split(": ")[1]
                    # Popula Preço do Produto
                    produto["price"] = lines[i+3].strip().split(": ")[1]
                    # Adiciona o produto à lista de produto
                    produtos.append(produto.copy())
                    # Pula 5 linhas, pois os produtos estão separados por \n
                    i += 5
                else:
                    # Se não possui mais produtos no arquivo, quebra.
                    break

# Adicionando Item
def addItem():
    # Escolha a Categoria
    print("Qual Categoria?")
    # Percorre as categorias exibindo cada uma delas
    for key, value in categorias.items():
        #Exibe as categorias
        print(f"{key}) {value}")
    optionC = input("Digite o número da categoria: ")
    # Verificar se a categoria escolhida é válida
    if optionC in categorias:
        # Popula Categoria do Produto
        produto["category"] = categorias[optionC]
    else:
        print("Categoria inválida. Item não adicionado.")
        return
    # Popula Tipo do Produto
    produto["item"] = input("Digite o Tipo de Produto: ")
    # Popula Nome do Produto
    produto["name"] = input("Digite o Nome do Produto: ")
    # Verifica se o nome do produto já existe na lista
    for p in produtos:
        if p["name"] == produto["name"]:
            print("Produto com este nome já existe. Item não adicionado.")
            return
    # Popula Preço do Produto
    produto["price"] = input("Digite o Preço do Produto: ")
    # Adiciona o produto à lista de produtos
    produtos.append(produto.copy())
    print("\nItem adicionado com sucesso!\n")
    # Salva as alterações no arquivo "cardapio.txt"
    save()

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

def save():
    # Cria ou abre o arquivo chamado "cardápio.txt"
    with open("cardapio.txt", "w") as file:
        # Percorre a lista de Produtos
        for produto in produtos:
            file.write(f"Categoria: {produto['category']}\n")
            file.write(f"Tipo: {produto['item']}\n")
            file.write(f"Nome: {produto['name']}\n")
            file.write(f"Preço: {produto['price']}\n")
            file.write("\n")

# Carrega os itens que estão no arquivo "cardápio.txt"
loadItems()

# Looping de execução do programa
while True:
    # Limpa Console
    if contagem > 0:
        clearConsole()
    contagem += 1
    # Exibe menu
    printMenu()
    option = input("Escolha uma das opções: ")
    # Adicionar Item
    if(option == "1"):
        addItem()

    # Remover item
    elif(option == "2"):
        removeItem()

    # Editar Item
    elif(option == "3"):
        editItem()

    # Buscar Item
    elif(option == "4"):
        searchItem()

    # Exibir Itens
    elif(option == "5"):
        printItens()

    # Sair
    elif(option == "6"):
        print("Saindo...")
        break
    # Opção Inválida
    else:
        print("Opção inválida, digite novamente.")
