# importing the sys module
import sys, os     

def addToPath():

    absolutepath = os.path.abspath("about_functions.py")

    fileDirectory = os.path.dirname(absolutepath)
    
    # inserting the mod.py directory at
    # position 1 in sys.path
    sys.path.insert(1, fileDirectory)  