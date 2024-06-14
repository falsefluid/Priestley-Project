# leaderboard.py
import csv

def leaderboard(user_info):
    filename = "MainSheet.csv"

    # Setting up arrays
    fields = []
    rows = []
    user_scores = {}
    
    # Reading the database
    with open(filename, "r") as mainfile:
        csvreader = csv.reader(mainfile)
        fields = next(csvreader)
        for row in csvreader:
            rows.append(row)
            user_scores[row[3]] = int(row[10])  

    # Sorting users by scores in descending order
    sorted_users = sorted(user_scores.items(), key=lambda x: x[1], reverse=True)

    # Final leaderboard
    print(" ")
    print("<>=<>=<>=<>=<>=<>=<>=<>=<>=<>=<>=<>=<>=<>=<>=<>=<>=<>=<>=<>=<>\n")
    print("LEADERBOARD:")
    for rank, (user, score) in enumerate(sorted_users, start=1):
        print(f"{rank}. {user}: {score} points")
        if user == user_info["Uname"].values[0]:
            user_rank = rank
    print(" ")
    print("* This is your score! Your rank is", user_rank, "overall! *")
    print("\n<>=<>=<>=<>=<>=<>=<>=<>=<>=<>=<>=<>=<>=<>=<>=<>=<>=<>=<>=<>=<>")


def friend_leaderboard(user_info):
    filename = "MainSheet.csv"
    users = []
    user_scores = {}

    # Load the usernames and scores
    with open(filename, "r") as mainfile:
        csvreader = csv.reader(mainfile)
        fields = next(csvreader)
        for row in csvreader:
            users.append(row[3])
            user_scores[row[3]] = int(row[10])

    logged_in_username = user_info["Uname"].values[0]
    selected_friends = [logged_in_username]

    print("Available users:")
    for user in users:
        if user != logged_in_username:
            print(user)
    print("")

    while True:
        friend = input("Enter a username to add to your friend leaderboard (or type 'done' to finish): ").strip()
        
        if friend.lower() == 'done':
            break
        elif friend not in users:
            print(f"{friend} not found in the user list. Please try again.")
        elif friend in selected_friends:
            print(f"{friend} is already in your friend leaderboard. Please try again.")
        else:
            selected_friends.append(friend)
            print(f"{friend} added to your friend leaderboard.")

    # Sort selected friends by their scores
    selected_friends.sort(key=lambda x: user_scores[x], reverse=True)

    print(" ")
    print("<>=<>=<>=<>=<>=<>=<>=<>=<>=<>=<>=<>=<>=<>=<>=<>=<>=<>=<>=<>=<>\n")
    print("FRIEND LEADERBOARD: ")
    for rank, friend in enumerate(selected_friends, start=1):
        print(f"{rank}. {friend}: {user_scores[friend]} points")

    # Find and print the logged-in user's rank
    user_rank = selected_friends.index(logged_in_username) + 1
    print(f"\nYou ({logged_in_username}) are ranked {user_rank} out of {len(selected_friends)} friends.")
    print("\n<>=<>=<>=<>=<>=<>=<>=<>=<>=<>=<>=<>=<>=<>=<>=<>=<>=<>=<>=<>=<>")


