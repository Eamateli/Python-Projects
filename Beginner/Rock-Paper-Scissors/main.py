from tkinter import *
import random

# Rock Paper Scissors Game - Version 1: Beginner GUI with Tkinter

# STEP 1: Initialize the main window
root = Tk()  # Create the main window object
root.geometry('400x400')  # Set window size: width=400px, height=400px
root.resizable(0,0)  # Make window non-resizable (width=0, height=0 means fixed size)
root.title('Rock, Paper, Scissors Game')  # Set the window title that appears in title bar
root.config(bg='seashell3')  # Set background color of the entire window

# STEP 2: Create the main title label
# Label widget displays text that users cannot edit
title_label = Label(
    root,  # Parent widget (the main window)
    text='Rock, Paper, Scissors',  # Text to display
    font='arial 20 bold',  # Font family, size, and style
    bg='seashell2'  # Background color of the label
)
title_label.pack()  # Pack the label into the window (automatic positioning)

# STEP 3: Create instruction label
instruction_label = Label(
    root,
    text='Choose any one: rock, paper, scissors',
    font='arial 15 bold',
    bg='seashell2'
)
instruction_label.place(x=20, y=70)  # Place at specific coordinates (x=20px from left, y=70px from top)

# STEP 4: Create input field for user choice
user_take = StringVar()  # StringVar is a special tkinter variable that can be linked to widgets
user_entry = Entry(
    root,
    font='arial 15',  # Font for the text inside the entry
    textvariable=user_take,  # Link this entry to the StringVar so we can get/set its value
    bg='antiquewhite2',  # Background color of the entry field
    width=15  # Width of the entry field in characters
)
user_entry.place(x=90, y=130)  # Position the entry field

# STEP 5: Create result display field
Result = StringVar()  # Another StringVar to store and display the game result
result_entry = Entry(
    root,
    font='arial 10 bold',
    textvariable=Result,  # Link to Result StringVar to display game outcomes
    bg='antiquewhite2',
    width=50,  # Wider field to display longer result messages
    state='readonly'  # Make it read-only so user can't edit the result
)
result_entry.place(x=25, y=250)

# STEP 6: Generate computer's choice
def generate_computer_choice():
    """Generate a random choice for the computer."""
    comp_pick = random.randint(1, 3)  # Generate random number: 1, 2, or 3
    
    # Convert number to choice using if-elif-else
    if comp_pick == 1:
        return 'rock'
    elif comp_pick == 2:
        return 'paper'
    else:  # comp_pick == 3
        return 'scissors'

# STEP 7: Main game logic function
def play():
    """Main function that runs when PLAY button is clicked."""
    
    # Get user's choice from the entry field
    user_pick = user_take.get().lower().strip()  # Get text, convert to lowercase, remove spaces
    
    # Generate computer's choice
    comp_pick = generate_computer_choice()
    
    # Game logic: Determine winner using if-elif statements
    if user_pick == comp_pick:
        # It's a tie - both chose the same thing
        Result.set(f'Tie! You both chose {user_pick}')
    
    elif user_pick == 'rock' and comp_pick == 'paper':
        # Rock vs Paper: Paper wins (paper covers rock)
        Result.set('You lose! Computer chose paper')
    
    elif user_pick == 'rock' and comp_pick == 'scissors':
        # Rock vs Scissors: Rock wins (rock blunts scissors)
        Result.set('You win! Computer chose scissors')
    
    elif user_pick == 'paper' and comp_pick == 'scissors':
        # Paper vs Scissors: Scissors wins (scissors cut paper)
        Result.set('You lose! Computer chose scissors')
    
    elif user_pick == 'paper' and comp_pick == 'rock':
        # Paper vs Rock: Paper wins (paper covers rock)
        Result.set('You win! Computer chose rock')
    
    elif user_pick == 'scissors' and comp_pick == 'rock':
        # Scissors vs Rock: Rock wins (rock blunts scissors)
        Result.set('You lose! Computer chose rock')
    
    elif user_pick == 'scissors' and comp_pick == 'paper':
        # Scissors vs Paper: Scissors wins (scissors cut paper)
        Result.set('You win! Computer chose paper')
    
    else:
        # Invalid input - user didn't enter rock, paper, or scissors
        Result.set('Invalid choice! Please enter: rock, paper, or scissors')

# STEP 8: Reset function
def Reset():
    """Function to clear all fields when RESET button is clicked."""
    Result.set("")  # Clear the result field
    user_take.set("")  # Clear the user input field

# STEP 9: Exit function
def Exit():
    """Function to close the program when EXIT button is clicked."""
    root.destroy()  # This closes the window and stops the program

# STEP 10: Create buttons
# Button widgets create clickable buttons that execute functions when clicked

play_button = Button(
    root,
    font='arial 13 bold',  # Font for button text
    text='PLAY',  # Text displayed on button
    padx=5,  # Horizontal padding inside button
    bg='seashell4',  # Background color of button
    command=play  # Function to call when button is clicked (no parentheses!)
)
play_button.place(x=150, y=190)  # Position the PLAY button

reset_button = Button(
    root,
    font='arial 13 bold',
    text='RESET',
    padx=5,
    bg='seashell4',
    command=Reset  # Calls Reset function when clicked
)
reset_button.place(x=70, y=310)  # Position the RESET button

exit_button = Button(
    root,
    font='arial 13 bold',
    text='EXIT',
    padx=5,
    bg='seashell4',
    command=Exit  # Calls Exit function when clicked
)
exit_button.place(x=230, y=310)  # Position the EXIT button

# STEP 11: Start the GUI event loop
root.mainloop()  # This keeps the window open and responsive to user interactions

# EXPLANATION OF KEY GUI CONCEPTS:
# 
# 1. TKINTER WIDGETS:
#    - Tk(): Main window
#    - Label(): Display text (non-editable)
#    - Entry(): Text input field
#    - Button(): Clickable button
#    - StringVar(): Special variable that links to widgets
#
# 2. LAYOUT METHODS:
#    - pack(): Automatic positioning (top to bottom)
#    - place(): Manual positioning with x,y coordinates
#    - grid(): Table-like positioning (rows and columns)
#
# 3. EVENT-DRIVEN PROGRAMMING:
#    - Functions are called when user clicks buttons
#    - command parameter links buttons to functions
#    - mainloop() waits for user interactions
#
# 4. WIDGET PROPERTIES:
#    - font: Text appearance
#    - bg: Background color
#    - fg: Text color (foreground)
#    - padx/pady: Internal spacing
#    - width/height: Widget size
#
# 5. STRINGVAR EXPLAINED:
#    - Normal variables don't update GUI automatically
#    - StringVar() creates a special variable that GUI can watch
#    - When StringVar changes, connected widgets update automatically
#    - get(): Retrieve the value
#    - set(): Change the value