# -*- coding: utf-8 -*-
"""
Created on Sat Jun  5 13:44:40 2021

@author: hp
"""

from tkinter import *
from tkinter.font import Font
from PIL import Image, ImageTk
 


class popup():
    def __init__(self):
       self.root = Tk()

    def countdown(self,time):
        if time == -1:
            self.root.destroy()
        else:
            self.root.after(1000, self.countdown, time-1)

    def alert_popup(self,title, img):
        """Generate a pop-up window for special messages."""
        
        self.root.title(title)
        w = 1200     # popup window width
        h = 750     # popup window height
        sw = self.root.winfo_screenwidth()
        sh = self.root.winfo_screenheight()
        x = (sw - w)/2
        y = (sh - h)/2
        self.root.geometry('%dx%d+%d+%d' % (w, h, x, y))
        x = Image.open(img)
        x = ImageTk.PhotoImage(x)
        w = Label(self.root ,image=x ,bg="white" , width=1200, height=750) #,image=render
        w.pack()
        self.countdown(5)
        mainloop()





# window_2=popup().alert_popup("Title goes here..","face.png")
# 
# window_3=popup().alert_popup("Title goes here..","face.png")
# 
# 
# 
# 
# 
