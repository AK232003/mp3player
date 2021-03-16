import tkinter as tk
import pygame
from tkinter.messagebox import showinfo
from tkinter import filedialog



mp3= tk.Tk()
mp3.title("ESS112_Team1-Python_project")
mp3.iconbitmap("e:/Python_project/Images/MP3.ico")
mp3.geometry("500x400")
mp3.option_add('*Font', '5')
mp3['bg'] = 'white'

#To start pygame mixer which is used to play music here 

pygame.mixer.init()

# Defining Add Song Function
def add_song():
    song = filedialog.askopenfilename(initialdir="e:/Python_project/Songs/" , title="Select One Song" , filetypes=(("MP3 Files", "*.mp3"), ))
   # To Remove Extra Stuffs Getting printed While Adding Song Name in Queue
    song = song.replace("E:/Python_project/Songs/", "")
    song = song.replace(".mp3", "")
    
   # Adding Song To Playlist
    playlist.insert(tk.END, song)

# Defining About Function

def About():
    showinfo("MP3 PLAYER", "MP3 PLAYER by ESS112_GROUP-1")

# Giving Works To Every Buttons 

    # Defining Play Button

def Play():
    
    # Calling Selected Song
    song = playlist.get(tk.ACTIVE)
    # Adding Extra Part Of Path Of Function
    song = f'E:/Python_project/Songs/{song}.mp3'
    
    # Playing song with the help of pygame 
    pygame.mixer.music.load(song)
    pygame.mixer.music.play(loops=0)



    # Defining Pause Button
def Pause():
    pass

    # Defining Forward Button
def Forward():
    pass

    # Defining Back Button
def Back():
    pass

    # Defining Stop Button
def Stop():
    pass
    
    
    
# Making playlist of songs

playlist = tk.Listbox(mp3, bg="orange", fg="White", width=70, selectbackground='DarkGreen')
playlist.pack(pady=30)

# Defining button images of our mp3 player 

forward_image = tk.PhotoImage(file="e:/Python_project/Images/forward.png")
back_image = tk.PhotoImage(file="e:/Python_project/Images/back.png")
stop_image = tk.PhotoImage(file="e:/Python_project/Images/stop.png")
pause_image = tk.PhotoImage(file="e:/Python_project/Images/pause.png")
play_image = tk.PhotoImage(file="e:/Python_project/Images/play.png")


#Creating Frame to add buttons to align them in in one line in centre of screen using pack

Buttons_frame = tk.Frame(mp3, bg='white')
Buttons_frame.pack()

# Create Buttons using images defined above by aligning them in one single line

back = tk.Button(Buttons_frame, image=back_image, borderwidth=0, command=Back)
forward = tk.Button(Buttons_frame, image=forward_image, borderwidth=0, command=Forward)
play = tk.Button(Buttons_frame, image=play_image, borderwidth=0, command=Play)
pause = tk.Button(Buttons_frame, image=pause_image, borderwidth=0, command=Pause)
stop = tk.Button(Buttons_frame, image=stop_image, borderwidth=0, command=Stop)

back.grid(row=0, column=0, padx=8)
forward.grid(row=0, column=4, padx=8) 
play.grid(row=0, column=1, padx=8) 
pause.grid(row=0, column=2, padx=8)
stop.grid(row=0, column=3, padx=8)

# Create Options Menu Structure
Options_list = tk.Menu(mp3)
mp3.config(menu=Options_list)

# Adding Options to Menu Structure

    # Adding Add Songs Option
add_songs = tk.Menu(Options_list) # Making a new menu named add_songs inside Options_list menu
Options_list.add_cascade(label="Add Songs", menu=add_songs) # Allowing to access all contents of add_menu to Options_list 
add_songs.add_command(label="Add A Song", command=add_song) # Giving command to add_song to what to do

    # Adding About Option
about = tk.Menu(Options_list)
about.add_command(label='About', command=About)
Options_list.add_cascade(label="About", menu=about)

mp3.mainloop()