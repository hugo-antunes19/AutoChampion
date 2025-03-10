import cv2
import numpy as np
import pyautogui
import time
import threading
import tkinter as tk
from tkinter import ttk
import sys
import os

threshold = 0.8
champion = "Lee sin"
running = False

def resource_path(relative_path):
    """ Obtenha o caminho absoluto para o recurso, lidando com pacotes PyInstaller. """
    base_path = getattr(sys, '_MEIPASS', os.path.dirname(os.path.abspath(__file__)))
    return os.path.join(base_path, relative_path)

def aceitarPartida():
    global running
    image_to_detect = cv2.imread(resource_path('assets/images/accept.png'), cv2.IMREAD_GRAYSCALE)
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
    buscarImage = cv2.imread(resource_path('assets\\images\\buscar.png'), cv2.IMREAD_GRAYSCALE)
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
    championImage = cv2.imread(resource_path(f'assets/images/champions/{champion}.png'), cv2.IMREAD_GRAYSCALE)
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
    image_to_detect = cv2.imread(resource_path('assets/images/runa.png'), cv2.IMREAD_GRAYSCALE)
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
    image_to_detect = cv2.imread(resource_path('assets/images/fechar.png'), cv2.IMREAD_GRAYSCALE)
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
    image_to_detect = cv2.imread(resource_path('assets/images/confirm.png'), cv2.IMREAD_GRAYSCALE)
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

def buscarBan():
    global running
    image_to_detect = cv2.imread(resource_path('assets/images/buscarBanir.png'), cv2.IMREAD_GRAYSCALE)
    while running:
        screen = pyautogui.screenshot()
        screen_np = np.array(screen)
        screen_gray = cv2.cvtColor(screen_np, cv2.COLOR_BGR2GRAY)
        result = cv2.matchTemplate(screen_gray, image_to_detect, cv2.TM_CCOEFF_NORMED)
        loc = np.where(result >= threshold)
        if len(loc[0]) > 0:
            print("Buscando banimento")
            x, y = loc[::-1][0][0], loc[::-1][1][0]
            pyautogui.moveTo(x + (image_to_detect.shape[1] // 2), y + (image_to_detect.shape[0] // 2),duration=1)
            pyautogui.click()
            time.sleep(1)
            pyautogui.typewrite(str(ban))
            time.sleep(2)
            break
        time.sleep(2)

def banirChampion():
    global running
    banImage = cv2.imread(resource_path(f'assets/images/champions/{ban}.png'), cv2.IMREAD_GRAYSCALE)
    while running:
        screen = pyautogui.screenshot()
        screen_np = np.array(screen)
        screen_gray = cv2.cvtColor(screen_np, cv2.COLOR_BGR2GRAY)
        resultChampion = cv2.matchTemplate(screen_gray, banImage, cv2.TM_CCOEFF_NORMED)
        locChampion = np.where(resultChampion >= threshold)
        if len(locChampion[0]) > 0:
            print("Banimento Selecionado")
            x, y = locChampion[::-1][0][0], locChampion[::-1][1][0]
            pyautogui.moveTo(x + (banImage.shape[1] // 2), y + (banImage.shape[0] // 2),duration=1)
            pyautogui.click()
            time.sleep(2)
            break
        time.sleep(2)

def banir():
    global running
    image_to_detect = cv2.imread(resource_path('assets/images/banir.png'), cv2.IMREAD_GRAYSCALE)
    while running:
        screen = pyautogui.screenshot()
        screen_np = np.array(screen)
        screen_gray = cv2.cvtColor(screen_np, cv2.COLOR_BGR2GRAY)
        result = cv2.matchTemplate(screen_gray, image_to_detect, cv2.TM_CCOEFF_NORMED)
        loc = np.where(result >= threshold)
        if len(loc[0]) > 0:
            print("Banimento confirmado")
            x, y = loc[::-1][0][0], loc[::-1][1][0]
            pyautogui.moveTo(x + (image_to_detect.shape[1] // 2), y + (image_to_detect.shape[0] // 2),duration=1)
            pyautogui.click()
            time.sleep(2)
            break
        time.sleep(2)

def main_loop():
    while running:
        if aceitar_var.get(): aceitarPartida()
        else:
            aceitarPartida()
            if Banimento_var.get():
                buscarBan()
                banirChampion()
                banir()
            else:
                time.sleep(45)
            buscarChampion()
            selecionarChampion()
            if runa_var.get(): runa()
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
    
def update_ban():
    global ban
    ban = ban_var.get()
    print("Banimento atualizado para:", ban)

def on_closing():
    stop()
    root.destroy()

def filter_champions(event):
    typed_text = champion_var.get()
    if typed_text == '':
        champion_menu['values'] = champions
    else:
        filtered_champions = [champ for champ in champions if typed_text.lower() in champ.lower()]
        champion_menu['values'] = filtered_champions

def filter_bans(event):
    typed_text = ban_var.get()
    if typed_text == '':
        ban_menu['values'] = champions
    else:
        filtered_champions = [champ for champ in champions if typed_text.lower() in champ.lower()]
        ban_menu['values'] = filtered_champions

# Cria a interface gráfica
root = tk.Tk()
root.title("AutoSelect Champion")
root.iconbitmap(resource_path('assets/images/icon.ico'))
root.geometry("300x350")

# Advice
advice_label = tk.Label(root, text="Digite as iniciais \nou selecione o campeão no menu acima.", font=("Arial", 10))
advice_label.pack()

# Ban button
ban_label = tk.Label(root, text="Banimento:", font=("Arial", 12))
ban_label.pack()
list = os.listdir(resource_path('assets/images/champions/'))
champions = []
for champ in list:
    champions += [champ[:-4]]
    
ban_var = tk.StringVar(root)

ban_menu = ttk.Combobox(root, textvariable=ban_var, values=champions)
ban_menu.pack()
ban_menu.bind('<KeyRelease>', filter_bans)

ban_button = tk.Button(root, text="Atualizar Banimento", command=update_ban)
ban_button.pack()

champion_label = tk.Label(root, text="Seu Campeão:", font=("Arial", 12))
champion_label.pack()
champion_var = tk.StringVar(root)

champion_menu = ttk.Combobox(root, textvariable=champion_var, values=champions)
champion_menu.pack()
champion_menu.bind('<KeyRelease>', filter_champions)

update_button = tk.Button(root, text="Atualizar Campeão", command=update_champion)
update_button.pack()

start_button = tk.Button(root, text="Iniciar", command=start)
start_button.pack()

stop_button = tk.Button(root, text="Parar", command=stop)
stop_button.pack()

# Flag Runa
runa_var = tk.IntVar()  # Variável para armazenar o estado (0 ou 1)
runa_check = tk.Checkbutton(root, text="Runas Automáticas", variable=runa_var)
runa_check.pack()

# Flag Banimento
Banimento_var = tk.IntVar()  # Variável para armazenar o estado (0 ou 1)
Banimento_check = tk.Checkbutton(root, text="Banimenmto Automático", variable=Banimento_var)
Banimento_check.pack()

# Flag apenas aceitar partida
aceitar_var = tk.IntVar()  # Variável para armazenar o estado (0 ou 1)
aceitar_check = tk.Checkbutton(root, text="APENAS aceitar partida", variable=aceitar_var)
aceitar_check.pack()

root.protocol("WM_DELETE_WINDOW", on_closing)

root.mainloop()

# python -m PyInstaller --onefile --add-data "assets;assets" interface2.py