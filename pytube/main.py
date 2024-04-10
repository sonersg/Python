

# python3 -m venv pytube.venv
# source pytube.venv/bin/activate
# pip install customtkinter
# pip install pytube
# deactivate

import tkinter
import customtkinter
from pytube import YouTube
from pytube.exceptions import RegexMatchError, VideoUnavailable

# on_progress function
def on_progress(stream, chunk, bytes_remaining):
    total_size = stream.filesize
    print(total_size)
    bytes_downloaded = total_size - bytes_remaining
    percentage_of_completion = bytes_downloaded / total_size * 100
    per = str(int(percentage_of_completion))
    pp.configure(text=per + "%")
    pp.update()
    progress_bar.set(percentage_of_completion / 100)

# start_download function
def start_download():
    try:
        finish_label.configure(text="", text_color="white")
        ytlink = inpt.get()
        ytobject = YouTube(ytlink, on_progress_callback=on_progress)
        label.configure(text=ytobject.title)
        audio = ytobject.streams.get_audio_only()
        audio.download()
        # video = ytobject.streams.get_highest_resolution()
        # video.download()
        finish_label.configure(text="Download complete!", text_color="green")
    except RegexMatchError as e:
        finish_label.configure(text="Invalid YouTube link!", text_color="red")
    except VideoUnavailable as e:
        finish_label.configure(text="Video is unavailable!", text_color="red")
    except Exception as e:
        finish_label.configure(text="An error occurred: " + str(e), text_color="red")

# System Settings
customtkinter.set_appearance_mode("System")
customtkinter.set_default_color_theme("blue")

# App Frame
app = customtkinter.CTk()
app.geometry("720x480")
app.title("Youtube Downloader")

# UI Elements
label = customtkinter.CTkLabel(app, text="Insert a youtube link...")
label.pack(padx=10, pady=20)

query = tkinter.StringVar()
inpt = customtkinter.CTkEntry(app, width=350, height=30, textvariable=query)
inpt.pack()

download_btn = customtkinter.CTkButton(app, text="Download", command=start_download)
download_btn.pack(pady=10)

finish_label = customtkinter.CTkLabel(app, text="")
finish_label.pack(pady=50)

pp = customtkinter.CTkLabel(app, text="0%")
pp.pack()

progress_bar = customtkinter.CTkProgressBar(app, width=400)
progress_bar.set(0)
progress_bar.pack(pady=10)

# Run App
app.mainloop()

