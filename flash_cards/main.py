from tkinter import *
import pandas
import random

BACKGROUND_COLOR = "#B1DDC6"
current_card = {}
to_learn = {}

try:
    data = pandas.read_csv("flash_cards/data/words_to_learn.csv")
except FileNotFoundError:
    original_data = pandas.read_csv("flash_cards/data/spanish_words.csv")    
    to_learn = original_data.to_dict(orient="records")
else:
    to_learn = data.to_dict(orient="records")


def next_card():
    global current_card
    current_card = random.choice(to_learn)
    canvas.itemconfig(card_title, text="Hiszpański", fill="black")
    canvas.itemconfig(card_word, text=current_card["Spanish"], fill="black")
    canvas.itemconfig(card_image, image=card_front_image)


def is_known():
    to_learn.remove(current_card)
    df = pandas.DataFrame(to_learn)
    df.to_csv("flash_cards/data/words_to_learn.csv", index=False)
    next_card()
    

def flip_card(event):
    global current_card
    if canvas.itemcget(card_title, "text") == "Hiszpański":
        canvas.itemconfig(card_title, text="Polski", fill="white")
        canvas.itemconfig(card_word, text=current_card["Polish"], fill="white")
        canvas.itemconfig(card_image, image=card_back_image)
    else:
        canvas.itemconfig(card_title, text="Hiszpański", fill="black")
        canvas.itemconfig(card_word, text=current_card["Spanish"], fill="black")
        canvas.itemconfig(card_image, image=card_front_image)
 
window = Tk()
window.config(bg=BACKGROUND_COLOR, padx=50, pady=50)
window.title("Flash Card")

canvas = Canvas(width=800, height=526)
card_front_image = PhotoImage(file="flash_cards/images/card_front.png")
card_back_image = PhotoImage(file="flash_cards/images/card_back.png")
card_image = canvas.create_image(400, 263, image=card_front_image)
card_title = canvas.create_text(400, 150, text="", font=("ariel", 40, "italic"))
card_word = canvas.create_text(400, 263, text="", font=("ariel", 60, "bold"))
canvas.config(bg=BACKGROUND_COLOR, highlightthickness=0)
canvas.bind("<Button-1>", func=flip_card)
canvas.grid(column=0, row=0, columnspan=2)

right_button_image = PhotoImage(file=r"flash_cards\images\right.png")
wrong_button_image = PhotoImage(file=r"flash_cards\images\wrong.png")

right_button = Button(image=right_button_image, highlightthickness=0, borderwidth=0, command=is_known)
right_button.grid(column=1, row=1)

wrong_button = Button(image=wrong_button_image, highlightthickness=0, borderwidth=0, command=next_card)
wrong_button.grid(column=0, row=1)

next_card()

window.mainloop()