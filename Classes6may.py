class Human:

    def __init__(self,name,age,weight,height,gender):
        self.name = name
        self.age = age
        self.weight = weight
        self.height = height
        self.gender = gender
        self.soul = True
        self.health = 100
        self.viruses = []

    def __str__(self):
        return self.name


    def __repr__(self):
        return self.name

    def add_viruses(self,viruse):
        if viruse not in self.viruses:
            self.viruses.append(viruse)
            self.health -= 10
            print(f'Человек болен {viruse},текущее здоровье {self.health}')
human1 = Human(name='john',age=48,weight=90,height=185,gender='M')
human1.add_viruses('covid')
print(human1.viruses)
human2 = Human(name='Sue',age=50,weight=40,height=160,gender='F')

humans = [human1,human2]
print(humans)

