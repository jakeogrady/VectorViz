import tkinter as tk
from tkinter import font
import ttkbootstrap as ttk
import main 

# Initialize window
window = tk.Tk()
window.title("VectorViz")
window.minsize(570,420)
window.maxsize(1000,850)
window.geometry("700x550")

#String Variable
operation = ""

entryVal1 = tk.StringVar()
entryVal2 = tk.StringVar()
def clickEntry(args):
    args.delete(0, 'end')
    
def clickButton(args):
    operation = args.cget('text')
    if (operation == 'Add'):
        vector2Entry.config(state='enabled')
    else:
        vector2Entry.config(state='disabled')
    calcButton.config(state='enabled')

def calc(operation,entryVal1, entryVal2):
    print(operation)
    print(entryVal1.get())
    print(entryVal2.get())
    

# set stringvar with value of button for later
# use match statement when submit button to run appropriate function
# SetUp Style
style = ttk.Style()
style.configure('TButton', ipadx=100,ipady=30,
                width=15,font=("Arial",12))

# Initialize Main Frame
mainFrame = tk.Frame(window)
# Initialize button frame
buttonFrame = tk.Frame(mainFrame,width=1000,bg='red',height=100)

# Initialize button grid
buttonFrame.columnconfigure(0, weight = 1)
buttonFrame.columnconfigure(1, weight = 1)
buttonFrame.columnconfigure(2, weight = 1)
buttonFrame.columnconfigure(3, weight = 1)
buttonFrame.columnconfigure(4, weight = 1)
buttonFrame.columnconfigure(5, weight = 1)
buttonFrame.rowconfigure(0, weight= 1)


#Buttons
addButton = ttk.Button(buttonFrame,text="Add", command = lambda: clickButton(addButton))
scalarButton = ttk.Button(buttonFrame, text="Mult", command = lambda: clickButton(scalarButton))
ReflYButton = ttk.Button(buttonFrame, text="Refl Y", command = lambda: clickButton(ReflYButton))
ReflXButton = ttk.Button(buttonFrame, text="Refl X", command = lambda: clickButton(ReflXButton))
ShearXButton = ttk.Button(buttonFrame, text="Shear X", command = lambda: clickButton(ShearXButton))
ShearYButton = ttk.Button(buttonFrame, text="Shear Y", command = lambda: clickButton(ShearYButton))

addButton.grid(row=0, column=0,padx=10)
scalarButton.grid(row=0, column=1,padx = 10)
ReflXButton.grid(row=0, column=2,padx=10)
ReflYButton.grid(row=0, column=3,padx=10)
ShearXButton.grid(row=0, column=4,padx=10)
ShearYButton.grid(row=0, column=5,padx=10)

#Entry Frame
entryFrame = tk.Frame(mainFrame)
entryFrame.rowconfigure(0, weight=1)
entryFrame.rowconfigure(1, weight=1)
entryFrame.rowconfigure(2 ,weight=1)
entryFrame.columnconfigure(0, weight=1)


calcButton = ttk.Button(entryFrame, text="Calculate",
                        state="disabled",
                        command = lambda: main.options(operation,entryVal1,entryVal2))
calcButton.grid(row = 2, column=0)

#Entry Fields
vector1Entry = ttk.Entry(entryFrame, width=80,
                         textvariable=entryVal1)
vector2Entry = ttk.Entry(entryFrame, width=80,
                         textvariable=entryVal2)

#Remove Entry text from Entry Fields when clicked
vector1Entry.bind("<Button-1>", lambda event: clickEntry(vector1Entry))
vector2Entry.bind("<Button-1>", lambda event: clickEntry(vector2Entry))

# Placeholder Text for Entry Fields
vector1Entry.insert(0,"Enter a vector here: ")
vector2Entry.insert(0,"Enter a vector here: ")

vector1Entry.grid(row=0, column=0, pady = 10)
vector2Entry.grid(row=1, column=0, pady = 10)

# Calculate Button
mainFrame.pack(side='bottom', pady = 30)
buttonFrame.pack(side='top',fill=None,expand=False,pady=30)
entryFrame.pack(side ='top',fill=None, expand=False)
window.mainloop()