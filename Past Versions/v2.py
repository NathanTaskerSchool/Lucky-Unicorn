# Lucky Unicorn - Nathan Tasker

def display_statistics():

def ask_to_play():

def get_initial_payment():
    value = float(input("Input payment of initial amount: ")) # Potential for errors
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