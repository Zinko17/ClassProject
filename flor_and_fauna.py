import Planets

class Flora:

    def __init__(self,name,lifespan,habitat,plant_type):
        self.name = name
        self.lifespan = lifespan
        self.habitat = habitat
        self.plant_type = plant_type
        self.plant_size = 0

class Fauna:

    def __init__(self,name):
        self.name = name

class Predator(Fauna):

    def __init__(self,name:str,predator_type:str,what_eats:str,lifespan:int):
        super().__init__(name)
        self.predator_type = predator_type
        self.what_eats = what_eats
        self.lifespan = lifespan

    # def check_planet(self,planet:Planets.Planet):
    #     if planet.fauna:
    #         print('YES!')

class Mammal(Fauna):

    def __init__(self, name:str, mammal_type:str,lifespan:int):
        super().__init__(name)
        self.mammal_type = mammal_type
        self.lifespan = lifespan

    def check_planet(self,planet:Planets.Planet):
        if planet.flora and planet.fauna and not planet.humanity:
            planet.add_fauna(self)


shark = Predator('baby shark','sea','all',20)
giraffe = Mammal('Malwan','earth',20)
giraffe.check_planet(Planets.friendly)
print(Planets.friendly.__dict__)
print(help(Planets.friendly))