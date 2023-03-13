import turtle
import random
import time
import sys

sys.setrecursionlimit(50000)

try:
    i = int(input("Type the total amount of dots: "))
    x = int(input("Type the diameter for each dot: "))

    st = time.time()
    t = turtle.Turtle()
    t.hideturtle()
    t.width(5)
    t.penup()
    t.setposition(0, -100)
    t.pendown()


    def pointer(rand, i, x):
        if i > 0:
            corner = random.choice([[200, -100], [0, 200*(3**(1/2))-100], [-200, -100]])
            t.penup()
            t.setposition(rand)
            t.pendown()
            t.dot(x, "red")
            new = [(corner[0] + rand[0])/2, (corner[1] + rand[1])/2]
            pointer(new, i-1, x)


    t.forward(200)

    for j in range(2):
        t.left(120)
        t.forward(400)
    t.left(120)
    t.forward(200)

    rnd_x = random.randint(-200, 200)

    if rnd_x < 0:
        rnd_y = random.choice([i-100 and i*(3**(1/2))-100 for i in range(200 + rnd_x + 1)])
        
    if rnd_x >= 0:
        rnd_y = random.choice([i-100 and i*(3**(1/2))-100 for i in range(200 - rnd_x + 1)])

    rnd_point = [rnd_x, rnd_y]

    pointer(rnd_point, i, x)

    et = time.time()
    print(f"Whole thing takes {et - st} seconds.")

    turtle.mainloop()

except ValueError:
    print("ValueError: How hard could it be to type an integer?")

except RecursionError:
    print("RecursionError: Recursion limit was set to 50000 initially. What made you think that was not enough?")
