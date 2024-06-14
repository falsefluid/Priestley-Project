# login.py
import pandas as pd
import time

# Load the data
df = pd.read_csv('MainSheet.csv', converters={'ID': str,
                 'Password':str}) # makes ID and password string just in case they start with 0

# Identification and validation of the user
def login_system():
    while True:
        try:
            username = input("What is your username? ")
            if username not in df["Uname"].values: # check if the username exists in the loaded DataFrame
                print("This username does not exist, try again.")
            else:
                user_info = df[df["Uname"] == username] # retrieve user information based on username
                print(f"{username} found!")
                for attempt in range(3): # attempt password verification up to 3 times
                    password = input(f"Enter your password (Attempt {attempt + 1}/3): ")
                    if password != user_info["Password"].values[0]: # check if the entered password matches the stored password
                        print("Password is wrong. Retry.")
                    else:
                        print("Password is correct!\n")
                        time.sleep(1)
                        print(f"Welcome, {user_info['Uname'].values[0]}!")
                        return user_info  # return user information DataFrame if login successful
                print("Number of attempts reached. Restarting.")
                time.sleep(1) # if maximum attempts reached, simulate locking out
        except Exception as e:
            print(f"An unexpected error occurred: {e}. Restarting...")
            time.sleep(1) # handles unexpected errors and restarts the login process

