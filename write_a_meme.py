"""
file: wite_a_meme.py
description: displaying the message HELLO TOM
language: python3
author: Revaa Naik, rn7416@rit.edu

"""

import turtle

def init():
    """
    Initialize the screen
    :pre: pos(0,0), heading east, pen down
    :post: pos(0,0), heading east, pen up
    :return: None
    """

    turtle.title('Write_a_Meme')
    turtle.penup()
    
    turtle.speed(6)
    turtle.showturtle()

def draw_H():
    """
    Draw letter H
    :pre: pos(-300,120), heading east, pen up
    :post: pos(-190,120), heading east, pen up
    :return: None
    """

    turtle.penup()
    turtle.back(500)
    turtle.pendown()
    turtle.right(90)
    turtle.forward(120)
    turtle.penup()
    turtle.right(180)
    turtle.pendown()
    turtle.forward(60)
    turtle.right(90)
    turtle.forward(60)
    turtle.left(90)
    turtle.forward(60)
    turtle.right(180)
    turtle.forward(120)
    turtle.penup()
    turtle.left(180)
    turtle.forward(120)
    turtle.penup()
    turtle.right(90)
    turtle.forward(50)


def draw_E():
    """
    Draw letter E
    :pre: pos(-190,120), heading east, pen up
    :post: pos(-80,120), heading east, pen up
    :return: None
    """

    turtle.pendown()
    turtle.forward(60)
    turtle.penup()
    turtle.right(180)
    turtle.forward(60)
    turtle.left(90)
    turtle.pendown()
    turtle.forward(120)
    turtle.penup()
    turtle.left(180)
    turtle.forward(60)
    turtle.right(90)
    turtle.pendown()
    turtle.forward(60)
    turtle.right(180)
    turtle.forward(60)
    turtle.left(90)
    turtle.forward(60)
    turtle.left(90)
    turtle.forward(60)
    turtle.penup()
    turtle.left(90)
    turtle.forward(120)
    turtle.right(90)
    turtle.forward(50)

def draw_L():
    """
    Draw letter L
    :pre: pos(-80,120), heading east, pen up
    :post: pos(30,120), heading east, pen up
    :return: None
    """
    turtle.pendown()
    turtle.right(90)
    turtle.forward(120)
    turtle.left(90)
    turtle.forward(60)
    turtle.penup()
    turtle.left(90)
    turtle.forward(120)
    turtle.right(90)
    turtle.forward(50)
    turtle.pendown()

def draw_O():
    """
    Draw letter O
    :pre: pos(140,120), heading east, pen up
    :post: pos(250,120), heading east, pen up
    :return: None
    """

    turtle.pendown()
    turtle.forward(60)
    turtle.right(90)
    turtle.forward(120)
    turtle.right(90)
    turtle.forward(60)
    turtle.right(90)
    turtle.forward(120)
    turtle.right(90)
    turtle.penup()
    turtle.forward(60)
    turtle.forward(50)

def draw_T():
    """
    Draw letter T
    :pre: pos(250,120), heading east, pen up
    :post: pos(360,120), heading east, pen up
    :return: None
    """
    turtle.pendown()
    turtle.forward(60)
    turtle.right(180)
    turtle.forward(30)
    turtle.left(90)
    turtle.forward(120)
    turtle.penup()
    turtle.left(180)
    turtle.forward(120)
    turtle.right(90)
    turtle.forward(30)
    turtle.forward(50)

def draw_M():
    """
    Draw letter M
    :pre: pos(360,120), heading east, pen up
    :post: pos(470,120), heading east, pen up
    :return: None
    """
    turtle.pendown()
    turtle.right(90)
    turtle.forward(120)
    turtle.backward(120)
    turtle.left(90)
    turtle.right(60)
    turtle.forward(90)
    turtle.left(120)
    turtle.forward(90)
    turtle.right(150)
    turtle.forward(120)
    turtle.penup()
    turtle.left(180)
    turtle.forward(120)
    turtle.right(90)
    turtle.forward(50)

def draw_meme():
    draw_H()
    draw_E()
    draw_L()
    draw_L()
    draw_O()
    turtle.forward(100)
    draw_T()
    draw_O()
    draw_M()


def main():
    init()
    draw_meme()
    turtle.mainloop()
if __name__=='__main__':
    main()
