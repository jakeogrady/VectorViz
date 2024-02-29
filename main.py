import numpy as np
import matplotlib.pyplot as plt
from matplotlib.ticker import MaxNLocator


def welcome():
    print("Welcome to the Vector Visualizer!\n\n")
    print("Here you can see the results of vector addition, multiplication and a few simple linear transformations")
    answer = input("You can add two vectors together or you can multiply a vector by a scalar:\n")
    arr = []
    if (answer.lower() == 'add'):
        arr = getVectors(answer)
        v3 = addVectors(arr)
        arr.append(v3)
    elif(answer.lower() == 'multiply'):
        arr = getVectors(answer)
        v2 = multVectors(arr)
        arr.append(v3)
    return arr
    
    
def getVectors(answer):
    vectorSpace = []
    userInput = input("Enter elements for vector 1. Please make sure they are space-seperated:\n")
    v1 = np.fromstring(userInput, sep=' ', dtype=int)
    vectorSpace.append(v1)
    
    if (answer.lower() == "add"):
        userInput = input("Enter elements for vector 2. Please make sure they are space-seperated\n")
        v2 = np.fromstring(userInput, sep = ' ', dtype=int)
        vectorSpace.append(v2)
    else:
        scalar = int(input("Enter an integer that will be used as a scalar\n"))
        vectorSpace.append(scalar)
        
    return vectorSpace

def addVectors(arr):
    v1 = arr[0]
    v2 = arr[1]
    return (v1+v2)

def multVectors(arr):
    v1 = arr[0]
    scalar = arr[1]
    del arr[1]
    return (v1*scalar)
    
    
def graphVectors(vectorSpace):
    fig, ax = plt.subplots(figsize=(12,10))
    setAxLims(ax,vectorSpace)    
    createAx(ax)
    drawVectors(ax,vectorSpace)
    ax.set_xlabel("X")
    ax.set_ylabel("Y")
    plt.legend()
    plt.show()
    
def setAxLims(ax, vectorSpace):
    minX, minY = np.min(vectorSpace, axis=0)
    maxX, maxY = np.max(vectorSpace, axis=0)
    if (minX >= 0 and maxX >= 0):
        ax.set_xlim(0,maxX+1)
    else:
        ax.set_xlim(maxX,-maxX)
    if (minY>=0 and maxY>=0):
        ax.set_ylim(0,maxY+1)
    else:
        ax.set_xlim(maxY,-maxY)
 
def createAx(ax):
    plt.grid()
    ax.spines['bottom'].set_position('zero')
    ax.spines['left'].set_position('zero')
    ax.spines['top'].set_visible(False)
    ax.spines['right'].set_visible(False)

    ax.xaxis.set_major_locator(MaxNLocator(integer=True))
    ax.yaxis.set_major_locator(MaxNLocator(integer=True))

def drawVectors(ax,vectorSpace):
    '''
    For each vector in vector space
    We will run that vector in another function that
    takes that plots it using ax.quiver
    '''
    colors = ['r','b','k','g']
    count = 0
    for v in vectorSpace:
        ax.quiver(0,0,v[0],v[1], angles='xy',scale_units='xy',scale=1,color=colors[count],zorder=2-count,label="v"+str(count+1))
        count +=1
   
    
vectorSpace = welcome()
vectorSpace = np.array(vectorSpace)
graphVectors(vectorSpace)