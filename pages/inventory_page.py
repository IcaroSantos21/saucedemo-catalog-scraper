from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait

class InventoryPage:
    PRODUCT_CARD = (By.CLASS_NAME, "inventory_item")
    PRODUCT_NAME = (By.CLASS_NAME, "inventory_item_name")
    PRODUCT_DESCRIPTION = (By.CLASS_NAME, "inventory_item_desc")
    PRODUCT_PRICE = (By.CLASS_NAME, "inventory_item_price")

    def __init__(self, driver, timeout=10):
        self.driver = driver
        self.wait = WebDriverWait(driver, timeout)

    def wait_for_products(self):
        self.wait.until(EC.presence_of_element_located(self.PRODUCT_CARD))

    def get_products(self):

        produtos = self.driver.find_elements(*self.PRODUCT_CARD)
        catalogo = []

        for produto in produtos:
                nome = produto.find_element(*self.PRODUCT_NAME).text
                descricao = produto.find_element(*self.PRODUCT_DESCRIPTION).text
                preco_texto = produto.find_element(*self.PRODUCT_PRICE).text

                preco = float(preco_texto.replace("$", ""))  # Remove o símbolo de dólar e converte para float
        
                catalogo.append({"nome": nome, "descricao": descricao, "preco": preco})

        return catalogo