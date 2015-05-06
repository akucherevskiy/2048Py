import sys
import random

class Point:
    def __init__(self, x, y, value):
        self.x = x
        self.y = y
        self.value = value

def init():
    fill_matrix()
    add_random_points(2)
    print_matrix()

def add_random_points(point_count):
    for i in range(point_count):
	compare_res = 0     	
	while compare_res < 1 :
	    rand_x = random.randint(0,range_matrix-1)
            rand_y = random.randint(0,range_matrix-1)
            if elements[rand_x][rand_y].value > 0:
                compare_res = 0
            else:
                elements[rand_x][rand_y].value = random.randrange(2,5,2)
		compare_res = 1			
		break
    
def fill_matrix():
    global elements 
    global range_matrix           
    
    range_matrix = 4
    elements = [[Point(i,j,0) for i in range(range_matrix)] for j in range(range_matrix)]   
    
def print_matrix():
   for x1 in range(range_matrix):
	for y1 in range(range_matrix):
	    sys.stdout.write(  "\033[93m %s \033[0m " %  elements[x1][y1].value)	    
	print

def check_if_lose():
    zeroes = 0
    for x1 in range(range_matrix):
	for y1 in range(range_matrix):
	    if elements[x1][y1].value == 0:
	        zeroes += 1
    if zeroes == 0 :
        print "YOU LOSE!"
        return
        
def slip_left(elements):
    slip_count = 1
    add_new_point_flag = 0        
    while slip_count > 0:
        for i in range(len(elements)-1):
            if elements[i].value == 0 and elements[i+1].value > elements[i].value:
	        elements[i].value = elements[i+1].value
		elements[i+1].value = 0
		slip_count +=1
		add_new_point_flag +=1
	count = 0 
        for i in range(len(elements)-1):
           if elements[i].value == 0 and elements[i+1].value>elements[i].value:
	       count += 1
	if count>0:
	    slip_count = count
	else:
	    slip_count = 0
    return add_new_point_flag

def slip_right(elements):
    add_new_point_flag = 0        
    slip_count = 1        
    while slip_count > 0:
        for i in range(len(elements)-1):
            if elements[i+1].value == 0 and elements[i].value > elements[i+1].value:
	        elements[i+1].value = elements[i].value
		elements[i].value = 0
		slip_count +=1
		add_new_point_flag +=1

	count = 0 
        for i in range(len(elements)-1):
           if elements[i+1].value == 0 and elements[i].value>elements[i+1].value:
	       count += 1
	if count>0:
	    slip_count = count
	else:	    
	    slip_count = 0
    return add_new_point_flag

def slip_up(elements):
    add_new_point_flag = 0
    slip_count = 1        
    while slip_count > 0:
        for i in xrange(len(elements)-1):
            if elements[i].value == 0 and elements[i+1].value > elements[i].value:
	        elements[i].value = elements[i+1].value
		elements[i+1].value = 0
		slip_count +=1
		add_new_point_flag +=1
	count = 0 
        for i in range(len(elements)-1):
           if elements[i].value == 0 and elements[i+1].value>elements[i].value:
	       count += 1
	if count>0:
	    slip_count = count
	else:
	    slip_count = 0
    return add_new_point_flag

def slip_down(elements):
    add_new_point_flag = 0
    slip_count = 1        
    while slip_count > 0:
        for i in xrange(len(elements)-1):
            if elements[i+1].value == 0 and elements[i].value > elements[i+1].value:
	        elements[i+1].value = elements[i].value
		elements[i].value = 0
		slip_count +=1
		add_new_point_flag +=1
	count = 0 
        for i in range(len(elements)-1):
           if elements[i].value == 0 and elements[i].value>elements[i+1].value:
	       count += 1
	if count>0:
	    slip_count = count
	else:
	    slip_count = 0
    return add_new_point_flag

def move_left(x):
    random_flag = 0
    for i in xrange(0,len(elements)-1):
         if elements[x][i].value != 0 and elements[x][i].value == elements[x][i+1].value:
             elements[x][i].value *= 2
	     elements[x][i+1].value = 0
	     random_flag += 1
    return random_flag	
          
def move_right(x):
    random_flag = 0
    for i in xrange(0,len(elements)-1):
        if elements[x][i].value != 0 and elements[x][i].value == elements[x][i+1].value:
            elements[x][i+1].value *= 2
	    elements[x][i].value = 0	
	    random_flag += 1
    return random_flag

def move_up(x):
    random_flag = 0
    for i in xrange(0,len(elements)-1):
        if elements[i][x].value != 0 and  elements[i][x].value == elements[i+1][x].value:
            elements[i][x].value *= 2
	    elements[i+1][x].value = 0
	    random_flag += 1	
    return random_flag            

def move_down(x):
    random_flag = 0
    for i in xrange(0,len(elements)-1):
        if elements[i][x].value != 0 and  elements[i][x].value == elements[i+1][x].value:
            elements[i+1][x].value *= 2
	    elements[i][x].value = 0
	    random_flag += 1	
    return random_flag

def elements_to_slip(x):
    elements_to_slip =[]    
    for y in range(range_matrix):
        elements_to_slip.append(elements[y][x]) 
    return elements_to_slip

def make_move(arg):
    random_flag = 0
    i = 0

    for x in range(range_matrix):
        #left
	if arg == 'a':
	    random_flag += slip_left(elements[x])
	    random_flag += move_left(x)
	    random_flag += slip_left(elements[x])
	#right
        elif arg == 'd':
	    random_flag += slip_right(elements[x])
	    random_flag += move_right(x)
	    random_flag += slip_right(elements[x])
	#up
        elif arg == 'w':
	    random_flag += slip_up(elements_to_slip(x))	
	    random_flag += move_up(x)
	    random_flag += slip_up(elements_to_slip(x))	
	#down 
        else:
	    random_flag += slip_down(elements_to_slip(x))	
	    random_flag += move_down(x)
	    random_flag += slip_down(elements_to_slip(x))	
    
    check_if_lose()
    if random_flag > 0:
        add_random_points(1)

def main():
    while True:    
        arg = raw_input("enter something: ")
        if arg == 'a' or arg == 'w' or arg == 's' or arg == 'd':
            make_move(arg)
    	    print_matrix()			
	    print
        else:
            print 'Only a w s d allowed!\n'

init()
main()
