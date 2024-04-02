# VectorViz
VectorViz is a new way to help students understand the value of linear transformations in relation to vectors geometrically. By inputting vectors and choosing your transformation with the clean GUI, the program will display the results along with the original vector, so you can see how the matrices affect the vector's magnitude and direction.

## Getting Started
These instructions will get you a copy of the project up and running

## Prerequisites
Before running this project you need to have Python3 installed on your computer

### Windows
1. Go to https://www.python.org/downloads/windows/
2. Download latest version of Python (3.x.x)
3. Run downloaded .exe file
4. Tick "Add Python 3.x.x to PATH" box
5. Follow instructions for correct installation
6. Open cmd and type 'python --version' to verify installation

### macOs
1. Go to https://www.python.org/downloads/windows/
2. Download latest version of Python (3.x.x)
3. Open downloaded '.pkg' file and follow instructions given
4. Run 'python --version' to ensure correct results

### Linux/Unix
Python 3 should be installed already, use 'python --version' or 'python3 --version' to check for this. If not for some reason, follow these steps.

For Ubuntua and Debian-based systems:
```bash
sudo apt-get update
sudo apt-get install python3
sudo apt-get install python3-pip
```

For Fedora-style systems:
```bash
sudo dnf install python3
sudo dnf install python3.pip
```

For Arch Linux:
```bash
sudo pacman -S python python.pip
```

Again, to verify correct installation, use 'python3 --version'

## Installation
1. You need to clone the repo:
```bash
git clone https://github.com/jakeogrady/VectorViz.git
```

2. Install dependencies needed:
```bash
cd vectorViz
pip3 install -r requirements.txt
```

## Running the Files
Simply run the line in terminal
```bash
python3 gui.py
```

Then just enter your vectors of choice and click the button corresponding to the linear transformation you want. Please note all vectors must be space seperated and only consist of 2 digits.
