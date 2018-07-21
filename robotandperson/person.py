import robot


class Person():
    name = ''
    personality = ''
    isSitting = False
    robotOwned = None

    def __init__(self, n, p, i):
        self.name = n
        self.personality = p
        self.isSitting = i

    def sitDown(self):
        self.isSitting = True

    def standUp(self):
        self.isSitting = False
