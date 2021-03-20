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
import random
from pygame.constants import K_PRINTSCREEN
import playlist as pl
from functools import partial

# Initializing pygame mixer 
pygame.mixer.init()
songs_list=[]

# Defining Function to Get length and time information about current song
def song_time():
    global song_list
    global Check
    #There occurs an issue regarding the playtime func... because of the stop func... the slider moves at twice pace...
    if Check==True:
        return
    # Current Position of song in seconds (Dividing by thousand as default is milliseconds)
    current_time = pygame.mixer.music.get_pos() / 1000     
    # Converting given time to SPECIFIC FORMAT (more formal way H:M:S here)
    formal_time = time.strftime('%M:%S', time.gmtime(current_time))
    song = playlist.get(tk.ACTIVE) 
    index=playlist.get(0,"end").index(song)
    song = songs_list[index]
    # Now Finding Length Of A song using Mutagen after getting current song as above
    song_in_mut = MP3(song)
    global song_len # Passing song in mutagen and loading it with module to find it's Length
    song_len = song_in_mut.info.length  # This will return us the length of selected song in seconds
    # Now converting the time we got in seconds to M:S form
    
    song_length = time.strftime('%M:%S', time.gmtime(song_len))    
    # Output time and song length to show on screen using config
    # Now we want to do this every time our new song starts playing so calling this song_time in play
    # Now updating current_time of song every single second(1000 milliseconds) till it's Playing that is done by after
    # Basically like looping(i.e Calling function every single second till length of song)
    current_time += 1 #Because there is difference of 1 between the song position and the slider position

    if (int(song_slider.get()) == int(song_len)): #If we are at the end of the song.
        status_bar.config(text = f" Song Duration: {song_length}  /  {song_length}")#At the last second to update the label
         
    elif Check==True:
	    pass     #Rest of the elif and else statements would not execute.

    elif int(song_slider.get()) == int(current_time):#Slider hasnt moved...
	    slider_position = int(song_len)
	    song_slider.config(to = slider_position, value = int(current_time))
    
    else: 
            #If the slider has moved... sync the song
	    slider_position = int(song_len)
	    song_slider.config(to = slider_position, value = int(song_slider.get()))
		
	    converted_current_time = time.strftime('%M:%S', time.gmtime(int(song_slider.get())))

	    #Status Bar info
	    status_bar.config(text=f' Song Duration: {converted_current_time}  /  {song_length}')
	    #To keep things moving....
	    next_time = int(song_slider.get()) + 1
	    song_slider.config(value = next_time)
    
    status_bar.after(1000, song_time)

# Defining Remove A Song Function in Add Option in Main Menu
def remove_song():
    global song_list # Removes a selected one  
    #Also When we delete the songs... then the slider keeps on moving
    Stop()  
    # Removing Selected song from songs_list too i.e. temporary songs list 
    song = playlist.get(tk.ANCHOR) # To get selected song
    index = playlist.index(song)
    songs_list.pop(index)
    # Removing the Highlighted Song (i.e. here so called ANCHORED SONG)
    playlist.delete(tk.ANCHOR)
    # After deleting the song it must stop playing it so we stop the song here (if playing)
    pygame.mixer.music.stop()

# Defining Remove Many Songs Function in Add Option in Main Menu 
def remove_all_songs(): # Removes all
    global song_list
    #Also When we delete the songs... then the slider keeps on moving
    Stop()
    # Passing All Songs(we selected before in playlist) at once to delete using range form (0, till END) 
    playlist.delete(0, tk.END)
    # Stop playing any song (if its playing) 
    pygame.mixer.music.stop()
    # Removing All Songs from songs_list too i.e. temporary songs list also must be empty
    songs_list.clear()

# Defining Add A Song Function in Add Option in Main Menu 
def add_song():
    
    # To Open files to select songs from any directory
    song = filedialog.askopenfilename(title="Select One Song" , filetypes=(("MP3 Files", "*.mp3"), ))
    # Adding one other variable to give our songs whole path to it
    temp_song=song
    global song_list
    # Inserting the path of selected in list
    songs_list.append(temp_song)
    # To Remove Extra Stuffs Getting printed While Adding Song Name in Queue
    h=-1
    for i in range(len(song)):
        if(song[h]=="\\" or song[h]=="/"):
            song = song.replace(song[0:(h+1)], "")
            song = song.replace(".mp3", "")
            break
        else:
            h=h-1
    
   # Adding Song To playlist
    playlist.insert(tk.END, song)


# Defining Add Many Songs Function in Add Option in Main Menu 

def add_many_songs():
    global song_list
    songs = filedialog.askopenfilenames(title="Select Many Songs" , filetypes=(("MP3", "*.mp3"), ))
    
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
            if(song[h]=="\\" or song[h]=="/"):
                song = song.replace(song[0:(h+1)], "")
                song = song.replace(".mp3", "")
                break
            else:
                h=h-1

        # Adding Song To playlist
        playlist.insert(tk.END, song)
        
# Giving Works To Every Buttons 	
	
# Defining Help Button's Function

def Help():
    # Showinginfo is a command to display written things on Screen inside tkinter.messagebox, whose syntax is (Label, Message to be shown)
    showinfo("MP3 PLAYER", "Contact ESS112_GROUP-1 For Doubts Related To This Code")   


# Defining About Button's Function

def About():
    # Showinginfo is a command to display written things on Screen inside tkinter.messagebox, whose syntax is (Label, Message to be shown)
    showinfo("MP3 PLAYER", "MP3 PLAYER by ESS112_GROUP-1")


    # x here holds the value that where basically the volume slider is there
def Volume(x):
    # Using this command we can increase volume from above to down 
    # MAX value at Bottom is 1 and Above is 0
    pygame.mixer.music.set_volume(volume_slider.get()) 
    #To get the current volume
    current_volume = pygame.mixer.music.get_volume()
    current_volume = current_volume * 100

    #To change the Volumetric graphs
    if int(current_volume) == 0 :
        volumetric_graph.config(image = vol0)
    elif int(current_volume) > 0 and int(current_volume) <= 25:
        volumetric_graph.config(image = vol25)
    elif int(current_volume) > 25 and int(current_volume) <= 50:
        volumetric_graph.config(image = vol50)
    elif int(current_volume) > 50 and int(current_volume) <= 75:
        volumetric_graph.config(image = vol75)
    elif int(current_volume) > 75 and int(current_volume) <= 100:
        volumetric_graph.config(image = vol100)
    

    # Defining Play Button
def add_playlist(i):
    global songs_list
    songs_list+=pl.play_playlist(i)
    for song in songs_list:
        # To Remove Extra Stuffs Getting printed While Adding Song Name in Queue
        h=-1
        for i in range(len(song)):
            if(song[h]=="\\" or song[h]=="/"):
                song = song.replace(song[0:(h+1)], "")
                song = song.replace(".mp3", "")
                break
            else:
                h=h-1
        playlist.insert(tk.END, song)

def Play():
    global song_list
    #In play func...
    global stop
    stop = False
    # To Load Selected Song
    song = playlist.get(tk.ACTIVE)
    # Taking Index of song and finding it's corresponding path from songs_list 
    ind = playlist.get(0, tk.END).index(song)
    song = songs_list[ind]
    # Playing song with the help of pygame 
    pygame.mixer.music.load(song)
    pygame.mixer.music.play(loops=0)
    song_time()
    global song_len
    slider_position = int(song_len)
    song_slider.config(to = slider_position, value = 0) #Whenever new song plays default value should be 0

    current_volume = pygame.mixer.music.get_volume()
    current_volume = current_volume * 100

    #To change the Volumetric graphs
    if int(current_volume) == 0 :
        volumetric_graph.config(image = vol0)
    elif int(current_volume) > 0 and int(current_volume) <= 25:
        volumetric_graph.config(image = vol25)
    elif int(current_volume) > 25 and int(current_volume) <= 50:
        volumetric_graph.config(image = vol50)
    elif int(current_volume) > 50 and int(current_volume) <= 75:
        volumetric_graph.config(image = vol75)
    elif int(current_volume) > 75 and int(current_volume) <= 100:
        volumetric_graph.config(image = vol100)
    

# We here gave Curvol as it shows The Current Volume while we play any song after being loaded
    # Curvol shows Current volume here 
    curvol = pygame.mixer.music.get_volume()
    volume_slider_label.config(text=curvol * 100) # Multiplied by 100 as volume by default is shown in floating points using pygame 
    volume_slider_label["bg"]= "red" # Setting Red colour to background where it shows text(volume level)
    volume_slider_label["fg"]= "white" # Setting white colour to text shown 
# Given Below Part is used in play but is a part of Volume slider, so added here as comments
# We here gave Curvol as it shows The Current Volume while we play any song after being loaded
    # Curvol shows Current volume here 
    # curvol = pygame.mixer.music.get_volume()
    # volume_slider_label.config(text=curvol * 100) # Multiplied by 100 as volume by default is shown in floating points using pygame 	
	
# Create Check Variable To Check Whether A Song Is Running Or Not
global Check
Check = False

    # Defining Pause Button
def Pause(is_paused):
    global song_list
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
    song_time()
    # Defining Forward Button

def Forward():
    global song_list
    #To reset the slider position...
    status_bar.config(text = '')
    song_slider.config(value = 0)
# Converting Songs To Tuples here using curselection so to know which song is being played
# Basically here Songs Are Numbered
# Curselection is Current Selection To know which song is being played from given list of tuples of songs
    next_song = playlist.curselection()
    print(next_song)
    # Now Adding One To Current Song number from tuples to Select "NEXT" song from Tuple of songs(OR Order in which we selected the songs)
    next_song = next_song[0]+1
    
    
    
    # Getting The Song Corresponding To Number In Tuple
    song = playlist.get(next_song)
    
    # Taking Index of song and finding it's corresponding path from songs_list
    index=playlist.get(0,"end").index(song)
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
    global song_list
    #To reset the slider position...
    status_bar.config(text = '')
    song_slider.config(value = 0)
    previous_song = playlist.curselection()
    previous_song = previous_song[0]-1
    song = playlist.get(previous_song)
    # Taking Index of song and finding it's corresponding path from songs_list
    index=playlist.get(0,"end").index(song)
    song = songs_list[index]
    pygame.mixer.music.load(song)
    pygame.mixer.music.play(loops=0)
    playlist.selection_clear(0, tk.END)
    playlist.selection_set(previous_song, last=None)

#Also create a stop global variable so that we can use it later on...
global stop 
stop = False

# Defining Stop button
def Stop():
    #Above stop func def
    global stop
    stop = True
    #Reset the song slider
    status_bar.config(text = '')
    song_slider.config(value = 0)
    # Used Direct Command with Mixer Module To Stop Song
    pygame.mixer.music.stop()
    # Clearing Selection line from current song
    playlist.selection_clear(tk.ACTIVE)
    
    # Clearing Status_Bar by writing nothing inside it as, when we use stop as no song will be played after it
    status_bar.config(text=" ")

def song_slide(x):
    #song_length should be global
    song = playlist.get(tk.ACTIVE)
    for i in songs_list:
        if song in i:
            song=i

    pygame.mixer.music.load(song)
    pygame.mixer.music.play(loops = 0, start = int(song_slider.get()))
    
   
#Creating Master Frame in which our frame (including all buttons and status toolbar, header ) and volume slider will be there
def main(mp3):
    
    global playlist
    global status_bar
    global volume_slider   
    global volume_slider_label 
    global song_slider   
    master_frame = tk.Frame(mp3)
    master_frame.pack(pady = 30)# pady means padding in y to make it look properly aligned and attractive (same for padx in x direction so not explaining it everywhere)
    master_frame['bg'] = 'white' # Changing Overall background colour to white of master frame
    #Making the playlist of the songs...
    playlist = tk.Listbox(master_frame, bg="orange", fg="White", width=50, selectbackground='DarkGreen') # Putting our playlist in Master frame
    playlist.grid(row=0, column=0) # Assigning row and column as 0 as it reprents first element of master _current_frames
    global vol0
    global vol25
    global vol50
    global vol75
    global vol100
    vol0 = tk.PhotoImage(file = 'icons/volume0.png')
    vol25 = tk.PhotoImage(file = 'icons/volume25.png')
    vol50 = tk.PhotoImage(file = 'icons/volume50.png')
    vol75 = tk.PhotoImage(file = 'icons/volume75.png')
    vol100 = tk.PhotoImage(file = 'icons/volume100.png')



    # Creating Volume Label Frame To Add Volume Slider here to make it look attractive in box and putting volume_frame in master_frame
    volume_frame = tk.LabelFrame(master_frame, text="Volume")
        # Assigning Volume Part next to mp3_frame of Ours using row=0 and col=1
    volume_frame.grid(row=0, column=1, padx=30)



    # Creating Status Bar
        # Relief is border-type, ipady is internal padding in y
    status_bar = tk.Label(mp3, text='ENJOY MUSIC  ', borderwidth=1, relief=tk.SUNKEN, anchor=tk.E)
    status_bar.pack(fill=tk.X, side=tk.BOTTOM, ipady=3)

    # Creating Volume Slider To increase and decrease volume and putting it in volume frame to look more great 
        # Orienting it in vertical direction 
        # Did 0 to 1 as volume in pygame will be given in decimals like 0.001 and all,.. so MAX volume shows 1 here
        # Value here is by default 1 it means song will play at MAX volume and Length is value that how much space will it occupy in vertical direction and assigning that value properly to look more perfect
    volume_slider = ttk.Scale(volume_frame, from_=1, to=0, orient=tk.VERTICAL, value=1, command=Volume, length=180)
        # PAcking slider in volume_frame
    volume_slider.pack(pady=10) # Here padded in Y direction so to look more Attractive with spaces above and below of length (10)

    song_slider = ttk.Scale(master_frame, from_=0, to=100, orient=tk.HORIZONTAL, value=0, command=song_slide, length=360)
    song_slider.grid(row=2, column=0, pady=0)
    
    #To display these graphs
    global volumetric_graph 
    volumetric_graph = tk.Label( master_frame, image = vol100)
    volumetric_graph.grid(row = 1, column = 1, padx = 30)
    
    # Create Volume Slider Label to Show Current Volume 
    volume_slider_label = tk.Label(mp3, text="0") # Shows initial text = 0
    volume_slider_label.pack(pady=10)

root=tk.Tk()
root.geometry("800x500")
root.title("MP3 PLAYER")
#icon=tk.PhotoImage(r"icons\MP3.png")
#root.iconphoto(False,icon)
root["bg"]="#191414"

menubar=tk.Menu(root,bg="#1DB954",bd=1,font=['Verdana',12],activebackground="#1DB954")
add=tk.Menu(root,tearoff=0,bg="#40704d",bd=1,font=['Verdana',12],activebackground="#1DB954")
menubar.add_cascade(label='Add',menu=add)
add.add_command(label ='Add A Song', command = add_song) 
add.add_command(label ='Add Songs', command = add_many_songs) 

root.config(menu = menubar) 

remove_songs = tk.Menu(root,tearoff=0,bg="#40704d",bd=1,font=['Verdana',12],activebackground="#1DB954") # Making a new menu named remove_songs inside Options_list menu
menubar.add_cascade(label="Remove", menu=remove_songs)

# Adding "Remove Selected Song" Option To "Remove" Menu
remove_songs.add_command(label="Remove Selected Song", command=remove_song)
# Adding "Remove All Songs" Option To "Remove" Menu
remove_songs.add_command(label="Remove All Songs", command=remove_all_songs)

playlis=tk.Menu(root,tearoff=0,bg="#40704d",bd=1,font=['Verdana',12],activebackground="#1DB954")
menubar.add_cascade(label='Playlists',menu=playlis)
playlis.add_command(label ='Create Playlist', command = partial(pl.create_playlist,root)) 
playlis.add_command(label ='Add Songs', command = partial(pl.playlist_names,pl.add_songs,root))
playlis.add_command(label ='Delete All Songs',command = partial(pl.playlist_names,pl.delete_song,root))
playlis.add_command(label ='Delete Playlist',command = partial(pl.playlist_names,pl.delete_playlist,root))
root.config(menu = menubar) 

# Adding About Option To Main Menu
about = tk.Menu(root,bg="#1DB954",bd=1,font=['Verdana',12],activebackground="#1DB954)
about.add_command(label='About', command=About)
root.add_cascade(label="About", menu=about)

# Adding Help Option To Main Menu
help1 = tk.Menu(root,bg="#1DB954",bd=1,font=['Verdana',12],activebackground="#1DB954)
help1.add_command(label='Help', command=Help)
root.add_cascade(label="Help", menu=help1)


button_frame=tk.Frame(root,bg="black")
button_frame.pack( side = tk.BOTTOM )
# Defining button images of our mp3 player 
forward_image = tk.PhotoImage(file=r"icons\resized\fast-forward-button.png")
back_image = tk.PhotoImage(file=r"icons\resized\rewind.png")
stop_image = tk.PhotoImage(file=r"icons\resized\stop-button.png")
pause_image = tk.PhotoImage(file=r"icons\resized\pause_button.png")
play_image = tk.PhotoImage(file=r"icons\resized\play-button.png")


back = tk.Button(button_frame, image=back_image,fg="black", borderwidth=0, command=Back)
forward = tk.Button(button_frame, image=forward_image,fg="black", borderwidth=0, command=Forward)
play = tk.Button(button_frame, image=play_image,fg="black", borderwidth=0, command=Play)
pause = tk.Button(button_frame, image=pause_image,fg="black", borderwidth=0, command=lambda: Pause(Check))
stop = tk.Button(button_frame, image=stop_image,fg="black", borderwidth=0, command=Stop)

back.grid(row=0, column=0, padx=8)
forward.grid(row=0, column=4, padx=8) 
play.grid(row=0, column=1, padx=8) 
pause.grid(row=0, column=2, padx=8)
stop.grid(row=0, column=3, padx=8)

side_frame=tk.Frame(root,bg="black",width=300,height=800,relief='sunken', borderwidth=0)
side_frame.pack(expand=False, fill='y', side='left', anchor='nw')
pl.cursor.execute("Show tables;")
myresult = pl.cursor.fetchall()
    
for i in range(len(myresult)): 
    b=tk.Button(side_frame,text=myresult[i],command=partial(add_playlist,i))
    b.grid(row=i,column=0,padx=8)

#Entering into the event loop... and allowing all the data we entered above to appear on the screen.		
main(root)
root.mainloop()
