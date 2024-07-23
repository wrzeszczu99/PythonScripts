import turtle
import time
import random

WIDTH, HEIGHT  = 1080, 720
COLOURS = ['red', 'green', 'blue', 'orange', 'yellow', 'black', 'purple', 'pink', 'brown', 'cyan']


def get_game_settings():
    while True:
        number_of_turtles = input("How many turtles do you want to race? (2-10): ")
        if(number_of_turtles.isdigit()):
            number_of_turtles = int(number_of_turtles)
            if 2<= number_of_turtles <=10:
                break
            else:
                print("Must be between 2 and 10(inclusive)")
        else:
            print("Must be a number")

    return number_of_turtles


def init_turtle_screen():
    screen = turtle.Screen()
    screen.setup(WIDTH, HEIGHT)
    screen.title("TURTLE RACING !!!")


def create_racers(number_of_racers):
    random.shuffle(COLOURS)
    colours = COLOURS[:number_of_racers]
    turtles =[]
    for i in range(number_of_racers):
        racer = turtle.Turtle()
        racer.color(colours[i])
        racer.shape('turtle')
        racer.penup()
        racer.left(90)
        racer.setpos([-WIDTH//2 + ((WIDTH//(number_of_racers+1)) * (i +1)) , -HEIGHT/2 + 20])
        racer.pendown()
        turtles.append(racer)
    return turtles;

def WinnerSequence(winner):
    turtle.color(COLOURS[winner])
    turtle.hideturtle()
    turtle.write("The winner is the turtle with color: " + COLOURS[winner], False, align = 'center', font= ("Arial", 20, "normal"))
    print("The winner is the turtle with color:", COLOURS[winner])
    time.sleep(5)

def race(turtles):
    while True:
        for racer in turtles:
            distance = random.randrange(1, 20)
            racer.forward(distance)
            
            x, y = racer.pos()
            if y >= HEIGHT//2 -20:
                racer.setpos(x, HEIGHT//2-20)
                return turtles.index(racer)

racers = get_game_settings()
init_turtle_screen()
winner = race(create_racers(racers))
WinnerSequence(winner)