import tkinter as tk
import customtkinter
from pytube import YouTube
import os
import threading  # For threading the download process

# Function to extract video ID from YouTube URL
def extract_video_id(url):
    return url.split('=')[-1]

# Function to get Downloads folder path
def get_downloads_folder():
    return os.path.join(os.path.expanduser('~'), 'Downloads')

# Downloader function
def startDownload(): 
    try: 
        ytLink = link.get()
        if not ytLink.startswith('https://www.youtube.com/'):
            raise ValueError("Invalid YouTube URL")
        
        video_id = extract_video_id(ytLink)
        youtube_url = f'https://www.youtube.com/watch?v={video_id}'
        youtubeObject = YouTube(youtube_url, on_progress_callback=on_progress)
        video = youtubeObject.streams.get_highest_resolution()
        
        # Get path to Downloads folder
        download_path = get_downloads_folder()

        # Output the title
        title.configure(text=f"Downloading: {youtubeObject.title}")
        
        # Download video to Downloads folder (run in a separate thread)
        download_thread = threading.Thread(target=download_video, args=(video, download_path))
        download_thread.start()
        
    except Exception as e:
        finishedLabel.configure(text=f"Error: {e}", text_color="red")
        title.configure(text="Insert a YouTube link")
        print(f"Error: {e}")

def download_video(video, download_path):
    try:
        video.download(output_path=download_path)
        app.after(1000, lambda: finishedLabel.configure(text=f"Download completed. Video saved to: {download_path}", text_color="green"))
        title.configure(text="Insert a YouTube link")
    except Exception as e:
        app.after(1000, lambda: finishedLabel.configure(text=f"Error: {e}", text_color="red"))
        title.configure(text="Insert a YouTube link")
        print(f"Error: {e}")

def on_progress(stream, chunk, bytes_remaining):
    total_size = stream.filesize
    bytes_downloaded = total_size - bytes_remaining
    percentage_of_completion = (bytes_downloaded / total_size) * 100
    per = f"{percentage_of_completion:.1f}%"
    pPercentage.configure(text=per)
    progressBar.set(percentage_of_completion)

# System settings
customtkinter.set_appearance_mode("System")
customtkinter.set_default_color_theme("blue")

# App frame
app = customtkinter.CTk()
app.geometry("720x480")
app.title("YouTube Downloader") 

# Adding UI elements
title = customtkinter.CTkLabel(app, text="Insert a YouTube link")
title.pack(padx=10, pady=10)

# Link input
url_var = tk.StringVar()
link = customtkinter.CTkEntry(app, width=300, textvariable=url_var)
link.pack(pady=10)

# Finished downloading label
finishedLabel = customtkinter.CTkLabel(app, text="")
finishedLabel.pack(pady=5)

# Progress percentage label
pPercentage = customtkinter.CTkLabel(app, text="0%")
pPercentage.pack()

# Progress bar
progressBar = customtkinter.CTkProgressBar(app, width=300)
progressBar.set(0)
progressBar.pack(padx=10, pady=10)

# Download button
download = customtkinter.CTkButton(app, text="Download", command=startDownload)
download.pack(pady=10)

# Run app
app.mainloop()