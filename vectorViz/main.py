import array
from tkinter import *
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.ticker import MaxNLocator

def options(operation, ev1, ev2):
    arr = list()
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
        arr.append(v2)
    elif(operation == 'Refl X'):
        reflMatrix = np.array([[1,0],[0,-1]])
        v2 = np.matmul(v1,reflMatrix)
        arr.append(v2)
    elif(operation == 'Refl Y'):
        reflMatrix = np.array([[-1,0],[0,1]])
        v2 = np.matmul(v1,reflMatrix)
        arr.append(v2)
    elif(operation == 'Shear Y'):
        shearFactor = getVector(ev2)[0]
        shearMatrix = np.array([[1,0],[shearFactor,1]])
        v2 = np.matmul(shearMatrix,v1)
        arr.append(v2)
    elif(operation == 'Shear X'):
        shearFactor = getVector(ev2)[0]
        shearMatrix = np.array([[1,shearFactor],[0,1]])
        v2 = np.matmul(shearMatrix,v1)
        arr.append(v2)
    elif (operation == 'Rotate'):
        angle = getVector(ev2)[0]
        rotationMatrix = createRotationMatrix(angle)
        v2 = np.matmul(rotationMatrix,v1)
        arr.append(v2)
    else:
        print("Help")
        exit()
        
    return arr

def getVector(userInput):
    v1 = np.fromstring(userInput, sep=' ', dtype=int)
    return v1

def addVectors(arr):
    v1 = arr[0]
    v2 = arr[1]
    return (v1+v2)

def createRotationMatrix(angle):
    theta = angle % 360
    degreeAngle = theta * (np.pi/180)
    cos = np.cos(degreeAngle)
    sine = np.sin(degreeAngle)
    print(cos,sine)
    rotationMatrix = np.array([[cos,-sine],[sine,cos]])
    print(f'{rotationMatrix}: rotation matrix')
    return (rotationMatrix)
    
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
    plt.legend()
    if (len(vectorSpace)>2):
        drawDottedLines(vectorSpace)
    return fig
    
def setAxLims(ax, vectorSpace):
    minX, minY = np.min(vectorSpace, axis=0)
    maxX, maxY = np.max(vectorSpace, axis=0)
    bigY = np.max(np.abs([maxY, minY]))
    bigX = np.max(np.abs([maxX, minX]))
    #print(bigX,bigY)
    if (minX >= 0 and maxX >= 0):
        ax.set_xlim(0,bigX+1)
    else:
        ax.set_xlim(-bigX,bigX)
    if (minY>=0 and maxY>=0):
        ax.set_ylim(0,bigY+1)
    else:
        ax.set_ylim(-bigY,bigY)
         
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
    colors = ['r','b','magenta','g']
    count = 0
    for v in vectorSpace:
        ax.quiver(0,0,v[0],v[1], angles='xy',scale_units='xy',scale=1,
                  color=colors[count],zorder=3-count,
                  label=str(v))
        count +=1
       
          
def drawDottedLines(vectorSpace):
    v3 = vectorSpace[2]
    for v in vectorSpace[:2]:
        plt.plot([v[0],v3[0]],[v[1],v3[1]],c='green',linewidth=2,
                 marker='o', linestyle='--')
