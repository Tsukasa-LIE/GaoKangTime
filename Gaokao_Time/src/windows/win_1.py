import tkinter as tk
import datetime
import tkinter
import random
import sys
from tkinter import font
from tkinter.font import Font
import time1
from tkinter import ttk
import os , re

#list1 = [1, 2, 3, 4, 5]
#random_element = random.choice(list1)
#print(random_element)



#fnt = font.Font(family='Arial', size=16, weight='bold')
exam_date = datetime.date(2025,6,7)
today = datetime.date.today()
days_left = (exam_date - today).days
print(days_left)

#class DragWindow(tk.Tk):
#    root_x, root_y, abs_x, abs_y = 0, 0, 0, 0
#    width, height = None, None


root = tk.Tk()

root = tkinter.Tk()
text = tkinter.Text(root , height=2 , width=20)
str = "距离高考还剩"
day = "天"
test = "    "

root.wm_attributes("-alpha" , 0.9) #透明度
root.wm_attributes("-toolwindow" , True) #置顶工具
root.wm_attributes("-topmost" , True) #最顶层


def sizeChange(event):
    f = Font(size=20)
    text.configure(font=f)

text.insert(tkinter.INSERT, str)
text.insert(tkinter.END, days_left)
text.insert(tkinter.END, day)
text.insert(tkinter.INSERT, test,'\n')
#text = tk.Label(root, str)
text.pack(fill=tkinter.BOTH, expand=True)
text.config(font=('Bahnschrift', 60))

#style = {
#    'font': ('Arial', 16)
#}
#root = DragWindow()
#
#root.overrideredirect(True) #去边框
root.mainloop()