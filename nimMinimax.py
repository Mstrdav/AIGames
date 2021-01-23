class Nim:
    def __init__(self):
        self.initializeGame()

    def initializeGame(self):
        self.batons = 21

        # L'IA commence
        self.player_turn = "IA"

    def printBatons(self):
        for i in range(self.batons):
            print('|', end="")
        print(" (" + str(self.batons) + ")")

    def isValid(self, move):
        if move>0 and move<4 and self.batons-move>0:
            return True

        return False

    def isWon(self):
        if self.batons==1:
            return self.player_turn

        return None

    def max(self): # joueur max, essaye de maximiser le score de l'AI
        maxv = -2
        if not self.isWon():
            coup = 0
            for i in range(1,4):
                if self.isValid(i):
                    self.batons -= i
                    (m, coupMin) = self.min()
                    self.batons += i
                    if m > maxv:
                        maxv = m
                        coup = i
            return (maxv, coup)

        else:
            if self.isWon()=="human":
                return (-1, 0)
            else:
                return (1, 0)

    def min(self): # joueur min, essaye de minimiser le score de l'AI
        minv = 2
        if not self.isWon():
            coup = 0
            for i in range(1,4):
                if self.isValid(i):
                    self.batons -= i
                    (M, coupMax) = self.max()
                    self.batons += i
                    if M < minv:
                        minv = M
                        coup = i
            return (minv, coup)

        else:
            if self.isWon()=="IA":
                return (-1, 0)
            else:
                return (1, 0)

    def play(self):
        while True:
            self.printBatons()
            if self.player_turn=="human":
                self.player_turn = "IA"
                good = False
                while not good:
                    try:
                        coup = input("Votre coup - ")
                        coup = int(coup)
                        if self.isValid(coup):
                            good = True
                        else:
                            raise Exception
                    except Exception as e:
                        print("Coup invalide (entrez 1, 2 ou 3).\n", e)

                self.batons -= coup

            else:
                self.player_turn = "human"
                (score, coup) = self.max()
                print("L'IA enlève " + str(coup) + " batons. (score :" + str(score) + ")")
                self.batons -= coup

            if self.batons == 1:
                break

        print("Partie terminée.")
        print("Le perdant est " + self.player_turn)


nim = Nim()
nim.play()
