from tkinter import *
import pygame
import os
from tkinter import filedialog
import vlc



p = vlc.MediaPlayer("http://stream.dancewave.online:8080/dance.mp3")
def Radio_start():
    
    # p = vlc.MediaPlayer("http://stream.dancewave.online:8080/dance.mp3")
    p.play()
    lebel1.set("YourTrance Radio")
    lebel2.set("Radio playing")
def Radio_stop():
    
    #p = vlc.MediaPlayer("http://stream.dancewave.online:8080/dance.mp3")
    p.stop()
    lebel1.set("YourTrance Radio")
    lebel2.set("Radio stop")
def song_play():
    #self.p.stop()
    no = len(list1)
    
    pygame.mixer.music.load(mylist.get(ACTIVE))
    lebel1.set(mylist.get(ACTIVE))
    lebel2.set("Playing")
    pygame.mixer.music.set_volume(0.7)
    pygame.mixer.music.play()
def song_pause():
    #self.p.stop()
    pygame.mixer.music.pause()
    lebel1.set(mylist.get(ACTIVE))
    lebel2.set("Pause")
def song_unpause():
    #self.p.stop()
    pygame.mixer.music.unpause()
    lebel1.set(mylist.get(ACTIVE))
    lebel2.set("Playing")
def song_stop():
    #self.p.stop()
    pygame.mixer.music.stop()
    lebel1.set(mylist.get(ACTIVE))
    lebel2.set("Stop")










root = Tk()
root.title("Music Player")



root.geometry("1000x200")


        
folder_selected = filedialog.askdirectory()


path1 = folder_selected.split("/")

path1 = "\\".join(path1)



pygame.init()
pygame.mixer.init()
lebel1 = StringVar()
lebel2 = StringVar()
list1 = []

trackframe = LabelFrame(root, text="Song Track",bg ="red",fg="white")
buttonframe = LabelFrame(root, text="Control Panel",bg ="blue",fg="white")
songframe = LabelFrame(root, text="Song List",bg ="white")

trackframe.place(x=0,y=0,width=600,height=100)
buttonframe.place(x=0,y=105,width=600,height=100)
songframe.place(x=610,y=0,width=390,height=190)

l1 = Label(trackframe, textvariable = lebel1, bg="blue",font=("Helvetica", 16),width =23).grid(row=0,column=0,padx=10,pady=10)
l2 = Label(trackframe, textvariable = lebel2,bg="green",font=("Helvetica", 16),width =10).grid(row=0,column=1,padx=20,pady=10)

b1 = Button(buttonframe,text = "play",command=song_play,width =10,height=2).grid(row=0,column=0,padx=8,pady=12)
b2 = Button(buttonframe,text = "pause",command=song_pause,width =10,height=2).grid(row=0,column=2,padx=8,pady=12)
b3 = Button(buttonframe,text = "unpause",command=song_unpause,width =10,height=2).grid(row=0,column=3,padx=8,pady=12)
b4 = Button(buttonframe,text = "stop",command=song_stop,width =10,height=2).grid(row=0,column=4,padx=8,pady=12)
b5 = Button(buttonframe,text = "Radio",command = Radio_start,width =10,height=2).grid(row=0,column=5,padx=8,pady=12)
b4 = Button(buttonframe,text = "Radio Stop",command = Radio_stop,width =10,height=2).grid(row=0,column=6,padx=12,pady=12)

scb = Scrollbar(songframe)
scb.pack(side=RIGHT,fill=Y) 

mylist = Listbox(songframe, yscrollcommand = scb.set ,width=100)
mylist.pack(side=LEFT)
scb.config(command=mylist.yview) 


path = path1
os.chdir(path)


for file_name in os.listdir(path):
    if file_name.endswith("mp3") :
        mylist.insert(END, file_name)
        list1.append(file_name)


































root.mainloop()











