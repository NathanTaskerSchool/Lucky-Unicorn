# Lucky Unicorn - Nathan Tasker
import random
TOKEN_OUTCOMES = ["zebra", "horse", "donkey", "unicorn"]
ROUND_COST = 1
MAX_STARTING_MONEY = 10
UNICORN_PRIZE_MONEY = 5
ZEBRA_PRIZE_MONEY = 0.5
HORSE_PRIZE_MONEY = 0.5
DONKEY_PRIZE_MONEY = 0


def display_statistics():
    print(f"Current Money: {money}")


def ask_to_play():
    input_answer = "test"
    while input_answer != "y" and input_answer != "n":
        input_answer = input(f"Do you want to spend ${ROUND_COST} to play a round? (y/n): ")
        input_answer = input_answer.lower()
        if input_answer == "y":
            return True
        elif input_answer == "n":
            return False
        else:
            print("Invalid input. Try again.")


def get_initial_payment():
    value = float(input(f"Input payment of initial amount (0-{MAX_STARTING_MONEY}): "))
    while value > MAX_STARTING_MONEY or value < 0:
        print("Invalid input. Try again.")
        value = float(input(f"Input payment of initial amount (0-{MAX_STARTING_MONEY}): "))
    return value


def get_token():
    token_index = random.randint(0, len(TOKEN_OUTCOMES) - 1)
    print(f"Your token is a {TOKEN_OUTCOMES[token_index]}.")
    return TOKEN_OUTCOMES[token_index]


def print_prize_message(value):
    if value <= 0:
        print("Sorry, you didn't win any money.")
    elif value < ROUND_COST:
        print(f"Sorry, you only won ${value} back.")
    else:
        print(f"Congratulations, you won ${value}!")


def calculate_money_change(token):
    # I used literal strings instead of indexes, as indexes may change
    if token == "unicorn":
        print_prize_message(UNICORN_PRIZE_MONEY)
        return UNICORN_PRIZE_MONEY
    elif token == "zebra":
        print_prize_message(ZEBRA_PRIZE_MONEY)
        return ZEBRA_PRIZE_MONEY
    elif token == "horse":
        print_prize_message(HORSE_PRIZE_MONEY)
        return HORSE_PRIZE_MONEY
    elif token == "donkey":
        print_prize_message(DONKEY_PRIZE_MONEY)
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
