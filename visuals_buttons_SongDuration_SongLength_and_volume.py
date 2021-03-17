# Importing all required Modules
import tkinter as tk
import pygame
from tkinter.messagebox import showinfo
from tkinter import filedialog
import time
import mutagen.mp3
from mutagen.mp3 import MP3

# Defining Basic Structure (Looks, Fonts,etc.. type)
mp3= tk.Tk() # Defining mp3 as Tk object
mp3.title("ESS112_Team1-Python_project") # Adding main title to MP3 PLAYER
x=tk.PhotoImage(file="icons/MP3.png")
mp3.iconphoto(False,x) # Setting icon for MP3 PLAYER
mp3.geometry("500x450") # Setting The Size it shows by default widthxheight
mp3.maxsize(500, 450) # Setting Max Size Above Which Our MP3 PLAYER can't be stretched in (width, height)
mp3.option_add('*Font', '5') # Changing Font Size
mp3['bg'] = 'white' # Changing Overall background colour

#To start pygame mixer which is used to play music here 
pygame.mixer.init()

# Defining Function to Get length and time information about current song
def song_time():
    
    # Current Position of song in seconds (Dividing by thousand as default is milliseconds)
    current_time = pygame.mixer.music.get_pos() / 1000 
    
    # Converting given time to SPECIFIC FORMAT (more formal way H:M:S here)
    formal_time = time.strftime('%M:%S', time.gmtime(current_time))
    
    # Now Finding Current Song
    song = playlist.get(tk.ACTIVE) # Grab song title from playlist using ACTIVE that represents current song here
    song = f'E:/Python_project/Songs/{song}.mp3' # Adding extra removed stuffs of path of a song
    
    # Now Finding Length Of A song using Mutagen after getting current song as above
    song_in_mut = MP3(song) # Passing song in mutagen and loading it with module to find it's Length
    song_len = song_in_mut.info.length # This will return us the length of selected song in seconds
    
    # Now converting the time we got in seconds to M:S form
    song_length = time.strftime('%M:%S', time.gmtime(song_len))    
    
    # Output time and song length to show on screen using config
    status_bar.config(text=f" Song Duration: {formal_time}  /  {song_length}  ")
    # Now we want to do this every time our new song starts playing so calling this song_time in play

    # Now updating current_time of song every single second(1000 milliseconds) till it's Playing that is done by after
    # Basically like looping(i.e Calling function every single second till length of song)
    
    status_bar.after(1000, song_time)


# Defining Remove A Song Function in Add Option in Main Menu
def remove_song(): # Removes a selected one
    
    # Removing the Highlighted Song (i.e. here so called ANCHORED SONG)
    playlist.delete(tk.ANCHOR)
    # After deleting the song it must stop playing it so we stop the song here (if playing)
    pygame.mixer.music.stop()

# Defining Remove Many Songs Function in Add Option in Main Menu 
def remove_all_songs(): # Removes all
    
    # Passing All Songs(we selected before in playlist) at once to delete using range form (0, till END) 
    playlist.delete(0, tk.END)
    # Stop playing any song (if its playing) 
    pygame.mixer.music.stop()

# Defining Add A Song Function in Add Option in Main Menu 
def add_song():
    
    # To Open files to select songs
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
        
# Defining Help Button's Function

def Help():
    # Showinginfo is a command to display written things on Screen inside tkinter.messagebox, whose syntax is (Label, Message to be shown)
    showinfo("MP3 PLAYER", "Contact ESS112_GROUP-1 For Doubts Related To This Code")   
# Defining About Button's Function

def About():
    # Showinginfo is a command to display written things on Screen inside tkinter.messagebox, whose syntax is (Label, Message to be shown)
    showinfo("MP3 PLAYER", "MP3 PLAYER by ESS112_GROUP-1")

# Giving Works To Every Buttons 

    # Defining Play Button

def Play():
    
    # Calling Selected Song
    song = playlist.get(tk.ACTIVE)
    
    # Adding Extra Part Of Path Of Function As No Song will be played just by its name 
    song = f'E:/Python_project/Songs/{song}.mp3'
    
    # Playing song with the help of pygame 
    pygame.mixer.music.load(song)
    pygame.mixer.music.play(loops=0)

    # Calling song_time function in Play
    song_time()


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
    
# Converting Songs To Tuples here using curselection so to know which song is being played
# Basically here Songs Are Numbered
# Curselection is Current Selection To know which song is being played from given list of tuples of songs
    next_song = playlist.curselection()
    
    # Now Adding One To Current Song number from tuples to Select "NEXT" song from Tuple of songs(OR Order in which we selected the songs)
    next_song = next_song[0]+1
    
    
    
    # Getting The Song Corresponding To Number In Tuple
    song = playlist.get(next_song)
    
    # Adding Extra Part Of Path Of Function As No Song will be played just by its name 
    song = f'E:/Python_project/Songs/{song}.mp3'
    
    # Now After Selecting The Next Song By Above Steps, We'll Play THE NEXT SONG
    
    # Playing song with the help of pygame 
    pygame.mixer.music.load(song)
    pygame.mixer.music.play(loops=0)

# Now to Move Selection Line(Showing Current Song) to Next Song in Playlist by clearing it from Current song and Make it appear on Next Song
    
    # So, clearing bar From Current Song here.
    playlist.selection_clear(0, tk.END)
    # Making Appear(Activating) Selection Line On Next Song After clearing it from current song
    playlist.activate(next_song) # This Will just move underline from current song to next song
    
    # Here, we did last = none means it says we are not highlighting more than one thing in list and just ending highlighting in one element only
    playlist.selection_set(next_song, last=None) # This will move highlighter to next song
    
    
    # Defining Back Button
def Back():
    
# Not Commenting Back Part As it is just Reverse to what we did in Forward and process is simple

    previous_song = playlist.curselection()
    previous_song = previous_song[0]-1
    song = playlist.get(previous_song)
    song = f'E:/Python_project/Songs/{song}.mp3'
    pygame.mixer.music.load(song)
    pygame.mixer.music.play(loops=0)
    playlist.selection_clear(0, tk.END)
    playlist.selection_set(previous_song, last=None)

    # Defining Stop Button
def Stop():
    # Used Direct Command with Mixer Module To Stop Song
    pygame.mixer.music.stop()
    # Clearing Selection line from current song
    playlist.selection_clear(tk.ACTIVE)
    
    # Clearing Status_Bar by writing nothing inside it as, when we use stop as no song will be played after it
    status_bar.config(text=" ")
    
    
# Making playlist of songs

playlist = tk.Listbox(mp3, bg="orange", fg="White", width=40, selectbackground='DarkGreen')
playlist.pack(pady=30) # pady means padding in y to make it look properly aligned and attractive (same for padx in x direction so not explaining it everywhere)

# Defining button images of our mp3 player 

forward_image = tk.PhotoImage(file="icons/forward.png")
back_image = tk.PhotoImage(file="icons/back.png")
stop_image = tk.PhotoImage(file="icons/stop.png")
pause_image = tk.PhotoImage(file="icons/pause.png")
play_image = tk.PhotoImage(file="icons/play.png")


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

# Adding "Add" Option To Main Menu
add_songs = tk.Menu(Options_list) # Making a new menu named add_songs inside Options_list menu
Options_list.add_cascade(label="Add", menu=add_songs) # Allowing to access all contents of add menu to Options_list 
    
    # Adding "Add One Song" Option To "Add" Menu
add_songs.add_command(label="Add A Song", command=add_song) # Giving command to add_song to what to do

    # Adding Add Many Songs Option To Add Menu
add_songs.add_command(label="Add Many Songs", command=add_many_songs)  # Giving command to add_many_songs to what to do


# Adding "Remove" Option To Main Menu
remove_songs = tk.Menu(Options_list) # Making a new menu named remove_songs inside Options_list menu
Options_list.add_cascade(label="Remove", menu=remove_songs) # Allowing to access all contents of remove menu to Options_list 

    # Adding "Remove One Song" Option To "Remove" Menu
remove_songs.add_command(label="Remove A Song", command=remove_song)
# Adding "Remove All Songs" Option To "Remove" Menu
remove_songs.add_command(label="Remove All Songs", command=remove_all_songs)

# Adding About Option To Main Menu
about = tk.Menu(Options_list)
about.add_command(label='About', command=About)
Options_list.add_cascade(label="About", menu=about)

# Adding Help Option To Main Menu
help1 = tk.Menu(Options_list)
help1.add_command(label='Help', command=Help)
Options_list.add_cascade(label="Help", menu=help1)

# Creating Status Bar
# Relief is border-type, ipady is internal padding in y
status_bar = tk.Label(mp3, text='Song Is Being Played   ', borderwidth=1, relief=tk.SUNKEN, anchor=tk.E)
status_bar.pack(fill=tk.X, side=tk.BOTTOM, ipady=3)

# Entering in event loop and allowing all the data we entered above to appear on screen
mp3.mainloop()
