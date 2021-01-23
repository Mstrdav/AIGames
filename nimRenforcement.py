import random, math

class Nim:
    def __init__(self):
        self.initializeGame()
        self.reseauIA = [[5 for i in range(3)] for i in range(21)] #

    def initializeGame(self):
        self.batons = 21
        self.coupsJouesIA = []

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

    def playIA(self):
        turn_factor = 1 if self.player_turn=="IA" else -1
        nbBatons = self.batons
        choices = random.choices([1,2,3], self.reseauIA[nbBatons-1])

        if self.isValid(choices[0]):
            choice = choices[0]
        elif self.isValid(choices[0] - 1):
            choice = choices[0] - 1
        else:
            choice = choices[0] -2

        return (nbBatons, choice, turn_factor)

    def evaluate(self, aGagne):
        increment = 1 if aGagne else -1
        for coup in self.coupsJouesIA:
            self.reseauIA[coup[0]-1][coup[1]-1] = max(1, self.reseauIA[coup[0]-1][coup[1]-1] + increment*coup[2])

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
                (nbBatons, coup, turn_factor) = self.playIA()
                print("L'IA enlève " + str(coup) + " batons.")
                self.batons -= coup

            if self.batons == 1:
                break

        print("Partie terminée.")
        print("Le perdant est " + self.player_turn)
        self.initializeGame()

    def trainIA(self, n):
        print("Training AI")
        toPrint = ""
        for i in range(n):
            toPrint = "[PROGRESS] "
            for j in range(round(i/n*100)):
                toPrint += "/"
            for j in range(round((n-i)/n*100)):
                toPrint += "."
            toPrint += str(round((i/n*100))) + "%"
            print(toPrint, end="\r")
            while True:
                (nbBatons, coup, turn_factor) = self.playIA()
                self.coupsJouesIA.append((nbBatons, coup, turn_factor))
                self.batons -= coup

                if self.player_turn=="human":
                    self.player_turn = "IA"
                else:
                    self.player_turn = "human"

                if self.batons == 1:
                    break

            IAGagnante = True if self.player_turn=="human" else False
            self.evaluate(IAGagnante)
            self.initializeGame()

        print(toPrint)
        print("AI trained.\n")
        print(self.reseauIA)

nim = Nim()
nim.trainIA(10000)
nim.play()
