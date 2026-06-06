import pydirectinput
import keyboard
import time
import mouse

def scan(): #Сканирование точки

    print("Нажимаю T")
    pydirectinput.press("t")

    time.sleep(1)
    print('Сканирую - 1')
    pydirectinput.mouseDown(button='right')
    time.sleep(6)
    pydirectinput.mouseUp(button='right')

def vzlom():
    print('Взлом')
    #выбор цели для дрона
    mouse.wheel(1)
    #взлом дрона
    time.sleep(1)
    pydirectinput.press(";") #в настройках задать доп клавишу для основной или вторичной огневой группы, в зависимости от того, где дроны
    print('Жду')

def perezahod():
    print('Выхожу меню')
    pydirectinput.press("esc")
    time.sleep(1)
    pydirectinput.press("w")
    time.sleep(1)
    pydirectinput.press("space")
    time.sleep(1)
    pydirectinput.press("space")
    time.sleep(5)
    #Уже меню
    pydirectinput.press("space")
    time.sleep(1)
    pydirectinput.press("space")
    print('Захожу')