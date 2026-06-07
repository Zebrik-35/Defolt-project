import pydirectinput
import time
import mouse
import config

# Загружаем конфиг

WAIT_TIME_PRESS = config.WAIT_TIME_PRESS
SCAN_TIME = config.SCAN_TIME
VIBOR_CELI = config.VIBOR_CELI

DRONE_WORK_TIME = config.DRONE_WORK_TIME
OGNEVAY_GRUPPA = config.OGNEVAY_GRUPPA

VREMY_ZAHODA_V_IGRU = config.VREMY_ZAHODA_V_IGRU
VREMY_VIHODA = config.VREMY_VIHODA

KNOPKA_MENU = config.KNOPKA_MENU
DEISTVIE_VVERH = config.DEISTVIE_VVERH
VIBOR = config.VIBOR

def scan(): #Сканирование точки

    print("Нажимаю T")
    pydirectinput.press(VIBOR_CELI)
    time.sleep(WAIT_TIME_PRESS)
    print('Сканирую - 1')
    pydirectinput.mouseDown(button='right')
    time.sleep(SCAN_TIME + 1) #Время сканирование + 1 секунда прозопас
    pydirectinput.mouseUp(button='right')
    time.sleep(1)

def vzlom():

    print('Взлом')
    #выбор цели для дрона
    mouse.wheel(1)
    #взлом дрона
    time.sleep(WAIT_TIME_PRESS)
    pydirectinput.press(OGNEVAY_GRUPPA) #в настройках задать доп клавишу для основной или вторичной огневой группы, в зависимости от того, где дроны
    print('Жду')
    time.sleep(DRONE_WORK_TIME + 7) #Время взлома + время полета до передатчика

def perezahod():

    #Выход в меню
    print('Выхожу меню')
    pydirectinput.press(KNOPKA_MENU)
    time.sleep(WAIT_TIME_PRESS)
    pydirectinput.press(DEISTVIE_VVERH)
    time.sleep(WAIT_TIME_PRESS)
    pydirectinput.press(VIBOR)
    time.sleep(WAIT_TIME_PRESS)
    pydirectinput.press(VIBOR)
    time.sleep(VREMY_VIHODA) #Ждем загрузки меню
    #Уже меню
    pydirectinput.press(VIBOR)
    time.sleep(WAIT_TIME_PRESS)
    pydirectinput.press(VIBOR)
    print('Захожу')
    time.sleep(VREMY_ZAHODA_V_IGRU)