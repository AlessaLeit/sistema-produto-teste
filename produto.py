def cadastrar_produto(codigo, nome, preco, estoque):
    return {
        "Código": codigo,
        "Nome": nome,
        "Preço": preco,
        "Estoque": estoque
    }

def buscar_produto(termo_busca):
    with open("produtos.txt", "r", encoding="utf-8") as arquivo:
        produto_atual = []
        for linha in arquivo:
            if linha.strip() == "=== Produto Cadastrado ===":
                if produto_atual:
                    # Verifica se o termo está nesse produto
                    texto_produto = "\n".join(produto_atual)
                    if termo_busca.lower() in texto_produto.lower():
                        print("\n=== Produto Encontrado ===")
                        print(texto_produto)
                    produto_atual = []  # limpa pra começar novo produto
            elif linha.strip() != "":
                produto_atual.append(linha.strip())
        
        # Verifica o último produto
        if produto_atual:
            texto_produto = "\n".join(produto_atual)
            if termo_busca.lower() in texto_produto.lower():
                print("\n=== Produto Encontrado ===")
                print(texto_produto)

def codigo_existe(codigo_procurado):
    try:
        with open("produtos.txt", "r", encoding="utf-8") as arquivo:
            for linha in arquivo:
                if linha.strip().startswith("Código:"):
                    codigo_lido = linha.strip().split(":")[1].strip()
                    if codigo_lido == codigo_procurado:
                        return True
    except FileNotFoundError:
        return False
    return False

def listar_produtos():
    try:
        with open("produtos.txt", "r", encoding="utf-8") as arquivo:
            conteudo = arquivo.read().strip()
            if conteudo:
                print("\n==== Lista de Produtos ====")
                print(conteudo)
            else:
                print("\nNenhum produto cadastrado ainda.")
    except FileNotFoundError:
        print("\nArquivo de produtos não encontrado.")

