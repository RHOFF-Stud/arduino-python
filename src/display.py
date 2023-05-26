class Display():
    def display_clear(self):
        self.pins["TOP"].write(False)
        self.pins["TOPLEFT"].write(False)
        self.pins["TOPRIGHT"].write(False)
        self.pins["CENTER"].write(False)
        self.pins["BOTTOM"].write(False)
        self.pins["BOTTOMLEFT"].write(False)
        self.pins["BOTTOMRIGHT"].write(False)
        self.pins["COMMA"].write(False)

    def display_minus(self):
        self.pins["CENTER"].write(True)
    
    def display_comma(self):
        self.pins["COMMA"].write(True)

    def display_0(self):
        self.pins["TOP"].write(True)
        self.pins["TOPLEFT"].write(True)
        self.pins["TOPRIGHT"].write(True)
        self.pins["BOTTOM"].write(True)
        self.pins["BOTTOMLEFT"].write(True)
        self.pins["BOTTOMRIGHT"].write(True)
    
    def display_1(self):
        self.pins["TOPRIGHT"].write(True)
        self.pins["BOTTOMRIGHT"].write(True)
    
    def display_2(self):
        self.pins["TOP"].write(True)
        self.pins["TOPRIGHT"].write(True)
        self.pins["CENTER"].write(True)
        self.pins["BOTTOM"].write(True)
        self.pins["BOTTOMLEFT"].write(True)
    
    def display_3(self):
        self.pins["TOP"].write(True)
        self.pins["TOPRIGHT"].write(True)
        self.pins["CENTER"].write(True)
        self.pins["BOTTOM"].write(True)
        self.pins["BOTTOMRIGHT"].write(True)
    
    def display_4(self):
        self.pins["TOPLEFT"].write(True)
        self.pins["TOPRIGHT"].write(True)
        self.pins["CENTER"].write(True)
        self.pins["BOTTOMRIGHT"].write(True)
        self.pins["COMMA"].write(True)        
    
    def display_5(self):
        self.pins["TOP"].write(True)
        self.pins["TOPLEFT"].write(True)
        self.pins["CENTER"].write(True)
        self.pins["BOTTOM"].write(True)
        self.pins["BOTTOMRIGHT"].write(True)
    
    def display_6(self):
        self.pins["TOP"].write(True)
        self.pins["TOPLEFT"].write(True)
        self.pins["CENTER"].write(True)
        self.pins["BOTTOM"].write(True)
        self.pins["BOTTOMLEFT"].write(True)
        self.pins["BOTTOMRIGHT"].write(True)
    
    def display_7(self):
        self.pins["TOP"].write(True)
        self.pins["TOPRIGHT"].write(True)
        self.pins["CENTER"].write(True)
        self.pins["BOTTOMRIGHT"].write(True)
    
    def display_8(self):
        self.pins["TOP"].write(True)
        self.pins["TOPLEFT"].write(True)
        self.pins["TOPRIGHT"].write(True)
        self.pins["CENTER"].write(True)
        self.pins["BOTTOM"].write(True)
        self.pins["BOTTOMLEFT"].write(True)
        self.pins["BOTTOMRIGHT"].write(True)
    
    def display_9(self):
        self.pins["TOP"].write(True)
        self.pins["TOPLEFT"].write(True)
        self.pins["TOPRIGHT"].write(True)
        self.pins["CENTER"].write(True)
        self.pins["BOTTOM"].write(True)
        self.pins["BOTTOMRIGHT"].write(True)

    def display(self, digit, value, has_comma=False):
        self.display_clear()

        if value == "":
            self.control_pins[digit].write(True)
            return
        elif value == "-": self.display_minus()
        elif value == "0": self.display_0()
        elif value == "1": self.display_1()
        elif value == "2": self.display_2()
        elif value == "3": self.display_3()
        elif value == "4": self.display_4()
        elif value == "5": self.display_5()
        elif value == "6": self.display_6()
        elif value == "7": self.display_7()
        elif value == "8": self.display_8()
        elif value == "9": self.display_9()

        if has_comma: self.display_comma()

        self.control_pins[digit].write(False)
        self.control_pins[digit].write(True)            

    def loop(self):
        while self.running:
            count = self.display_length
            comma = False
            string_value = str(self.value)[::-1]
            for substring in string_value:
                if count == 0:
                    break
                elif substring == ".":
                    comma = True
                elif substring.isnumeric():
                    self.display(digit=count, value=substring, has_comma=comma)
                    comma = False
                    count -= 1
                elif substring == "-": 
                    self.display(digit=count, value=substring, has_comma=comma)
                    comma = False
                    count -= 1

    def stop(self):
        self.display_clear()
        for digit in self.control_pins:
            self.control_pins[digit].write(True)
        self.running = False

    def start(self):
        self.running = True
        self.loop()

    def __init__(self, board, initial_value=None, display_length=4):
        self.board = board
        self.value = initial_value
        self.display_length = display_length

        self.running = False

        self.control_pins = {}
        self.control_pins[1] = board.get_pin('d:13:o')
        self.control_pins[2] = board.get_pin('d:10:o')
        self.control_pins[3] = board.get_pin('d:9:o')
        self.control_pins[4] = board.get_pin('d:7:o')

        self.pins = {}
        self.pins["TOP"] = board.get_pin('d:12:o')
        self.pins["TOPLEFT"] = board.get_pin('d:11:o')
        self.pins["TOPRIGHT"] = board.get_pin('d:8:o')
        self.pins["CENTER"] = board.get_pin('d:6:o')

        self.pins["BOTTOM"] = board.get_pin('d:3:o')
        self.pins["BOTTOMLEFT"] = board.get_pin('d:2:o')
        self.pins["BOTTOMRIGHT"] = board.get_pin('d:5:o')

        self.pins["COMMA"] = board.get_pin('d:4:o')
        