import random

class Morpion():
    def __init__(self):
        self.initiate()

    def initiate(self):
        self.grid = [[" " for i in range(3)] for i in range(3)]
        self.player_turn = "O"

    def print_grid(self):
        for row in self.grid:
            print(' | '.join(row))

    def isValid(self, x, y):
        return (x>0 and x<4 and y>0 and y<4 and self.grid[x-1][y-1] == " ")

    def isWon(self):
        # horizontal
        if ["X","X","X"] in self.grid or ["O","O","O"] in self.grid:
            return self.player_turn

        # vertical
        for i in range(3):
            if self.grid[0][i] != " " and self.grid[0][i] == self.grid[1][i] == self.grid[2][i]:
                return self.player_turn

        # diagonal 1
        if self.grid[0][0] != " " and self.grid[0][0] == self.grid[1][1] == self.grid[2][2]:
            return self.player_turn

        # diagonal 2
        if self.grid[0][2] != " " and self.grid[0][2] == self.grid[1][1] == self.grid[2][0]:
            return self.player_turn

        full = True
        for i in range(3):
            if " " in self.grid[i]: full = False

        if full: return "tie"
        return None

    def toggle_turn(self):
        self.player_turn = "X" if (self.player_turn == "O") else "O"

    def max(self):
        maxv = -2
        if not self.isWon():
            coups = []
            for i in range(1,4):
                for j in range(1,4):
                    if self.isValid(i,j):
                        self.grid[i-1][j-1] = self.player_turn
                        self.toggle_turn()
                        (m, (iMin, jMin)) = self.min()
                        self.grid[i-1][j-1] = " "
                        self.toggle_turn()
                        if m > maxv:
                            maxv = m
                            coups = [(i, j)]
                        elif m==maxv:
                            coups.append((i,j))
            return (maxv, random.choice(coups))

        else:
            if self.isWon()==self.player_turn:
                return (-1, (0,0))
            elif self.isWon()=="tie":
                return (0, (0,0))
            else:
                return (1, (0,0))

    def min(self):
        minv = 2
        if not self.isWon():
            coups = []
            for i in range(1,4):
                for j in range(1,4):
                    if self.isValid(i,j):
                        self.grid[i-1][j-1] = self.player_turn
                        self.toggle_turn()
                        (m, (iMax, jMax)) = self.max()
                        self.grid[i-1][j-1] = " "
                        self.toggle_turn()
                        if m < minv:
                            minv = m
                            coups = [(i, j)]
                        elif m==minv:
                            coups.append((i,j))
            return (minv, random.choice(coups))

        else:
            if self.isWon()==self.player_turn:
                return (1, (0,0))
            elif self.isWon()=="tie":
                return (0, (0,0))
            else:
                return (-1, (0,0))

    def play(self):
        while True:
            if self.isWon(): break
            self.toggle_turn()

            if self.player_turn=="X":
                (score, (x,y)) = self.max()
                print("L'IA joue " + str((x,y)) + " s: " + str(score))
            else:
                x = input("row : ")
                y = input("col : ")
                valid = False

                try:
                    x = int(x)
                    y = int(y)
                    valid = self.isValid(x,y)
                except:
                    print("err - not digits")

                while not valid:
                    print("Please enter digits between 1 and 3.")
                    try:
                        x = int(input("row : "))
                        y = int(input("col : "))
                        valid = self.isValid(x,y)
                    except:
                        print("err - not digits")

            self.grid[x-1][y-1] = self.player_turn
            self.print_grid()

        if self.isWon() == "tie":
            print("Partie finie: Egalite.")
            return
        print("Partie finie. Gagnant : " + self.player_turn)

morpion = Morpion()
morpion.play()
