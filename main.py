import time
import threading
from pynput.mouse import Button, Controller as MouseController
import keyboard

mouse = MouseController()
running = False
right_down = False

def toggle():
    global running, right_down
    running = not running
    if running:
        print("Makró bekapcsolva")
        if not right_down:
            mouse.press(Button.right)
            right_down = True
    else:
        print("Makró kikapcsolva")
        if right_down:
            mouse.release(Button.right)
            right_down = False

def click_loop():
    while True:
        if running:
            mouse.click(Button.left)
        time.sleep(30)

# Hotkey beállítás
keyboard.add_hotkey('F6', toggle)

# Külön threaden futtatjuk a ciklust
threading.Thread(target=click_loop, daemon=True).start()

print("F6-tal ki/be kapcsolható. Nyomj Ctrl+C-t a kilépéshez.")
keyboard.wait()  # főszál várakozik, hogy a script élve maradjon
