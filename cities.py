class City:
    def __init__(self, name: str):
        self.name = name
        self.first = name[0]
        self.last = name[-1]
