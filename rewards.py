#rewards.py

import csv

def rewards(user_info):
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
            user_scores[row[3]] = int(row[10])  # assuming row[3] is Uname and row[10] is TotalPoints

    # Sorting users by scores in descending order
    sorted_users = sorted(user_scores.items(), key=lambda x: x[1], reverse=True)

    # Top 3 users
    top_users = sorted_users[:3]

    # Define rewards
    rewards_list = [
        "30 Pounds Amazon Gift Card",
        "Library Book Voucher",
        "Free Starbucks Voucher"
    ]

    # Assign rewards to top 3 users
    print(" ")
    print("<>=<>=<>=<>=<>=<>=<>=<>=<>=<>=<>=<>=<>=<>=<>=<>=<>=<>=<>=<>=<>\n")
    print("REWARD SYSTEM (end of month):")
    for rank, (user, score) in enumerate(top_users, start=1):
        reward = rewards_list[rank - 1]
        print(f"{rank}. {user}: {score} points - Reward: {reward}")
        if user == user_info["Uname"].values[0]:
            user_rank = rank
            user_reward = reward
    print(" ")
    if user_info["Uname"].values[0] in [user for user, score in top_users]:
        print(f"* Congratulations! You are ranked {user_rank} and could earn the reward: {user_reward} *")
        print("If you keep this up by the end of the month, you will receive the reward!")
    else:
        print("You are not in the top 3. Keep recycling to earn more points!")
    print("\n<>=<>=<>=<>=<>=<>=<>=<>=<>=<>=<>=<>=<>=<>=<>=<>=<>=<>=<>=<>=<>")