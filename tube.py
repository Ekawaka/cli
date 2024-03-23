from pytube import YouTube
import tkinter  
import customtkinter

# To download youtube video 
def StartDownload():

    # To handle errrors and exceptions we use try and except blocks with except Exception as e.
    try:
        ytlink = link.get()
        ytObject = YouTube(ytlink) 
        video = ytObject.streams.get_highest_resolution() # To download the highest resolution.
        video = ytObject.streams.get_audio_only()
        video.download()

    except:
        print("YouTube link is invalid")
    print("Download Completed successfully!")
        
#app frame
app = customtkinter.CTk()
app.geometry("720*480")
app.title("YouTube Downloader")

#add UI elements
title = customtkinter.CTkLabel(app, text="Insert a youtube link")
title.pack(padx=0, pady=0)

#link input
url_var = tkinter.StringVar()
link = customtkinter.CTkEntry(app, width=400, height=50, textvariable=url_var)
link.pack()

#Download Button
download = customtkinter.CTkButton(app, text = "Download", command=StartDownload)
download.pack(padx=0, pady=0)

#Run app
app.mainloop()