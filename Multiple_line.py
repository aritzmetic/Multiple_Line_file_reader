# Delera, Aritz B.

# Write a method in python to write multiple line of text contents into a text file mylife.txt. See sample output:
# Enter line: Beautiful is better than ugly.
# Are there more lines y/n? y
# Enter line: Explicit is better than implicit.
# Are there more lines y/n? y
# Enter line: Simple is better than complex.
# Are there more lines y/n? n 

# Make a function def method
def multiple_line():
    # Make a file called "mylife.txt" and give it permission to be written to with the "write" command. 
    with open('mylife.txt', 'w') as input_file:
        # Loop over the code using a while statement.
        while True:
            # ask the user to input a line
            line = input("Enter line: ")
            # The "write" method of the file object will be used to save the line of text to the file, followed by a newline character (\n).
            input_file.write(line + '\n')
            # Ask if the user wants to add more lines by asking y/n.
            add_lines = input('Are there more lines y/n? ')
            # If n, then break the code.
            # use lower() function to convert the character into lowercase
            if add_lines.lower() == 'n':
                
# call the method to run the code