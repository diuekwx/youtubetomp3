from pytube import YouTube
import tkinter as tk
from tkinter import filedialog


def videodownload(url, save_path):
    try:
        yt = YouTube(url)
        streams =  yt.streams.filter(file_extension='mp4', progressive=True)
        highest_res_stream = streams.get_highest_resolution()
        highest_res_stream.download(output_path=save_path)
        print("Video downloaded successfully!")
    except Exception as e:
        print(e)

def mp3download(url, save_path):
    try:
        yt = YouTube(url)
        streams = yt.streams.filter(only_audio=True).first()
        streams.download(output_path=save_path)
        print("Video downloaded successfully!")
    except Exception as e:
        print(e)

def open_file_dialog():
    folder = filedialog.askdirectory()
    if folder:
        print(f"Selected folder: {folder}")

    return folder

if __name__ == "__main__":
    root = tk.Tk()
    root.withdraw()

    video_url = input("Please enter a YouTube url: ")
    save_dir = open_file_dialog()

    if save_dir:
        print("Started download...")
        mp3download(video_url, save_dir)
    else:
        print("Invalid save location.")