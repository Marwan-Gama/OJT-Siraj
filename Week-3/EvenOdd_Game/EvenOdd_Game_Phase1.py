import random

def Player(name):
    return {"name":name , "score":0}

def play_round(player1, player2):
    number = random.randint(-5, 13)
    if number % 2 == 0:
        player1['score'] += 1
        print(f"Round: {player1['name']} scored!")
    else:
        player2['score'] += 1
        print(f"Round: {player2['name']} scored!")
    print(f"Status: {player1['name']} {player1['score']}, {player2['name']} {player2['score']}")

def play_game():
    player1_name = input("Enter Player 1's name: ")
    player2_name = input("Enter Player 2's name: ")
    player1 = Player(player1_name)
    player2 = Player(player2_name)
    while player1['score'] < 3 and player2['score'] < 3:
        play_round(player1, player2)
    if player1['score'] == 3:
        print(f"{player1['name']} Wins!")
    else:
        print(f"{player2['name']} Wins!")

if __name__ == "__main__":
    play_game()
