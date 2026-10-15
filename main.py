import csv

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait

URL = "https://www.saucedemo.com"
ARQUIVO_CSV = "catalogo.csv"

driver = webdriver.Firefox()

driver.get(URL)

try:
    wait = WebDriverWait(driver, 10)

    # Login
    driver.find_element(By.ID, "user-name").send_keys("standard_user")
    driver.find_element(By.ID, "password").send_keys("secret_sauce")
    driver.find_element(By.ID, "login-button").click()

    # Confirmando o login e esperando os produtos aparecerem
    wait.until(EC.presence_of_element_located((By.CLASS_NAME, "inventory_item")))

    # Pegando todos os containers de uma vez
    produtos = driver.find_elements(By.CLASS_NAME, "inventory_item")

    # Busca os dados de cada produto
    catalogo = []
    for produto in produtos:
        nome = produto.find_element(By.CLASS_NAME, "inventory_item_name").text
        descricao = produto.find_element(By.CLASS_NAME, "inventory_item_desc").text
        preco_texto = produto.find_element(By.CLASS_NAME, "inventory_item_price").text

        preco = float(preco_texto.replace("$", ""))  # Remove o símbolo de dólar e converte para float

        catalogo.append({"nome": nome, "descricao": descricao, "preco": preco})

    with open(ARQUIVO_CSV, mode="w", newline="", encoding="utf-8") as arquivo_csv:
        writer = csv.DictWriter(arquivo_csv, fieldnames=["nome", "descricao", "preco"])
        writer.writeheader()
        writer.writerows(catalogo)

    print(len(catalogo), "produtos salvos em", ARQUIVO_CSV)

finally:
    driver.quit()