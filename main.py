import numpy as np
import matplotlib.pyplot as plt
from matplotlib.ticker import MaxNLocator

def options(operation, v1, v2=None):
    
    operations = {
        'add': addVectors,
        'reflectionx': reflX,
        'reflectiony': reflY,
        'shearx': shearX,
        'sheary': shearY
    }
    
    if operation == 'add' and v2 is not None:
        return operations[operation](v1,v2)
    else:
        return operations[operation](v1)

        

def getVector(v):
    v1 = np.fromstring(v, sep=' ', dtype=int)
    return v1

def addVectors(v1, v2):
    return v1 + v2

def reflX(v1):
    reflMatrix = np.array([[1,0],[0,-1]])
    return np.dot(v1,reflMatrix)

def reflY(v1):
    reflMatrix = np.array([[-1,0],[0,1]])
    return np.dot(v1,reflMatrix)
    
def shearX(v1):
    shearMatrix = np.array([[1,2],[0,1]])
    return np.dot(v1,shearMatrix)

def shearY(v1):
    shearMatrix = np.array([[1,0],[2,1]])
    return np.dot(v1,shearMatrix)
    
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
'''
welcome()     
vectorSpace = options()
vectorSpace = np.array(vectorSpace)
graphVectors(vectorSpace)'''