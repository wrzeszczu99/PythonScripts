import random

class player:
    points = 0
    name = ""

def roll_dice():
    roll = random.randint(1, 6) 
    if(roll == 1):
        return 0
    else:
        return roll
    
def win(player):
    print("Player: " +player.name+" won!")
    quit()

def play(player):
    while True:
        decision = input(player.name + "! Do you want to roll(y/n)? ").lower()
        if(decision == 'y'):
            roll = roll_dice()
            if roll == 0:
                print("You rolled a 1! your points goes to 0!")
                player.points = 0
                return
            else:
                player.points += roll
                print("You rolled a " +str(roll)+"! Your points goes to " +str(player.points))
                if player.points >= max_points:
                    win(player)
        if(decision == 'n'):
            return

while True:
    number_of_players = input("How many players are there(2-4)? ")
    if(number_of_players.isdigit()):
        number_of_players = int(number_of_players)
        if 2<= number_of_players <=4:
            break
        else:
            print("Must be between 2 and 4(inclusive)")
    else:
        print("Must be a number")

players = [player() for _ in range(number_of_players)]
for i, pl in enumerate(players):
    pl.name = input("Player"+str(i)+ " name: ")

max_points = 0
while True:
    max_points = input("Max points? ")
    if(max_points.isdigit()):
        max_points = int(max_points)
        break
    else:
        print("Must be a number")

while True:
    for pl in players:
        play(pl)