#!Python3

#Importações
import os

# Lista de Produtos
produtos = []
# Lista de Produtos na comanda
comanda = []
#Taxa de serviço
taxa = 0.10

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
    "price": 0.0,
    "quantity": 0,
    "total": 0
}

# Impressão da Comanda
def printMenuComanda():
    print("-------------------------------------")
    print("Seja bem vindo ao Pedido \n")
    print("1) Adicionar itens a comanda")
    print("2) Excluir itens da comanda")
    print("3) Exibir comanda")
    print("4) Limpar comanda")
    print("5) Sair")
    print("-------------------------------------")

# Limpa Console
def clearConsole():
    input("\nPressione Enter para continuar...")
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
                    # Popula Preço do Produto (Substitui vírgula por ponto)
                    price_str = lines[i+3].strip().split(": ")[1].replace(",", ".")
                    produto["price"] = float(price_str)
                    # Adiciona o produto à lista de produto
                    produtos.append(produto.copy())
                    # Pula 5 linhas, pois os produtos estão separados por \n
                    i += 5
                else:
                    # Se não possui mais produtos no arquivo, quebra.
                    break

# Adicionando Item
def addItem():
   # Verifica se a lista de produtos está vazia
    if not produtos:
        print("A lista de produtos está vazia. Nenhum item para adicionar.")
        return
    
    print("Escolha um item que deseja adicionar: \n")
    # Exibe os produtos da lista
    for idx, produto in enumerate(produtos):
        print(f"Identificador: {idx + 1}"
              + f"| Categoria: {produto['category']} "
              + f"| Tipo: {produto['item']} "
              + f"| Nome: {produto['name']} "
              + f"| Preco: {produto['price']}")

    # Solicita o identificador do produto
    idx = int(input("Digite o identificador do produto que deseja adicionar: ")) - 1
    
    # Verifica se existe nos produtos o índice selecionado
    if idx < 0 or idx >= len(produtos):
        print("Identificador inválido.")
        return
    
    # Solicita a quantidade
    quantidade = int(input("Digite a quantidade do produto: "))

     # Clona o produto selecionado e ajusta a quantidade e total
    selecionado = produtos[idx].copy()
    selecionado["quantity"] = quantidade
    selecionado["total"] = quantidade * selecionado["price"]
    
    # Adiciona o produto à comanda
    comanda.append(selecionado)
    
    print(f"Produto adicionado à comanda: {selecionado['name']}, Quantidade: {selecionado['quantity']}, Total: {selecionado['total']:.2f}")

    save()

# Exibição da Comanda
def printComanda():
    # Verifica se a comanda não está vazia
    if not comanda:
        print("A comanda está vazia.")
        return
    
    print("Itens na comanda:\n")
    total_comanda = 0.0

    # Percorre os itens da comanda
    for idx, produto in enumerate(comanda):
        print(f"Nome: {produto['name']} "
              + f" | Preço: {produto['price']:.2f} "
              + f" | Quantidade: {produto['quantity']} "
              + f" | Total: {produto['total']:.2f}")
        total_comanda += produto["total"]
    
    # Calcula Gorjeta e Total
    gorjeta = total_comanda * taxa
    total = total_comanda + gorjeta
    
    print(f"\nTotal da Comanda: R$ {total_comanda:.2f}")
    print(f"Gorjeta ({taxa * 100:.2f}%): R$ {gorjeta:.2f}")
    print(f"Total com Gorjeta: R$ {total:.2f}")

# Remover item da comanda
def removeItem():
    # Verifica se a comanda não está vazia
    if not comanda:
        print("A comanda está vazia. Nenhum item para remover.")
        return

    print("Escolha um item que deseja remover: \n")
    # Exibe os produtos na comanda
    for idx, produto in enumerate(comanda):
        print(f"Identificador: {idx + 1}"
              + f" | Nome: {produto['name']} "
              + f" | Preço: {produto['price']:.2f} "
              + f" | Quantidade: {produto['quantity']} "
              + f" | Total: {produto['total']:.2f}")

    # Solicita o identificador do produto
    idx = int(input("Digite o identificador do produto que deseja remover: ")) - 1
    
    # Verifica se existe nos produtos o índice selecionado
    if idx < 0 or idx >= len(comanda):
        print("Identificador inválido.")
        return

    # Remove o produto da comanda
    removido = comanda.pop(idx)
    print(f"Produto removido da comanda: {removido['name']}, Quantidade: {removido['quantity']}, Total: {removido['total']:.2f}")

    save()

# Limpa a comanda
def clearComanda():
    # Verifica se a comanda não está vazia
    if not comanda:
        print("A comanda já está vazia.")
        return
    # Limpa a lista da comanda
    comanda.clear()
    print("Comanda limpa com sucesso")

    save()

# Salva a Comanda no arquivo
def save():
    # Cria ou abre o arquivo chamado "comanda.txt"
    with open("comanda.txt", "w") as file:
        file.write(f"--------------------------------- \n")
        file.write(f"---------   COMANDA   ----------- \n")
        file.write(f"--------------------------------- \n")
        # Percorre a lista de Produtos na comanda
        for produto in comanda:
            file.write(f"Categoria: {produto['category']}\n")
            file.write(f"Tipo: {produto['item']}\n")
            file.write(f"Nome: {produto['name']}\n")
            file.write(f"Preco: {produto['price']:.2f}\n")
            file.write(f"Quantidade: {produto['quantity']}\n")
            file.write(f"Total: {produto['total']:.2f}\n")
            file.write("\n")
        
        # Calcula e escreve o total da comanda, gorjeta e total com gorjeta
        total_comanda = sum(produto["total"] for produto in comanda)
        gorjeta = total_comanda * taxa
        total = total_comanda + gorjeta

        file.write(f"--------------------------------- \n")
        file.write(f"Total da Comanda: R$ {total_comanda:.2f}\n")
        file.write(f"Gorjeta ({taxa * 100:.2f}%): R$ {gorjeta:.2f}\n")
        file.write(f"Total com Gorjeta: R$ {total:.2f}\n")


# Carrega os itens que estão no arquivo "cardápio.txt"
loadItems()

# Looping de execução do programa
while True:
    # Limpa Console
    if contagem > 0:
        clearConsole()
    contagem += 1
    # Exibe Comanda
    printMenuComanda()
    option = input("Escolha uma das opções: ")
    # Adicionar Item
    if(option == "1"):
        addItem()

    # Remover item
    elif(option == "2"):
        removeItem()

    # Exibir Comanda
    elif(option == "3"):
        printComanda()

    # Limpar Comanda
    elif(option == "4"):
        clearComanda()

    # Sair
    elif(option == "5"):
        print("Saindo...")
        break
    # Opção Inválida
    else:
        print("Opção inválida, digite novamente.")
