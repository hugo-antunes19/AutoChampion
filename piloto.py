import cv2
import numpy as np
import pyautogui
import time
import keyboard

# Define um limiar para considerar uma correspondência
threshold = 0.8
champion = "Lee sin"

def aceitarPartida():
    # Carrega a imagem que você quer detectar
    image_to_detect = cv2.imread('images/accept.png', cv2.IMREAD_GRAYSCALE)
    
    # Loop para o print
    while True:
        # Captura a tela
        screen = pyautogui.screenshot()
        screen_np = np.array(screen)
        
        # Converte a imagem da tela para escala de cinza
        screen_gray = cv2.cvtColor(screen_np, cv2.COLOR_BGR2GRAY)
        
        # Usa o método de correspondência de template para encontrar a imagem
        result = cv2.matchTemplate(screen_gray, image_to_detect, cv2.TM_CCOEFF_NORMED)
        loc = np.where(result >= threshold)
        if len(loc[0]) > 0:
            print("Partida aceita!")
            # Obter a posição da imagem encontrada
            x, y = loc[::-1][0][0], loc[::-1][1][0]
            # Realiza o clique na posição encontrada
            pyautogui.moveTo(x + (image_to_detect.shape[1] // 2), y + (image_to_detect.shape[0] // 2),duration=1)
            pyautogui.click()
            time.sleep(2)
            return
        time.sleep(1)
        if keyboard.is_pressed('ctrl+q'):
            print("Conjunto de teclas pressionado. Saindo do loop...")
            break

def buscarChampion():
    # Carrega a imagem que você quer detectar
    buscarImage = cv2.imread('images/buscar.png', cv2.IMREAD_GRAYSCALE)
    
    # Loop para o print
    while True:
        # Captura a tela
        screen = pyautogui.screenshot()
        screen_np = np.array(screen)
        
        # Converte a imagem da tela para escala de cinza
        screen_gray = cv2.cvtColor(screen_np, cv2.COLOR_BGR2GRAY)
        
        # Usa o método de correspondência de template para encontrar a imagem
        resultBuscar = cv2.matchTemplate(screen_gray, buscarImage, cv2.TM_CCOEFF_NORMED)
        locBuscar = np.where(resultBuscar >= threshold)
        
        if len(locBuscar[0]) > 0:
            # Obter a posição da imagem encontrada
            x, y = locBuscar[::-1][0][0], locBuscar[::-1][1][0]
            # Realiza o clique na posição encontrada
            pyautogui.moveTo(x + (buscarImage.shape[1] // 2), y + (buscarImage.shape[0] // 2),duration=1)
            pyautogui.click()
            time.sleep(1)
            pyautogui.typewrite(str(champion))
            time.sleep(2)
            return
        if keyboard.is_pressed('ctrl+q'):
            print("Conjunto de teclas pressionado. Saindo do loop...")
            break
        time.sleep(2)

def selecionarChampion():
    # Carrega a imagem que você quer detectar
    championImage = cv2.imread('images/leesin.png', cv2.IMREAD_GRAYSCALE)
    
    while True:
        # Captura a tela
        screen = pyautogui.screenshot()
        screen_np = np.array(screen)
        
        # Converte a imagem da tela para escala de cinza
        screen_gray = cv2.cvtColor(screen_np, cv2.COLOR_BGR2GRAY)
        
        resultChampion = cv2.matchTemplate(screen_gray, championImage, cv2.TM_CCOEFF_NORMED)
        locChampion = np.where(resultChampion >= threshold)
        
        if len(locChampion[0]) > 0:
            print("Campeão Selecionado")
            # Obter a posição da imagem encontrada
            x, y = locChampion[::-1][0][0], locChampion[::-1][1][0]
            # Realiza o clique na posição encontrada
            print(championImage.shape)
            pyautogui.moveTo(x + (championImage.shape[1] // 2), y + (championImage.shape[0] // 2),duration=1)
            pyautogui.click()
            time.sleep(2)
            return

        if keyboard.is_pressed('ctrl+q'):
            print("Conjunto de teclas pressionado. Saindo do loop...")
            break
        
        time.sleep(2)
     
def confirmar():
    # Carrega a imagem que você quer detectar
    image_to_detect = cv2.imread('images/confirm.png', cv2.IMREAD_GRAYSCALE)
    
    # Loop para o print
    while True:
        # Captura a tela
        screen = pyautogui.screenshot()
        screen_np = np.array(screen)
        
        # Converte a imagem da tela para escala de cinza
        screen_gray = cv2.cvtColor(screen_np, cv2.COLOR_BGR2GRAY)
        
        # Usa o método de correspondência de template para encontrar a imagem
        result = cv2.matchTemplate(screen_gray, image_to_detect, cv2.TM_CCOEFF_NORMED)
        loc = np.where(result >= threshold)
        if len(loc[0]) > 0:
            print("Partida Confirmada!")
            # Obter a posição da imagem encontrada
            x, y = loc[::-1][0][0], loc[::-1][1][0]
            # Realiza o clique na posição encontrada
            pyautogui.moveTo(x + (image_to_detect.shape[1] // 2), y + (image_to_detect.shape[0] // 2),duration=1)
            pyautogui.click()
            time.sleep(2)
            return
        
        if keyboard.is_pressed('ctrl+q'):
            print("Conjunto de teclas pressionado. Saindo do loop...")
            break
        
        time.sleep(2)
        
def runa():
    # Carrega a imagem que você quer detectar
    image_to_detect = cv2.imread('images/runa.png', cv2.IMREAD_GRAYSCALE)
    
    # Loop para o print
    while True:
        # Captura a tela
        screen = pyautogui.screenshot()
        screen_np = np.array(screen)
        
        # Converte a imagem da tela para escala de cinza
        screen_gray = cv2.cvtColor(screen_np, cv2.COLOR_BGR2GRAY)
        
        # Usa o método de correspondência de template para encontrar a imagem
        result = cv2.matchTemplate(screen_gray, image_to_detect, cv2.TM_CCOEFF_NORMED)
        loc = np.where(result >= threshold)
        if len(loc[0]) > 0:
            print("Partida Confirmada!")
            # Obter a posição da imagem encontrada
            x, y = loc[::-1][0][0], loc[::-1][1][0]
            # Realiza o clique na posição encontrada
            pyautogui.moveTo(x + (image_to_detect.shape[1] // 2), y + (image_to_detect.shape[0] // 2),duration=1)
            pyautogui.click()
            pyautogui.moveTo(x + 400, y - 200,duration=1)
            pyautogui.click()
            time.sleep(2)
            return
        
        if keyboard.is_pressed('ctrl+q'):
            print("Conjunto de teclas pressionado. Saindo do loop...")
            break
        
        time.sleep(2)
    
def fechar():
    # Carrega a imagem que você quer detectar
    image_to_detect = cv2.imread('images/fechar.png', cv2.IMREAD_GRAYSCALE)
    
    # Loop para o print
    while True:
        # Captura a tela
        screen = pyautogui.screenshot()
        screen_np = np.array(screen)
        
        # Converte a imagem da tela para escala de cinza
        screen_gray = cv2.cvtColor(screen_np, cv2.COLOR_BGR2GRAY)
        
        # Usa o método de correspondência de template para encontrar a imagem
        result = cv2.matchTemplate(screen_gray, image_to_detect, cv2.TM_CCOEFF_NORMED)
        loc = np.where(result >= threshold)
        if len(loc[0]) > 0:
            # Obter a posição da imagem encontrada
            x, y = loc[::-1][0][0], loc[::-1][1][0]
            # Realiza o clique na posição encontrada
            pyautogui.moveTo(x + (image_to_detect.shape[1] // 2), y + (image_to_detect.shape[0] // 2),duration=1)
            pyautogui.click()
            time.sleep(2)
            return
        
        if keyboard.is_pressed('ctrl+q'):
            print("Conjunto de teclas pressionado. Saindo do loop...")
            break
        
        time.sleep(2)

while True:
    # aceitarPartida()
    # if keyboard.is_pressed('ctrl+q'):
    #         print("Conjunto de teclas pressionado. Saindo do loop...")
    #         break
    buscarChampion()
    if keyboard.is_pressed('ctrl+q'):
            print("Conjunto de teclas pressionado. Saindo do loop...")
            break
    selecionarChampion()
    if keyboard.is_pressed('ctrl+q'):
            print("Conjunto de teclas pressionado. Saindo do loop...")
            break
    runa()
    if keyboard.is_pressed('ctrl+q'):
            print("Conjunto de teclas pressionado. Saindo do loop...")
            break
    fechar()
    if keyboard.is_pressed('ctrl+q'):
            print("Conjunto de teclas pressionado. Saindo do loop...")
            break
    confirmar()
    if keyboard.is_pressed('ctrl+q'):
            print("Conjunto de teclas pressionado. Saindo do loop...")
            break
