import time

class Button():
    def loop(self):
        while self.running:
            if self.button.read():
                self.state = self.button.read() > 0.7
                print(self.button.read())
            time.sleep(1)

    def stop(self):
        self.running = False

    def start(self):
        self.running = True
        self.loop()

    def __init__(self, board):
        self.board = board
        self.running = False
        self.button = board.get_pin('a:3:i')
        self.button.enable_reporting()
        self.state = False