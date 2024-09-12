import turtle
import random


def init():
    """
    Initialize the screen
    :pre: pos(0,0), heading east, pen down
    :post: pos(0,0), heading east, pen up
    :return: None
    """
    turtle.penup()
    turtle.speed(3)
    turtle.title("Snake")


BOUNDING_BOX = 200
MIN_SEGMENTS = 0
MAX_SEGMENTS = 500
MIN_LENGTH = 1
MAX_LENGTH = 20
MIN_THICKNESS = 1
MAX_THICKNESS = 10
MIN_ANGLE = -30
MAX_ANGLE = 30


def draw_border():
    turtle.left(180)
    turtle.forward(BOUNDING_BOX)
    turtle.right(90)
    turtle.forward(BOUNDING_BOX)
    turtle.right(90)
    turtle.pendown()
    for i in range(4):
        turtle.forward(BOUNDING_BOX * 2)
        turtle.right(90)
    turtle.penup()
    turtle.goto(0, 0)


while(True):
    segment_no = int(input("Please enter the number of segments"))
    if segment_no not in range(0,500):
        print("Enter valid input")
        continue
    else:
        break

def drawSnake():
    length = random.randint(MIN_LENGTH, MAX_LENGTH)
    thickness = random.randint(MIN_THICKNESS, MAX_THICKNESS)
    angle = random.randint(MIN_ANGLE, MAX_ANGLE)
    color = ["red","blue","green"]
    leng = 0
    turtle.pendown()
    turtle.pencolor(random.choice(color))
    turtle.forward(length)
    leng= leng+length
    turtle.pensize(thickness)
    turtle.right(angle)

    return leng


def drawSnakeIter(segment_no):
    for i in range(segment_no):
        drawSnake()

def drawSnakeRec(segment_no):
    if segment_no == 0:
        pass
    else:
        drawSnake()
        drawSnakeRec(segment_no-1)



def main():
    init()
    draw_border()
    drawSnakeIter(segment_no)
    x=drawSnake()
    print("The length is:"+" " +str(x))
    input("Press enter for next drawing")
    turtle.reset()
    init()
    draw_border()
    drawSnakeRec(segment_no)

    input("press enter to quit")
    exit()

    turtle.mainloop()


if __name__ == "__main__":
    main()
