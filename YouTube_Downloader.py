import tkinter as tk # used to create a graphical user interface
from pytube import YouTube

def StartDownload(): # To create a function

    try:    # Try to get the video and download
        ytlink = link.get()
        ytObject = YouTube(ytlink) 
        video = ytObject.streams.get_highest_resolution() # To download the highest resolution.
        video.download()
    # To handle errrors and exceptions we use try and except blocks
    except:
        print("YouTube link is invalid")
    print("Download Completed successfully!")

# To create Frame of the user interface
root = tk.Tk()  # To initialize the frame
root.geometry("500x300") # To set the size or resolution of the frame
root.title("YouTube Downloader") # To set the title of the frame

# To add user interface elements
label = tk.Label(root, text="Insert a youtube link") # To create where to be inserting the links
label.pack(padx=10, pady=10) # This is to enable the element to show on the frame

#To creat link input
url_var = tk.StringVar() # This is used to pass the url variable
link = tk.Entry(root, textvariable=url_var)
link.pack()

#To create Download Button
download = tk.Button(root, text = "Download", command=StartDownload) #This helps to put a text on the frame 
#and pass a command function 
download.pack(padx=10, pady=10) # To show the download Button on the frame

# To run 
root.mainloop() # To ensure you are directly running the python file before it executes anything that happens under this.
    # This is because  there could be files that are reused by another file.
