from pynput.mouse import Listener
from pynput import keyboard
import time
import threading
import screen_brightness_control as sbc
import os

time_elapsed = 0
running = True

# Get initial monitor brightness
brightness = sbc.get_brightness()[0]
print(brightness)

def process():
    global time_elapsed
    while running:
        time.sleep(1)
        print(time_elapsed)
        time_elapsed += 1

        if time_elapsed == 600: #10 minutes
            sbc.set_brightness(10)
        elif time_elapsed == 900: # 15 minutes
            os.system("shutdown /h")

th = threading.Thread(target=process)
th.daemon = True
th.start()

def on_click(x, y, button, pressed):
    global time_elapsed, running
    if pressed:
        time_elapsed = 0
        sbc.set_brightness(brightness)

def on_press(key):
    global time_elapsed
    time_elapsed = 0
    sbc.set_brightness(brightness)

key_listener = keyboard.Listener(on_press=on_press)
key_listener.start()

with Listener(on_click=on_click) as listener:
    listener.join()