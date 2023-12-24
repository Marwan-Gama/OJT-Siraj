import random

def play_round(player1, player2):
    number = random.randint(-5, 13)
    print(f"Random Number is {number}.")
    if number % 2 == 0:
        player1['score'] += 1
        print(f"Round: {player1['name']} scored!")
    else:
        player2['score'] += 1
        print(f"Round: {player2['name']} scored!")
    print(f"Status: {player1['name']} {player1['score']}, {player2['name']} {player2['score']}")
    return player1, player2

def conduct_tournament(players, rounds_to_win):
    playing = True
    while playing:
        player1, player2 = random.sample(players, 2)
        if player1['score'] < rounds_to_win and player2['score'] < rounds_to_win:
            player1, player2 = play_round(player1, player2)

        for player in players:
            if player['name'] == player1['name']:
                player['score'] = player1['score']
            elif player['name'] == player2['name']:
                player['score'] = player2['score']

        for player in players:
            if player['score'] == rounds_to_win:
                print(f"{player['name']} Wins the round!")
                playing = False
                break

def play_game():
    num_players = int(input("Enter the number of players (no less than 2): "))
    players = []
    for i in range(num_players):
        name = input(f"Enter Player {i+1}'s name: ")
        players.append({'name': name, 'score': 0})
    rounds_to_win = int(input("Enter the number of rounds to win: "))
    conduct_tournament(players, rounds_to_win)

if __name__ == "__main__":
    play_game()
