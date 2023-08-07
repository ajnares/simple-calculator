import tkinter as tk
from tkinter import *
from tkinter import filedialog, Text
from tkinter.ttk import *
import os

root = tk.Tk()
canvas = tk.Canvas(root, height=500, width=400, bg="#263d42")

#background
frame = tk.Frame(root, bg="#3e646c")
frame.place(relwidth=0.8, relheight=0.8, rely=0.1, relx=0.1)

#operators button
equalsBtn = tk.Button(root, text="=")
equalsBtn.place(relheight=0.09, relwidth=0.15,rely=0.78, relx=0.7)

addBtn = tk.Button(root, text="+")
addBtn.place(relheight=0.09, relwidth=0.15,rely=0.68, relx=0.7)

subBtn = tk.Button(root, text="-")
subBtn.place(relheight=0.09, relwidth=0.15,rely=0.58, relx=0.7)

mulBtn = tk.Button(root, text="*")
mulBtn.place(relheight=0.09, relwidth=0.15,rely=0.48, relx=0.7)

divBtn = tk.Button(root, text="/")
divBtn.place(relheight=0.09, relwidth=0.15,rely=0.38, relx=0.7)

#numbers
nineBtn = tk.Button(root, text="9")
nineBtn.place(relheight=0.09, relwidth=0.15,rely=0.48, relx=0.53)

eightBtn = tk.Button(root, text="8")
eightBtn.place(relheight=0.09, relwidth=0.15,rely=0.48, relx=0.36)

sevBtn = tk.Button(root, text="7")
sevBtn.place(relheight=0.09, relwidth=0.15,rely=0.48, relx=0.19)

sixBtn = tk.Button(root, text="6")
sixBtn.place(relheight=0.09, relwidth=0.15,rely=0.58, relx=0.53)

fiveBtn = tk.Button(root, text="5")
fiveBtn.place(relheight=0.09, relwidth=0.15,rely=0.58, relx=0.36)

fourBtn = tk.Button(root, text="4")
fourBtn.place(relheight=0.09, relwidth=0.15,rely=0.58, relx=0.19)

thrBtn = tk.Button(root, text="3")
thrBtn.place(relheight=0.09, relwidth=0.15,rely=0.68, relx=0.53)

twoBtn = tk.Button(root, text="2")
twoBtn.place(relheight=0.09, relwidth=0.15,rely=0.68, relx=0.36)

oneBtn = tk.Button(root, text="1")
oneBtn.place(relheight=0.09, relwidth=0.15,rely=0.68, relx=0.19)

zeroBtn = tk.Button(root, text="0")
zeroBtn.place(relheight=0.09, relwidth=0.15,rely=0.78, relx=0.36)

#other buttons
decimalBtn = tk.Button(root, text=".")
decimalBtn.place(relheight=0.09, relwidth=0.15,rely=0.78, relx=0.53)

percentBtn = tk.Button(root, text="%")
percentBtn.place(relheight=0.09, relwidth=0.15,rely=0.78, relx=0.19)

openBtn = tk.Button(root, text="(")
openBtn.place(relheight=0.09, relwidth=0.15,rely=0.38, relx=0.36)

closeBtn = tk.Button(root, text=")")
closeBtn.place(relheight=0.09, relwidth=0.15,rely=0.38, relx=0.53)

raiseTwoBtn = tk.Button(root, text="x^2")
raiseTwoBtn.place(relheight=0.09, relwidth=0.15,rely=0.38, relx=0.19)

#screen 
message_box = tk.Text(root, wrap="word", state="disabled")
message_box.place(relheight=0.15, relwidth=0.65,rely=0.18, relx=0.19)

canvas.pack()
root.mainloop()

