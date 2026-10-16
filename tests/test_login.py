import pytest

CENARIOS_INVALIDOS = [
    ("standard_user", "senha_errada", "xyz"),
    ("", "secret_sauce", "Username is required"),
    ("standard_user", "", "Password is required"),
    ("locked_out_user", "secret_sauce", "locked out"),
]

@pytest.mark.parametrize(
    'usuario, senha, trecho_esperado',
    CENARIOS_INVALIDOS,
    ids=['senha_errada', 'usuario_vazio', 'senha_vazia', 'usuario_bloqueado']
)
def test_login_invalido_mostra_erro(driver, login_page, usuario, senha, trecho_esperado):
    login_page.login(usuario, senha)


    mensagem = login_page.get_error_message()

    assert trecho_esperado in mensagem
    assert "inventory" not in driver.current_url