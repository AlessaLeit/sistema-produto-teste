from produto import (
    cadastrar_produto, buscar_produto, codigo_existe, listar_produtos
)

# Função executável para usar manualmente
if __name__ == "__main__":
    while True:
        print("\n=== Menu Principal ===")
        print("1 - Cadastrar Produto")
        print("2 - Buscar Produto")
        print("3 - Listar Todos os Produtos")
        print("0 - Sair")
        opcao = input("Digite a opção: ")

        if opcao == "1":
            print("\n=== Cadastro de Produto ===")
            codigo = input("Digite o código do produto: ")

            if codigo_existe(codigo):
                print("Já existe um produto com esse código.")
            else:
                nome = input("Digite o nome do produto: ")
                preco = float(input("Digite o preço do produto: "))
                estoque = int(input("Digite a quantidade em estoque: "))

                produto = cadastrar_produto(codigo, nome, preco, estoque)

                print("\nProduto cadastrado com sucesso:")
                for chave, valor in produto.items():
                    print(f"{chave}: {valor}")

                with open("produtos.txt", "a", encoding="utf-8") as arquivo:
                    arquivo.write("=== Produto Cadastrado ===\n")
                    for chave, valor in produto.items():
                        arquivo.write(f"{chave}: {valor}\n")
                    arquivo.write("\n")

        elif opcao == "2":
            termo = input("Digite o código do produto que deseja buscar: ")
            buscar_produto(termo)

        elif opcao == "3":
            listar_produtos()
        
        elif opcao == "0":
            print("Saindo do sistema...")
            break
        
        else:
            print("Opção inválida. Tente novamente.")
