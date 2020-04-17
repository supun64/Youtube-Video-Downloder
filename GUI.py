from tkinter import *
from PIL import ImageTk, Image

root = Tk()
root.title("YouTube Video Downloader")

title_icon = ImageTk.PhotoImage(Image.open("title_logo.png"))
title_label = Label(root, image=title_icon)
title_label.grid(row=0, column=0, columnspan=2)

label_description = Label(root, text="!!!!YOUTUBE VIDEO DOWNLOADER!!!!", fg='#D80707', padx=100, pady =20)
label_description.config(font=("Courier", 27))
label_description.grid(row=1, column=0, pady=20, columnspan = 2)

link = Entry(root, width=50)
link_label = Label(root, text="Enter The URL:", padx=50)
link_label.config(font=("TimesNewRoman",12))
link_label.grid(row=2, column=0, sticky=E, pady=3)
link.grid(row=2, column=1, sticky=W, pady=3)

path = Entry(root, width=50)
path_label = Label(root, text="Enter The Path You Want To Save The Video:", padx=50)
path_label.config(font=("TimesNewRoman", 12))
path_label.grid(row=3, column=0, sticky=E, pady=3)
path.grid(row=3, column=1, sticky=W, pady=3)

path_browser = Button(text='Browse', borderwidth=3, font=("TimesNewRoman", 12))
path_browser.grid(row=4, column=1, sticky=W)

download = Button(text='DOWNLOAD', font=("TimesNewRoman", 18), borderwidth=5, padx=20, pady=10, bg="#3AEE60")
download.grid(row=5, column=0, columnspan=3, pady=20)


mainloop()
