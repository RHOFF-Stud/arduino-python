import pyfirmata as pf
import time

serial_port = 'COM3'
board = pf.Arduino(serial_port)

it = pf.util.Iterator(board)
it.start()

button = board.get_pin('a:3:i')

running = True
while running:
    if button.read():
        print(button.read())
    time.sleep(0.1)

board.exit()
