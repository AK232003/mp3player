from tkinter import *
import mysql.connector
import os
from mysql.connector.cursor import CursorBase
import pygame
import tkinter.filedialog as fd
from functools import partial

tk=Tk()                           #initiating app

my_db=mysql.connector.connect(host="localhost",user="root",passwd='raheja1907',database='playlists')   #initiating mysql
cursor=my_db.cursor()                              
cursor.execute("use playlists")

def create_playlist():
    playname=StringVar()

    def submit():
        play=playname.get()
        cursor.execute("create table "+str(play)+"(id int(3) unsigned auto_increment primary key,song_name varchar(1000) not null);")
        playname.set("")
        new1.destroy()

    new1=Toplevel(tk)
    new1.geometry("500x100")    
    name_label = Label(new1, text = 'Enter the name of the playlist', font=('calibre',10, 'bold'))
    name=Entry(new1,font=40,textvariable=playname)
    b=Button(new1,text="Create",command=submit)
    name_label.grid(row=0,column=0)
    name.grid(row=0,column=1)
    b.grid(row=1,column=1)

def add_songs(n):
    filename =fd.askopenfilenames(filetypes=(("mp3","*.mp3"),("All files",".")))

    for i in filename:
        print(i)
        cursor.execute("insert into "+str(myresult[n])[2:-3]+"(song_name) values (\'"+str(i)+"\');")
    my_db.commit()

def delete_song(i):
    deletewindow =Toplevel(tk)
    cursor.execute("select * from "+str(myresult[i])[2:-3])
    songs=cursor.fetchall()
    for i in songs:
        b=Button(deletewindow,text=i,command=partial(cursor.execute,"delete from "+str(myresult[i])[2:-3]+"where song_name="+str(i)))

def delete_playlist(i):
    cursor.execute("Drop table "+str(myresult[i])[2:-3])

def playlist_names(func):
    newwindow=Toplevel(tk)
    newwindow.title("Select Playlist")
    newwindow.geometry("500x500")
    cursor.execute("Show tables;") 
    global myresult
    myresult = cursor.fetchall()

    for i in range(len(myresult)):
        b=Button(newwindow,text=myresult[i],command=partial(func,i)).grid(row=i,column=0)
    newwindow.destroy()

b1=Button(tk,text="try1",font=40,command=create_playlist)
b2=Button(tk,text="try2",font=40,command=partial(playlist_names,add_songs))
b1.grid(row=0,column=1)
b2.grid(row=0,column=2)
tk.mainloop()
