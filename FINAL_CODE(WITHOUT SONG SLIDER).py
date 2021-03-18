# Importing all required Modules
import tkinter as tk
import pygame
from pygame import mixer
from tkinter.messagebox import showinfo
from tkinter import filedialog
import time
import mutagen.mp3
from mutagen.mp3 import MP3
import tkinter.ttk as ttk


# Defining Basic Structure (Looks, Fonts,etc.. type)
mp3= tk.Tk() # Defining mp3 as Tk object
mp3.title("ESS112_Team1-Python_project") # Adding main title to MP3 PLAYER
mp3.iconbitmap("e:/Python_project/Images/MP3.ico") # Setting icon for MP3 PLAYER
mp3.geometry("600x430") # Setting The Size it shows by default widthxheigth
mp3.maxsize(600, 430) # Setting Max Size Above Which Our MP3 PLAYER can't be stretched out (width, height)
mp3.minsize(600, 15) # Setting Min Size Below Which Our MP3 PLAYER can't be stretched in (width, height)
mp3.option_add('*Font', '5') # Changing Font Size
mp3['bg'] = 'white' # Changing Overall background colour to white of mp3 frame

#To start pygame mixer which is used to play music here 
pygame.mixer.init()


# Defining a Variable List having songs with whole path in it

songs_list=[]


# Defining Function to Get length and time information about current song
def song_time():
    
    # Current Position of song in seconds (Dividing by thousand as default is milliseconds)
    current_time = pygame.mixer.music.get_pos() / 1000 
    
    # Converting given time to SPECIFIC FORMAT (more formal way M:S here)
    formal_time = time.strftime('%M:%S', time.gmtime(current_time))
    
    # Now Finding Current Song
    song = playlist.get(tk.ACTIVE) # Grab song title from playlist using ACTIVE that represents current song here
    
    # Taking Index of song and finding it's corresponding path from songs_list 
    # 0 to end here represents to search in whole list and scan for given song 
    
    index = playlist.get(0, "end").index(song)
    song = songs_list[index]
    
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
    
    # To Open files to select songs from any directory
    song = filedialog.askopenfilename(title="Select One Song" , filetypes=(("MP3 Files", "*.mp3"), ))
    
    # Adding one other variable to give our songs whole path to it
    temp_song=song
    
    # Inserting the path of selected in list
    songs_list.append
    
    # To Remove Extra Stuffs Getting printed While Adding Song Name in Queue
    h=-1
    for i in range(len(song)):
        if(song[h]=="/"):
            song = song.replace(song[0:(h+1)], "")
            song = song.replace(".mp3", "")
            break
        else:
            h=h-1
    
   # Adding Song To playlist
    playlist.insert(tk.END, song)


# Defining Add Many Songs Function in Add Option in Main Menu 

def add_many_songs():
    songs = filedialog.askopenfilenames(title="Select Many Songs" , filetypes=(("MP3 Files", "*.mp3"), ))
    
    # Giving paths of all songs in tuple to a temporary variable so as to access the whole path of any song from anywhere
    temp_songs=songs
    
    # Making A list of paths of all songs inserted
    for i in temp_songs:
        songs_list.append(i)
    
    # As Add Many Songs Is just Repetiton Of What We Did In Add A Song, We will Do That Things in loop
    
    for song in songs:
        # To Remove Extra Stuffs Getting printed While Adding Song Name in Queue
        h=-1
        for i in range(len(song)):
            if(song[h]=="/"):
                song = song.replace(song[0:(h+1)], "")
                song = song.replace(".mp3", "")
                break
            else:
                h=h-1

        # Adding Song To playlist
        playlist.insert(tk.END, song)
        
    
        
# Defining Help Button's Function

def Help():
    # Showinginfo is a command to display written things on Screen inside tkinter.messagebox, whose syntax is (Label, Message to be shown)
    showinfo("MP3 PLAYER", "Contact ESS112_GROUP-1 For Doubts Related To This Code")   


# Defining About Button's Function

def About():
    # Showinginfo is a command to display written things on Screen inside tkinter.messagebox, whose syntax is (Label, Message to be shown)
    showinfo("MP3 PLAYER", "MP3 PLAYER by ESS112_GROUP-1")


# Defining Volume Function to do it's work

# To See The level Of Volume Stretch from below or MP3 Player to see volume there 

    # pos here holds the value that where basically the volume slider is there
def Volume(pos):
    # Using this command we can increase volume from above to down 
    # MAX value at Bottom is 1 and Above is 0
    pygame.mixer.music.set_volume(volume_slider.get()) 
    
# Given Below Part is used in play but is a part of Volume slider, so added here as comments
# We here gave Curvol as it shows The Current Volume while we play any song after being loaded
    # Curvol shows Current volume here 
    # curvol = pygame.mixer.music.get_volume()
    # volume_slider_label.config(text=curvol * 100) # Multiplied by 100 as volume by default is shown in floating points using pygame 

# Giving Works To Every Buttons 

    # Defining Play Button

def Play():
    
    # To Load Selected Song
    song = playlist.get(tk.ACTIVE)
    
    # Taking Index of song and finding it's corresponding path from songs_list 
    index = playlist.get(0, "end").index(song)
    song = songs_list[index]
    
    # Playing song with the help of pygame 
    pygame.mixer.music.load(song)
    pygame.mixer.music.play(loops=0)

    # Calling song_time function in Play
    song_time()

# We here gave Curvol as it shows The Current Volume while we play any song after being loaded
    # Curvol shows Current volume here 
    curvol = pygame.mixer.music.get_volume()
    volume_slider_label.config(text=curvol * 100) # Multiplied by 100 as volume by default is shown in floating points using pygame 
    volume_slider_label["bg"]= "red" # Setting Red colour to background where it shows text(volume level)
    volume_slider_label["fg"]= "white" # Setting white colour to text shown 

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
    
    # Taking Index of song and finding it's corresponding path from songs_list
    index = playlist.get(0, "end").index(song)
    song = songs_list[index]
    
    # Now After Selecting The Next Song By Above Steps, We'll Play THE NEXT SONG
    
    # Playing song with the help of pygame 
    pygame.mixer.music.load(song)
    pygame.mixer.music.play(loops=0)

# Now to Move Selection Line(Showing Current Song) to Next Song in playlist by clearing it from Current song and Make it appear on Next Song
    
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
    # Taking Index of song and finding it's corresponding path from songs_list
    index = playlist.get(0, "end").index(song)
    song = songs_list[index]
    pygame.mixer.music.load(song)
    pygame.mixer.music.play(loops=0)
    playlist.selection_clear(0, tk.END)
    playlist.selection_set(previous_song, last=None)


# Stop playing current song
global stopped
stopped = False


    # Defining Stop Button
def Stop():
    # Used Direct Command with Mixer Module To Stop Song
    pygame.mixer.music.stop()
    # Clearing Selection line from current song
    playlist.selection_clear(tk.ACTIVE)
    
    # Clearing Status_Bar by writing nothing inside it as, when we use stop as no song will be played after it
    status_bar.config(text=" ")

    # Set Stop Variable To True
    global stopped
    stopped = True
    
#Creating Master Frame in which our frame (including all buttons and status toolbar, header ) and volume slider will be there
    
master_frame = tk.Frame(mp3)
master_frame.pack(pady = 30)# pady means padding in y to make it look properly aligned and attractive (same for padx in x direction so not explaining it everywhere)
master_frame['bg'] = 'white' # Changing Overall background colour to white of master frame


# Making playlist of songs

playlist = tk.Listbox(master_frame, bg="orange", fg="White", width=50, selectbackground='DarkGreen') # Putting our playlist in Master frame
playlist.grid(row=0, column=0) # Assigning row and column as 0 as it reprents first element of master _current_frames

# Defining button images of our mp3 player 

forward_image = tk.PhotoImage(file="e:/Python_project/Images/forward.png")
back_image = tk.PhotoImage(file="e:/Python_project/Images/back.png")
stop_image = tk.PhotoImage(file="e:/Python_project/Images/stop.png")
pause_image = tk.PhotoImage(file="e:/Python_project/Images/pause.png")
play_image = tk.PhotoImage(file="e:/Python_project/Images/play.png")


#Creating Frame to add buttons to align them in in one line in centre of screen using pack

    # Putting Buttons in master frame and griding it inside master frame properly
Buttons_frame = tk.Frame(master_frame, bg='white') # Did bgcolor of buttons as white
    # Putting buttons frame just below playlist frame by doing row=1 and col=0
Buttons_frame.grid(row=1, column=0) 


# Creating Volume Label Frame To Add Volume Slider here to make it look attractive in box and putting volume_frame in master_frame
volume_frame = tk.LabelFrame(master_frame, text="Volume")
    # Assigning Volume Part next to mp3_frame of Ours using row=0 and col=1
volume_frame.grid(row=0, column=1, padx=30)


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
remove_songs.add_command(label="Remove Selected Song", command=remove_song)

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
status_bar = tk.Label(mp3, text='ENJOY MUSIC  ', borderwidth=1, relief=tk.SUNKEN, anchor=tk.E)
status_bar.pack(fill=tk.X, side=tk.BOTTOM, ipady=3)

# Creating Volume Slider To increase and decrease volume and putting it in volume frame to look more great 
    # Orienting it in vertical direction 
    # Did 0 to 1 as volume in pygame will be given in decimals like 0.001 and all,.. so MAX volume shows 1 here
    # Value here is by default 1 it means song will play at MAX volume and Length is value that how much space will it occupy in vertical direction and assigning that value properly to look more perfect
volume_slider = ttk.Scale(volume_frame, from_=0, to=1, orient=tk.VERTICAL, value=1, command=Volume, length=180)
    # PAcking slider in volume_frame
volume_slider.pack(pady=10) # Here padded in Y direction so to look more Attractive with spaces above and below of length (10)


# Create Volume Slider Label to Show Current Volume 
volume_slider_label = tk.Label(mp3, text="0") # Shows initial text = 0
volume_slider_label.pack(pady=10)


# Entering in event loop and allowing all the data we entered above to appear on screen
mp3.mainloop()
