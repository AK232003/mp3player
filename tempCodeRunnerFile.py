
# Defining Basic Structure (Looks, Fonts,etc.. type)
mp3= tk.Tk() # Defining mp3 as Tk object
mp3.title("ESS112_Team1-Python_project") # Adding main title to MP3 PLAYER
mp3.iconbitmap("e:/Python_project/Images/MP3.ico") # Setting icon for MP3 PLAYER
mp3.geometry("600x430") # Setting The Size it shows by default widthxheigth
mp3.maxsize(600, 430) # Setting Max Size Above Which Our MP3 PLAYER can't be stretched out (width, height)
mp3.minsize(600, 15) # Setting Min Size Below Which Our MP3 PLAYER can't be stretched in (width, height)
mp3.option_add('*Font', '5') # Changing Font Size
mp3['bg'] = 'white' # Changing Overall background colour to white of mp3 frame
