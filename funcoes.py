from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

# FUNÇÃO INICIAR NAVEGADOR / FUNCTION TO START BROWSER
def iniciar_navegador(link):
    service = Service(ChromeDriverManager().install())
    navegador = webdriver.Chrome(service=service)
    navegador.get(link)
    navegador.maximize_window() # Maximiza a janela / Maximizes the window
    return navegador

# FUNÇÃO REALIZAR LOGIN / FUNCTION TO FILL LOGIN
def preencher_login(navegador, caminho, entrada):
    campo = WebDriverWait(navegador, 10).until(EC.visibility_of_element_located((By.XPATH, f'{caminho}')))
    campo.send_keys(f"{entrada}") # Preenche o campo de login / Fills in the login field

# FUNÇÃO ADICIONAR PRODUTO AO CARRINHO / FUNCTION TO ADD PRODUCT TO CART
def pressionar_enter(navegador, delay_apos_enter=1.5):
    acoes = ActionChains(navegador)
    acoes.send_keys(Keys.ENTER).perform()
    time.sleep(delay_apos_enter)

# FUNÇÃO SELECIONAR PRODUTOS / FUNCTION TO SELECT PRODUCTS
def selecionar_produtos(navegador, caminho, direcao):
    acoes = ActionChains(navegador)

    # Navega para baixo ou para cima / Scrolls down or up
    if direcao == "page_down":
        acoes.send_keys(Keys.PAGE_DOWN).perform()
        time.sleep(0.5)
    else:
        acoes.send_keys(Keys.PAGE_UP).perform()
        time.sleep(0.5)

    item = WebDriverWait(navegador, 10).until(EC.visibility_of_element_located((By.XPATH, f'{caminho}')))
    item.click()
    time.sleep(1)

# FUNÇÃO QUE DIRECIONA PARA O CARRINHO / FUNCTION TO GO TO THE CART
def iniciar_checkout(navegador, clicavel):
    carrinho = WebDriverWait(navegador, 10).until(EC.visibility_of_element_located((By.XPATH, f'{clicavel}')))
    carrinho.click()
    time.sleep(0.5)

# FUNÇÃO QUE REPASSA DADOS DO CLIENTE / FUNCTION TO FILL CUSTOMER DATA
def dados_cliente(navegador, caminho, entrada):
    campo = WebDriverWait(navegador, 10).until(EC.visibility_of_element_located((By.XPATH, f'{caminho}')))
    campo.send_keys(f"{entrada}")

# FUNÇÃO QUE FINALIZA A COMPRA / FUNCTION TO FINALIZE THE PURCHASE
def finalizar_compra(navegador, clicavel):
    acoes = ActionChains(navegador)
    item = WebDriverWait(navegador, 10).until(EC.visibility_of_element_located((By.XPATH, f'{clicavel}')))
    item.click()
    acoes.send_keys(Keys.PAGE_DOWN).perform()