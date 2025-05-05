import pyautogui
import time

# Captura a posição atual do mouse após uma pausa de 5 segundos
# Captures the current mouse position after a 5-second delay
print("Você tem 5 segundos para posicionar o mouse no ponto desejado.")
time.sleep(5)

# Exibe as coordenadas X e Y capturadas
# Displays the captured X and Y coordinates
posicao = pyautogui.position()
print(f"Posição capturada: x={posicao.x}, y={posicao.y}")