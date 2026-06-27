from random import *
from graphics import *
from Minesweeper_graphics import *
from Minesweeper_Objects import *
import time
import sys

def menu(win):
    win.setBackground("gray")

    title = Text(Point(50, 80), "MINESWEEPER")
    title.setSize(36)
    title.draw(win)

    Text(Point(20, 60), "Length:").draw(win)
    Text(Point(45, 60), "Height:").draw(win)
    Text(Point(70, 60), "Mines:").draw(win)

    help1 = Text(Point(50, 53), "Length and Height must be between 1 and 50.")
    help1.setSize(10)
    help1.draw(win)

    help2 = Text(Point(50, 49), "Mines must be such that there is at least 1 free space.")
    help2.setSize(10)
    help2.draw(win)

    length = Entry(Point(32.5, 60), 4)
    height = Entry(Point(57.5, 60), 4)
    mines = Entry(Point(82.5, 60), 4)

    length.draw(win)
    height.draw(win)
    mines.draw(win)

    start_button = Button(Rectangle(Point(40, 35), Point(60, 45)), "Start")
    start_button.draw_button(win)

    help3 = Text(Point(50, 27.5), "Press Return to return to this menu once in the game.\nPress s to toggle between placing flags and clicking cells.")
    help3.setSize(10)
    help3.draw(win)

    p = Point(0,0)

    done = False

    while not done:
        try:
            if int(length.getText()) in range(1, 51) and int(height.getText()) in range(1, 51) and int(mines.getText()) in range(int(length.getText())*int(height.getText())):
                start_button.activate()
            else:
                start_button.deactivate()
        except:
            start_button.deactivate()
        
        done = start_button.clicked(p)
        
        click = win.checkMouse()
        
        if click != None and start_button.isActive():
            p = click

    win.close()
    return int(length.getText()), int(height.getText()), int(mines.getText())

def mineSize(l, h):
    if l <= 25:
        mineSize1 = 40
    else:
        mineSize1 = 930/l

    if h <= 25:
        mineSize2 = 40
    else:
        mineSize2 = 930/h
    
    return min(mineSize1, mineSize2)
    
def findCellAddress(point, length, height, a):
    if point.getX() != length*a and point.getY() != height*a:
        return floor(point.getY()/a), floor(point.getX()/a)
    elif point.getX() == length*a and point.getY() != height*a:
        return floor(point.getX()/a), length-1
    elif point.getX() != length*a and point.getY() == height*a:
        return height-1, floor(point.getX()/a)
    elif point.getX() == length*a and point.getY() == height*a:
        return height-1, length-1

def near(cell_matrix, i, j, testCell):
    xstart, ystart = -1, -1
    xend, yend = 2, 2
    if not i:
        ystart = 0
    if not j:
        xstart = 0
    if i == len(cell_matrix) - 1:
        yend = 1
    if j == len(cell_matrix[0]) - 1:
        xend = 1
                
    for k in range(ystart, yend):
        for l in range(xstart, xend):
            if cell_matrix[i+k][j+l] is testCell:
                return True
    
    return False

def cellsRevealed(cell_matrix, i, j):
    xstart, ystart = -1, -1
    xend, yend = 2, 2
    if not i:
        ystart = 0
    if not j:
        xstart = 0
    if i == len(cell_matrix) - 1:
        yend = 1
    if j == len(cell_matrix[0]) - 1:
        xend = 1
                
    revealed = (yend-ystart)*(xend-xstart)
    
    return revealed

def mineSpreading(cell_matrix, length, height, a, mines, clickedCell_row, clickedCell_column):
    remaining = mines

    if mines < length*height/3 and not cellsRevealed(cell_matrix, clickedCell_row, clickedCell_column) >= length*height*2/3+1:
        while remaining != 0:
            i, j = findCellAddress(Point(length*a*random(), height*a*random()), length, height, a)
            chosenCell = cell_matrix[i][j]
            if chosenCell.getStatus() >= 0 and not near(cell_matrix, clickedCell_row, clickedCell_column, chosenCell):
                chosenCell.plantMine()
                remaining -= 1
    else:
        while remaining != 0:
            i, j = findCellAddress(Point(length*a*random(), height*a*random()), length, height, a)
            chosenCell = cell_matrix[i][j]
            if chosenCell.getStatus() >= 0 and chosenCell != cell_matrix[clickedCell_row][clickedCell_column]:
                chosenCell.plantMine()
                remaining -= 1

def setupValues(cell_matrix):
    for i in range(len(cell_matrix)):
        for j in range(len(cell_matrix[0])):
            if cell_matrix[i][j].getStatus() == -1:
                xstart, ystart = -1, -1
                xend, yend = 2, 2
                if not i:
                    ystart = 0
                if not j:
                    xstart = 0
                if i == len(cell_matrix) - 1:
                    yend = 1
                if j == len(cell_matrix[0]) - 1:
                    xend = 1
                
                for k in range(ystart, yend):
                    for l in range(xstart, xend):
                        if cell_matrix[i+k][j+l].getStatus() != -1:
                            cell_matrix[i+k][j+l].incrementStatus()

def reveal_mines(cell_matrix):
    for i in cell_matrix:
        for j in i:
            if j.getStatus() <= -1 and not j.getFlaggedStatus():
                j.reveal()
            elif j.getFlaggedStatus() and j.getStatus() != -1:
                j.redFlag()
                j.reveal()

def zeroSpread(clickedCell_row, clickedCell_column, cell_matrix):
    total_cells_revealed = 0
    
    xstart, ystart = -1, -1
    xend, yend = 2, 2
    if not clickedCell_row:
        ystart = 0
    if not clickedCell_column:
        xstart = 0
    if clickedCell_row == len(cell_matrix) - 1:
        yend = 1
    if clickedCell_column == len(cell_matrix[0]) - 1:
        xend = 1
    
    for k in range(ystart, yend):
        for l in range(xstart, xend):
            if not (k == 0 and l == 0) and not cell_matrix[clickedCell_row+k][clickedCell_column+l].isRevealed():
                cell_matrix[clickedCell_row+k][clickedCell_column+l].reveal()
                total_cells_revealed += 1
                if cell_matrix[clickedCell_row+k][clickedCell_column+l].getStatus() == 0:
                    total_cells_revealed += zeroSpread(clickedCell_row+k, clickedCell_column+l, cell_matrix)
    
    return total_cells_revealed

def chord(cell_matrix, clickedCell_row, clickedCell_column):
    flags = 0
    revealed = 0
    bad = False
    
    xstart, ystart = -1, -1
    xend, yend = 2, 2
    if not clickedCell_row:
        ystart = 0
    if not clickedCell_column:
        xstart = 0
    if clickedCell_row == len(cell_matrix) - 1:
        yend = 1
    if clickedCell_column == len(cell_matrix[0]) - 1:
        xend = 1
    
    for k in range(ystart, yend):
        for l in range(xstart, xend):
            if cell_matrix[clickedCell_row+k][clickedCell_column+l].getFlaggedStatus():
                flags += 1
    
    if flags == cell_matrix[clickedCell_row][clickedCell_column].getStatus():
        for k in range(ystart, yend):
            for l in range(xstart, xend):
                if not cell_matrix[clickedCell_row+k][clickedCell_column+l].isRevealed() and not cell_matrix[clickedCell_row+k][clickedCell_column+l].getFlaggedStatus() and cell_matrix[clickedCell_row+k][clickedCell_column+l].getStatus() != -1:
                    cell_matrix[clickedCell_row+k][clickedCell_column+l].reveal()
                    revealed += 1
                    if cell_matrix[clickedCell_row+k][clickedCell_column+l].getStatus() == 0:
                        revealed += zeroSpread(clickedCell_row+k, clickedCell_column+l, cell_matrix)
                elif cell_matrix[clickedCell_row+k][clickedCell_column+l].getStatus() == -1 and not cell_matrix[clickedCell_row+k][clickedCell_column+l].getFlaggedStatus():
                    reveal_mines(cell_matrix)
                    bad = True
                    break
            
            if bad:
                break
    
    return bad, revealed

def playMinesweeper(length, height, mines):
    a = mineSize(length, height)

    win = GraphWin("Minesweeper", max(200,a*length+20), a*height+90)

    if a*length+20 >= 200:
        win.setCoords(-10, -10, length*a+10, height*a+80)
        draw_border(win, -10, -10, length*a+10, height*a+80, length*a, True)
        timer = NumBox(win, Rectangle(Point(15, a*height+17.5), Point(a*length/3, a*height+37.5)), "0")
        mine_counter = NumBox(win, Rectangle(Point(15, a*height+42.5), Point(a*length/3, a*height+62.5)), str(mines))
        mode_select = Select(win, Rectangle(Point(length*a-70, height*a+25), Point(length*a-10, height*a+55)))
    else:
        win.setCoords(-(200-a*length)/2, -10, length*a+(200-a*length)/2, height*a+80)
        draw_border(win, -(200-a*length)/2, -10, length*a+(200-a*length)/2, height*a+80, length*a, False)
        timer = NumBox(win, Rectangle(Point(-(200-a*length)/2+15, a*height+17.5), Point(-(200-a*length)/2+70, a*height+37.5)), "0")
        mine_counter = NumBox(win, Rectangle(Point(-(200-a*length)/2+15, a*height+42.5), Point(-(200-a*length)/2+70, a*height+62.5)), str(mines))
        mode_select = Select(win, Rectangle(Point(length*a+(200-a*length)/2-75, height*a+25), Point(length*a+(200-a*length)/2-15, height*a+55)))

    draw_smiley(win, a*length/2-20, a*height+20, 40)
    reset_button = Button(Rectangle(Point(a*length/2-20, a*height+20), Point(a*length/2+20, a*height+60)), "")
    reset_button.activate()

    cells = []

    for i in range(height):
        cells.append([])
        for j in range(length):
            cells[i].append(Cell(win, a*j, a*i, a))
    
    started = False
    won = False
    reset = False
    lost = False
    p = None
    key = None
    cells_revealed = 0

    win.checkMouse()

    while True:
        if key != None or key != "":
            if key == "Return":
                break
            elif key == "s" and not (won or lost):
                mode_select.swap()
        if p != None:
            if reset_button.clicked(p):
                reset = True
                break
            elif 0 <= p.getX() <= length*a and 0 <= p.getY() <= height*a and not (won or lost):
                i, j = findCellAddress(p, length, height, a)
                cell_clicked = cells[i][j]
                if not cell_clicked.isRevealed() and mode_select.getMode() == "flag":
                    if cell_clicked.getFlaggedStatus():
                        mine_counter.changeVal(1)
                    else:
                        mine_counter.changeVal(-1)
                    cell_clicked.flag()
                elif not cell_clicked.getFlaggedStatus():
                    if not started:
                        mineSpreading(cells, length, height, a, mines, i, j)
                        setupValues(cells)
                        startTime = time.monotonic()
                        started = True
                    if cell_clicked.getStatus() == -1:
                        cell_clicked.redMine()
                        reveal_mines(cells)
                        lost = True
                    elif cell_clicked.isRevealed():
                        lost, cells_revealed_via_chording = chord(cells, i, j)
                        cells_revealed += cells_revealed_via_chording
                    else:
                        cell_clicked.reveal()
                        cells_revealed += 1
                        if cell_clicked.getStatus() == 0:
                            cells_revealed += zeroSpread(i, j, cells)
        
        if cells_revealed >= (length*height - mines):
            won = True

        if started and not (won or lost):
            newTime = time.monotonic()
            if newTime - startTime >= 1:
                timeInc = floor(newTime - startTime)
                timer.changeVal(timeInc)
            
                startTime = newTime

        key = win.checkKey()
        p = win.checkMouse()

    if reset:
        win.close()
        playMinesweeper(length, height, mines)
    else:
        win.close()
        main()

def main():
    try:
        men = GraphWin("Minesweeper", 400, 400)
        men.setCoords(0, 0, 100, 100)

        x, y, n = menu(men)

        sys.setrecursionlimit(2600)

        playMinesweeper(x, y, n)
    
    except GraphicsError:
        pass
    
if __name__ == "__main__": main()