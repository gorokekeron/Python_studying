# Ghost Game
from random import randint
print ('유령게임')
feeling_brave =  True
score = 0
while feeling_brave :
    ghost_door =randint(1,3)
    print('there are three doors')
    print('there is a ghost in once door')
    print('choose the number')
    door = input('1, 2 or 3?')
    door_num=int(door)
    if door_num == ghost_door :
        print('ghost!')
        feeling_brave = False
    else :
            print('no ghost!')
            print('  go to the next door')
            score=score+1
    print('run!')
    print('game over. your score is ',score)
