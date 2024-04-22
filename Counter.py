class Count:
    def __init__(self, start=0):
        self.start=start
        self.time=0
        self.odometer = 0

    def countup(self):
        self.start += 1

    def countdown(self):
        self.