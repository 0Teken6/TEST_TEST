from basic import Creature

class Hero(Creature):
    def __init__(self, name):
        super().__init__("Peaceful")
        self.name = name

    def __str__(self):
        return f'Class Hero with name {self.name}.'
    