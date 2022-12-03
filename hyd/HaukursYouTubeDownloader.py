from tkinter import *
from moviepy.editor import *
from pytube import YouTube
from time import time
import os

def main():
    window = Tk()
    path = os.path.join(os.path.join(os.environ["HOME"]), 'YoutubeDownloads') # Make path
    os.makedirs(path, exist_ok=True) # Create folder if it doesn't exist already
    start_time = 0 # Start time
    end_time = 0 # Stop time
    mp3IsClicked = False

    # The window itself
    window.geometry('600x150')
    window.resizable(False, False)
    window.configure(bg="#222222")
    window.title('''Haukur's YouTube Downloader''') # Title in the fixedtitle bar

    # Paste label
    link = StringVar()
    pasteModule = Entry(window,
                width=55,
                bg="#222222",
                fg="#EDEDED",
                highlightbackground="#000000",
                highlightthickness=3,
                text="link",
                textvariable=link)
    pasteLabel = Label(window,
                width=5,
                height=1,
                bg="#222222",
                fg="#EDEDED",
                text="← Link")

    # Download button
    downloadButtonMP4 = Button(window,
                width=12,
                height=1,
                text="Download MP4",
                font=("UbuntuMono", 13),
                bg="#910000",
                fg="#111111",
                border=False,
                activebackground="#750000",
                command=lambda: download(link.get()))
    downloadButtonMP3 = Button(window,
                width=12,
                height=1,            
                text="Download MP3",
                font=("UbuntuMono", 13),
                bg="#910000",
                fg="#111111",
                border=False,
                activebackground="#750000",
                command=lambda: mp3IsClickedFunction())

    # Locations
    pasteModule.place(relx=0.5, rely=0.45, anchor=CENTER)
    pasteLabel.place(relx=0.87, rely=0.45, anchor=CENTER)
    downloadButtonMP4.place(relx=0.37, rely=0.7, anchor=CENTER)
    downloadButtonMP3.place(relx=0.63, rely=0.7, anchor=CENTER)


    def mp3IsClickedFunction():
        global mp3IsClicked
        mp3IsClicked = True
        download(link.get())

    def download(link):
        try:
            fixedtitle = YouTube(link).title
            unwanted_chars = ".$'%"
            for char in unwanted_chars:
                fixedtitle = fixedtitle.replace(char, "")
            start_time = time()
            YouTube(link).streams.get_highest_resolution().download(path)
            if os.path.exists(f"{path}/{fixedtitle}.mp4") and mp3IsClicked == True:
                video = VideoFileClip(f"{path}/{fixedtitle}.mp4")
                os.remove(f"{path}/{fixedtitle}.mp4")
                video.audio.write_audiofile(f"{path}/{fixedtitle}.mp3")
            end_time = time()
            mp3IsClicked == False
            popup = Tk()
            popup.title("Download Success!")
            popup.geometry("350x125")
            popup.resizable(False, False)
            popup.configure(bg="#333333")
            popupLabel = Label(popup, text=f"Successfuly downloaded video at \n{path}.\nTotal time taken: {round(end_time-start_time,3)} seconds", fg="#EDEDED", bg="#333333")
            popupLabel.place(relx=0.5, rely=0.25, anchor=CENTER)
            popup.mainloop()
        except:
            error = Tk()
            error.title("Download Failed :/")
            error.geometry("350x125")
            error.resizable(False, False)
            error.configure(bg="#333333")
            errorLabel = Label(error, text="Download Failed :/ \n Please check your internet connection.",  fg="#EDEDED", bg="#333333")
            errorLabel.place(relx=0.5, rely=0.25, anchor=CENTER)
            error.mainloop()

    window.mainloop()
if __name__ == '__main__':
  main()
