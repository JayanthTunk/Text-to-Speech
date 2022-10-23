from tkinter import *
from gtts import gTTS
import os
root = Tk()
frame1 = Frame(root,bg = "cyan",height = "150")
frame1.pack(fill = X)
frame2 = Frame(root,bg = "blue2",height = "750")
frame2.pack(fill=X)
label = Label(frame1, text = "Convert Text to Speech",font = "bold, 30",bg = "lightgrey")
label.place(x = 120, y = 50)
entry = Entry(frame2, width = 45,bd = 4, font = 14)
entry.place(x = 130, y = 52)
entry.insert(0, "")
def play():
	language = "en"
	myobj = gTTS(text = entry.get(),lang = language,slow = False)
	myobj.save("convert.wav")
	os.system("convert.wav")
btn = Button(frame2, text = "Convert",width = "15", pady = 10,font = "bold, 15",command = play, bg='Maroon1')
btn.place(x = 250,y = 130)
root.title("Jayanth's Text to Speech Convertor")
root.geometry("650x400+350+200")
root.mainloop()
