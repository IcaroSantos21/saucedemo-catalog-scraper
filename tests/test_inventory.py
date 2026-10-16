def test_catalogo_tem_6_produtos(inventory_page):
    produtos = inventory_page.get_products()

    assert len(produtos) == 6


# TODO 1: todo produto tem nome e descrição não vazios
def test_produtos_tem_nome_e_descricao(inventory_page):
    produtos = inventory_page.get_products()
    for produto in produtos:
        assert produto['nome'] != ""
        assert produto['descricao'] != ""

# TODO 2: todo preço é maior que zero
def test_produtos_tem_preco_maior_que_zero(inventory_page):
    produtos = inventory_page.get_products()

    for produto in produtos:
        assert produto['preco'] > 0

# TODO 3: não existem dois produtos com o mesmo nome
def test_produtos_nao_tem_o_mesmo_nome(inventory_page):
    produtos = inventory_page.get_products()

    nomes = [produto['nome'] for produto in produtos]

    set_nomes = set(nomes)

    assert len(nomes) == len(set_nomes)

# TODO 4: o "Sauce Labs Backpack" existe e custa 29.99
def test_valida_se_produto_existe(inventory_page):
    produtos = inventory_page.get_products()

    backpack = None

    for produto in produtos:
        if produto['nome'] == "Sauce Labs Backpack":
            backpack = produto

    assert backpack is not None
    assert backpack['preco'] == 29.99