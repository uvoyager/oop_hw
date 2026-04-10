from turtle import Turtle
t = Turtle()

class Figure:
    def __init__(self, x, y):
        self.x = x
        self.y = y
    def setPosition(self):
        return t.goto(self.x, self.y)
    def show(self):
        raise NotImplementedError()
    def hide(self):
        t.clear()

class Circle(Figure):
    def show(self):
        t.penup()
        self.setPosition()
        t.color("red")
        t.pendown()
        t.circle(10)

class Cross(Figure):
    def show(self):
        t.penup()
        self.setPosition()
        t.setheading(0)
        t.color("orange")
        t.pendown()
        t.right(45)
        t.forward(10)
        t.penup()
        self.setPosition()
        t.setheading(0)
        t.pendown()
        t. right(135)
        t.forward(10)
        t.penup()
        self.setPosition()
        t.setheading(0)
        t.pendown()
        t.right(225)
        t.forward(10)
        t.penup()
        self.setPosition()
        t.setheading(0)
        t.pendown()
        t.right(315)
        t.forward(10)
        t.penup()

def drawGrid():
    for x in [-50, 50]:
        t.penup()
        t.goto(x, -150)
        t.pendown()
        t.goto(x, 150)
    for y in [-50, 50]:
        t.penup()
        t.goto(-150, y)
        t.pendown()
        t.goto(150, y)

board = [[None]* 3 for i in range(3)]
currentPlayer = "O"
figures = []

def cell(x, y):
    row = int((x+150)//100)
    col = int((150-y)//100)
    if 0<=row<3 and 0<=col<3:
        return row, col
    return None

def winner():
    for i in range(3):
        if board[i][0] == board[i][1] == board[i][2] != None:
            return board[i][0]
        if board[0][i] == board[1][i] == board[2][i] != None:
            return board[0][i]
    for j in range(3):
         if board[0][0] == board[1][1] == board[2][2] != None:
             return board[0][0]
         if board[0][2] == board[1][1] == board[2][0] != None:
             return board[0][2]

    return None

def gameTurn(x, y):
    global currentPlayer
    c = cell(x, y)
    if not c:
        return None
    row, col = c
    if board[row][col] is not None:
        return
    cx = row*100 - 100
    cy = 100 - col*100 
    if currentPlayer == "O":
        fig = Circle(cx, cy)
        board[row][col] = "O"
        currentPlayer = "X"
    elif currentPlayer == "X":
        fig = Cross(cx, cy)
        board[row][col] = "X"
        currentPlayer = "O"
    fig.show()
    figures.append(fig)
    win = winner()
    if win:
        print("winner: ", win)

t.screen.setup(400, 400)
drawGrid()
t.screen.onclick(gameTurn)
t.screen.mainloop()

