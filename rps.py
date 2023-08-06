import random


def get_player():
    player = input("Try your luck:  ")
    while player not in("Rock", "Paper", "Scissors") :
        print("This is Rock, Paper, Scissors; Try again! ")
        player = input("Try your luck:  ")
    return player

def get_computer():
    return random.choice(["Rock", "Paper", "Scissors"])

def get_winner(player, computer):
        if player == computer:
            return "Tie!"
        elif (player == "Rock" and computer == "Scissors") or \
            (player == "Scissors" and computer == "Paper") or \
            (player == "Paper" and computer == "Rock"):
                return "You win!"
        else:
            return "You lose pimp!"

def play_game():
    print("Welcome to Rock-Paper-Scissors!")
    print("Good Luck!")
    player_score = 0
    computer_score = 0
    rounds = 3



    for rounds in range(1, rounds+1):
        print(f"\nRound {rounds}")
        player = get_player()
        computer = get_computer()

        print(f"Your turn lol: {player}")
        print(f"Computer turn: {computer}")


        result = get_winner(player, computer)
        print(result)

        if "You win!" in result:
            player_score +=1
        elif "You lose pimp!" in result:
            computer_score +=1
            print(f'\nFinal Score!')
            print(f"Your score: {player_score} \nComputer: {computer_score}")

    if player_score > computer_score:
        print("You shot that BB gun!")
    elif computer_score > player_score:
        print("Sorry player!")
    else:
        print("Tie")

        play_again = input("Do you want another round? (Y/N):  ")

        if play_again != "Y":
            print(f"Thank you come again!")


if __name__ == "__main__":
    play_game()
