class Planet:

    def __init__(self,name,size,loc):
        self.name = name
        self.size = size
        self.loc = loc
        self.population = 0
        self.temp = 0
        self.sats = []
        self.humanity = False
        self.water = False
        self.oxygen = False
        self.flora = False
        self.fauna = False
        self.flora_list = None
        self.fauna_list = None


    def add_sat(self,sat_list:list):
        for sat in sat_list:
            if sat not in self.sats:
                self.sats.append(sat)

    def set_humanity(self):
        if self.temp >= -20 and self.water and self.oxygen:
            self.humanity = True
        else:
            self.humanity = False

    def set_flora_and_fauna(self):
        flag = None
        if self.water and self.oxygen and self.temp >= -50:
            flag = True
        else:
            flag = False
        self.fauna = flag
        self.flora = flag

    def set_live(self):
        flag = None
        if self.flora and self.fauna:
            self.flora_list = []
            self.fauna_list = []


class Giant(Planet):

    def __init__(self, name, size, loc,):
        super().__init__(name, size, loc)
        self.size += 100


class Gas(Giant):

    def __init__(self,name,size,loc,gas_type):
        super().__init__(name,size,loc)
        self.gas_type = gas_type
        self.temp = -273


    def set_humanity(self):
        if self.temp >= -20 and self.gas_type == 'O':
            self.humanity = True
            print(f'Планета: {self.name} пригодна для жилья!')
        else:
            print(f'Планета: {self.name} не пригодна для жилья!')


    def add_population(self,people_count):
        self.population += people_count


class Soil(Giant):

    def __init__(self,name,size,loc,soil):
        super().__init__(name,size,loc)
        self.soil = soil


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

    def __init__(self,name,predator_type,what_eats,lifespan):
        super().__init__(name)
        self.predator_type = predator_type
        self.what_eats = what_eats
        self.lifespan = lifespan
class Mammal(Fauna):

    def __init__(self, name, mammal_type,lifespan):
        super().__init__(name)
        self.mammal_type = mammal_type
        self.lifespan = lifespan



friendly = Gas('Friend', 30, 'andromeda', 'O')
friendly.temp = -19
friendly.set_humanity()
friendly.add_population(100)
friendly.water = True
friendly.oxygen = True
friendly.set_flora_and_fauna()
friendly.set_live()

soil_planet = Soil('Zemlya',15,'solar system','zemlya')
giant_planet = Giant('Big',111,'milky way')

print(friendly.__dict__)
print(giant_planet.__dict__)
