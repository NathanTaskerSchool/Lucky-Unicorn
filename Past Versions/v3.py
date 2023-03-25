# Lucky Unicorn - Nathan Tasker


def display_statistics():


def ask_to_play():
    input_answer = input("Do you want to spend $1 to play a round? (y/n)")
    if input_answer == "y":
        return True
    elif input_answer == "n":
        return False
    else:
        # ask again

def get_initial_payment():
    value = float(input("Input payment of initial amount: "))  # Potential for errors
    return value


def get_token():


initialPayment = get_initial_payment()
playingGame = True

while playingGame:
    if ask_to_play():
        get_token()
        display_statistics()
    else:
        playingGame = False

display_statistics()