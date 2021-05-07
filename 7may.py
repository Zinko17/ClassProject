# class Employe:
#     """
#     Описание сотрудников нашей компании
#     """
#
#
#     def __init__(self,full_name,age,email,address,phone,position):
#         self.full_name = full_name
#         self.age = age
#         self.email = email
#         self.address = address
#         self.phone = phone
#         self.position = position
#         self.salary = 0
#
#     def __repr__(self):
#         return  f'Сотрудник: {self.full_name}'
#
#     def set_salary(self):
#         if self.position == 'developer':
#             self.salary = 100000
#         elif self.position == 'manager':
#             self.salary = 90000
#
# john = Employe('john snow',18,'winteriscome@gmail.com','winterfall','+123456','developer')
# denis = Employe('deniska',20,'manager@email.com','moscow','+845465454','manager')
# denis.set_salary()
# john.set_salary()
# print(john)
# print(denis)
# print(john.__dict__)



class Person:

    def __init__(self,name,race):
        self.name = name
        self.race = race
        self.power = 5
        self.health = 100
        self.defense = 10
        self.stamina = 10
        self.clothes = dict.fromkeys(['armor','weapon'])
        self.position = -1


    def set_armor(self,item):
        self.clothes['armor'] = item
        self.power += 3
        self.health += 10
        self.defense += 5
        self.stamina -= 4

    def set_weapon(self,item):
        self.clothes['weapon'] = item



paladin = Person('Uther','Human')
paladin.set_armor('plate')
paladin.set_weapon('sword')
print(paladin.__dict__)

person_info_dict = {'name':['john','vova','aliya', 'begimai','erbol'],
                    'race':['orc','human','human','elf','human']}

person_database = []
for index,names in enumerate(person_info_dict['name']):
    new_person = Person(name=names,race=person_info_dict['race'][index])
    person_database.append(new_person)


