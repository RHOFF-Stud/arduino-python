import pyfirmata as pf
import time
import threading as thr

from display import Display
from thermostat import Thermostat
from blink import Blink
from controller import Controller

serial_port = 'COM3'
board = pf.Arduino(serial_port)

it = pf.util.Iterator(board)
it.start()

#my_blink = Blink(board)
my_display = Display(board)
my_thermostat = Thermostat(board)
#controller = Controller()

#blink_id = controller.add_method(my_blink.start)
#controller.threads[blink_id].start()

#display_id = controller.add_method(my_display.start)
thermostat_thread = thr.Thread(target=my_thermostat.start)
thermostat_thread.start()

display_thread = thr.Thread(target=my_display.start)
display_thread.start()

my_display.value = 1234

time.sleep(10)

running = True
while running:
    my_display.value = my_thermostat.temperature
    print(thr.active_count())
    if (thr.active_count() == 2):
        board.exit()
        running = False
    time.sleep(1)