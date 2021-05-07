import random

import person
import weapon
import armor


"""
Создать класс Armor со всеми характеристиками персонажа для брони: health,power,defense,stamina
1. Создать метод armor_type по примеру в Sword
2. Сгенерировать обьекты мечей и брони
"""

person_info_dict = {
    'name':['john','vova','aliya','begimai','erbol'],
    'race':['orc','human','human','elf','human']
}

person_database = []
for index,names in enumerate(person_info_dict['name']):
    new_person = person.Person(name=names, race=person_info_dict['race'][index])
    person_database.append(new_person)





sword_info_dict = {
    'name':['kleimor', 'bastard', 'bstock', 'espadon', 'flamberg'],
    'sword_type':['rare','legendary','rare','legendary','normal'],
    'desc':['wfl,Меч дракона','okfoskfor','Меч крутой короче','fksdok'],
    'size':[random.randint(1,10) for i in range(5)],
    'weight':[random.randint(7,15) for i in range(5)],
    'power':[33,64,32,70,17],
    'stamina':[random.randint(0,25) for i in range(5)],
    'health':[random.randint(0,10) for i in range(5)],
    'defense':[random.randint(0,10) for i in range(5)],
}

sword_database = []
for index,names in enumerate(person_info_dict['name']):



