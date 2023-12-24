import random


def create_player(name):
    return {"name": name, "score": 0}


def play_round(player1, player2):
    number = random.randint(-5, 13)
    print(f"Random Number is {number}.")

    if number % 2 == 0:
        player1['score'] += 1
        print(f"Round: {player1['name']} scored!")
    else:
        player2['score'] += 1
    return player1, player2

def play_round_boos(player1, player2):
    number = random.randint(-5, 13)
    print(f"Random Number is {number}.")

    if number % 2 == 0 and number >= 0:
        player1['score'] += 1
        print(f"Round: {player1['name']} scored!")
    elif number % 2 != 0 :
        player2['score'] += 1
        print(f"Round: {player2['name']} scored!")
    elif number % 2 == 0 and number < 0:
        print("The Boss has nullified this round! Replay the round.")

    print(f"Status: {player1['name']} {player1['score']}, {player2['name']} {player2['score']}")
    return player1, player2



def conduct_tournament(players, rounds_to_win):
    playing = True

    while playing:
        player1, player2 = random.sample(players, 2)
        if player1['score'] < rounds_to_win and player2['score'] < rounds_to_win:
            player1, player2 = play_round(player1, player2)

        for i, player in enumerate(players):
            if player['name'] == player1['name']:
                players[i]['score'] = player1['score']
            elif player['name'] == player2['name']:
                players[i]['score'] = player2['score']

        for player in players:
            if int(player['score']) == rounds_to_win:
                print(f"{player['name']} Wins the round!")
                playing = False
                return player


def play_game():
    num_players = int(input("Enter the number of players: "))
    players = []

    for i in range(num_players):
        name = input(f"Enter Player {i + 1}'s name: ")
        players.append(create_player(name))

    rounds_to_win = int(input("Enter the number of rounds to win: "))
    winner = conduct_tournament(players, rounds_to_win)

    # Winner of the tournament plays against the Boss
    boss = create_player("Boss")
    print("\n=== Final Round: Winner vs. Boss ===")
    print(f"{winner['name']} vs. {boss['name']}")
    winner['score'] = 0

    while winner['score'] <= rounds_to_win and boss['score'] <= rounds_to_win:
        winner, boss = play_round_boos(winner, boss)
        if winner['score'] == rounds_to_win:
            print(f"{winner['name']} Wins the final round and is the ultimate champion!")
            break
        elif boss['score'] == rounds_to_win:
            print("The Boss Wins the final round. Better luck next time!")
            break


if __name__ == "__main__":
    play_game()
