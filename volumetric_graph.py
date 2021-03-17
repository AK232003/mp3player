#VOLUME IMAGES
#Volumetric_graphs
#Make sure that the images are in the current directory
from tkinter import *
import pygame

global vol0
global vol25
global vol50
global vol75
global vol100
vol0 = PhotoImage(file = 'volume0.png')
vol1 = PhotoImage(file = 'volume25.png')
vol2 = PhotoImage(file = 'volume50.png')
vol3 = PhotoImage(file = 'volume75.png')
vol4 = PhotoImage(file = 'volume100.png')

#To display these graphs 
volumetric_graph = Label( master_frame, img = vol100)
volumetric_graph.grid(row = 1, column = 1, padx = 30)

#In Volume Function
#To get the current volume
current_volume = pygame.mixer.music.get_volume()
current_volume = current_volume * 100

#To change the Volumetric graphs
if int(current_volume) == 0 :
	volume_meter.config(image = vol0)
elif int(current_volume) > 0 and int(current_volume) <= 25:
	volume_meter.config(image = vol25)
elif int(current_volume) > 25 and int(current_volume) <= 50:
	volume_meter.config(image = vol50)
elif int(current_volume) > 50 and int(current_volume) <= 75:
	volume_meter.config(image = vol75)
elif int(current_volume) > 75 and int(current_volume) <= 100:
	volume_meter.config(image = vol100)	

#Also, copy paste the whole code of the volume function in the play function (except the pygame setvolume part)