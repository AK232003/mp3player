def Play():
    
    # To Load Selected Song
    song = playlist.get(tk.ACTIVE)
    
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
