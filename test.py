from math import exp
import tkinter as tk
from tkinter import font
import ttkbootstrap as ttk
from ttkbootstrap.constants import *

def click():
    vector1Entry.delete(0,'end')
    
    
# Initialize window
window = tk.Tk()
window.title("VectorViz")
window.minsize(570,420)
window.maxsize(1000,850)
window.geometry("700x550")

# SetUp Style
style = ttk.Style()
style.configure('TButton', ipadx=100,ipady=30,
                width=15,font=("Arial",12))
# Initialize Main Frame
# Initialize button frame
buttonFrame = tk.Frame(window,width=1000,bg='red',height=100)

# Initialize button grid
buttonFrame.columnconfigure(0, weight = 1)
buttonFrame.columnconfigure(1, weight = 1)
buttonFrame.columnconfigure(2, weight = 1)
buttonFrame.columnconfigure(3, weight = 1)
buttonFrame.columnconfigure(4, weight = 1)
buttonFrame.columnconfigure(5, weight = 1)
buttonFrame.rowconfigure(0, weight= 1)


#Buttons
addButton = ttk.Button(buttonFrame,text="Add", )
scalarButton = ttk.Button(buttonFrame, text="Mult")
ReflYButton = ttk.Button(buttonFrame, text="Refl Y")
ReflXButton = ttk.Button(buttonFrame, text="Refl X")
ShearXButton = ttk.Button(buttonFrame, text="Shear X")
ShearYButton = ttk.Button(buttonFrame, text="Shear Y")

addButton.grid(row=0, column=0,padx=10)
scalarButton.grid(row=0, column=1,padx = 10)
ReflXButton.grid(row=0, column=2,padx=10)
ReflYButton.grid(row=0, column=3,padx=10)
ShearXButton.grid(row=0, column=4,padx=10)
ShearYButton.grid(row=0, column=5,padx=10)

#Entry Frame
entryFrame = tk.Frame(window)
entryFrame.rowconfigure(0, weight=1)
entryFrame.rowconfigure(1, weight=1)
entryFrame.columnconfigure(0, weight=1)

#Entry Fields
vector1Entry = ttk.Entry(entryFrame, width=80)
vector2Entry = ttk.Entry(entryFrame, width=80)

#Remove Entry text from Entry Fields when clicked
vector1Entry.bind("<Button-1>",click)

# Placeholder Text for Entry Fields
vector1Entry.insert(0,"Enter a vector here: ")
vector2Entry.insert(0,"Enter a vector here: ")

vector1Entry.grid(row=0, column=0, pady = 10)
vector2Entry.grid(row=1, column=0, pady = 10)

buttonFrame.pack(side='top',fill=None,expand=False,pady=30)
entryFrame.pack(side ='top',fill=None, expand=False)
window.mainloop()