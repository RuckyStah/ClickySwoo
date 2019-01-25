import time
import threading
import random
from pynput.mouse import Button, Controller
from pynput.keyboard import Listener, Key


button = Button.left
start_stop_key = Key.ctrl_l
exit_key = Key.esc


print("Left Ctrl: Start/Pause script" + "\n"
      "Esc:       Exit script")

    


class Clicker(threading.Thread):
    def __init__(self, button):
        super().__init__()
        self.delay = None
        self.button = button
        self.running = False
        self.program_running = True


    def get_delay(self):
        self.delay = random.uniform(0.3, 0.7)


    def start_clicking(self):
        self.running = True


    def stop_clicking(self):
        self.running = False


    def exit(self):
        print("Programme exiting")
        self.stop_clicking()
        self.program_running = False


    def run(self):
        while self.program_running:
            while self.running:
                self.get_delay()
                mouse.click(self.button)
                time.sleep(self.delay)



mouse = Controller()
click_thread = Clicker(button)
click_thread.start()


def on_press(key):
    if key == start_stop_key:
        if click_thread.running:
            click_thread.stop_clicking()
        else:
            click_thread.start_clicking()

    elif key == exit_key:
        click_thread.exit()
        listener.stop()


with Listener(on_press=on_press) as listener:
    listener.join()
    
