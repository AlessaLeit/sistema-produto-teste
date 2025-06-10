from produto import (
    cadastrar_produto
)

def test_cadastro_produto_v():
    produto = cadastrar_produto("01", "Abacaxi", 11.11, 1)
    assert isinstance(produto, dict)
    
def test_cadastro_produto_i():
    resultado = cadastrar_produto("0", "X", 0, 0)
    assert isinstance(resultado, str)
    
# 1 failed, 1 passed in 0.36s