import pydirectinput
import keyboard
import time
import mouse
import comands

wait_time_press = 0.5 #Время между нажатий клавишь
RUN = True

def stop():
    global RUN
    RUN = False

keyboard.add_hotkey("F1", stop)

print("Переключись в игру. Старт через 5 секунд...")
time.sleep(5)

while RUN:
    #Выбор корабля носителя
    comands.scan(wait_time_press)
    time.sleep(1)

    #Выбор передатчика данных
    comands.scan(wait_time_press)
    time.sleep(1)

    #Взлом
    comands.vzlom(wait_time_press)
    time.sleep(30)

    #меню и выход
    comands.perezahod(wait_time_press)
    time.sleep(30)

print('Программа остановлена')