import pyfirmata as pf
import time
import threading as thr

from display import Display
from thermostat import Thermostat
from button import Button
from blink import Blink
from controller import Controller

serial_port = 'COM3'
board = pf.Arduino(serial_port)

it = pf.util.Iterator(board)
it.start()

my_display = Display(board)
my_thermostat = Thermostat(board)
my_button = Button(board)

thermostat_thread = thr.Thread(target=my_thermostat.start)
thermostat_thread.start()

display_thread = thr.Thread(target=my_display.start)
display_thread.start()

button_thread = thr.Thread(target=my_button.start)
button_thread.start()

time.sleep(5)

running = True
while running:
    my_display.value = my_thermostat.temperature
    if my_button.state:
        print("I have been pressed")
        my_display.stop()
        my_thermostat.stop()
        my_button.stop()
    if (thr.active_count() == 2):
        board.exit()
        running = False
    time.sleep(1)