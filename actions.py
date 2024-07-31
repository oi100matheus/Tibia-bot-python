import pyautogui as pg
import constantes
import keyboard
pg.useImageNotFoundException(False)


def eat_food():
    pg.press('F6')
    print('comendo food...')

def hole_down(should_down=True):
    if should_down:
        box = pg.locateOnScreen('imgs/escada.PNG', confidence=0.7)
        if box:
            x, y = pg.center(box)
            pg.moveTo(x, y)
            pg.click()
            pg.sleep(5)


def hole_up(img_anchor):
    box = pg.locateOnScreen(img_anchor, confidence=0.8)
    if box:
        x, y = pg.center(box)
        pg.moveTo(x, y, 3)
keyboard.wait('h')
hole_up('imgs/anchor_floor2.PNG')

def check_status(name, delay, x, y, rgb, buttom_name):
    print(f'checando {name}...')
    pg.sleep(delay)
    if pg.pixelMatchesColor(x, y, rgb):
        pg.press(buttom_name)

def check_battle():
    return pg.locateOnScreen('imgs/region_battle.PNG', region=constantes.REGION_BATTLE)









