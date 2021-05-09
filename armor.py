class Armor:

    def __init__(self,name:str,size:int,weight:int,power:int,
                 stamina=0,health=0,defense=0):
        self.name = name
        self.size = size
        self.weight = weight
        self.power = power
        self.stamina = stamina
        self.health = health
        self.defense = defense
        self.__armor_type = None


    def armor_type(self,type):
        if type == 'rare':
            self.power *= 1.1
        elif type == 'legendary':
            self.power *= 1.7
        self.__armor_type = type