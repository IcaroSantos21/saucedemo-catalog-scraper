import csv

from selenium import webdriver

from pages.inventory_page import InventoryPage
from pages.login_page import LoginPage

ARQUIVO_CSV = "catalogo.csv"

def salvar_csv(catalogo):
    with open(ARQUIVO_CSV, mode="w", newline="", encoding="utf-8") as arquivo_csv:
            writer = csv.DictWriter(arquivo_csv, fieldnames=["nome", "descricao", "preco"])
            writer.writeheader()
            writer.writerows(catalogo)

def main():
    driver = webdriver.Firefox()

    try:
        login_page = LoginPage(driver)
        login_page.open()
        login_page.login("standard_user", "secret_sauce")

        inventory_page = InventoryPage(driver)
        inventory_page.wait_for_products()
        catalogo = inventory_page.get_products()

        salvar_csv(catalogo)
        print(len(catalogo), "produtos salvos em", ARQUIVO_CSV)

    finally:
        driver.quit()

if __name__ == "__main__":
     main()