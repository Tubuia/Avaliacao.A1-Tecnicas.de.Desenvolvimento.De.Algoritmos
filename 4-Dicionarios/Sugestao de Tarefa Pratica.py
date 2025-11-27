#Desenvolver um sistema simples de cadastro de produtos com nome e preço, armazenando em dicionário.
produtos = {}  # Dicionário que armazena o nome e o preço dos produtos

while True: #estrutura de repetição
    print("Menu: ") #instruções dos comandos do sistema
    print("1 - Cadastrar produto")
    print("2 - Listar produtos")
    print("3 - Sair")

    opcao = input("Escolha uma opção: ") #variavel para decidir qual parte do sistema você quer acessar

    if opcao == "1": #opção de cadastro de produtos
        nome = input("Nome do produto: ") #variavel do nome do produto
        preco = float(input("Preço do produto: ")) #variavel do preço do produto

        produtos[nome] = preco #Colocação dos dados no dicinario, aonde o nome do produto é a chave e o preço é o valor
        print(f"O produto '{nome}' foi cadastrado com sucesso.")

    elif opcao == "2": #opção de visualização dos produtos cadastrados
        if not produtos: #Saida caso nenhum produto tenha sido cadastrado
            print("Nenhum produto cadastrado.")
        else: #Saida caso tenham produtos cadastrados
            print("Lista de Produtos: ")
            for nome, preco in produtos.items(): #estrutura condicional que permite a exibição de todos os dados
                print(f"{nome} - R$ {preco:.2f}")

    elif opcao == "3": #opção que encerra o sistema
        print("Encerrando o sistema.")
        break #quebra da estrutura de repeetição

    else:
        print("Opção inválida! Tente novamente.") #controle de erro