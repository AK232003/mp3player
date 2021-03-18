from tkinter import *
import playlist as pl
from functools import partial
import GENERALIZED_CODE as bf
import pygame

pygame.mixer.init()
tk=Tk()
tk.geometry("1200x600")
tk.title("MP3 PLAYER")
icon=PhotoImage("icons/MP3.png")
tk.iconphoto(False,icon)
tk["bg"]="#191414"

menubar=Menu(tk,bg="#1DB954",bd=1,font=['Verdana',12],activebackground="#1DB954")
add=Menu(tk,tearoff=0,bg="#40704d",bd=1,font=['Verdana',12],activebackground="#1DB954")
menubar.add_cascade(label='Add',menu=add)
add.add_command(label ='Add Song', command = bf.add_song) 
add.add_command(label ='Add Songs', command = bf.add_many_songs) 

tk.config(menu = menubar) 

remove_songs = Menu(menubar) # Making a new menu named remove_songs inside Options_list menu
menubar.add_cascade(label="Remove", menu=remove_songs)

remove_songs.add_command(label="Remove A Song", command=bf.remove_song)
# Adding "Remove All Songs" Option To "Remove" Menu
remove_songs.add_command(label="Remove All Songs", command=bf.remove_all_songs)

playlis=Menu(tk,tearoff=0,bg="#40704d",bd=1,font=['Verdana',12],activebackground="#1DB954")
menubar.add_cascade(label='Playlists',menu=playlis)
playlis.add_command(label ='Create playlist', command = partial(pl.create_playlist,tk)) 
playlis.add_command(label ='Add Songs', command = partial(pl.playlist_names,pl.add_songs,tk))
playlis.add_command(label ='Delete Songs',command = partial(pl.playlist_names,pl.delete_song,tk))
playlis.add_command(label ='Delete Playlist',command = partial(pl.playlist_names,pl.delete_playlist,tk))
tk.config(menu = menubar) 

button_frame=Frame(tk,bg="black")
button_frame.pack( side = BOTTOM )

forward_image = PhotoImage(file="icons/resized/fast-forward-button.png")
back_image = PhotoImage(file="icons/resized/rewind.png")
stop_image = PhotoImage(file="icons/resized/stop-button.png")
pause_image = PhotoImage(file="icons/resized/pause_button.png")
play_image = PhotoImage(file="icons/resized/play-button.png")

back = Button(button_frame, image=back_image,fg="black", borderwidth=0, command=bf.Back)
forward = Button(button_frame, image=forward_image,fg="black", borderwidth=0, command=bf.Forward)
play = Button(button_frame, image=play_image,fg="black", borderwidth=0, command=bf.Play)
pause = Button(button_frame, image=pause_image,fg="black", borderwidth=0, command=lambda: bf.Pause(bf.Check))
stop = Button(button_frame, image=stop_image,fg="black", borderwidth=0, command=bf.Stop)

back.grid(row=0, column=0, padx=8)
forward.grid(row=0, column=4, padx=8) 
play.grid(row=0, column=1, padx=8) 
pause.grid(row=0, column=2, padx=8)
stop.grid(row=0, column=3, padx=8)

side_frame=Frame(tk,bg="black",width=300,height=800,relief='sunken', borderwidth=0)
side_frame.pack(expand=False, fill='y', side='left', anchor='nw')
pl.cursor.execute("Show tables;")
myresult = pl.cursor.fetchall()
    


for i in range(len(myresult)): 
    b=Button(side_frame,text=myresult[i])#,command=partial(pl.play_playlist,i+1,bf.playlist,tk))
    b.grid(row=i,column=0,padx=8)


bf.main(tk)
tk.mainloop()
