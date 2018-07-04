import sys
import os
import time

# snake

# border
width = 60
height = 25

# snake
s_po = []
max_length = 15


# initialize
def init():
    for i in range(height):
        if (i == 0 or i == height-1):
            for j in range(width):
                print('-',end="")
        else: 
            for j in range (width):
                if (j == 0 or j == width-1):
                    print('|',end="")
                else:
                    print(' ',end="")

        print()
        time.sleep(1)

# snake move
def s_move():
    return







###
def main(argv):
        init()
        s_move()
        random()

###
main(sys.argv)

