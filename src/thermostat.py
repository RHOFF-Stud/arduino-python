import time

class Thermostat():
    def loop(self):
        while self.running:
            self.temperature = round(self.thermo_pin.read() * 100, 4)
            time.sleep(1)

    def stop(self):
        self.running = False

    def start(self):
        self.running = True
        while self.thermo_pin.read() == None: pass
        self.loop()

    def __init__(self, board):
        self.board = board
        self.running = False
        self.thermo_pin = board.get_pin('a:5:i')
        self.thermo_pin.enable_reporting()

        self.temperature = 0.0
