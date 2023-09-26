import random
from turtle import Screen, Turtle

screen = Screen()
screen.setup(width=600, height=600, startx=0, starty=0)

turtle_list = []

for _ in range(6):
    t = Turtle()
    t.shape("turtle")
    t.pu()
    turtle_list.append(t)

turtle_list[0].color("red")
turtle_list[1].color("blue")
turtle_list[2].color("green")
turtle_list[3].color("yellow")
turtle_list[4].color("orange")
turtle_list[5].color("purple")

y = 100
for _ in range(6):
    turtle_list[_].setx(-(screen.window_width() / 2) + 10)
    turtle_list[_].sety(y)
    y -= 50

user_bet = screen.textinput("Place Your Bet", "Who will win (red, blue, green, yellow, orange, purple) ?")

max_pos = 0
winner = ""
while max_pos <= (screen.window_width()/2 - 30):
    for _ in range(6):
        turtle_list[_].forward(random.randint(0, 11))

    for i in range(6):
        if max_pos < turtle_list[i].xcor():
            max_pos = turtle_list[i].xcor()
            winner = turtle_list[i].color()

if winner == user_bet:
    print(f"You Win! Winner is {winner[0]} turtle.")
else:
    print(f"You Lose! Winner is {winner[0]} turtle.")

screen.exitonclick()
