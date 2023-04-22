# Delera, Aritz B.

import pyfiglet
import random

opening = pyfiglet.figlet_format("= O.O.P =", font = "starwars")
print(opening)


# Create an introduction
print("=" * 51)
print("\033[32m Welcome to AritzMetic's Story Keeper! \033[0m".center(60, "+"))
print("=" * 51)

# Ask the name of the user to create a greeting
name = input("\033[34mHi Smart Pipol! what is your name?\033[0m")
print(f"\033[33m\nHello, {name}! Let's put together the pieces of your life story!\033[0m")
print("\033[33mStart typing and press Enter after each line to add it.\033[0m")
print("\033[33mWhen you're done, your story will be saved to a file.\n\033[0m")

# Make a function def method
def multiple_line():
    # Make a file called "mylife.txt" and give it permission to be written to with the "write" command. 
    with open('mylife.txt', 'w') as input_file:
        # Loop over the code using a while statement.
        while True:
            # ask the user to input a line
            line = input("\033[35mEnter line: \033[0m")

            # Use the random module to inject some random encouragement.
            encouragements = ["Great job!", "Keep pushing!", "Never give up!", "You're doing great!", "You've got this!", "There you go!"]
            print(random.choice(encouragements))

            # The "write" method of the file object will be used to save the line of text to the file, followed by a newline character (\n).
            input_file.write(line + '\n')
            # Ask if the user wants to add more lines by asking y/n.
            add_lines = input('\033[34mAre there more lines y/n? \033[0m')
            # If n, then break the code.
            # use lower() function to convert the character into lowercase
            if add_lines.lower() == 'n':
                print(f"\n\033[32mYour life story has been written down and stored as '{name}_life.txt'! We appreciate you telling us your story!\n\033[0m")
                closing = pyfiglet.figlet_format("Thank you for using AritzMetic's Story Keeper. Have a nice day!", font="puffy")
                print(closing)
                break
            
# call the method to run the code
multiple_line()