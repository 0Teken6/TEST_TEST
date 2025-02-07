creature_types = ('Peaceful', 'Hostile', 'NPC')

class Creature:
    def __init__(self, cr_type):
        if cr_type not in creature_types:
            raise ValueError(f"Invalid creature type: {cr_type}. Valid types are: {creature_types}")
        self.cr_type = cr_type

    def __str__(self):
        return self.cr_type
        
