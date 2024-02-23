import numpy as np
import matplotlib.pyplot as plt

def welcome():
    print("Welcome to the Vector Visualizer!\n\n")
    print("Here you can see the results of vector addition, multiplication and a few simple linear transformations")
    answer = input("You can add or multiply two vectors together")
    
    if (answer.lower() == 'add'):
        arr = getVectors()
        v3 = addVectors(arr)
        graphVectors(arr[0],arr[1],v3)
    elif(answer.lower() == 'mult'):
        arr = getVectors()
        v3 = multVectors(arr)
    
    
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
    
def graphVectors(v1,v2,v3):
    origin = [0,0]

    fig, ax = plt.subplots()
    ax.set_xlim(0,10)
    ax.set_ylim(0,10)
    ax.quiver(origin[0],origin[1],v1[0],v1[1], angles='xy',
            scale_units='xy',scale=1,color='red',label="v1")
    ax.quiver(origin[0],origin[1],v2[0],v1[1],angles ='xy',scale_units='xy',scale=1,
            color='blue',label='v2')
    ax.quiver(origin[0],origin[1],v3[0],v3[1],angles ='xy',scale_units='xy',scale=1,
            color='green',label='v3 = v1 + v2')
    plt.legend()


    plt.show()