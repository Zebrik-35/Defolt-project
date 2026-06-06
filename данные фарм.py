import pydirectinput
import keyboard
import time
import mouse
import comands


RUN = True

def stop():
    global RUN
    RUN = False

keyboard.add_hotkey("F1", stop)

print("Переключись в игру. Старт через 5 секунд...")
time.sleep(5)

while RUN:
    #Выбор корабля носителя
    '''print("Нажимаю T")
    pydirectinput.press("t")

    time.sleep(1)
    print('Сканирую - 1')
    pydirectinput.mouseDown(button='right')
    time.sleep(6)
    pydirectinput.mouseUp(button='right')'''

    comands.scan()
    
    time.sleep(1)
    #Выбор передатчика данных
    '''print("Нажимаю T")
    pydirectinput.press("t")

    time.sleep(1)
    print('Сканирую - 2')
    pydirectinput.mouseDown(button='right')
    time.sleep(6)
    pydirectinput.mouseUp(button='right')'''

    comands.scan()

    time.sleep(1)

    '''#выбор цели для дрона
    mouse.wheel(1)
    #взлом дрона
    time.sleep(1)
    pydirectinput.press(";")
    print('Жду')'''

    comands.vzlom()

    time.sleep(30)

    #меню и выход
    '''print('Меню')
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
    print('Захожу')'''

    comands.perezahod()

    time.sleep(30)
