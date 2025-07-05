#                 S W G
# computer =      0 1 2
# player =  S  0  D W L
#           W  1  L D W
#           G  2  W L D

from random import randint
win=0
tie=0
lose=0
print("Game will run 13 times\n")
print("USE : \n 0 for Snake \n 1 for Water \n 2 for Gun \n")
for i in range(1,13):
    comp=randint(0,2)

    user=int(input(" Enter user choice : "))
    print(f'Computer chooses {comp} and user chooses {user} \n')
    if(user == 0 and comp==1 or user ==1 and comp == 2 or user==2 and comp==0 ):
        print(" User Win ")
        win+=1
    elif(user == 0 and comp==0 or user ==1 and comp == 1 or user==2 and comp==2):
        print(" Its a Tie")
        tie+=1
    else:
        print(" User Loses")
        lose+=1
    print(f'Score is WIN = {win} , DRAW = {tie} , LOSE = {lose} \n')

if(win>lose):
    print("User Winss the game ")
else:
    print("Computer won")

