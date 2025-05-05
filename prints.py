import pyautogui
from PIL import Image
import os
from datetime import datetime
import time

# FUNÇÃO PARA CAPTURAR PRINT DA TELA / FUNCTION TO TAKE SCREENSHOT
def tirar_print(nome, salvar_em="prints"):
    os.makedirs(salvar_em, exist_ok=True)

    # Coordenadas fornecidades (ajuste conforme seu monitor) / Provided coordinates (adjust according to your monitor)
    x1, y1 = 10, 130 # Canto superior esquerdo / Top left corner
    x2, y2 = 1330, 721 # Canto inferior direito / Bottom right corner

    # Definindo a região para a captura de tela / Defining the region for the screenshot
    largura = x2 - x1
    altura = y2 - y1

    screenshot = pyautogui.screenshot(region=(x1, y1, largura, altura))

    # Salva imagem com nome e timestamp / Saves the image with name and timestamp
    timestamp = datetime.now().strftime("%Y-%m-%d_%H-%M")
    caminho = os.path.join(salvar_em, f"{nome}_{timestamp}.png")
    screenshot.save(caminho)

    print(f"Print do navegador salvo em: {caminho}")

# FUNÇÃO PARA SALVAR PRINTS EM PDF / FUNCTION TO SAVE SCREENSHOTS AS PDF
def salvar_prints_em_pdf(pasta="prints", nome_pdf="prints_salvos.pdf"):
    imagens = [] # Lista de imagens / List of images

    # Lista os arquivos da pasta / Lists the files in the folder
    arquivos = os.listdir(pasta)

    for arquivo in arquivos:
        if arquivo.lower().endswith((".png", ".jpg", ".jpeg")):
            caminho = os.path.join(pasta, arquivo)
            imagem = Image.open(caminho).convert("RGB")
            imagens.append(imagem)

    if imagens:
        # A primeira imagem é usada como base, as outras são adicionadas como páginas
        # The first image is used as the base, the others are added as pages
        imagens[0].save(
            nome_pdf, save_all=True, append_images=imagens[1:]
        )
    else:
        print("Nenhuma imagem encontrada para salvar no PDF.")