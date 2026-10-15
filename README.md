# saucedemo-catalog-scraper

Script em Python que automatiza o login no [Swag Labs](https://www.saucedemo.com) (site de demonstração da Sauce Labs), coleta o catálogo de produtos e salva tudo em um arquivo CSV.

Fiz este projeto para praticar automação web com Selenium: waits explícitos, localização de elementos e extração de dados.

## O que o script faz

1. Abre o Firefox e acessa o site
2. Faz login com o usuário de teste `standard_user`
3. Espera a lista de produtos carregar (confirma que o login funcionou)
4. Percorre cada produto e extrai nome, descrição e preço
5. Converte o preço para número e grava o resultado em `catalogo.csv`
6. Fecha o navegador, mesmo se algo der errado no meio

## Tecnologias

- Python 3.10+
- Selenium 4
- Firefox

## Como rodar

```bash
git clone https://github.com/SEU_USUARIO/saucedemo-catalog-scraper.git
cd saucedemo-catalog-scraper

python3 -m venv .venv
source .venv/bin/activate        # no Windows: .venv\Scripts\activate

pip install -r requirements.txt
python main.py
```

O Selenium 4.6+ baixa o driver do navegador automaticamente, então não precisa instalar o geckodriver à mão. O Firefox precisa estar instalado.

## Resultado

O arquivo `catalogo.csv` é gerado na pasta do projeto, com este formato:

| nome | descricao | preco |
|------|-----------|-------|
| Sauce Labs Backpack | carry.allTheThings() with the sleek... | 29.99 |
| Sauce Labs Bike Light | A red light isn't the desired state... | 9.99 |

São 6 produtos, mais a linha de cabeçalho.

## Estrutura

```
.
├── main.py
├── requirements.txt
└── README.md
```

## Decisões do código

- **Wait explícito** em vez de `time.sleep`: o script segue assim que a página carrega e falha com `TimeoutException` se o login não funcionar.
- **Busca relativa ao produto**: nome, descrição e preço são procurados dentro de cada cartão (`produto.find_element`), não na página inteira.
- **`try/finally`** garante que o navegador feche sempre.
- **`DictWriter`** com `encoding="utf-8"` e `newline=""` para o CSV sair correto em qualquer sistema.

## Próximos passos

- [ ] Separar em Page Objects (`LoginPage` e `InventoryPage`)
- [ ] Adicionar testes com pytest (por exemplo, validar que são 6 produtos)
- [ ] Refazer o fluxo com Playwright e comparar as duas abordagens
- [ ] Rodar em modo headless e configurar no GitHub Actions
