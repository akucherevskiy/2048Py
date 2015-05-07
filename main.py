import sys
import random
global range_matrix
range_matrix = 4

class Point:
    def __init__(self, x, y, value):
        self.x = x
        self.y = y
        self.value = value
class Game:
    def init(self):
        self.fill_matrix() 
        self.add_random_points(2)
	print '\n    2048! \n'
        self.print_matrix()

    def add_random_points(self, point_count):
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
    
    def fill_matrix(self):
        global elements 
        elements = [[Point(i,j,0) for i in range(range_matrix)] for j in range(range_matrix)]   
    
    def print_matrix(self, col_count = range_matrix):
        for x1 in range(range_matrix):
	    for y1 in range(col_count):
	        sys.stdout.write(" %s " %  elements[x1][y1].value)	    
	    print

    def check_if_lose(self): #to test
        zeroes = 0
        for x1 in range(range_matrix):
	    for y1 in range(range_matrix):
	        if elements[x1][y1].value == 0:
	            zeroes += 1
        if zeroes == 0 :
            print "YOU LOSE!"
            return

    def side_point(self, arg,i):
        if arg == 'a' or arg == 'w':
            return [i, i+1]
        elif arg == 's' or arg == 'd':
            return [i+1, i]
        else:
            print 'Invalid arg!'
            return

    def slip(self, side, elem): #to test
        slip_count = 1
        add_new_point_flag = 0        
        while slip_count > 0:
            for i in range(len(elements)-1):
                if elem[self.side_point(side, i)[0]].value == 0 and elem[self.side_point(side, i)[1]].value > elem[self.side_point(side, i)[0]].value:
	            elem[self.side_point(side, i)[0]].value = elem[self.side_point(side, i)[1]].value
		    elem[self.side_point(side, i)[1]].value = 0
		    slip_count +=1
		    add_new_point_flag +=1
	    count = 0 
            for i in range(len(elem)-1):
                if elem[self.side_point(side, i)[0]].value == 0 and elem[self.side_point(side, i)[1]].value > elem[self.side_point(side, i)[0]].value:
	            count += 1
            slip_count = count if count > 0 else 0
        return add_new_point_flag

    def elements_to_slip(self, x):
        elements_to_slip =[]    
        for y in range(range_matrix):
            elements_to_slip.append(elements[y][x]) 
        return elements_to_slip

    def move_left(self, x):
        random_flag = 0
        random_flag += self.slip('a', elements[x])
        for i in range(0,len(elements)-1):
            if elements[x][i].value != 0 and elements[x][i].value == elements[x][i+1].value:
                 elements[x][i].value *= 2
	         elements[x][i+1].value = 0
	         random_flag += 1
        random_flag += self.slip('a', elements[x])    
        return random_flag	
          
    def move_right(self, x):
        random_flag = 0
        random_flag += self.slip('d', elements[x])
        for i in range(0,len(elements)-1):
            if elements[x][i].value != 0 and elements[x][i].value == elements[x][i+1].value:
                elements[x][i+1].value *= 2
	        elements[x][i].value = 0	
	        random_flag += 1
        random_flag += self.slip('d', elements[x])
        return random_flag

    def move_up(self, x):
        random_flag = 0
        random_flag += self.slip('w', self.elements_to_slip(x))	
        for i in range(0,len(elements)-1):
            if elements[i][x].value != 0 and  elements[i][x].value == elements[i+1][x].value:
                elements[i][x].value *= 2
	        elements[i+1][x].value = 0
	        random_flag += 1	
        random_flag += self.slip('w', self.elements_to_slip(x))	
        return random_flag            

    def move_down(self, x):
        random_flag = 0
        random_flag += self.slip('s', self.elements_to_slip(x))	
        for i in range(0,len(elements)-1):
            if elements[i][x].value != 0 and  elements[i][x].value == elements[i+1][x].value:
                elements[i+1][x].value *= 2
	        elements[i][x].value = 0
	        random_flag += 1	
        random_flag += self.slip('s', self.elements_to_slip(x))	
        return random_flag

    def make_move(self, arg):
        random_flag = 0

        for x in range(range_matrix):
            #left
	    if arg == 'a':
	        random_flag += self.move_left(x)
	    #right
            elif arg == 'd':
	        random_flag += self.move_right(x)
	    #up
            elif arg == 'w':
	        random_flag += self.move_up(x)
	    #down 
            else:
	        random_flag += self.move_down(x)

        #check_if_lose()
        if random_flag > 0:
            self.add_random_points(1)

    def main(self):
        while True:    
            arg = raw_input("enter something: ")
            if arg == 'a' or arg == 'w' or arg == 's' or arg == 'd':
                self.make_move(arg)
    	        self.print_matrix()			
	        print
            else:
                print 'Only a w s d allowed!\n'

class TestCase(Game):
    
    def __init__(self, errors_count = 0):
        self.errors_count = errors_count

    def return_error(self,func_name):
        return '\033[91merror in ' + func_name + '! \033[0m'

    def return_success(self,func_name):
	return '\033[92msuccess in ' + func_name + '\033[0m'
    
    def test_fill_matrix(self):
        self.fill_matrix()
	for x in range(range_matrix):
	    for y in range(range_matrix):
	        if isinstance(elements[x][y], Point):
		    print self.return_success('test_fill_matrix')		
		else:
		    print self.return_error('test_fill_matrix\n')
		    self.errors_count += 1

    def test_add_random_points(self):
	last_count = 0
	self.fill_matrix()
	for k in [1,2]:
	    #print 'test_add_random_points - ', 'with matrix update\n' if k==2 else 'without matrix update\n', 
	    for i in range(1, 5):
	        tmp = 0 if k == 1 else self.fill_matrix() 
	        self.add_random_points(i)
	        count = 0
		
	        for x in range(range_matrix):
	            for y in range(range_matrix):
	                count += 1 if elements[x][y].value > 0 else 0
	        
	        if count == (last_count+1 if k == 1 else i):
		    print self.return_success('test_add_random_points') 		
		else:
		    print self.return_error('test_add_random_points')
		    self.errors_count += 1
	        last_count =  count + i if k == 1 else 0
    def test_slip(self):
	global elements
	self.fill_matrix()
	col_ar = [ [[0,0,0,0],[0,0,0,0]],
		   [[0,0,0,1],[0,0,0,1]],
		   [[0,0,1,0],[0,0,0,1]],
		   [[0,0,1,1],[0,0,1,1]],
		   [[0,1,0,0],[0,0,0,1]],
		   [[0,1,0,1],[0,0,1,1]],
		   [[0,1,1,0],[0,0,1,1]],
		   [[0,1,1,1],[0,1,1,1]],
		   [[1,0,0,0],[0,0,0,1]],
		   [[1,0,0,1],[0,0,1,1]],
		   [[1,0,1,0],[0,0,1,1]],
		   [[1,0,1,1],[0,1,1,1]],
		   [[1,1,0,0],[0,0,1,1]],
		   [[1,1,0,1],[0,1,1,1]],
		   [[1,1,1,0],[0,1,1,1]],
		   [[1,1,1,1],[1,1,1,1]]]
	for y in range(0,4):	
	    for i in range(0, 16):
                for x in range(0,4):
    		    elements[x][y].value = col_ar[i][0][x]
	        self.slip('s', [elements[0][y],elements[1][y],elements[2][y],elements[3][y]])
 	        for x in range(0,4):
		    if elements[x][y].value == col_ar[i][1][x]:
		        print self.return_success('test_slip')
		    else:
			print self.return_error('test_slip')
			self.errors_count +=1
test_obj = TestCase()
test_obj.test_fill_matrix()
test_obj.test_add_random_points()
test_obj.test_slip()
print '\033[94mTotal errors - ', test_obj.errors_count, '\033[0m'
#game = Game()
#game.init()
#game.main()

