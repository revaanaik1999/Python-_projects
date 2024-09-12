"""
file: card_design.py
description: designing two cards having same rank number but from different suits
language: python3
author: Revaa Naik, rn7416@rit.edu

"""
import turtle  # importing turtle

LONG_SIDE = 300  # length of the long side of card
SHORT_SIDE = 200  # length of the short side of card
TRIANGLE_SIDE = 100  # length of the side of triangle


def init():
    """
    Initialize the screen
    :pre: pos(0,0), heading east, pen down
    :post: pos(0,0), heading east, pen up
    :return: None
    """
    turtle.title("Cards")
    turtle.penup()
    turtle.setup(1000, 700)
    turtle.speed(6)
    turtle.showturtle()


def draw_border():
    """
    Drawing the border of the card
    :pre: pos(0,0), heading east, pen down
    :post: pos(0,0), heading east, pen up
    :return: None
    """
    turtle.pendown()
    turtle.forward(SHORT_SIDE)
    turtle.right(90)
    turtle.forward(LONG_SIDE)
    turtle.right(90)
    turtle.forward(SHORT_SIDE)
    turtle.right(90)
    turtle.forward(LONG_SIDE)
    turtle.right(90)
    turtle.penup()


def draw_triangle(TRIANGLE_SIDE):
    """
    Drawing the triangle with red color filled in it.
    The drawTriangle function is reused for drawing the
    diamond shape and the heart shape of the card.
    :pre: pos(0,0), heading east, pen down
    :post: pos(0,0), heading east, pen up
    :return: None
    """
    turtle.begin_fill()
    turtle.color("Red")
    turtle.forward(TRIANGLE_SIDE)
    turtle.left(120)
    turtle.forward(TRIANGLE_SIDE)
    turtle.left(120)
    turtle.forward(TRIANGLE_SIDE)
    turtle.left(120)
    turtle.end_fill()


def draw_symbol1():
    """
    Drawing the diamond symbol at the upper left corner of the card
    :pre: pos(0,0), heading east, pen down
    :post: pos(0,0), heading east, pen up
    :return: None
    """
    turtle.right(90)
    turtle.forward((LONG_SIDE // 2) // 5)
    turtle.left(90)
    turtle.forward((SHORT_SIDE // 2) // 5)
    turtle.pendown()
    draw_triangle(TRIANGLE_SIDE // 4)
    turtle.right(60)
    draw_triangle(TRIANGLE_SIDE // 4)
    turtle.left(60)
    turtle.penup()
    turtle.back((SHORT_SIDE // 2) // 5)
    turtle.left(90)
    turtle.forward((LONG_SIDE // 2) // 5)
    turtle.right(90)


def draw_symbol2():
    """
    Drawing the diamond symbol at the lower right corner of the card
    :pre: pos(0,0), heading east, pen down
    :post: pos(0,0), heading east, pen up
    :return: None
    """
    turtle.right(90)
    turtle.forward(LONG_SIDE)
    turtle.back(30)
    turtle.left(90)
    turtle.forward(SHORT_SIDE)
    turtle.back(50)
    turtle.pendown()
    draw_triangle(TRIANGLE_SIDE // 4)
    turtle.right(60)
    draw_triangle(TRIANGLE_SIDE // 4)
    turtle.left(60)
    turtle.penup()
    turtle.back((SHORT_SIDE // 2) + 50)
    turtle.right(90)
    turtle.forward(30)
    turtle.back(LONG_SIDE)
    turtle.left(90)


def draw_card1():
    """
    Drawing the card of diamonds with rank 10
    :pre: pos(0,0), heading east, pen down
    :post: pos(0,0), heading east, pen up
    :return: None
    """
    draw_symbol1()  # this function will draw the diamond symbol at the upper left corner of the card
    turtle.right(90)
    turtle.forward(60)
    turtle.left(90)
    turtle.forward(SHORT_SIDE // 2)
    turtle.write("10", align="center", font=("Arial", 30, "bold"))  # this writes the rank number 10 on the card
    turtle.back(SHORT_SIDE // 2)
    turtle.left(90)
    turtle.forward(60)
    turtle.right(90)
    turtle.right(90)
    turtle.forward(LONG_SIDE // 2)
    turtle.left(90)
    turtle.forward(SHORT_SIDE // 2)
    turtle.back(SHORT_SIDE // 4)
    turtle.pendown()
    draw_triangle(TRIANGLE_SIDE)  # this function will draw the upper triangle of the diamond
    turtle.right(60)
    draw_triangle(TRIANGLE_SIDE)  # this function will draw the lower triangle of the diamond
    turtle.left(60)
    turtle.penup()
    turtle.back(SHORT_SIDE // 4)
    turtle.left(90)
    turtle.forward(LONG_SIDE // 2)
    turtle.right(90)
    draw_symbol2()   # this function will draw the diamond symbol at the lower right side of the card



def draw_heart1():
    """
    Drawing the heart symbol at the upper left corner of the card
    :pre: pos(220,0), heading east, pen down
    :post: pos(220,0), heading east, pen up
    :return: None
    """
    turtle.right(90)
    turtle.forward((LONG_SIDE // 2) // 5)
    turtle.left(90)
    turtle.forward((SHORT_SIDE // 2) // 5)
    turtle.pendown()
    turtle.right(60)
    draw_triangle(TRIANGLE_SIDE // 4)
    turtle.left(60)
    turtle.right(90)
    turtle.color("Red")
    turtle.begin_fill()
    turtle.circle(TRIANGLE_SIDE // 16)
    turtle.left(90)
    turtle.forward(TRIANGLE_SIDE // 8)
    turtle.right(90)
    turtle.circle(TRIANGLE_SIDE // 16)
    turtle.end_fill()
    turtle.color("black")
    turtle.penup()
    turtle.right(90)
    turtle.forward(TRIANGLE_SIDE // 8)
    turtle.right(180)
    turtle.back((SHORT_SIDE // 2) // 5)
    turtle.left(90)
    turtle.forward((LONG_SIDE // 2) // 5)
    turtle.right(90)


def draw_heart2():
    """
    Drawing the heart symbol at the lower right corner of the card
    :pre: pos(220,0), heading east, pen down
    :post: pos(220,0), heading east, pen up
    :return: None
    """
    turtle.right(90)
    turtle.forward(LONG_SIDE)
    turtle.back(30)
    turtle.left(90)
    turtle.forward(SHORT_SIDE)
    turtle.back(50)
    turtle.pendown()
    turtle.right(60)
    draw_triangle(TRIANGLE_SIDE // 4)
    turtle.left(60)
    turtle.right(90)
    turtle.color("Red")
    turtle.begin_fill()
    turtle.circle(TRIANGLE_SIDE // 16)
    turtle.left(90)
    turtle.forward(TRIANGLE_SIDE // 8)
    turtle.right(90)
    turtle.circle(TRIANGLE_SIDE // 16)
    turtle.end_fill()
    turtle.color("black")
    turtle.penup()
    turtle.right(90)
    turtle.forward(TRIANGLE_SIDE // 8)
    turtle.forward((SHORT_SIDE // 2) + 50)
    turtle.right(90)
    turtle.back(30)
    turtle.forward(LONG_SIDE)
    turtle.right(90)


def draw_card2():
    """
    Drawing the card of hearts with rank 10
    :pre: pos(0,0), heading east, pen down
    :post: pos(0,0), heading east, pen up
    :return: None
    """
    turtle.forward(SHORT_SIDE + 20)
    turtle.pendown()
    turtle.color("Black")
    draw_border()    # this draws the outline for the card
    draw_heart1()        # this function draws the heart symbol at the upper left corner of the card
    turtle.right(90)
    turtle.forward(60)
    turtle.left(90)
    turtle.forward(SHORT_SIDE // 2)
    turtle.color("Red")
    turtle.write("10", align="center", font=("Arial", 30, "bold"))
    turtle.back(SHORT_SIDE // 2)
    turtle.left(90)
    turtle.forward(60)
    turtle.right(90)
    turtle.right(90)
    turtle.forward(LONG_SIDE // 2)
    turtle.left(90)
    turtle.forward(SHORT_SIDE // 2)
    turtle.back(SHORT_SIDE // 4)
    turtle.pendown()
    turtle.right(60)
    draw_triangle(TRIANGLE_SIDE)  # this function draws the lower part of the heart shape
    turtle.left(60)
    turtle.right(90)
    turtle.color("Red")
    turtle.begin_fill()
    turtle.circle(TRIANGLE_SIDE // 4)
    turtle.left(90)
    turtle.forward(TRIANGLE_SIDE // 2)
    turtle.right(90)
    turtle.circle(TRIANGLE_SIDE // 4)
    turtle.end_fill()
    turtle.color("black")
    turtle.penup()
    turtle.back(TRIANGLE_SIDE)
    turtle.back(SHORT_SIDE // 4)
    turtle.right(90)
    turtle.forward(SHORT_SIDE // 2)
    turtle.right(180)
    draw_heart2()    # this function draws the heart symbol at the lower right corner of the card
    turtle.back(SHORT_SIDE + 20)


def main():
    init()
    draw_border()
    draw_card1()
    draw_card2()
    turtle.mainloop()


if __name__ == "__main__":
    main()
