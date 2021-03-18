import playlist as pl
from tkinter import *
import pygame

pygame.mixer.init()
#For Queue
def add_songs(n,tk):
    pl.cursor.execute("create table queue(id int(3) unsigned auto_increment primary key,song_name varchar(1000) not null);")
    filename =pl.fd.askopenfilenames(filetypes=(("mp3","*.mp3"),("All files",".")))

    for i in filename:
        print(i)
        pl.cursor.execute("insert into queue(song_name) values (\'"+str(i)+"\');")
    pl.my_db.commit()

    pl.cursor.execute("select * from queue")
    global song_list
    song_list=pl.cursor.fetchall()
    
def remove_songs(n,tk,i):    
    pl.cursor.execute("delete from queue where id="+str(i+1))
    pl.my_db.commit()

def remove_song(playlist):
    global song_list
    playlist.delete(ANCHOR)
]   pygame.mixer.music.stop() 
    song = playlist.get(ANCHOR) 
    index = playlist.index(song)
    song_list.pop(index)





