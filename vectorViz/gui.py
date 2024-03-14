import tkinter as tk
from tkinter import END, font
import ttkbootstrap as ttk
import customtkinter as ctk
import main as main
from matplotlib.backends.backend_tkagg import (FigureCanvasTkAgg, NavigationToolbar2Tk) 

# Initialize window
window = ctk.CTk()
window.title("VectorViz")
window.minsize(570,420)
window.maxsize(1000,850)
window.geometry("700x550")

#String Variable
operation = ""
canvas = None

entryVal1 = tk.StringVar()
entryVal2 = tk.StringVar()

def close():
    window.quit()
    window.destroy()
    
def clickButton(args):
    global operation
    operation = args.cget('text')
    
    checkEntries = True
    
    if (operation !='Add'):
        vector2Entry.delete(0,END)

    
    if (operation == 'Add' or operation == 'Scalar'):
        vector2Entry.configure(state='normal')
    else:
        vector2Entry.configure(state='disabled')
        
    for widget in entryFrame.winfo_children():
        if isinstance(widget, tk.Entry):
            if widget.cget('state') == 'normal' and not widget.get():
                checkEntries = False
                break
            
    if (checkEntries):
        calcButton.configure(state='normal')
    else:
        calcButton.configure(state='disabled')
        
   
def v1EntryGet():
    return vector1Entry.get()   

def v2EntryGet():
    return vector2Entry.get()

def calc():
    global canvas
    val1 = entryVal1.get()

    val2 = entryVal2.get() if vector2Entry.cget('state') == 'normal' else None

    vectorSpace = main.options(operation,val1,val2)
    fig = main.graphVectors(vectorSpace)
    
    if canvas:
        canvas.get_tk_widget().destroy()
        
    canvas = FigureCanvasTkAgg(fig, master=window)
    canvas.draw()
    canvas.get_tk_widget().pack()
    

# SetUp Style

style = ttk.Style()
style.configure('TButton', ipadx=80,ipady=20,
                width=10,font=("Arial",12))

# Initialize Main Frame
mainFrame = ctk.CTkFrame(window,width=1000,)
# Initialize button frame
buttonFrame = ctk.CTkFrame(mainFrame,width=1000,height=100)

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
addButton = ctk.CTkButton(buttonFrame,text="Add", command = lambda: clickButton(addButton))
ReflYButton = ctk.CTkButton(buttonFrame, text="Refl Y", command = lambda: clickButton(ReflYButton))
ReflXButton = ctk.CTkButton(buttonFrame, text="Refl X", command = lambda: clickButton(ReflXButton))
shearXButton = ctk.CTkButton(buttonFrame, text="Shear X", command = lambda: clickButton(shearXButton))
shearYButton = ctk.CTkButton(buttonFrame, text="Shear Y", command = lambda: clickButton(shearYButton))
scalarButton = ctk.CTkButton(buttonFrame, text="Scalar", command = lambda: clickButton(scalarButton))


addButton.grid(row=0, column=0,padx=10)
ReflXButton.grid(row=0, column=2,padx=10)
ReflYButton.grid(row=0, column=3,padx=10)
shearXButton.grid(row=0, column=4,padx=10)
shearYButton.grid(row=0, column=5,padx=10)
scalarButton.grid(row=0, column=6,padx=10)

#Entry Frame
entryFrame = ctk.CTkFrame(mainFrame,width=1000,height=100)
entryFrame.rowconfigure(0, weight=1)
entryFrame.rowconfigure(1, weight=1)
entryFrame.rowconfigure(2 ,weight=1)
entryFrame.columnconfigure(0, weight=1)


calcButton = ctk.CTkButton(entryFrame, text="Calculate",
                        state="disabled",
                        command = calc,
                        width=400)
calcButton.grid(row = 2, column=0)

#Entry Fields
vector1Entry = ctk.CTkEntry(entryFrame, width=400,
                           state='normal',
                           textvariable = entryVal1,
                           border_width=0)

vector2Entry = ctk.CTkEntry(entryFrame, width=400,
                            textvariable = entryVal2,
                            border_width=0)

vector1Entry.grid(row=0, column=0, pady = 10)
vector2Entry.grid(row=1, column=0, pady = 10)

# Calculate Button
mainFrame.pack(side='bottom', pady = 30)
buttonFrame.pack(side='top',fill=None,expand=False,pady=30)
entryFrame.pack(side ='top',fill='both', expand=True)

window.protocol("WM_DELETE_WINDOW", close)
window.mainloop()