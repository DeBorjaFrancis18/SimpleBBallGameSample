#A Simple Basketball Game Sample
#John Francis De Borja

import random
"""I have imported random module so that randomness
   can be applied when a shot is missed or hit or pass"""

class Player:
    def __init__(self, name, number):
        self.name = name
        self.number = number
        self.pScore = 0

    def shoot(self):
        isBasket = random.choice([True, False])
        if isBasket:
            self.pScore += 2
            print(f"{self.name} scored 2 points!")
        else:
            print(f"{self.name} missed the shot.")

    def passBall(self, teammate):
        print(f"{self.name} passed the ball to {teammate.name}.")

    def score(self):
        return self.pScore

class Team:
    def __init__(self, name):
        self.name = name
        self.players = []

    def addPlayer(self, player):
        if len(self.players) < 5:
            self.players.append(player)
            if self.name != "Opponent Team":
                print(f"{player.name} is added to {self.name}.\n")
        else:
            print(f"{self.name} has 5 players already.")

    def shoot(self):
        player = random.choice(self.players)
        player.shoot()

    def passBall(self):
        if len(self.players) > 1:
            passing = random.choice(self.players)
            receiving = random.choice([p for p in self.players if p != passing])
            passing.passBall(receiving)

    def teamScore(self):
        totalScore = 0
        for player in self.players:
            totalScore += player.score()
        return totalScore

class OpponentTeam(Team):
    def __init__(self, name):
        super().__init__(name)
        for i in range(1, 6):
            opponentName = f"Opponent {i}"
            opponentPlayer = Player(opponentName, i)
            self.addPlayer(opponentPlayer)

    def defend(self):
        defender = random.choice(self.players)
        isDefended = random.choice([True, False])
        if isDefended:
            print(f"{defender.name} defended!")
        else:
            print(f"{defender.name} failed. Shot is clear!")

class Ball:
    def __init__(self):
        self.isHeld = False

    def pick_up(self):
        self.isHeld = True
        print("The ball is picked up.")

    def release(self):
        self.isHeld = False
        print("The ball is released.")

    def is_free(self):
        return not self.isHeld

def main():
    print("Welcome to the Basketball Game!")

    playerName = input("Enter player's name: ")
    player = Player(playerName, 99)

    teamName = input("Enter your team name: ")
    teamPlayer = Team(teamName)
    teamPlayer.addPlayer(player)

    for i in range(4):
        playerName = input(f"Enter player {i+2}'s name: ")
        player = Player(playerName, i + 2)
        teamPlayer.addPlayer(player)

    opponentTeam = OpponentTeam("Opponent Team")
    ball = Ball()

    while True:
        print("\nMenu:")
        print("1. Shoot the ball")
        print("2. Pass the ball")
        print("3. View your team's score")
        print("4. View opponent team's score")
        print("5. Exit")

        choice = input("Enter your choice (1/2/3/4/5): ")

        if choice == '1':
            teamPlayer.shoot()
            ball.release()
            if teamPlayer.teamScore() >= 10:
                print(f"{teamPlayer.name} wins! The game is over.")
                break
            elif opponentTeam.teamScore() >= 10:
                print(f"{opponentTeam.name} wins! The game is over.")
                break
        elif choice == '2':
            if len(teamPlayer.players) > 1:
                ball.release()
                teamPlayer.passBall()
        elif choice == '3':
            print(f"{teamPlayer.name}'s score: {teamPlayer.teamScore()} points")
        elif choice == '4':
            print(f"{opponentTeam.name}'s score: {opponentTeam.teamScore()} points")
        elif choice == '5':
            print("Thanks for playing! Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
        main()