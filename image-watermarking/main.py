from tkinter import *
from tkinter import filedialog as fd
from PIL import Image, ImageDraw, ImageFont
from tkinter.messagebox import showinfo
import os

root = Tk()
root.title("Image watermarking")
root.geometry('300x300')
    
def save_image(img, filename):
    name, extension = os.path.splitext(filename)
    save_filename = fd.asksaveasfilename(defaultextension=extension, filetypes=[("Files", f"*{extension}"), ("All files", "*.*")])
    img = img.convert('RGB')
    img.save(save_filename)

def open_watermark():
    filetypes = (
        ('image files', "*.jpg;*.png;*.gif"),
        ('all_files', '*.*')
    )
    
    filename = fd.askopenfilename(
        title = 'Open a file',
        initialdir = '/',
        filetypes=filetypes
    )
    
    if filename:
        wm_img = Image.open(filename).convert('RGBA')
        open_watermark_button.destroy()
        open_button = Button(
            root,
            text='Select Image',
            command=lambda: select_file(wm_img)
        )
        open_button.pack(expand=True)
        

def select_file(wm_img):
    filetypes = (
        ('image files', "*.jpg;*.png;*.gif"),
        ('all_files', '*.*')
    )
    
    filename = fd.askopenfilename(
        title = 'Open a file',
        initialdir = '/',
        filetypes=filetypes
    )
    
    if filename:
        img = Image.open(filename).convert('RGBA')
        
        alpha = 0.3
        wm_img = wm_img.resize(img.size)
        
        img_w_wm = Image.blend(img, wm_img, alpha)
        
        save_button = Button(
            root,
            text='Save Image',
            command=lambda: save_image(img_w_wm, filename)
        )
        save_button.pack(expand=True)

open_watermark_button = Button(
    root,
    text='Select Watermark',
    command=open_watermark
)
open_watermark_button.pack(expand=True)

root.mainloop()