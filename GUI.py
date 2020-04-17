from tkinter import *
from PIL import ImageTk, Image

root = Tk()
root.title("YouTube Video Downloader")
root.iconbitmap("img\\icon.ico")

back_color = "#000000"
f_color = "#FFFFFF"
logo_color = "#5B0303"

main_frame = LabelFrame(root, bd=3, relief=SOLID, padx=10, pady=10, bg=back_color, fg=f_color)
main_frame.pack(padx=5, pady=5, anchor='center')

logo_frame = LabelFrame(main_frame, bd=2, relief="ridge", bg=logo_color)
logo_frame.grid(row=0, column=0, columnspan=3, pady=10)

# This is the code to add the LoneWolf Logo
title_icon = ImageTk.PhotoImage(Image.open("img\\title_logo.png"))
title_label = Label(logo_frame, image=title_icon, bg=logo_color)
title_label.grid(row=0, column=0, columnspan=2, pady=10)

# This is the code to add the description
label_description = Label(logo_frame, text="!!!!YOUTUBE VIDEO DOWNLOADER!!!!", fg='#FFF300', padx=100, pady=20, bg=logo_color)
label_description.config(font=("Courier", 27))
label_description.grid(row=1, column=0, pady=20, columnspan=2)

# This is the code to add the URL entry and label
link = Entry(main_frame, width=50)
link_label = Label(main_frame, text="Enter The URL:", padx=50, anchor=E, bg=back_color, fg=f_color)
link_label.config(font=("TimesNewRoman", 12))
link_label.grid(row=3, column=0, pady=3, sticky=W+E)
link.grid(row=3, column=1, sticky=W, pady=3)

# This is the code to add Browser path entry and label
path = Entry(main_frame, width=50)
path_label = Label(main_frame, text="Enter The Path You Want To Save The Video:", padx=50, anchor=E, bg=back_color, fg=f_color)
path_label.config(font=("TimesNewRoman", 12))
path_label.grid(row=4, column=0, sticky=W+E, pady=3)
path.grid(row=4, column=1, sticky=W, pady=3)

# This is the code to browser button
path_browser = Button(main_frame, text='Browse', borderwidth=3, font=("TimesNewRoman", 12))
path_browser.grid(row=5, column=1, sticky=W)

# This is the code to download button
download = Button(main_frame, text='DOWNLOAD', font=("TimesNewRoman", 18), borderwidth=5, padx=20, pady=10, bg="#27F316")
download.grid(row=6, column=0, columnspan=3, pady=20)


mainloop()
