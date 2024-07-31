import pyautogui as pg
import keyboard
import actions
import constantes
import json
pg.useImageNotFoundException(False)  # ODEIO ESSA MERDA!!!!!!!!!


def kill_monster():

        while actions.check_battle() is None:
            print('Matando monstros')
            pg.press('space')
            while pg.locateOnScreen('imgs/red_target.png', confidence=0.7, region=constantes.REGION_BATTLE) is not None:
                print('esperando monstro morrer')
                pg.sleep(0.5) 
            print('procurando outro monstro')
        pg.sleep(0.5)

#def get_loot():
#   loot = pg.locateAllOnScreen('imgs/monster_dead.PNG', confidence=0.9, region=constantes.REGION_LOOT)
#    for box in loot:
#        x, y =pg.center(box)
#        pg.moveTo(x, y)
#        pg.click(button="right")


def go_to_flag(path, wait):
     flag = pg.locateOnScreen(path, confidence=0.8, region=constantes.MAPA)
     x, y= pg.center(flag)
     pg.moveTo(x, y)
     pg.click(wait)


def check_player_position():
    return pg.locateOnScreen('imgs/point_player.png', confidence=0.8, region=constantes.MAPA)



def run():
    with open(f'{constantes.FOLDER_NAME}/infos.json', 'r') as file:
        data = json.loads(file.read())
        for item in data:
            kill_monster()
            pg.sleep(1)
            go_to_flag(item['path'], item['wait'])
            if check_player_position():
                kill_monster()
                go_to_flag(item['path'], item['wait'])
            actions.eat_food()
            actions.hole_down(item['down_hole'])
            actions.hole_up(item['up_hole'],f'{constantes.FOLDER_NAME}imgs/anchor_floor2.PNG')


keyboard.wait('h')
run()
















        

