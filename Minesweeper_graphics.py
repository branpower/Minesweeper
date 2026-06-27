from graphics import *
from math import *

dgray = color_rgb(130, 130, 130)
gray = color_rgb(180, 180, 180)
navy = color_rgb(0, 0, 128)

def font_size(a):
    if a < 5:
        return 5
    elif a > 36:
        return 36
    else:
        return int(a)

def draw_empty(win, x, y, a):
    inside = Rectangle(Point(x+a/8,y+a/8), Point(x+7/8*a,y+7/8*a))
    inside.setFill(gray)
    inside.setOutline(gray)

    side1 = Polygon(Point(x,y), Point(x, y+a), Point(x+a, y+a))
    side2 = Polygon(Point(x,y), Point(x+a, y+a), Point(x+a, y))
    side1.setFill("white")
    side1.setOutline("white")
    side2.setFill(dgray)
    side2.setOutline(dgray)

    side1.draw(win)
    side2.draw(win)
    inside.draw(win)

def draw_zero(win, x, y, a):
    border = Rectangle(Point(x,y), Point(x+a,y+a))
    border.setFill(gray)
    border.setOutline(dgray)
    border.setWidth(2)

    border.draw(win)

def draw_mine(win, x, y, a):

    body = Circle(Point(x+a/2, y+a/2), a/4)
    body.setFill("black")
    horz = Line(Point(x+a/8, y+a/2), Point(x+7/8*a, y+a/2))
    horz.setWidth(a/20)
    vert = Line(Point(x+a/2, y+7/8*a), Point(x+a/2, y+a/8))
    vert.setWidth(a/20)
    diag1 = Line(Point(x+a/2-3*a/(8*sqrt(2)), y+a-(a/2-3*a/(8*sqrt(2)))), Point(x+a-(a/2-3*a/(8*sqrt(2))), y+a/2-3*a/(8*sqrt(2))))
    diag1.setWidth(a/20)
    diag2 = Line(Point(x+a/2-3*a/(8*sqrt(2)), y+a/2-3*a/(8*sqrt(2))), Point(x+a-(a/2-3*a/(8*sqrt(2))), y+a-(a/2-3*a/(8*sqrt(2)))))
    diag2.setWidth(a/20)

    body.draw(win)
    horz.draw(win)
    vert.draw(win)
    diag1.draw(win)
    diag2.draw(win)

def draw_flag(win, x, y, a):

    base = Rectangle(Point(x+a/4, y+3*a/16), Point(x+3*a/4, y+a/4))
    base.setFill("black")
    pole = Line(Point(x+a/2, y+a/4), Point(x+a/2, y+13*a/16))
    pole.setWidth(a/20)
    flag = Polygon(Point(x+a/2, y+13*a/16), Point(x+a/2, y+a/2), Point(x+3*a/4, y+21*a/32))
    flag.setFill("red")
    flag.setOutline("red")

    base.draw(win)
    pole.draw(win)
    flag.draw(win)

def draw_number(win, x, y, a, n):
    draw_zero(win, x, y, a)
    num = Text(Point(x+a/2, y+a/2), str(n))

    num.setSize(font_size(2*a/3))
    
    num.setStyle("bold")
    if n == 1:
        num.setFill("blue")
    elif n == 2:
        num.setFill("green")
    elif n == 3:
        num.setFill("red")
    elif n == 4:
        num.setFill(navy)
    elif n == 5:
        num.setFill("brown")
    elif n == 6:
        num.setFill("aquamarine4")
    elif n == 7:
        num.setFill("black")
    elif n ==8:
        num.setFill(dgray)
    
    num.draw(win)

def draw_smiley(win, x, y, a):
    draw_empty(win, x, y, a)

    head = Circle(Point(x+a/2, y+a/2), 9*a/28)
    head.setFill("yellow")

    eyes = []
    for i in [-1, 1]:
        eyes.append(Circle(Point(x+a/2+i*a/8, y+a*3/5), a/25))
    
    
    
    smile = Oval(Point(x+5*a/14, y+a*(1/8+1/5)), Point(x+9*a/14, y+3/5*a))
    smile.setWidth(2)

    block = Rectangle(Point(x+5*a/14, y+a*(1/8+1/3)), Point(x+9*a/14, y+3/5*a))
    block.setFill("yellow")
    block.setOutline("yellow")

    head.draw(win)
    smile.draw(win)
    block.draw(win)
    for i in eyes:
        i.setFill("black")
        i.draw(win)

def draw_border(win, x1, y1, x2, y2, x3, normal):

    y3 = y2 - 80

    darkEdge1 = Polygon(Point(x1, y1), Point(x1+3, y1+3), Point(x2-3, y1+3), Point(x2-3, y2-3), Point(x2, y2), Point(x2, y1))
    darkEdge1.setOutline(dgray)
    darkEdge1.setFill(dgray)
    lightEdge1 = Polygon(Point(x1, y1), Point(x1+3, y1+3), Point(x1+3, y2-3), Point(x2-3, y2-3), Point(x2, y2), Point(x1, y2))
    lightEdge1.setOutline("white")
    lightEdge1.setFill("white")

    if not normal:
        darkEdge2 = Polygon(Point(-3, y1+7), Point(0, y1+10), Point(0, y3), Point(x3, y3), Point(x3+3, y3+3), Point(-3, y3+3))
    else:
        darkEdge2 = Polygon(Point(x1+7, y1+7), Point(x1+10, y1+10), Point(x1+10, y3), Point(x2-10, y3), Point(x2-7, y3+3), Point(x1+7, y3+3))
    darkEdge2.setOutline(dgray)
    darkEdge2.setFill(dgray)
    if not normal:
        lightEdge2 = Polygon(Point(-3, y1+7), Point(0, y1+10), Point(x3, y1+10), Point(x3, y3), Point(x3+3, y3+3), Point(x3+3, y1+7))
    else:
        lightEdge2 = Polygon(Point(x1+7, y1+7), Point(x1+10, y1+10), Point(x2-10, y1+10), Point(x2-10, y3), Point(x2-7, y3+3), Point(x2-7, y1+7))
    lightEdge2.setOutline("white")
    lightEdge2.setFill("white")

    darkEdge3 = Polygon(Point(x1+7, y3+7), Point(x1+10, y3+10), Point(x1+10, y2-10), Point(x2-10, y2-10), Point(x2-7, y2-7), Point(x1+7, y2-7))
    darkEdge3.setOutline(dgray)
    darkEdge3.setFill(dgray)
    lightEdge3 = Polygon(Point(x1+7, y3+7), Point(x1+10, y3+10), Point(x2-10, y3+10), Point(x2-10, y2-10), Point(x2-7, y2-7), Point(x2-7, y3+7))
    lightEdge3.setOutline("white")
    lightEdge3.setFill("white")

    win.setBackground(gray)
    darkEdge1.draw(win)
    lightEdge1.draw(win)
    darkEdge2.draw(win)
    lightEdge2.draw(win)
    darkEdge3.draw(win)
    lightEdge3.draw(win)

def draw_red_mine(win, x, y, a):
    background = Rectangle(Point(x, y), Point(x+a, y+a))
    background.setFill("red")

    background.draw(win)
    draw_mine(win, x, y, a)

def draw_red_flag(win, x, y, a):
    background = Rectangle(Point(x, y), Point(x+a, y+a))
    background.setFill("dark salmon")

    background.draw(win)
    draw_flag(win, x, y, a)

def main():
    a = 40
    
    win = GraphWin("Test", 4*a, 4*a)

    draw_empty(win, 0, 0, a)
    draw_empty(win, a, 0, a)
    draw_flag(win, a, 0, a)
    draw_zero(win, 2*a, 0, a)
    draw_mine(win, 2*a, 0, a)
    draw_zero(win, 3*a, 0, a)
    for i in range(1, 9):
        draw_number(win, (i-1)*a%(4*a), a*(ceil(i/4)), a, i)
    draw_smiley(win, 0, 3*a, a)
    draw_smiley(win, a, 3*a, a)

    win.getMouse()

if __name__ == "__main__": main()