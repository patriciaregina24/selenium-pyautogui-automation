import pyautogui
import time
from prints import tirar_print, salvar_prints_em_pdf
from dados import (
    swaglabs, usuario, senha, produtos,
    checkout, caminhos_dados, campo_dados, botoes_final
)
from funcoes import (
    iniciar_navegador, preencher_login, pressionar_enter,
    selecionar_produtos, iniciar_checkout, dados_cliente, finalizar_compra
)

# Executando o script principal / Running the main script
if __name__ == "__main__":
    # Inicia o navegador e abre a página inicial / Starts the browser and opens the homepage
    navegador = iniciar_navegador(swaglabs)

    time.sleep(1)
    tirar_print("01_pagina_inicial") # Captura a tela da página inicial / Takes a screenshot of the homepage

    # Preenche os campos de login / Fills in the login fields
    preencher_login(navegador, usuario[0], usuario[1])
    preencher_login(navegador, senha[0], senha[1])
    tirar_print("02_preenchimento_login")
    pressionar_enter(navegador) # Pressiona ENTER para fazer login / Presses ENTER to login

    # Clica no item desejado / Clicks on the desired item
    pyautogui.click(x=849, y=360)
    time.sleep(1.5)

    # Seleciona os produtos / Select the products
    selecionar_produtos(navegador, produtos[0], "page_down")
    selecionar_produtos(navegador, produtos[1], "page_up")

    # Inicia o processo de checkout / Starts the checkout process
    iniciar_checkout(navegador, checkout[0])
    tirar_print("03_carrinho")
    iniciar_checkout(navegador, checkout[1])

    # Preenche os dados do cliente / Fills in the customer data
    dados_cliente(navegador, caminhos_dados[0], campo_dados[0])
    dados_cliente(navegador, caminhos_dados[1], campo_dados[1])
    dados_cliente(navegador, caminhos_dados[2], campo_dados[2])

    tirar_print("04_dados_preenchidos")

    # Finaliza a compra / Finalizes the purchase
    finalizar_compra(navegador, botoes_final[0])
    finalizar_compra(navegador, botoes_final[1])

    tirar_print("05_pagina_final")

    # Salva todos os prints como PDF / Saves all the screenshots as a PDF
    salvar_prints_em_pdf()

    # Fecha o navegador / Closes the browser
    navegador.quit()