import pydirectinput
import keyboard
import time
import mouse

def scan(wait_time_press): #Сканирование точки
    
    print("Нажимаю T")
    pydirectinput.press("t")
    time.sleep(wait_time_press)
    print('Сканирую - 1')
    pydirectinput.mouseDown(button='right')
    time.sleep(6) #Время сканирование + 1 секунда прозопас
    pydirectinput.mouseUp(button='right')

def vzlom(wait_time_press):
    
    print('Взлом')
    #выбор цели для дрона
    mouse.wheel(1)
    #взлом дрона
    time.sleep(wait_time_press)
    pydirectinput.press(";") #в настройках задать доп клавишу для основной или вторичной огневой группы, в зависимости от того, где дроны
    print('Жду')

def perezahod(wait_time_press):
    #Выход в меню
    print('Выхожу меню')
    pydirectinput.press("esc")
    time.sleep(wait_time_press)
    pydirectinput.press("w")
    time.sleep(wait_time_press)
    pydirectinput.press("space")
    time.sleep(wait_time_press)
    pydirectinput.press("space")
    time.sleep(5) #Ждем загрузки меню
    #Уже меню
    pydirectinput.press("space")
    time.sleep(wait_time_press)
    pydirectinput.press("space")
    print('Захожу')