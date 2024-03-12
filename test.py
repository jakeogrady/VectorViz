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
    
def clickButton(args):
    global operation
    operation = args.cget('text')
    
    checkEntries = True
    
    if (operation == 'Add' or operation == 'Scalar'):
        vector2Entry.config(state='enabled')
    else:
        vector2Entry.config(state='disabled')
        
    for widget in entryFrame.winfo_children():
        if isinstance(widget, tk.Entry):
            if widget.cget('state') == 'enabled' and not widget.get():
                checkEntries = False
                break
            
    if (checkEntries):
        calcButton.config(state='enabled')
    else:
        calcButton.config(state='disabled')

def v1EntryGet():
    return vector1Entry.get()   

def v2EntryGet():
    return vector2Entry.get()

def calc():
    val1 = entryVal1.get()
    val2 = entryVal2.get() if vector2Entry.cget('state') == 'enabled' else None

    vectorSpace = main.options(operation,val1,val2)
    main.graphVectors(vectorSpace)

# set stringvar with value of button for later
# use match statement when submit button to run appropriate function
# SetUp Style

style = ttk.Style()
style.configure('TButton', ipadx=80,ipady=20,
                width=10,font=("Arial",12))

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
buttonFrame.columnconfigure(6, weight = 1)

buttonFrame.rowconfigure(0, weight= 1)

#Buttons
addButton = ttk.Button(buttonFrame,text="Add", command = lambda: clickButton(addButton))
ReflYButton = ttk.Button(buttonFrame, text="Refl Y", command = lambda: clickButton(ReflYButton))
ReflXButton = ttk.Button(buttonFrame, text="Refl X", command = lambda: clickButton(ReflXButton))
shearXButton = ttk.Button(buttonFrame, text="Shear X", command = lambda: clickButton(shearXButton))
shearYButton = ttk.Button(buttonFrame, text="Shear Y", command = lambda: clickButton(shearYButton))
scalarButton = ttk.Button(buttonFrame, text="Scalar", command = lambda: clickButton(scalarButton))


addButton.grid(row=0, column=0,padx=10)
ReflXButton.grid(row=0, column=2,padx=10)
ReflYButton.grid(row=0, column=3,padx=10)
shearXButton.grid(row=0, column=4,padx=10)
shearYButton.grid(row=0, column=5,padx=10)
scalarButton.grid(row=0, column=6,padx=10)

#Entry Frame
entryFrame = tk.Frame(mainFrame)
entryFrame.rowconfigure(0, weight=1)
entryFrame.rowconfigure(1, weight=1)
entryFrame.rowconfigure(2 ,weight=1)
entryFrame.columnconfigure(0, weight=1)


calcButton = ttk.Button(entryFrame, text="Calculate",
                        state="disabled",
                        command = calc)
calcButton.grid(row = 2, column=0)

#Entry Fields
vector1Entry = ttk.Entry(entryFrame, width=80,
                         textvariable=entryVal1, state='enabled')
vector2Entry = ttk.Entry(entryFrame, width=80,
                         textvariable=entryVal2)

vector1Entry.grid(row=0, column=0, pady = 10)
vector2Entry.grid(row=1, column=0, pady = 10)

# Calculate Button
mainFrame.pack(side='bottom', pady = 30)
buttonFrame.pack(side='top',fill=None,expand=False,pady=30)
entryFrame.pack(side ='top',fill=None, expand=False)
window.mainloop()