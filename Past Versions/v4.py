# Lucky Unicorn - Nathan Tasker
import random
TOKEN_OUTCOMES = ["zebra", "horse", "donkey", "unicorn"]
ROUND_COST = 1
UNICORN_PRIZE_MONEY = 5
ZEBRA_PRIZE_MONEY = 0.5
HORSE_PRIZE_MONEY = 0.5
DONKEY_PRIZE_MONEY = 0


def display_statistics():
    print(money)


def ask_to_play():
    input_answer = "test"
    while input_answer != "y" and input_answer != "n":
        input_answer = input("Do you want to spend $1 to play a round? (y/n): ")
        input_answer = input_answer.lower()
        if input_answer == "y":
            return True
        elif input_answer == "n":
            return False
        else:
            print("Invalid input. Try again.")


def get_initial_payment():
    value = float(input("Input payment of initial amount: "))  # Potential for errors
    return value


def get_token():
    token_index = random.randint(0, len(TOKEN_OUTCOMES) - 1)
    print(f"Your token is a {TOKEN_OUTCOMES[token_index]}.")
    return TOKEN_OUTCOMES[token_index]


def calculate_money_change(token):
    # I used literal strings instead of indexes, as indexes may change
    if token == "unicorn":
        return UNICORN_PRIZE_MONEY
    elif token == "zebra":
        return ZEBRA_PRIZE_MONEY
    elif token == "horse":
        return HORSE_PRIZE_MONEY
    elif token == "donkey":
        return DONKEY_PRIZE_MONEY
    else:
        return 0


money = get_initial_payment()
playingGame = True

while playingGame:
    if ask_to_play():
        money -= ROUND_COST
        money += calculate_money_change(get_token())
        display_statistics()
    else:
        playingGame = False

display_statistics()
