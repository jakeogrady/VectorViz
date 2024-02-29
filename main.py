import numpy as np
import matplotlib.pyplot as plt
from matplotlib.ticker import MaxNLocator

def welcome():
    print("Welcome to the Vector Visualizer!\n\n")
    print("Here you can see the results of vector addition, multiplication and a few simple linear transformations")

def options():
    answer = input("You can add two vectors together or you can multiply a vector by a scalar:\n")
    arr = []
    answer = answer.lower()
    v1 = getVector()
    arr.append(v1)
    
    if (answer == 'add'):
        v2 = getVector()
        arr.append(v2)
        arr.append(addVectors(arr))
    elif(answer == 'multiply'):
        arr = getVector(answer)
        v2 = multVectors(arr)
    elif(answer == 'reflectionx'):
        reflMatrix = np.array([[1,0],[0,-1]])
        v2 = np.matmul(v1,reflMatrix)
    elif(answer == 'reflectiony'):
        reflMatrix = np.array([[-1,0],[0,1]])
        v2 = np.matmul(v1,reflMatrix)
    elif(answer == 'sheary'):
        shearMatrix = np.array([[1,0],[2,1]])
        v2 = np.matmul(v1,shearMatrix)
    elif(answer == 'shearx'):
        shearMatrix = np.array([[1,2],[0,1]])
        v2 = np.matmul(v1,shearMatrix)
    elif(answer == 'help'):
        print("Here are the following options for commands:\n")
        print("add, multiply, reflectionX, reflectionY, shearY, shearX")
    else:
        print("Help")
        
    arr.append(v2)
    return arr
    
    
def getVector():
    userInput = input("Enter elements for vector 1. Please make sure they are space-seperated:\n")
    v1 = np.fromstring(userInput, sep=' ', dtype=int)
    return v1

def addVectors(arr):
    v1 = arr[0]
    v2 = arr[1]
    return (v1+v2)

def multVectors(arr):
    scalar = int(input("Enter an integer that will be used as a scalar\n"))
    vectorSpace.append(scalar)
    v1 = arr[0]
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
    print(minX)
    print(maxX)
    
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
        
        
        
####################
#   Run Code Here
####################
welcome()     
vectorSpace = options()
vectorSpace = np.array(vectorSpace)
graphVectors(vectorSpace)