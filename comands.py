import pydirectinput
import keyboard
import time
import mouse
import config


def scan(): #Сканирование точки
    wait_time_press = config.WAIT_TIME_PRESS
    scan_time = config.SCAN_TIME
    vibor_celi = config.VIBOR_CELI

    print("Нажимаю T")
    pydirectinput.press(vibor_celi)
    time.sleep(wait_time_press)
    print('Сканирую - 1')
    pydirectinput.mouseDown(button='right')
    time.sleep(scan_time+1) #Время сканирование + 1 секунда прозопас
    pydirectinput.mouseUp(button='right')
    time.sleep(1)

def vzlom():
    wait_time_press = config.WAIT_TIME_PRESS
    drone_work_time = config.DRONE_WORK_TIME
    ognevay_gruppa = config.OGNEVAY_GRUPPA

    print('Взлом')
    #выбор цели для дрона
    mouse.wheel(1)
    #взлом дрона
    time.sleep(wait_time_press)
    pydirectinput.press(ognevay_gruppa) #в настройках задать доп клавишу для основной или вторичной огневой группы, в зависимости от того, где дроны
    print('Жду')
    time.sleep(drone_work_time+7) #Время взлома + время полета до передатчика

def perezahod():
    wait_time_press = config.WAIT_TIME_PRESS
    vremy_zahoda_v_igru = config.VREMY_ZAHODA_V_IGRU
    vremy_vihoda = config.VREMY_VIHODA
    knopka_menu = config.KNOPKA_MENU
    deistvie_vverh = config.DEISTVIE_VVERH
    vibor = config.VIBOR

    #Выход в меню
    print('Выхожу меню')
    pydirectinput.press(knopka_menu)
    time.sleep(wait_time_press)
    pydirectinput.press(deistvie_vverh)
    time.sleep(wait_time_press)
    pydirectinput.press(vibor)
    time.sleep(wait_time_press)
    pydirectinput.press(vibor)
    time.sleep(vremy_vihoda) #Ждем загрузки меню
    #Уже меню
    pydirectinput.press(vibor)
    time.sleep(wait_time_press)
    pydirectinput.press(vibor)
    print('Захожу')
    time.sleep(vremy_zahoda_v_igru)