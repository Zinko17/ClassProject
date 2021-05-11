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
    'name':['cleimor', 'bastard', 'bstock', 'espadon', 'flamberg'],
    'sword_type':['rare','legendary','rare','legendary','normal'],
    'size':[random.randint(1,10) for i in range(5)],
    'weight':[random.randint(7,15) for i in range(5)],
    'power':[random.randint(50,150) for i in range(5)],
    'stamina':[random.randint(0,25) for i in range(5)],
    'health':[random.randint(0,10) for i in range(5)],
    'defense':[random.randint(0,10) for i in range(5)],
}

sword_database = []
for index,names in enumerate(sword_info_dict['name']):
    new_sword = weapon.Sword(name=names,
                             size=sword_info_dict['size'][index],
                             weight=sword_info_dict['weight'][index],
                             power=sword_info_dict['power'][index],
                             stamina=sword_info_dict['stamina'][index],
                             health=sword_info_dict['health'][index],
                             defense=sword_info_dict['defense'][index])
    new_sword.sword_type(sword_info_dict['sword_type'][index])
    sword_database.append(new_sword)



armor_info_dict = {
    'name':['leather', 'chain mall', 'metal', 'aluminium', 'steel'],
    'armor_type':['rare','legendary','rare','legendary','normal'],
    'size':[random.randint(1,10) for i in range(5)],
    'weight':[random.randint(7,15) for i in range(5)],
    'power':[random.randint(0,20) for i in range(5)],
    'stamina':[random.randint(0,50) for i in range(5)],
    'health':[random.randint(0,70) for i in range(5)],
    'defense':[random.randint(20,100) for i in range(5)],
}

armor_database = []
for index,names in enumerate(armor_info_dict['name']):
    new_armor = armor.Armor(name=names,
                             size=armor_info_dict['size'][index],
                             weight=armor_info_dict['weight'][index],
                             power=armor_info_dict['power'][index],
                             stamina=armor_info_dict['stamina'][index],
                             health=armor_info_dict['health'][index],
                             defense=armor_info_dict['defense'][index])
    new_armor.armor_type((armor_info_dict['armor_type'][index]))
    armor_database.append(new_armor)


for index,per in enumerate(person_database):
    current_armor = armor_database[index]
    current_sword = sword_database[index]
    per.set_weapon(current_sword)
    per.set_armor(current_armor)
print(sword_database)
print(armor_database)
print(person_database[0].__dict__)


for i in person_database:
    print(i.__dict__)







