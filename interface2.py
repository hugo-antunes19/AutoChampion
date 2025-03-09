import cv2
import numpy as np
import pyautogui
import time
import keyboard
import threading
import tkinter as tk
import os

threshold = 0.8
champion = "Lee sin"
running = False

def aceitarPartida():
    global running
    image_to_detect = cv2.imread('images/accept.png', cv2.IMREAD_GRAYSCALE)
    while running:
        screen = pyautogui.screenshot()
        screen_np = np.array(screen)
        screen_gray = cv2.cvtColor(screen_np, cv2.COLOR_BGR2GRAY)
        result = cv2.matchTemplate(screen_gray, image_to_detect, cv2.TM_CCOEFF_NORMED)
        loc = np.where(result >= threshold)
        if len(loc[0]) > 0:
            print("Partida aceita!")
            x, y = loc[::-1][0][0], loc[::-1][1][0]
            pyautogui.moveTo(x + (image_to_detect.shape[1] // 2), y + (image_to_detect.shape[0] // 2),duration=1)
            pyautogui.click()
            time.sleep(2)
            break
        time.sleep(1)

def buscarChampion():
    global running, champion
    buscarImage = cv2.imread('images/buscar.png', cv2.IMREAD_GRAYSCALE)
    while running:
        screen = pyautogui.screenshot()
        screen_np = np.array(screen)
        screen_gray = cv2.cvtColor(screen_np, cv2.COLOR_BGR2GRAY)
        resultBuscar = cv2.matchTemplate(screen_gray, buscarImage, cv2.TM_CCOEFF_NORMED)
        locBuscar = np.where(resultBuscar >= threshold)
        if len(locBuscar[0]) > 0:
            x, y = locBuscar[::-1][0][0], locBuscar[::-1][1][0]
            pyautogui.moveTo(x + (buscarImage.shape[1] // 2), y + (buscarImage.shape[0] // 2),duration=1)
            pyautogui.click()
            time.sleep(1)
            pyautogui.typewrite(str(champion))
            time.sleep(2)
            break
        time.sleep(2)

def selecionarChampion():
    global running
    championImage = cv2.imread(f'images/champions/{champion}.png', cv2.IMREAD_GRAYSCALE)
    while running:
        screen = pyautogui.screenshot()
        screen_np = np.array(screen)
        screen_gray = cv2.cvtColor(screen_np, cv2.COLOR_BGR2GRAY)
        resultChampion = cv2.matchTemplate(screen_gray, championImage, cv2.TM_CCOEFF_NORMED)
        locChampion = np.where(resultChampion >= threshold)
        if len(locChampion[0]) > 0:
            print("Campeão Selecionado")
            x, y = locChampion[::-1][0][0], locChampion[::-1][1][0]
            pyautogui.moveTo(x + (championImage.shape[1] // 2), y + (championImage.shape[0] // 2),duration=1)
            pyautogui.click()
            time.sleep(2)
            break
        time.sleep(2)

def runa():
    global running
    image_to_detect = cv2.imread('images/runa.png', cv2.IMREAD_GRAYSCALE)
    while running:
        screen = pyautogui.screenshot()
        screen_np = np.array(screen)
        screen_gray = cv2.cvtColor(screen_np, cv2.COLOR_BGR2GRAY)
        result = cv2.matchTemplate(screen_gray, image_to_detect, cv2.TM_CCOEFF_NORMED)
        loc = np.where(result >= threshold)
        if len(loc[0]) > 0:
            print("Runa Confirmada!")
            x, y = loc[::-1][0][0], loc[::-1][1][0]
            pyautogui.moveTo(x + (image_to_detect.shape[1] // 2), y + (image_to_detect.shape[0] // 2),duration=1)
            pyautogui.click()
            pyautogui.moveTo(x + 400, y - 200,duration=1)
            pyautogui.click()
            time.sleep(2)
            break
        time.sleep(2)
    
def fechar():
    global running
    image_to_detect = cv2.imread('images/fechar.png', cv2.IMREAD_GRAYSCALE)
    while running:
        screen = pyautogui.screenshot()
        screen_np = np.array(screen)
        screen_gray = cv2.cvtColor(screen_np, cv2.COLOR_BGR2GRAY)
        result = cv2.matchTemplate(screen_gray, image_to_detect, cv2.TM_CCOEFF_NORMED)
        loc = np.where(result >= threshold)
        if len(loc[0]) > 0:
            x, y = loc[::-1][0][0], loc[::-1][1][0]
            pyautogui.moveTo(x + (image_to_detect.shape[1] // 2), y + (image_to_detect.shape[0] // 2),duration=1)
            pyautogui.click()
            time.sleep(2)
            break
        time.sleep(2)

def confirmar():
    global running
    image_to_detect = cv2.imread('images/confirm.png', cv2.IMREAD_GRAYSCALE)
    while running:
        screen = pyautogui.screenshot()
        screen_np = np.array(screen)
        screen_gray = cv2.cvtColor(screen_np, cv2.COLOR_BGR2GRAY)
        result = cv2.matchTemplate(screen_gray, image_to_detect, cv2.TM_CCOEFF_NORMED)
        loc = np.where(result >= threshold)
        if len(loc[0]) > 0:
            print("Partida Confirmada!")
            x, y = loc[::-1][0][0], loc[::-1][1][0]
            pyautogui.moveTo(x + (image_to_detect.shape[1] // 2), y + (image_to_detect.shape[0] // 2),duration=1)
            pyautogui.click()
            time.sleep(2)
            break
        time.sleep(2)

def main_loop():
    while running:
        # aceitarPartida()
        buscarChampion()
        selecionarChampion()
        runa()
        fechar()
        confirmar()

def start():
    global running
    running = True
    threading.Thread(target=main_loop).start()

def stop():
    global running
    running = False

def update_champion():
    global champion
    champion = champion_var.get()
    print("Campeão atualizado para:", champion)

def on_closing():
    stop()
    root.destroy()

# Cria a interface gráfica
root = tk.Tk()
root.title("Controle do Bot de Jogo")
root.geometry("300x200")

champion_label = tk.Label(root, text="Nome do Campeão:", font=("Arial", 12))
champion_label.pack()
list = os.listdir('./images/champions/')
champions = []
for champ in list:
    champions += [champ[:-4]]

champions = champions
champion_var = tk.StringVar(root)
champion_var.set(champions[0])  # Valor padrão

champion_menu = tk.OptionMenu(root, champion_var, *champions)
champion_menu.pack()

update_button = tk.Button(root, text="Atualizar Campeão", command=update_champion)
update_button.pack()

start_button = tk.Button(root, text="Iniciar", command=start)
start_button.pack()

stop_button = tk.Button(root, text="Parar", command=stop)
stop_button.pack()

advice_label = tk.Label(root, text="Selecione o campeão no menu acima", font=("Arial", 10))
advice_label.pack()

root.protocol("WM_DELETE_WINDOW", on_closing)

root.mainloop()
