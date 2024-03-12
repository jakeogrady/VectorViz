from tkinter import *
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.ticker import MaxNLocator


def options(operation, ev1, ev2):
    arr = []
    v1 = getVector(ev1)
    arr.append(v1)
    
    if (operation == 'Add'):
        v2 = getVector(ev2)
        arr.append(v2)
        arr.append(addVectors(arr))
    elif (operation == 'Scalar'):
        scalar = getVector(ev2)
        arr.append(scalar)
        v2 = scaleVector(arr)
    elif(operation == 'Refl X'):
        reflMatrix = np.array([[1,0],[0,-1]])
        v2 = np.matmul(v1,reflMatrix)
    elif(operation == 'Refl Y'):
        reflMatrix = np.array([[-1,0],[0,1]])
        v2 = np.matmul(v1,reflMatrix)
    elif(operation == 'Shear Y'):
        shearMatrix = np.array([[1,0],[2,1]])
        v2 = np.matmul(v1,shearMatrix)
    elif(operation == 'Shear X'):
        shearMatrix = np.array([[1,2],[0,1]])
        v2 = np.matmul(v1,shearMatrix)
    else:
        print("Help")
        exit()
        
    arr.append(v2)  
    return arr

def getVector(userInput):
    v1 = np.fromstring(userInput, sep=' ', dtype=int)
    return v1

def addVectors(arr):
    v1 = arr[0]
    v2 = arr[1]
    return (v1+v2)

def scaleVector(arr):
    v1 = arr[0]
    scalar = arr[1][0]
    v3 = v1*scalar
    del arr[1]
    return (v3)

def graphVectors(vectorSpace):
    fig, ax = plt.subplots(figsize=(12,10))
    setAxLims(ax,vectorSpace)    
    createAx(ax)
    drawVectors(ax,vectorSpace)
    ax.set_xlabel("X")
    ax.set_ylabel("Y")
    plt.legend()
    return fig
    
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
        ax.set_ylim(maxY,-maxY)
 
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
        ax.quiver(0,0,v[0],v[1], angles='xy',scale_units='xy',scale=1,color=colors[count],zorder=3-count,label="v"+str(count+1))
        count +=1
    if (len(vectorSpace)>2):
        drawDottedLines(vectorSpace)
          
def drawDottedLines(vectorSpace):
    v3 = vectorSpace[2]
    for v in vectorSpace[:2]:
        plt.plot([v[0],v3[0]],[v[1],v3[1]],c='g',linewidth=2,
                 marker='o', linestyle='--')
