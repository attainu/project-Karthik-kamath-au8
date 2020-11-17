import time
import random
import sys


SLEEP_BETWEEN_ACTIONS = 0.5
MAX_VAL = 100
DICE_FACE = 6


snakes = {
    8: 4,
    18: 1,
    26: 10,
    39: 5,
    51: 6,
    54: 36,
    56: 1,
    60: 23,
    75: 28,
    83: 45,
    85: 59,
    90: 48,
    92: 25,
    97: 87,
    99: 63
}

ladders = {
    3: 20,
    6: 14,
    11: 28,
    15: 34,
    17: 74,
    22: 37,
    38: 59,
    49: 67,
    57: 76,
    61: 78,
    73: 86,
    81: 98,
    88: 91
}

player_turn_text = [
    "Your turn.",
    "Go.",
    "Please proceed.",
]

snake_bite = [
    "ohhhoo",
    "bummer",
    "ssshshsshh",
    "ohooonoooo",
    "dangggg"
]

ladder_jump = [
    "woohoo",
    "wowow",
    "yupieee",
    "oh my God...",
    "yaayyy"
]


def welcome_msg():
    msg = """
    Welcome to Snake and Ladder Game.
    """
    print(msg)

def get_dice1_value():
    time.sleep(SLEEP_BETWEEN_ACTIONS)
    dice1_value = random.randint(1, DICE_FACE)
    print("Its a " + str(dice1_value))
    return dice1_value
def get_dice2_value():
    time.sleep(SLEEP_BETWEEN_ACTIONS)
    dice2_value = random.randint(1, DICE_FACE)
    print("Its a " + str(dice2_value))
    return dice2_value    


def got_snake_bite(old_value, current_value, player_name):
    print("\n" + random.choice(snake_bite).upper() + " /\/\/\//\>")
    print("\n" + player_name + " got a snake bite. Down from " + str(old_value) + " to " + str(current_value))


def got_ladder_jump(old_value, current_value, player_name):
    print("\n" + random.choice(ladder_jump).upper() + " =======")
    print("\n" + player_name + " climbed the ladder from " + str(old_value) + " to " + str(current_value))


def snake_ladder(player_name, current_value, dice1_value,dice2_value):
    time.sleep(SLEEP_BETWEEN_ACTIONS)
    old_value = current_value
    current_value = current_value + dice1_value + dice2_value

    if current_value > MAX_VAL:
        print("You need " + str(MAX_VAL - old_value) + " to win this game. Keep Rolling.")
        return old_value

    print("\n" + player_name + " moved from " + str(old_value) + " to " + str(current_value))
    if current_value in snakes:
        final_value = snakes.get(current_value)
        got_snake_bite(current_value, final_value, player_name)

    elif current_value in ladders:
        final_value = ladders.get(current_value)
        got_ladder_jump(current_value, final_value, player_name)

    else:
        final_value = current_value

    return final_value


def check_win(player_name, position):
    time.sleep(SLEEP_BETWEEN_ACTIONS)
    if MAX_VAL == position:
        print("\n\n\nThats it.\n\n" + player_name + " won the game.")
        print("Congratulations " + player_name)
        print("\nThank you for playing the game.\n\n")
        sys.exit(1)


def start():
    welcome_msg()
    time.sleep(SLEEP_BETWEEN_ACTIONS)
    player1_current_position = 0
    player2_current_position = 0
    player3_current_position = 0
    player4_current_position = 0

    while True:

        play=input("Press Enter to Play and Exit to quit the Game: ")
        if play=="":
            print("Choose your mode (Single player/Multiplayer)")#mode selection
            mode=input("Enter \"S\" for sigle player and \"M\" for multiplayer: ")
            if (mode=="S" or mode== "s"):
                Player2_Name="Computer"
                num_players=2
            else:
                num_players=int(input("Enter number of players: "))    
            Player1_Name=input("Enter player 1 name: ")
            if (mode=="M" or mode== "m") and 5 > num_players > 1:
                Player2_Name=input("Enter player 2 name: ")
            if 5>num_players>2:
                Player3_Name=input("Enter player 3 name: ")
            if 5>num_players>3:
                Player4_Name=input("Enter player 4 name: ") 
                print()
            print("Good Luck!")
            print() 

            while True:
                if 5>num_players>1:
                    time.sleep(SLEEP_BETWEEN_ACTIONS)
                    input_1 = input("\n" + Player1_Name + ": " + random.choice(player_turn_text) + " Hit the enter to roll dice: ")
                    print("\nRolling dice...")
                    dice1_value = get_dice1_value()
                    dice2_value = get_dice2_value()
                    time.sleep(SLEEP_BETWEEN_ACTIONS)
                    print(Player1_Name + " moving....")
                    player1_current_position = snake_ladder(Player1_Name, player1_current_position, dice1_value,dice2_value)
                    if check_win(Player1_Name, player1_current_position):
                        break
                    if 5>num_players>1:
                        input_2 = input("\n" + Player2_Name + ": " + random.choice(player_turn_text) + " Hit the enter to roll dice: ")
                        print("\nRolling dice...")
                        dice1_value = get_dice1_value()
                        dice2_value = get_dice2_value()
                        time.sleep(SLEEP_BETWEEN_ACTIONS)
                        print(Player2_Name + " moving....")
                        player2_current_position = snake_ladder(Player2_Name, player2_current_position,dice1_value,dice2_value)
                        if check_win(Player2_Name, player2_current_position):
                            break

                if 5>num_players>2:
                    input_3 = input("\n" + Player3_Name + ": " + random.choice(player_turn_text) + " Hit the enter to roll dice: ")
                    print("\nRolling dice...")
                    dice1_value = get_dice1_value()
                    dice2_value = get_dice2_value()
                    time.sleep(SLEEP_BETWEEN_ACTIONS)
                    print(Player3_Name + " moving....")
                    player3_current_position = snake_ladder(Player3_Name, player3_current_position,dice1_value,dice2_value)
                    if check_win(Player3_Name, player3_current_position):
                        break

                if 5>num_players>3:

                    input_4 = input("\n" + Player4_Name + ": " + random.choice(player_turn_text) + " Hit the enter to roll dice: ")
                    print("\nRolling dice...")
                    dice1_value = get_dice1_value()
                    dice2_value = get_dice2_value()
                    time.sleep(SLEEP_BETWEEN_ACTIONS)
                    print(Player4_Name + " moving....")
                    player4_current_position = snake_ladder(Player4_Name, player4_current_position,dice1_value,dice2_value)
                    if check_win(Player4_Name, player4_current_position):
                        break
                print("_________________________________________________________________________________________________________") 
        elif play=="exit" or play=="Exit":
            break
            quit           

start()