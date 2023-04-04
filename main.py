# Lucky Unicorn - Nathan Tasker
import random
TOKEN_OUTCOMES = ["zebra", "horse", "donkey", "unicorn"]
ROUND_COST = 1
MAX_STARTING_MONEY = 10
UNICORN_PRIZE_MONEY = 5
ZEBRA_PRIZE_MONEY = 0.5
HORSE_PRIZE_MONEY = 0.5
DONKEY_PRIZE_MONEY = 0


def display_statistics(final):
    if final:
        print(f"Final Money: ${money:.2f}")
    else:
        print(f"Current Money: ${money:.2f}")


def ask_to_play():
    input_answer = "test"
    if money >= ROUND_COST:
        while input_answer != "y" and input_answer != "n":
            input_answer = input(f"Do you want to spend ${ROUND_COST} to play a round? (y/n): ")
            input_answer = input_answer.lower()
            if input_answer == "y":
                return True
            elif input_answer == "n":
                return False
            else:
                print("Invalid input. Try again.")
    else:
        print("You do not have enough money to play a round")
        return False


def get_initial_payment():
    value = 0
    while value > MAX_STARTING_MONEY or value <= 0:
        try:
            value = float(input(f"Input payment of initial amount (0-{MAX_STARTING_MONEY}): "))
            if value > MAX_STARTING_MONEY or value <= 0:
                print("Invalid input. Please try again.")
        except ValueError:
            print("Invalid input. Please try again.")
    return value


def get_token():
    token_index = random.randint(0, len(TOKEN_OUTCOMES) - 1)
    print(f"Your token is a {TOKEN_OUTCOMES[token_index]}.")
    return TOKEN_OUTCOMES[token_index]


def print_prize_message(value):
    if value <= 0:
        print("Sorry, you didn't win any money.")
    elif value < ROUND_COST:
        print(f"Sorry, you only won ${value:.2f} back.")
    else:
        print(f"Congratulations, you won ${value:.2f}!")


def calculate_money_change(token):
    prize_money = {
        "unicorn": UNICORN_PRIZE_MONEY,
        "zebra": ZEBRA_PRIZE_MONEY,
        "horse": HORSE_PRIZE_MONEY,
        "donkey": DONKEY_PRIZE_MONEY
    }
    if token in prize_money:
        print_prize_message(prize_money[token])
        return prize_money[token]
    else:
        return 0


money = get_initial_payment()
playingGame = True

while playingGame:
    if ask_to_play():
        money -= ROUND_COST
        money += calculate_money_change(get_token())
        display_statistics(False)
    else:
        playingGame = False

display_statistics(True)
