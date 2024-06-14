#main.py
#run this one
from menu import menu 

def main():
    print("Welcome to the Recy Co. App!")
    
    while True:
        try:
            if not menu(): # call the menu function and check its return value
                break # exit the while loop if menu() returns False (user chooses to exit)
        except Exception as e:
            print(f"An error occurred: {e}")
            choice = input("Do you want to restart the app? (yes/no): ").strip().lower()
            if choice == 'no':
                print("Exiting the application. Goodbye!")
                break # exit the while loop if user chooses not to restart the app

if __name__ == "__main__":
    main()

