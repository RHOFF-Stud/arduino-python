import pyfirmata as pf
import time

class Blink():
    def loop(self):
        while self.running:
            self.LED_pin.write(True) 
            time.sleep(0.5) 
            self.LED_pin.write(False) 
            time.sleep(0.5)

    def stop(self):
        self.running = False

    def start(self):
        self.running = True
        self.loop()

    def __init__(self, board):
        self.board = board
        self.running = False
        self.LED_pin = board.get_pin('d:2:o')