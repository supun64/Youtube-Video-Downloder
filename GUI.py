from tkinter import *
from PIL import ImageTk, Image
import pytube
from tkinter import filedialog


def get_details(stream):
    """
    This is the code to get the useful video details from th URL
    :param stream: The video stream comtaining details as a string
    :return: dictionary of useful details
    """
    v_list = str(stream).split()
    v_list.pop(0)
    v_list.pop()
    details = {}
    for x in v_list:
        details[x[:x.index("=")]] = eval(x[x.index("=") + 1:])

    return details


def video_quality(sample_video):
    end_dialog_box = False


    # This is the code to create the new dialogue box to get the users choice of video quality
    format_window = Tk()
    format_window.title("Select The File Format To Download.")
    format_window.iconbitmap("img\\icon.ico")
    format_frame = LabelFrame(format_window, bd=2, padx=5, pady=5, bg="#C7C7C2", relief="ridge")
    format_frame.pack(padx=5, pady=5)

    v = IntVar(format_frame)  # in here we have to specify in which frame is this variable contains


    while True:
        def button_clicked():
            global end_dialog_box
            end_dialog_box = True

        # This is the code to create radio boxes
        for index, v_format in enumerate(sample_video):
            video_details = get_details(v_format)
            label_radio = '\t'.join(['Resolution : ' + video_details['res'], 'Format : ' + video_details['mime_type'],
                                     'FPS : ' + video_details['fps']])

            Radiobutton(format_frame, text=label_radio, font=('Courier', 12),
                        variable=v, value=index, pady=5, fg="#000000", bg="#C7C7C2").pack(padx=10, pady=10)

        # This is the define of the button
        Button(format_frame, text="Start Download", font=("Courier", 15), borderwidth=3,
               command=button_clicked, bg="#76EE68").pack(pady=10)

        if end_dialog_box:
            final_value = v.get()
            format_window.destroy()
            return final_value


def download_video(download_url, download_path):
    """
    This will download a single video
    :param download_url: The url of the youtube video
    :param download_path: directory you want to save the video
    :return: if playlist_down user choice video quality else None
    """
    video_link = pytube.YouTube(download_url)
    video = video_link.streams.filter(progressive=True)

    value = video_quality(video)

    video[value].download(download_path.replace("\\", '\\\\'))
    message("The Download Is Complete.", "Success", "img//success.ico")


def download_playlist(playlist_url, playlist_path):
    """
    This is the function to download a playlist
    :param playlist_url: URL of the playlist
    :param playlist_path: Download directory
    :return: None
    """
    playlist = pytube.Playlist(playlist_url)
    video_link = pytube.YouTube(playlist[0])
    video = video_link.streams.filter(progressive=True)
    user_quality = video_quality(video)

    for each_video in playlist:
        each_video_link = pytube.YouTube(each_video)
        reduced_video = video_link.streams.filter(progressive=True)

        # We use this exception if there are no such value in video we get the best first stream
        try:
            # reduced_video[user_quality].download(playlist_path.replace("\\", "\\\\"))
            print(user_quality)

        except:
            # reduced_video.first().download(playlist_path.replace("\\", "\\\\"))
            pass

    message("The Download Is Complete.", "Success", "img//success.ico")


def message(context, title_name="Error", icon="img\\error.ico"):
    """
    This is a function to pop up a message
    :param context: Message body
    :param title_name: Message title
    :param icon: Icon of the messsage the default vallue is assigned to a icon of a error message
    :return: None
    """
    message_box = Tk()
    message_box.title(title_name)
    message_box.iconbitmap(icon)

    error_frame = LabelFrame(message_box, bd=1, relief=SOLID)
    error_frame.pack(padx=5, pady=5)

    Label(error_frame, text=context, anchor=W, justify=LEFT, padx=20).grid(row=0, column=0, padx=10, pady=10)
    cmd_btn = Button(error_frame, text="OK", command=message_box.destroy, width=10)
    cmd_btn.grid(row=1, column=0, padx=10, pady=10, sticky=E)


def download_cmd(download_type):
    """
    This is the function for download button in root window
    :param download_type: if video download or a playlist download
    :return: None
    """
    if link.get() == "":
        message("Invalid URL input!!!\n"
                "\tYou should enter the URL for the video\n"
                "that you need to download.")

    elif path.get() == "":
        message("Invalid PATH input!!!\n"
                "\tYou should enter the path of the folder\n"
                "that you need to save the video.")

    else:
        try:
            if download_type == 1:
                download_video(link.get(), path.get())
            else:
                download_playlist(link.get(), path.get())
        except:
            message("Unexpected Error\n"
                    "check your download link. and Download path")

        finally:
            link.delete(0, len(link.get()))
            path.delete(0, len(path.get()))


def browser_btn():
    """
    This is the function to browser button
    :return:
    """
    browser_box = Tk()
    browser_box.withdraw()
    browser_box.filename = filedialog.askdirectory(initialdir="C:\\", title="Select Download Directory")
    path.delete(0, len(path.get()))
    path.insert(0, str(browser_box.filename))

    browser_box.destroy()


# The root code starts here
root = Tk()
root.title("YouTube Video Downloader")
root.iconbitmap("img\\icon.ico")

# These are some color variables
back_color = "#000000"
f_color = "#FFFFFF"
logo_color = "#5B0303"

# These are Label frames we created to group the context
main_frame = LabelFrame(root, bd=3, relief=SOLID, padx=10, pady=10, bg=back_color, fg=f_color)
main_frame.pack(padx=5, pady=5, anchor='center')

logo_frame = LabelFrame(main_frame, bd=2, relief="ridge", bg=logo_color)
logo_frame.grid(row=0, column=0, columnspan=3, pady=10)

# This is the code to add the LoneWolf Logo
title_icon = ImageTk.PhotoImage(Image.open("img\\title_logo.png"))
title_label = Label(logo_frame, image=title_icon, bg=logo_color)
title_label.grid(row=0, column=0, columnspan=2, pady=10)

# This is the code to add the description
label_description = Label(logo_frame, text="!!!!YOUTUBE VIDEO DOWNLOADER!!!!",
                          fg='#FFF300', padx=100, pady=20, bg=logo_color)
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
path_label = Label(main_frame, text="Enter The Path You Want To Save The Video:",
                   padx=50, anchor=E, bg=back_color, fg=f_color)
path_label.config(font=("TimesNewRoman", 12))
path_label.grid(row=4, column=0, sticky=W+E, pady=3)
path.grid(row=4, column=1, sticky=W, pady=3)

# This is the code to browser button
path_browser = Button(main_frame, text='Browse', borderwidth=3, font=("TimesNewRoman", 12), command=browser_btn)
path_browser.grid(row=5, column=1, sticky=W)

# This is the code to choose from video download and playlist download
r = IntVar(main_frame)
r.set(0)
Radiobutton(main_frame, text="One Video Download", variable=r, value=1, bd=4, relief=SUNKEN,
            fg="#000000", bg="#63635F", font=("TimesNewRoman", 12), anchor=E).grid(row=6, column=0, pady=5, sticky=E)
Radiobutton(main_frame, text="Playlist Download", variable=r, value=2, bd=4, relief=SUNKEN,
            fg="#000000", bg="#63635F", font=("TimesNewRoman", 12), anchor=W).grid(row=6, column=1, pady=5, sticky=W)

# This is the code to download button
download = Button(main_frame, text='DOWNLOAD', font=("TimesNewRoman", 18), command=lambda: download_cmd(r.get()),
                  borderwidth=5, padx=20, pady=10, bg="#27F316")
download.grid(row=7, column=0, columnspan=3, pady=20)

mainloop()
