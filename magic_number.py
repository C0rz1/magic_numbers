import os

REWARDS = {
    "Chocolate bar": 10,
    "Cinema ticket": 30,
    "Travel ticket": 40
}

MIN = 1
MAX = 10

# player variables
LIFES = 3
CREDITS = 0
PLAYER_NAME = None

# entry point
def main():
    intro()

def get_player_name():
    global PLAYER_NAME
    PLAYER_NAME = input("What is your name?")

def intro():
    clear_screen()
    print("="*25, "MAGIC NUMBER", "="*25)
    print("In this game you have to guess a number I'm thinking. The number must be between 1 and 10.")

def outro():
    clear_screen()
    print("See you later!")
    exit()

def clear_screen():
    os.system("cls" if os.name == "nt" else "clear")

main()