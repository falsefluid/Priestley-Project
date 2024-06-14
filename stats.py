# stats.py

def stats(user_info):
    print(" ")
    print("<>=<>=<>=<>=<>=<>=<>=<>=<>=<>=<>=<>=<>=<>=<>=<>=<>=<>=<>=<>=<>\n")
    print("YOUR STATS:")

    labels = {
        'FirstName': 'First Name',
        'LastName': 'Last Name',
        'Uname': 'Username',
        'ID': 'ID',
        'Rpoints': 'Recycle Points',
        'Hours': 'Community Service Hours',
        'PrintAmt': 'Printing Amount',
        'TotalPoints': 'Total Points',
        'GoodTransport (Y/N)': 'Good Transport',
        'CurrentRoom': 'Room'
    }

    for key, label in labels.items():
        try:
            value = user_info[key].values[0]
            print(f"{label}: {value}")
        except KeyError:
            print(f"{label}: N/A (Data not available)")

    print("\n<>=<>=<>=<>=<>=<>=<>=<>=<>=<>=<>=<>=<>=<>=<>=<>=<>=<>=<>=<>=<>\n")