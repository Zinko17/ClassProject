import random


list1 = random.sample([0,1,2,3,4,5,6,7,8,9],4)
print(list1)
for i in range(5):
    list_input = list(input())

    for index,number in enumerate(list_input):
        list_input[index] = int(number)
    bulls_list = []
    bulls = 0
    cows = 0
    for index,value in enumerate(list1):
        for index1,num in enumerate(list_input):
            if index == index1 and value == num:
                bulls += 1
                bulls_list.append(num)
            if index != index1 and value ==num and num not in bulls_list:
                cows += 1
    if bulls == 4:
        print('WIN')

    print(f'Bulls: {bulls},Cows: {cows}')
print(list1)
