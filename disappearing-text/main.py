from tkinter import *

counter = 0

root = Tk()
root.title('Disappearing text writing')
root.config(padx=30, pady=20)
root.minsize(600, 600)


def check():
    global counter, text
    if text == text_field.get(1.0, END):
        if counter == 9:
            text_field.delete(1.0, END)
            counter = 0
        root.after(1000, check)
        counter += 1
    else:
        root.after(1000, check)
        text = text_field.get(1.0, END)
        counter = 0


def save():
    text_to_save = text_field.get(1.0, END)
    with open('text.txt', 'w') as file:
        file.write(text_to_save)


text = ''
text_field = Text(height=30, width=70)
text_field.focus()
text_field.grid(column=0, row=0)

save_button = Button(text="Save", command=save)
save_button.grid(column=0, row=1)


root.after(1000, check)
root.mainloop()