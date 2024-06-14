# menu.py
import login
from leaderboard import leaderboard, friend_leaderboard
from room import room
from stats import stats
from rewards import rewards
import time
import sys

def menu():
    user_info = login.login_system()
    while True:
        try:
            menu_choice = int(input("""\nChoose your choice from the menu:
1. Leaderboard
2. Friend Leaderboard
3. Your Stats
4. Rewards
5. Rooms in use
6. Sign Out
7. Exit
8. Help\n"""))
            if (menu_choice >= 1) and (menu_choice <= 8):
                if menu_choice == 1:
                    leaderboard(user_info)
                elif menu_choice == 2:
                    friend_leaderboard(user_info)
                elif menu_choice == 3:
                    stats(user_info)
                    time.sleep(1)
                elif menu_choice == 4:
                    rewards(user_info)
                    time.sleep(1)
                elif menu_choice == 5:
                    room()
                    time.sleep(1)
                elif menu_choice == 6:
                    print("Sign out complete.")
                    return True # signal to main.py to restart the menu loop
                elif menu_choice == 8:
                    print("\nHelp: \n1. Leaderboard - View overall leaderboard.\n2. Friend Leaderboard - View leaderboard among friends.\n3. Your Stats - View your stats.\n4. Reward System - Check available rewards.\n5. Rooms in use - View rooms in use.\n6. Sign Out - Sign out of your account.\n7. Exit - Exit the application.")
                else:
                    print("Exiting the program. Goodbye!")
                    return False  # signal to main.py to exit the program
            else:
                print(f"{menu_choice} is not a valid choice, please pick from 1 - 8.")
        except ValueError:
            print("That is not a valid choice, please pick from 1 - 8.")
            time.sleep(1)
            