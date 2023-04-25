class Team:
    def __init__(self, name, players):
        self.name = name
        self.players = players

class Player:
    def __init__(self, name, position, score):
        self.name = name
        self.position = position
        self.score = score

def create_team():
    name = input("Enter team name: ")
    players = []
    for i in range(11):
        player_name = input(f"Enter name for player {i + 1}: ")
        player_position = input(f"Enter position for player {i + 1}: ")
        player_score = float(input(f"Enter score for player {i + 1}: "))
        player = Player(player_name, player_position, player_score)
        players.append(player)
    team = Team(name, players)
    return team

def main():
    teams = []
    while True:
        choice = input("Enter 1 to create a new team, 2 to list all teams, or 3 to exit: ")
        if choice == "1":
            team = create_team()
            teams.append(team)
        elif choice == "2":
            for team in teams:
                print(f"Team: {team.name}")
                for player in team.players:
                    print(f"Player: {player.name} | Position: {player.position} | Score: {player.score}")
                print()
        elif choice == "3":
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
