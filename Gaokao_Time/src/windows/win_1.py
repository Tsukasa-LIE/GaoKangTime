import tkinter as tk
import tkinter
from tkinter.font import Font
from tkinter import ttk
import os , re

class DragWindow(tk.Tk):
    root_x, root_y, abs_x, abs_y = 0, 0, 0, 0
    width, height = None, None


root = tk.Tk()

root = tkinter.Tk()
text = tkinter.Text(root , height=2 , width=15)
text.pack()
def sizeChange(event):
    
    text.configure(font=13)

root.wm_attributes("-alpha" , 0.4) #透明度
root.wm_attributes("-toolwindow" , True) #置顶工具
root.wm_attributes("-topmost" , True) #最顶层

#

root = DragWindow()
#
#root.overrideredirect(True) #去边框
root.mainloop()