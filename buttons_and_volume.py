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

# Defining Add A Song Function in Add Option in Main Menu 
def add_song():
    song = filedialog.askopenfilename(initialdir="e:/Python_project/Songs/" , title="Select One Song" , filetypes=(("MP3 Files", "*.mp3"), ))
   # To Remove Extra Stuffs Getting printed While Adding Song Name in Queue
    song = song.replace("E:/Python_project/Songs/", "")
    song = song.replace(".mp3", "")
    
   # Adding Song To Playlist
    playlist.insert(tk.END, song)

# Defining Add Many Songs Function in Add Option in Main Menu 

def add_many_songs():
    songs = filedialog.askopenfilenames(initialdir="e:/Python_project/Songs/" , title="Select Many Songs" , filetypes=(("MP3 Files", "*.mp3"), ))
    
    # As Add Many Songs Is just Repetiton Of What We Did In Add A Song, We will Do That Things in loop
    
    for song in songs:
        song = song.replace("E:/Python_project/Songs/", "")
        song = song.replace(".mp3", "")
        playlist.insert(tk.END, song)
        
# Defining About Button's Function

def Help():
    # Showinginfo is a command to display written things on Screen inside tkinter.messagebox, whose syntax is (Label, Message to be shown)
    showinfo("MP3 PLAYER", "Contact HEET VASANI For Doubts Related To This Code")   
# Defining About Button's Function

def About():
    # Showinginfo is a command to display written things on Screen inside tkinter.messagebox, whose syntax is (Label, Message to be shown)
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


# Create Check Variable To Check Whether A Song Is Running Or Not
global Check
Check = False

    # Defining Pause Button
def Pause(is_paused):
    
    # Using Global Variable Here So that Every Time We Pause Or Unpause A Song, The Value Of The "Check" Variable Changes, allowing us to work properly with our player
    global Check
    Check = is_paused    
    
    # Pausing A Song     
    if Check==False:
        # Used Direct Command with Mixer Module To Pause Song
        pygame.mixer.music.pause()
        # Changing "Check" Variable's value to True tell "SONG IS PAUSED NOW"
        Check = True
    
    # Unpausing A Song
    else:
        # Used Direct Command with Mixer Module To UnPause Song
        pygame.mixer.music.unpause()
        # Changing "Check" Variable's value to False tell "SONG IS UNPAUSED NOW"
        Check = False

    # Defining Forward Button
def Forward():
    pass

    # Defining Back Button
def Back():
    pass

    # Defining Stop Button
def Stop():
    # Used Direct Command with Mixer Module To Stop Song
    pygame.mixer.music.stop()
    playlist.selection_clear(tk.ACTIVE)
    
    
    
# Making playlist of songs

playlist = tk.Listbox(mp3, bg="orange", fg="White", width=40, selectbackground='DarkGreen')
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
pause = tk.Button(Buttons_frame, image=pause_image, borderwidth=0, command=lambda: Pause(Check))
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

    # Adding Add Option To Main Menu
add_songs = tk.Menu(Options_list) # Making a new menu named add_songs inside Options_list menu
Options_list.add_cascade(label="Add", menu=add_songs) # Allowing to access all contents of add_menu to Options_list 
    
    # Adding One Song Option To Add Menu
add_songs.add_command(label="Add A Song", command=add_song) # Giving command to add_song to what to do

    # Adding About Option To Main Menu
about = tk.Menu(Options_list)
about.add_command(label='About', command=About)
Options_list.add_cascade(label="About", menu=about)

    # Adding Help Option To Main Menu
help1 = tk.Menu(Options_list)
help1.add_command(label='Help', command=Help)
Options_list.add_cascade(label="Help", menu=help1)

    # Adding Add Many Songs Option To Add Menu
add_songs.add_command(label="Add Many Songs", command=add_many_songs)  # Giving command to add_many_songs to what to do


mp3.mainloop()