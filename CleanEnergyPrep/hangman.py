import turtle
import random

# Set up the screen
screen = turtle.Screen()
screen.title("Hangman")
screen.bgcolor("white")
screen.setup(800, 600)
screen.tracer(0)

# Set up the turtle
pen = turtle.Turtle()
pen.speed(0)
pen.penup()
pen.hideturtle()
pen.goto(-200, 0)

# Word bank
words = ["python", "hangman", "game", "programming", "computer", "code", "challenge", "fun"]

# Select a random word from the word bank
word = random.choice(words)

# Create a list to store the guessed letters
guessed_letters = []

# Function to draw the hangman
def draw_hangman(attempts):
    if attempts == 1:
        # Draw the gallows
        pen.pendown()
        pen.forward(200)
        pen.backward(100)
        pen.left(90)
        pen.forward(300)
        pen.left(90)
        pen.forward(100)
        pen.left(90)
        pen.forward(30)
    elif attempts == 2:
        # Draw the head
        pen.penup()
        pen.goto(-70, 150)
        pen.pendown()
        pen.circle(30)
    elif attempts == 3:
        # Draw the body
        pen.penup()
        pen.goto(-70, 120)
        pen.pendown()
        pen.forward(100)
    elif attempts == 4:
        # Draw the left arm
        pen.penup()
        pen.goto(-70, 100)
        pen.pendown()
        pen.left(45)
        pen.forward(60)
    elif attempts == 5:
        # Draw the right arm
        pen.penup()
        pen.goto(-70, 100)
        pen.pendown()
        pen.right(90)
        pen.forward(60)
    elif attempts == 6:
        # Draw the left leg
        pen.penup()
        pen.goto(-70, 20)
        pen.pendown()
        pen.left(45)
        pen.forward(60)
    elif attempts == 7:
        # Draw the right leg
        pen.penup()
        pen.goto(-70, 20)
        pen.pendown()
        pen.right(90)
        pen.forward(60)

# Function to update the word display
def update_word_display():
    display = ""
    for letter in word:
        if letter in guessed_letters:
            display += letter + " "
        else:
            display += "_ "
    pen.penup()
    pen.goto(-200, -100)
    pen.write(display, align="left", font=("Arial", 24, "normal"))

# Function to handle letter guesses
def guess_letter(letter):
    guessed_letters.append(letter)
    if letter not in word:
        draw_hangman(len(guessed_letters))
    update_word_display()
    check_game_status()

# Function to check the game status
def check_game_status():
    if len(guessed_letters) >= 7:
        game_over("You lost! The word was: " + word)
    elif all(letter in guessed_letters for letter in word):
        game_over("Congratulations! You won!")

# Function to display game over message
def game_over(message):
    pen.penup()
    pen.goto(-200, -200)
    pen.write(message, align="left", font=("Arial", 24, "normal"))

# Function to handle key presses
def handle_keypress(key):
    letter = key.lower()
    if letter.isalpha():
        if letter not in guessed_letters:
            guess_letter(letter)

# Set up keyboard bindings
screen.listen()
screen.onkeypress(handle_keypress, "a")
screen.onkeypress(handle_keypress, "b")
screen.onkeypress(handle_keypress, "c")
screen.onkeypress(handle_keypress, "d")
screen.onkeypress(handle_keypress, "e")
screen.onkeypress(handle_keypress, "f")
screen.onkeypress(handle_keypress, "g")
screen.onkeypress(handle_keypress, "h")
screen.onkeypress(handle_keypress, "i")
screen.onkeypress(handle_keypress, "j")
screen.onkeypress(handle_keypress, "k")
screen.onkeypress(handle_keypress, "l")
screen.onkeypress(handle_keypress, "m")
screen.onkeypress(handle_keypress, "n")
screen.onkeypress(handle_keypress, "o")
screen.onkeypress(handle_keypress, "p")
screen.onkeypress(handle_keypress, "q")
screen.onkeypress(handle_keypress, "r")
screen.onkeypress(handle_keypress, "s")
screen.onkeypress(handle_keypress, "t")
screen.onkeypress(handle_keypress, "u")
screen.onkeypress(handle_keypress, "v")
screen.onkeypress(handle_keypress, "w")
screen.onkeypress(handle_keypress, "x")
screen.onkeypress(handle_keypress, "y")
screen.onkeypress(handle_keypress, "z")

# Draw the initial word display
update_word_display()

# Main game loop
turtle.mainloop()
