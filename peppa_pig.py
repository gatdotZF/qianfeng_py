#! /usr/bin/env python
#coding=utf-8

from turtle import *


def nose(x,y):
    """鐢婚蓟�1�7��"""
    penup()
    # 灏嗘捣榫熺Щ鍔ㄥ埌鎸囧畾鐨勫潗鏍�
    goto(x,y)
    pendown()
    # 璁剧疆娴烽緹鐨勬柟鍚戯紙0-涓溿��90-鍖椼��180-瑗裤��270-鍗楋約1�7
    setheading(-30)
    begin_fill()
    a = 0.4
    for i in range(120):
        if 0 <= i < 30 or 60 <= i <90:
            a = a + 0.08
            # 鍚戝乏杞ￄ1�7��
            left(3)
            # 鍚戝墠璧ￄ1�7
            forward(a)
        else:
            a = a - 0.08
            left(3)
            forward(a)
    end_fill()
    penup()
    setheading(90)
    forward(25)
    setheading(0)
    forward(10)
    pendown()
    # 璁剧疆鐢荤瑪鐨勯鑹ￄ1�7(绾�, 缁�, 钃�)
    pencolor(255, 155, 192)
    setheading(10)
    begin_fill()
    circle(5)
    color(160, 82, 45)
    end_fill()
    penup()
    setheading(0)
    forward(20)
    pendown()
    pencolor(255, 155, 192)
    setheading(10)
    begin_fill()
    circle(5)
    color(160, 82, 45)
    end_fill()


def head(x, y):
    """鐢诲い1�7"""
    color((255, 155, 192), "pink")
    penup()
    goto(x,y)
    setheading(0)
    pendown()
    begin_fill()
    setheading(180)
    circle(300, -30)
    circle(100, -60)
    circle(80, -100)
    circle(150, -20)
    circle(60, -95)
    setheading(161)
    circle(-300, 15)
    penup()
    goto(-100, 100)
    pendown()
    setheading(-30)
    a = 0.4
    for i in range(60):
        if 0<= i < 30 or 60 <= i < 90:
            a = a + 0.08
            lt(3) #鍚戝乏杞ￄ1�7��
            fd(a) #鍚戝墠璧癮鐨勬闄1�7ￄ1�7
        else:
            a = a - 0.08
            lt(3)
            fd(a)
    end_fill()


def ears(x,y):
    """鐢昏�虫湄1�7"""
    color((255, 155, 192), "pink")
    penup()
    goto(x, y)
    pendown()
    begin_fill()
    setheading(100)
    circle(-50, 50)
    circle(-10, 120)
    circle(-50, 54)
    end_fill()
    penup()
    setheading(90)
    forward(-12)
    setheading(0)
    forward(30)
    pendown()
    begin_fill()
    setheading(100)
    circle(-50, 50)
    circle(-10, 120)
    circle(-50, 56)
    end_fill()


def eyes(x,y):
    """鐢荤溂鐫ￄ1�7"""
    color((255, 155, 192), "white")
    penup()
    setheading(90)
    forward(-20)
    setheading(0)
    forward(-95)
    pendown()
    begin_fill()
    circle(15)
    end_fill()
    color("black")
    penup()
    setheading(90)
    forward(12)
    setheading(0)
    forward(-3)
    pendown()
    begin_fill()
    circle(3)
    end_fill()
    color((255, 155, 192), "white")
    penup()
    seth(90)
    forward(-25)
    seth(0)
    forward(40)
    pendown()
    begin_fill()
    circle(15)
    end_fill()
    color("black")
    penup()
    setheading(90)
    forward(12)
    setheading(0)
    forward(-3)
    pendown()
    begin_fill()
    circle(3)
    end_fill()


def cheek(x,y):
    """鐢昏劯棰ￄ1�7"""
    color((255, 155, 192))
    penup()
    goto(x,y)
    pendown()
    setheading(0)
    begin_fill()
    circle(30)
    end_fill()


def mouth(x,y):
    """鐢诲槾宸ￄ1�7"""
    color(239, 69, 19)
    penup()
    goto(x, y)
    pendown()
    setheading(-80)
    circle(30, 40)
    circle(40, 80)


def setting():
    """璁剧疆鍙傛暟"""
    pensize(4)
    # 闅愯棌娴烽緹
    hideturtle()
    colormode(255)
    color((255, 155, 192), "pink")
    setup(840, 500)
    speed(10)


def main():
    """涓诲嚱鏁ￄ1�7"""
    setting() 
    nose(-100, 100)
    head(-69, 167)
    ears(0, 160)
    eyes(0, 140)
    cheek(80, 10)
    mouth(-20, 30)
    done()


if __name__ == '__main__':
    main()
