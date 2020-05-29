class Token:
    def __init__(self, type, value):
        self.type = type
        self.value = value

    def print(self):
        print(self.type + ": " + self.value)
