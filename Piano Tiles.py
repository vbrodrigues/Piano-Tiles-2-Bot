# LINK DO GAME: http://www.jogos360.com.br/piano_tiles_2_online.html
#OBS.: não dar nenhum scroll na página e começar da tela de apertar a tile de start já pra começar a partida

import pyautogui as pag 
import matplotlib.pyplot as plt 
import numpy as np
import time 

#Safe Mode: para abortar programa, levar o mouse até o canto superior esquerdo da tela
pag.FAILSAFE = True


tile_width = 87
tile_height = 145
end_game = False
def search_tiles():
    img = pag.screenshot(region = (650, 275, 340, 585))
    img = np.array(img)
    img = img[:, :, 2]
    for i in range(img.shape[0]-1, 0, -tile_height):
        for j in range(img.shape[1]-1, 0, -tile_width):
            if img[i][j] < 10:
                pag.click(j + 650 - tile_width/2, i + 275 + tile_height/2)
                return
            elif 100 < img[i][j] < 160:
                end_game = True

def play():
    img = pag.screenshot(region = (650, 275, 340, 585))
    img = np.array(img)
    img = img[:, :, 2]
    # plt.imshow(img)
    # plt.show()
    start_button_found = False
    for i in range(img.shape[0]-1, 0, -tile_height):
        for j in range(img.shape[1]-1, 0, -tile_width):
            if 190 < img[i][j] < 200:
                start_button_found = True
                pag.click(j + 650 - tile_width/2, i + 275 + tile_height/2)
                break
        if start_button_found:
            break

    for i in range(5000):
        search_tiles()
        if end_game:
            break
        # time.sleep(.01)

play()


