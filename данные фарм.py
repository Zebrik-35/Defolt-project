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
    comands.scan()

    #Выбор передатчика данных
    comands.scan()

    #Взлом
    comands.vzlom()

    #меню и выход
    comands.perezahod()

print('Программа остановлена')