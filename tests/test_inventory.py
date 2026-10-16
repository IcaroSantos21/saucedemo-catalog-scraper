import pytest

PRECOS_ESPERADOS = [
    ("Sauce Labs Backpack", 29.99),
    ("Sauce Labs Bike Light", 9.99),
    ("Sauce Labs Bolt T-Shirt", 15.99),
    ("Sauce Labs Fleece Jacket", 49.99),
    ("Sauce Labs Onesie", 7.99),
    ("Test.allTheThings() T-Shirt (Red)", 15.99),
]

def test_catalogo_tem_6_produtos(inventory_page):
    produtos = inventory_page.get_products()

    assert len(produtos) == 6

@pytest.mark.parametrize("campo", ["nome", "descricao"])
def test_campos_de_texto_preenchidos(inventory_page, campo):
    produtos = inventory_page.get_products()

    for produto in produtos:
        assert produto[campo], f"campo '{campo}' vazio em: '{produto}'" 

def test_precos_sao_positivos(inventory_page):
    produtos = inventory_page.get_products()

    for produto in produtos:
        assert produto['preco'] > 0, f"preço inválido em: '{produto}'"

def test_produtos_nao_tem_o_mesmo_nome(inventory_page):
    produtos = inventory_page.get_products()

    nomes = [produto['nome'] for produto in produtos]

    assert len(nomes) == len(set(nomes))

@pytest.mark.parametrize("nome, preco_esperado", PRECOS_ESPERADOS)
def test_valida_se_produto_existe(inventory_page, nome, preco_esperado):
    produtos = inventory_page.get_products()

    precos = {produto["nome"]: produto["preco"] for produto in produtos}

    assert nome in precos, f"produto: '{nome}' não encontrado"
    assert precos[nome] == preco_esperado