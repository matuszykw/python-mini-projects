from tkinter import *
from PIL import Image, ImageDraw, ImageFont
from random import randint


def open_image():
    url = url_input.get()
    watermark_text = text_input.get()
    save_url = save_url_input.get()
    img = Image.open(url).convert('RGBA')
    txt = Image.new('RGBA', img.size, (255, 255, 255, 0))
    w, h = img.size
    x, y = 100, int(h/2)
    font = ImageFont.truetype('arial.ttf', 80)
    editable_image = ImageDraw.Draw(txt)
    editable_image.text((x,y), watermark_text, font=font, fill=(255, 255, 255, 35))
    combined = Image.alpha_composite(img, txt)
    print(save_url)
    combined.save(save_url)


window = Tk()
window.title('Image watermarking')
window.config(padx=50, pady=50)

url_label = Label(text="Image URL: ")
url_label.grid(column=0, row=0)
url_input = Entry()
url_input.grid(column=1, row=0)

text_label = Label(text="Text: ")
text_label.grid(column=0, row=1)
text_input = Entry()
text_input.grid(column=1, row=1)

save_url_label = Label(text="Save URL: ")
save_url_label.grid(column=0, row=2)
save_url_input = Entry()
save_url_input.grid(column=1, row=2)

submit = Button(text="Submit", command=open_image)
submit.grid(column=0, row=4, columnspan=2)





window.mainloop()