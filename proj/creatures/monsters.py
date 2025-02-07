from basic import Creature

class Monster(Creature):
    def __init__(self, hp, ad):
        super().__init__("Hostile")
        self.hp = hp
        self.ad = ad

    def __str__(self):
        return f'Class Monster with {self.hp} hp and {self.ad} ad.'
    

class Goblin(Monster):
    GOBLINS_CREATED = 0
    
    def __init__(self, hp, ad):
        super().__init__(hp, ad)
        Goblin.GOBLINS_CREATED += 1

    def __str__(self):
        return f'Goblin with {self.hp} hp and {self.ad} ad.'

