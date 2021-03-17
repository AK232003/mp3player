from tkinter import *
import mysql.connector
import os
from mysql.connector.cursor import CursorBase
import pygame
import tkinter.filedialog as fd
from functools import partial

my_db=mysql.connector.connect(host="localhost",user="root",passwd='raheja1907',database='playlists')   #initiating mysql
cursor=my_db.cursor()                              
cursor.execute("use playlists")
myresult=[]

def create_playlist(tk):
    playname=StringVar()

    def submit():
        play=playname.get()
        cursor.execute("create table "+str(play)+"(id int(3) unsigned auto_increment primary key,song_name varchar(1000) not null);")
        myresult.append(play)
        playname.set("")
        new1.destroy()

    new1=Toplevel(tk,bg="#191414")
    new1.geometry("500x100")    
    name_label = Label(new1, text = 'Enter the name of the playlist   ', font=('calibre',10, 'bold'),fg="#40704d",bg="#191414")
    name=Entry(new1,font=40,textvariable=playname)
    b=Button(new1,text="Create",command=submit,bg="#1DB954")
    name_label.grid(row=0,column=0)
    name.grid(row=0,column=1)
    b.grid(row=1,column=1)

def add_songs(n,tk):
    filename =fd.askopenfilenames(filetypes=(("mp3","*.mp3"),("All files",".")))

    for i in filename:
        print(i)
        cursor.execute("insert into "+str(myresult[n])[2:-3]+"(song_name) values (\'"+str(i)+"\');")
    my_db.commit()

def delete_song(n,tk):
    deletewindow =Toplevel(tk,bg="#191414")
    cursor.execute("select * from "+str(myresult[n])[2:-3])
    songs=cursor.fetchall()
    print(songs)
    for i in songs:
        b=Button(deletewindow,text=i[1],command=partial(cursor.execute,"delete from "+str(myresult[n])[2:-3]+" where id= "+str(i[0])))
        b.grid(row=i[0],column=0)
    my_db.commit()

def delete_playlist(i,tk):
    cursor.execute("Drop table "+str(myresult[i])[2:-3])
    my_db.commit()
    newwindow.destroy()
    myresult.pop(i)

def playlist_names(func,tk):
    global newwindow
    newwindow=Toplevel(tk,bg="#191414")
    newwindow.title("Select Playlist")
    newwindow.geometry("500x500")
    cursor.execute("Show tables;") 
    global myresult
    myresult = cursor.fetchall()

    for i in range(len(myresult)):  
        b=Button(newwindow,text=myresult[i],command=partial(func,i,tk)).grid(row=i,column=0,padx=8)
    #newwindow.destroy()
    