# produto.py

def cadastrar_produto(codigo, nome, preco, estoque):
    produto = {
        "Código": codigo,
        "Nome": nome,
        "Preço": preco,
        "Estoque": estoque
    }
    return produto

# Função executável para usar manualmente
if __name__ == "__main__":
    print("=== Cadastro de Produto ===")
    codigo = input("Digite o código do produto: ")
    nome = input("Digite o nome do produto: ")
    preco = float(input("Digite o preço do produto: "))
    estoque = int(input("Digite a quantidade em estoque: "))

    produto = cadastrar_produto(codigo, nome, preco, estoque)

    print("\nProduto cadastrado com sucesso:")
    for chave, valor in produto.items():
        print(f"{chave}: {valor}")
