from tkinter import *
from moviepy.editor import *
from pytube import YouTube
from time import time
import os


def main():
    window = Tk()
    path = os.path.join(os.path.join(os.environ["HOME"]), 'hydownloads') # Define the path
    os.makedirs(path, exist_ok=True) # Create folder if it doesn't exist already


    window.geometry('600x150')
    window.resizable(False, False)
    window.configure(bg="#222222")
    window.title('''Haukur's YouTube Downloader''')
    link = StringVar()
    linkInputBox = Entry(window, # Textbox that you paste your link into e.g. https://www.youtube.com/watch?v=ZZ5LpwO-An4
                width=55,
                bg="#222222",
                fg="#EDEDED",
                highlightbackground="#000000",
                highlightthickness=3,
                text="link",
                textvariable=link)
    likeTextLabel = Label(window, # Text label attribute which leads you the way to the paste textbox
                width=5,
                height=1,
                bg="#222222",
                fg="#EDEDED",
                text="← Link")
    downloadButtonMP4 = Button(window, # MP4 download button
                width=12,
                height=1,
                text="Download MP4",
                font=("UbuntuMono", 13),
                bg="#910000",
                fg="#111111",
                border=False,
                activebackground="#750000",
                command=lambda: download(link.get(), False))
    downloadButtonMP3 = Button(window, # MP3 download button
                width=12,
                height=1,            
                text="Download MP3",
                font=("UbuntuMono", 13),
                bg="#910000",
                fg="#111111",
                border=False,
                activebackground="#750000",
                command=lambda: download(link.get(), True))

    # Window attribute locations and dimensions
    linkInputBox.place(relx=0.5, rely=0.45, anchor=CENTER)
    likeTextLabel.place(relx=0.87, rely=0.45, anchor=CENTER)
    downloadButtonMP4.place(relx=0.37, rely=0.7, anchor=CENTER)
    downloadButtonMP3.place(relx=0.63, rely=0.7, anchor=CENTER)


    def download(link, mp3IsClicked):
        print(f"The video link is {link}")
        print(f"Mp3 button was pushed: {mp3IsClicked}")
        try:
            fixedTitle = YouTube(link).title
            unwantedChars = ".$'%"
            print("Removing unwanted characters from final file name...")
            for char in unwantedChars: # Removes unwanted characters from final file name to avoid errors
                print(f"Removed {char} from final file name...")
                fixedTitle = fixedTitle.replace(char, "")
            print("Finished removing unwanted characters!\nStarting time...")
            startTime = time()
            print("Downloading video...")
            YouTube(link).streams.get_highest_resolution().download(path) # Downloads video
            if os.path.exists(f"{path}/{fixedTitle}.mp4") and mp3IsClicked:
                print("Mp3IsClicked is true; downloading converting mp4 download to mp3 download...")
                video = VideoFileClip(f"{path}/{fixedTitle}.mp4")
                os.remove(f"{path}/{fixedTitle}.mp4")
                video.audio.write_audiofile(f"{path}/{fixedTitle}.mp3")
                mp3IsClicked = False  
            endTime = time()
            print(f"Download success! Final Time was {endTime-startTime,3}")        
            popup = Tk()
            popup.title("Download Success!")
            popup.geometry("350x125")
            popup.resizable(False, False)
            popup.configure(bg="#222222")
            popupLabel = Label(popup, text=f"Successfuly downloaded video at \n{path}.\nTotal time taken: {round(endTime-startTime,3)} seconds", fg="#EDEDED", bg="#222222")
            popupLabel.place(relx=0.5, rely=0.25, anchor=CENTER)
            popup.mainloop()
        except:
            print("Download failed :/")        
            error = Tk()
            error.title("Download Failed :/")
            error.geometry("350x125")
            error.resizable(False, False)
            error.configure(bg="#222222")
            errorLabel = Label(error, text="Download Failed :/ \n Please check your internet connection \n Maybe try updating your pip packages.",  fg="#EDEDED", bg="#222222")
            errorLabel.place(relx=0.5, rely=0.25, anchor=CENTER)
            error.mainloop()
            
    window.mainloop()
if __name__ == '__main__':
    main()