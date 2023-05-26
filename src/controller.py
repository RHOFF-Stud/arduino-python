import threading as thr

class Controller():
    def add_method(self, method):
        new_thread = thr.Thread(target=method)
        self.threads[self.id] = new_thread
        self.id += 1
        return self.id - 1
    
    def done(self):
        return thr.active_count() == 1

    def __init__(self):
        self.threads = {}
        self.id = 0