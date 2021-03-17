from tkinter import *
import pygame
from tkinter.messagebox import showinfo
from tkinter import filedialog
import time
import mutagen.mp3
from mutagen.mp3 import MP3
import tkinter.ttk as ttk


root = Tk()

root.title('player')
icon=PhotoImage(file=r"icons/MP3.png")
root.iconphoto(False,icon)
root.geometry("1280x700")
root.configure(bg='#191414')


pygame.mixer.init()

# Defining Function to Get length and time information about current song
def song_time():
    
    # Current Position of song in seconds (Dividing by thousand as default is milliseconds)
    current_time = pygame.mixer.music.get_pos() / 1000 
    
    # Converting given time to SPECIFIC FORMAT (more formal way H:M:S here)
    formal_time = time.strftime('%M:%S', time.gmtime(current_time))
    
    # Now Finding Current Song
    song = playlist.get(ACTIVE) # Grab song title from playlist using ACTIVE that represents current song here
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
    playlist.delete(ANCHOR)
    # After deleting the song it must stop playing it so we stop the song here (if playing)
    pygame.mixer.music.stop()

# Defining Remove Many Songs Function in Add Option in Main Menu 
def remove_all_songs(): # Removes all
    
    # Passing All Songs(we selected before in playlist) at once to delete using range form (0, till END) 
    playlist.delete(0,END)
    # Stop playing any song (if its playing) 
    pygame.mixer.music.stop()

# Defining Add A Song Function in Add Option in Main Menu 
def add_song():
    
    # To Open files to select songs from any directory
    song = filedialog.askopenfilename(title="Select One Song" , filetypes=(("MP3 Files", "*.mp3"), ))
    
    # Adding one other variable to give our songs whole path to it
    temp_song=song
    
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
    playlist.insert(END, song)

# Defining Add Many Songs Function in Add Option in Main Menu 

def add_many_songs():
    songs = filedialog.askopenfilenames(title="Select Many Songs" , filetypes=(("MP3 Files", "*.mp3"), ))
    
    # Giving paths of all songs in tuple to a temporary variable so as to access the whole path of any song from anywhere
    temp_songs=songs
    
    
    # Assigning temporary variable to every song in songs 
    for temp_song in temp_songs:
        temp_song=temp_song
    
    
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
        playlist.insert(END, song)
        
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
    song = playlist.get(ACTIVE)
    
    # Adding Extra Part Of Path Of Function As No Song will be played just by its name 
    song = f'E:/Python_project/Songs/{song}.mp3'
    
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
    
    # Adding Extra Part Of Path Of Function As No Song will be played just by its name 
    song = f'E:/Python_project/Songs/{song}.mp3'
    
    # Now After Selecting The Next Song By Above Steps, We'll Play THE NEXT SONG
    
    # Playing song with the help of pygame 
    pygame.mixer.music.load(song)
    pygame.mixer.music.play(loops=0)

# Now to Move Selection Line(Showing Current Song) to Next Song in playlist by clearing it from Current song and Make it appear on Next Song
    
    # So, clearing bar From Current Song here.
    playlist.selection_clear(0, END)
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
    playlist.selection_clear(0, END)
    playlist.selection_set(previous_song, last=None)

    # Defining Stop Button
def Stop():
    # Used Direct Command with Mixer Module To Stop Song
    pygame.mixer.music.stop()
    # Clearing Selection line from current song
    playlist.selection_clear(ACTIVE)
    
    # Clearing Status_Bar by writing nothing inside it as, when we use stop as no song will be played after it
    status_bar.config(text=" ")
    
#basic_cmd_frame = Frame(root).grid(row=1, column=0)
master_frame = Frame(root)
master_frame.pack(pady = 30)# pady means padding in y to make it look properly aligned and attractive (same for padx in x direction so not explaining it everywhere)
master_frame['bg'] = 'white' 


"""button_frame=Frame(root,bg="black")
button_frame.grid(row=1, column=1)
"""
playlist = Listbox(master_frame, bg="orange", fg="White", width=40, selectbackground='DarkGreen') # Putting our playlist in Master frame
playlist.grid(row=0, column=0) 

volume_frame = LabelFrame(master_frame, text="Volume")
volume_frame.grid(row=0, column=1, padx=30)

forward_image = PhotoImage(file=r"icons/resized/fast-forward-button.png")
back_image = PhotoImage(file=r"icons/resized/rewind.png")
stop_image = PhotoImage(file=r"icons/resized/stop-button.png")
pause_image = PhotoImage(file=r"icons/resized/pause_button.png")
play_image = PhotoImage(file=r"icons/resized/play-button.png")

back = Button(root, image=back_image,fg="black", borderwidth=0, command=Back)
forward = Button(root, image=forward_image,fg="black", borderwidth=0, command=Forward)
play = Button(root, image=play_image,fg="black", borderwidth=0, command=Play)
pause = Button(root, image=pause_image,fg="black", borderwidth=0, command=lambda: Pause(Check))
stop = Button(root, image=stop_image,fg="black", borderwidth=0, command=Stop)

back.grid(row=1, column=1, padx=(270,8))
forward.grid(row=1, column=5, padx=8) 
play.grid(row=1, column=2, padx=8) 
pause.grid(row=1, column=3, padx=8)
stop.grid(row=1, column=4, padx=8)

#shuff_btn = Button(root, image=shuff_btn_img, borderwidth=0).grid(row=1, column=3, padx=40)
#loop_btn = Button(root, image=loop_btn_img, borderwidth=0).grid(row=1, column=7, padx=40)

bf.main()




root.mainloop()
