
import tkinter as tk
import random

# Create the GUI window
win = tk.Tk()
win.geometry("750x750")
win.title("PythonGeeks - Number Guessing Game")

# Initialize game variables BEFORE creating widgets
num = random.randint(1, 50)
score = 5
game_over = False

guess = tk.StringVar()
hint = tk.StringVar()
final_score = tk.StringVar(value=str(score))

hint.set("Guess a number between 1 and 50")

# Function to check the guess
def fun():
    global score, game_over

    if game_over:
        return

    try:
        x = int(guess.get())
    except ValueError:
        hint.set("Please enter a valid number!")
        return

    # Validate the range
    if x < 1 or x > 50:
        hint.set("Enter a number between 1 and 50!")
        return

    # Check the guess
    if x == num:
        hint.set("Congratulations! YOU WON!!!")
        game_over = True
        check_button.config(state=tk.DISABLED)

    else:
        score -= 1
        final_score.set(str(score))

        if score == 0:
            hint.set(f"Game over! The number was {num}.")
            game_over = True
            check_button.config(state=tk.DISABLED)

        elif x < num:
            hint.set("Your guess was too low! Guess higher.")

        else:
            hint.set("Your guess was too high! Guess lower.")

    guess.set("")

# Heading
tk.Label(
    win,
    text="I challenge you to guess the number!",
    font=("Courier", 22)
).place(relx=0.5, rely=0.09, anchor=tk.CENTER)

# Guess entry
tk.Entry(
    win,
    textvariable=guess,
    width=5,
    font=("Ubuntu", 35),
    justify="center"
).place(relx=0.5, rely=0.30, anchor=tk.CENTER)

# Check button
check_button = tk.Button(
    win,
    width=8,
    text="CHECK",
    font=("Courier", 25),
    command=fun,
    relief=tk.GROOVE,
    bg="light blue"
)
check_button.place(relx=0.5, rely=0.5, anchor=tk.CENTER)

# Hint display
tk.Entry(
    win,
    textvariable=hint,
    width=50,
    font=("Courier", 13),
    relief=tk.GROOVE,
    bg="orange",
    justify="center"
).place(relx=0.5, rely=0.7, anchor=tk.CENTER)

# Score label
tk.Label(
    win,
    text="Score out of 5",
    font=("Courier", 20)
).place(relx=0.3, rely=0.85, anchor=tk.CENTER)

# Score display
tk.Entry(
    win,
    textvariable=final_score,
    width=3,
    font=("Ubuntu", 24),
    justify="center",
    state="readonly"
).place(relx=0.65, rely=0.85, anchor=tk.CENTER)

# Start the GUI
win.mainloop()
