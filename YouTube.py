from pytube import YouTube
import tkinter as tk 
from tkinter import  filedialog # used to get directory of where to save the file.

# To download youtube video  we need the url and the path where we are going to save the video.
def download_video(url, save_path):

    # To handle errrors and exceptions we use try and except blocks with except Exception as e.
    try:
        yt = YouTube(url)
        streams = yt.streams.filter(progressive=True, file_extension="mp4") # To download the highest resolution.
        highest_res_stream = streams.get_highest_resolution()
        highest_res_stream.download(output_path=save_path)
        print("video downloaded successfully!")

    except Exception as e:
        print(e)

def open_file_dialog(): # To open the file where we are doing to save the video downloaded
    folder = filedialog.askdirectory()
    if folder:
        print(f"selected folder: {folder}")

    return folder


if __name__ == "__main__": # To ensure you are directly running the python file before it executes anything that happens under this.
    # This is because  there could be files that are reused by another file.
    root = tk.Tk() #initialize the window i.e creating tkinter window to enable the use of the filedialog.
    root.withdraw() #Hide the window so that it doesn't appear on the screen.

    video_url = input("please enter a YouTube url: ")

    save_dir = open_file_dialog()

    if  save_dir:
        print("started download....")
        download_video(video_url, save_dir)
        
    else:
        print("Invalid save location.")

else:
    print("progress tracking")
    
    





