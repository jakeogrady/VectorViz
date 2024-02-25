import numpy as np
import matplotlib.pyplot as plt
from matplotlib.ticker import MaxNLocator
'''
    Need a function that can return the vectorSpace list
    That holds all of the vectors for the display
'''

def welcome():
    print("Welcome to the Vector Visualizer!\n\n")
    print("Here you can see the results of vector addition, multiplication and a few simple linear transformations")
    answer = input("You can add or multiply two vectors together")
    arr = []
    if (answer.lower() == 'add'):
        arr = getVectors()
        v3 = addVectors(arr)
        arr.append(v3)
    elif(answer.lower() == 'mult'):
        arr = getVectors()
        v3 = multVectors(arr)
        arr.append(v3)
    return arr
    
    
def getVectors():
    vectorSpace = []
    
    userInput = input("Enter elements for vector 1. Please make sure they are space-seperated:\n")
    v1 = np.fromstring(userInput, sep=' ', dtype=int)   
    userInput = input("Enter elements for vector 2. Please make sure they are space-seperated\n")
    v2 = np.fromstring(userInput, sep = ' ', dtype=int)
    
    if(len(v1) != len(v2)):
        print("Make the vectors have the same length. Try again")
        getVectors()
        
    vectorSpace.append(v1)
    vectorSpace.append(v2)
    return vectorSpace

def addVectors(arr):
    v1 = arr[0]
    v2 = arr[1]
    return (v1+v2)

def multVectors(arr):
    v1 = arr[0]
    v2 = arr[1]
    print(f'{v1.dot(v2)} is the dot product of these two vectors')
    
def graphVectors(vectorSpace):
    fig, ax = plt.subplots()
    setAxLims(ax,vectorSpace)    
    createAx(ax)
    drawVectors(ax,vectorSpace)
   
    plt.legend()
    plt.show()
    
def setAxLims(ax, vectorSpace):
    maxVal = np.max(vectorSpace)
    minVal = np.min(vectorSpace)
    
    absMax = max(abs(maxVal), abs(minVal))
    ax.set(xlim=(-absMax, absMax), ylim=(-absMax, absMax))
    
def createAx(ax):
    ax.spines['bottom'].set_position('zero')
    ax.spines['left'].set_position('zero')
    ax.spines['top'].set_visible(False)
    ax.spines['right'].set_visible(False)

    ax.xaxis.set_major_locator(MaxNLocator(integer=True))
    ax.yaxis.set_major_locator(MaxNLocator(integer=True))

def drawVectors(ax,vectorSpace):
    v1 = vectorSpace[0]
    v2 = vectorSpace[1]
    v3 = vectorSpace[2]
    origin = [0,0]
    ax.quiver(origin[0],origin[1],v1[0],v1[1], angles='xy',
            scale_units='xy',scale=1,color='red',label="v1")
    ax.quiver(origin[0],origin[1],v2[0],v1[1],angles ='xy',scale_units='xy',scale=1,
            color='blue',label='v2')
    ax.quiver(origin[0],origin[1],v3[0],v3[1],angles ='xy',scale_units='xy',scale=1,
            color='green',label='v3 = v1 + v2')
    
vectorSpace = welcome()
graphVectors(vectorSpace)