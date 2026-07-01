from graphics import *
from Minesweeper_graphics import *

class Button:
    def __init__(self, rect, label):
        self.x1, self.y1 = rect.getP1().getX(), rect.getP1().getY()
        self.x2, self.y2 = rect.getP2().getX(), rect.getP2().getY()

        self.rect = rect
        self.label = Text(rect.getCenter(), label)

        self.deactivate()
    
    def clicked(self, p):
        return (self.active and self.x1 <= p.getX() <= self.x2 and self.y1 <= p.getY() <= self.y2)
    
    def draw_button(self, win):
        self.rect.draw(win)
        self.label.draw(win)
    
    def activate(self):
        self.rect.setFill("gray89")
        self.label.setFill("gray39")
        self.rect.setWidth(2)
        self.active = True
    
    def deactivate(self):
        self.rect.setFill("gray39")
        self.label.setFill("gray50")
        self.rect.setWidth(1)
        self.active = False
    
    def isActive(self):
        return self.active
    
    def getRekt(self):
        return self.rect

class Cell:
    def __init__(self, win, x, y, a):
        self.x = x
        self.y = y
        self.a = a
        self.win = win

        self.status = 0
        self.revealed = False
        self.flagged = False

        draw_empty(win, x, y, a)
    
    def getX(self):
        return self.x
    
    def getY(self):
        return self.y
    
    def getSize(self):
        return self.a
    
    def getStatus(self):
        return self.status
    
    def isRevealed(self):
        return self.revealed

    def getFlaggedStatus(self):
        return self.flagged
    
    def reveal(self):
        if not self.revealed:
            if self.status == -3:
                draw_red_flag(self.win, self.x, self.y, self.a)
            elif self.status == -2:
                draw_red_mine(self.win, self.x, self.y, self.a)
            elif self.status == -1:
                draw_zero(self.win, self.x, self.y, self.a)
                draw_mine(self.win, self.x, self.y, self.a)
            elif self.status == 0:
                draw_zero(self.win, self.x, self.y, self.a)
            else:
                draw_number(self.win, self.x, self.y, self.a, self.status)
        
        self.revealed = True
    
    def reset(self):
        self.flagged = False
        self.status = 0
        self.revealed = False
        draw_empty(self.win, self.x, self.y, self.a)
    
    def flag(self):
        if not self.revealed:
            if not self.flagged:
                draw_flag(self.win, self.x, self.y, self.a)
            else:
                draw_empty(self.win, self.x, self.y, self.a)
        
            self.flagged = not self.flagged
    
    def incrementStatus(self):
        self.status += 1
    
    def plantMine(self):
        self.status = -1
    
    def redMine(self):
        self.status = -2
    
    def redFlag(self):
        self.status = -3

class NumBox:
    def __init__(self, win, rect, start):
        self.val = start
        self.win = win
        rect.setFill("black")
        self.rect = rect
        self.label = Text(rect.getCenter(), start)
        self.label.setTextColor("red")
        self.draw()
    
    def draw(self):
        self.rect.draw(self.win)
        self.label.draw(self.win)
    
    def changeVal(self, val):
        self.val = str(int(self.val)+val)
        self.label.setText(self.val)
    
    def getVal(self):
        return self.val

class Select:
    def __init__(self, win, rect):
        self.box1 = Rectangle(rect.getP1(), Point(rect.getCenter().getX(), rect.getP2().getY()))
        self.box2 = Rectangle(Point(rect.getCenter().getX(), rect.getP1().getY()), rect.getP2())
        self.win = win

        self.mode = "mine"
        self.draw_flagBox()
        self.draw_mineBox()
        self.mineMode()
    
    def draw_flagBox(self):
        self.box1.draw(self.win)
        draw_flag(self.win, self.box1.getP1().getX(), self.box1.getP1().getY(), self.box1.getP2().getX() - self.box1.getP1().getX())
    
    def draw_mineBox(self):
        self.box2.draw(self.win)
        draw_mine(self.win, self.box2.getP1().getX(), self.box2.getP1().getY(), self.box2.getP2().getX() - self.box2.getP1().getX())
    
    def flagMode(self):
        self.box1.setFill("blue")
        self.box1.setOutline("blue")
        self.box2.setFill("gray40")
        self.box2.setOutline("gray40")

        self.mode = "flag"

    def mineMode(self):
        self.box2.setFill("blue")
        self.box2.setOutline("blue")
        self.box1.setFill("gray40")
        self.box1.setOutline("gray40")

        self.mode = "mine"
    
    def swap(self):
        if self.mode == "mine":
            self.flagMode()
        elif self.mode == "flag":
            self.mineMode()
    
    def getMode(self):
        return self.mode