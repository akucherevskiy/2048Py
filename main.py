import sys
import random

class Point:
    def __init__(self, x, y, value):
        self.x = x
        self.y = y
        self.value = value

def init():
    fill_matrix()
    print_matrix()

def fill_matrix():
    global elements 
    global range_matrix    
       
    range_matrix = 4
    compare_res = 0     
    point1x = random.randint(1,range_matrix)
    point1y = random.randint(1,range_matrix)

    elements = [[Point(i,j,0) for i in range(range_matrix)] for j in range(range_matrix)]   
        
    elements[point1x-1][point1y-1].value = random.randrange(2,5,2)

    while compare_res < 1 :
        point2x = random.randint(1,range_matrix)
	point2y = random.randint(1,range_matrix)
	if point1x == point2x and point1y == point2y:
	    compare_res = 0
	else:
            elements[point2x-1][point2y-1].value = random.randrange(2,5,2)
	    break

def print_matrix():
   for x1 in range(range_matrix):
	for y1 in range(range_matrix):
	    sys.stdout.write("%s " % elements[x1][y1].value)	    
	print

def make_move(arg):
    if arg == 'a':
        move_left()
    elif arg == 'w':
        move_up()
    elif arg == 'd':
        move_right()
    else:
        move_down()
    
def move_left():
    print 'left'
def move_up():
    print 'up'
def move_right():
    print 'right'
def move_down():
    print 'down'

def main():
    arg = raw_input("enter something: ")
    if arg == 'a' or arg == 'w' or arg == 's' or arg == 'd':
        make_move(arg)
    else:
        print 'Only a w s d allowed!\n'

init()
main()
