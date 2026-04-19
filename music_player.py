import tkinter as tk
from tkinter import filedialog
import os

songs = []

def add_song():
    files = filedialog.askopenfilenames(filetypes=[("Audio Files", "*.mp3 *.wav")])
    for file in files:
        songs.append(file)
        playlist.insert(tk.END, os.path.basename(file))

def play_song():
    selected = playlist.curselection()
    if selected:
        index = selected[0]
        song = songs[index]
        now_playing.config(text=f"Now Playing: {os.path.basename(song)}")
        os.startfile(song)

def stop_song():
    os.system("taskkill /f /im wmplayer.exe")
    now_playing.config(text="Stopped")

def delete_song():
    selected = playlist.curselection()
    if selected:
        index = selected[0]
        playlist.delete(index)
        songs.pop(index)

root = tk.Tk()
root.title("Music Player")
root.geometry("450x400")
root.configure(bg="#1e1e1e")

tk.Label(root, text="🎧 Music Player", font=("Arial", 18, "bold"),
         bg="#1e1e1e", fg="white").pack(pady=10)

playlist = tk.Listbox(root, width=45, height=10,
                      bg="#2e2e2e", fg="white",
                      selectbackground="#00adb5",
                      font=("Arial", 10))
playlist.pack(pady=10)

now_playing = tk.Label(root, text="No song playing",
                       bg="#1e1e1e", fg="#00adb5",
                       font=("Arial", 11))
now_playing.pack(pady=5)

frame = tk.Frame(root, bg="#1e1e1e")
frame.pack(pady=10)

def style_button(btn):
    btn.configure(bg="#393e46", fg="white", width=12, relief="flat")
    btn.bind("<Enter>", lambda e: btn.config(bg="#00adb5"))
    btn.bind("<Leave>", lambda e: btn.config(bg="#393e46"))

btn_add = tk.Button(frame, text="Add Songs", command=add_song)
btn_play = tk.Button(frame, text="Play", command=play_song)
btn_stop = tk.Button(frame, text="Stop", command=stop_song)
btn_delete = tk.Button(frame, text="Delete", command=delete_song)

for btn in [btn_add, btn_play, btn_stop, btn_delete]:
    style_button(btn)
    btn.pack(side="left", padx=5)

root.mainloop()