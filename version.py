import os
import sys

def detect_change(files):

    for i in files:
        if "models" in i:
            print (1)
            return

    print (0)


if __name__ == "__main__":

    files = []
    for i in range(1,len(sys.argv)):
        files.append(os.path.abspath(sys.argv[i])) 

    detect_change(files)
     
