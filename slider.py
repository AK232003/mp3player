#SONG SILIDER

#Karan would create the Slider(command = song_slide)
#Assuming slider name to be song_slider

#In play function
slider_position = int(song_length)
song_slider.config(to = slider_position, value = 0) #Whenever new song plays default value should be 0

def song_slide(x):
    #song_length should be global
    song = song_box.get(ACTIVE)
	song = f'C:/gui/audio/{song}.mp3'
    pygame.mixer.music.load(song)
	pygame.mixer.music.play(loops = 0, start = int(song_slider.get()))

#In Play time function

current_time += 1 #Because there is difference of 1 between the song position and the slider position
	
	if (int(song_slider.get()) == int(song_length)): #If we are at the end of the song.
		status_bar.config(text = f'Time Elapsed: {converted_song_length}  of  {converted_song_length}')#At the last second to update the label
	elif paused:
		pass #Rest of the elif and else statements would not execute.
	elif int(song_slider.get()) == int(current_time):
		slider_position = int(song_length)
		song_slider.config(to = slider_position, value = int(current_time))
    else: 
        #If the slider has moved... sync the song
		slider_position = int(song_length)
		song_slider.config(to = slider_position, value = int(song_slider.get()))
		
		converted_current_time = time.strftime('%M:%S', time.gmtime(int(song_slider.get())))

		#Status Bar info
		status_bar.config(text=f'Time Elapsed: {converted_current_time}  of  {converted_song_length}  ')

		next_time = int(my_slider.get()) + 1
		song_slider.config(value = next_time)
    
#In Stop Function
#Reset the song slider
status_bar.config(text = '')
song_slider.config(value = 0)
#Also create a stop global variable so that we can use it later on...
global stop 
stop = True
#Above stop func def
global stop
stop = False

#Also When we delete the songs... then the slider keeps on moving
#In delete and delete_all functions
stop()

#There occurs an issue regarding the playtime func... because of the stop func... the slider moves at twice pace...
#In play_time function
if stop :
    return
#This will tow playtime functions running at the same time...

#In play_next and play_prev
#To reset the slider position...
status_bar.config(text = '')
song_slider.config(value = 0)

#In play func...
global stop
stop = False