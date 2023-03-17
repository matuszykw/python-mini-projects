from tkinter import *
import pandas

BACKGROUND_COLOR = "#B1DDC6"

window = Tk()
window.config(bg=BACKGROUND_COLOR, padx=50, pady=50)
window.title("Flash Card")

canvas = Canvas(width=800, height=526)
card_front_image = PhotoImage(file="flash_cards/images/card_front.png")
canvas.create_image(400, 263, image=card_front_image)
canvas.create_text(400, 150, text="Title", font=("ariel", 40, "italic"))
canvas.create_text(400, 263, text="Word", font=("ariel", 60, "bold"))
canvas.config(bg=BACKGROUND_COLOR, highlightthickness=0)
canvas.grid(column=0, row=0, columnspan=2)

right_button_image = PhotoImage(file=r"flash_cards\images\right.png")
wrong_button_image = PhotoImage(file=r"flash_cards\images\wrong.png")

right_button = Button(image=right_button_image, highlightthickness=0, borderwidth=0)
right_button.grid(column=1, row=1)

wrong_button = Button(image=wrong_button_image, highlightthickness=0, borderwidth=0)
wrong_button.grid(column=0, row=1)







window.mainloop()