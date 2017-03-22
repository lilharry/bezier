from display import *
from draw import *
from parser import *
from matrix import *
import math,random

screen = new_screen()
color = [ 0, 255, 0 ]
edges = []
transform = new_matrix()

# print_matrix( make_translate(3, 4, 5) )
# print
# print_matrix( make_scale(3, 4, 5) )
# print
# print_matrix( make_rotX(math.pi/4) )
# print
# print_matrix( make_rotY(math.pi/4) )
# print
# print_matrix( make_rotZ(math.pi/4) )



'''
x = 0
bg = []
while (x<500):
    add_edge(bg,x,0,0,x,500,0)
    x+=1

x = 0
center = []
a = []
b = []
c = []
d = []
e = []
while (x < 215):
    if (x < 6):
        add_circle(center, 250, 250, 0, x, 0.01)
    elif (x < 15 or x < 100 and x > 85):
        add_circle(a, 250, 250, 0, x, 0.01)
    elif (x > 185 and x < 200):
        add_circle(b, 250, 250, 0, x, 0.01)
    elif ( x < 215 and x > 200):
        add_circle(c,250,250,0,x,0.01)
    else:
        if random.randrange(50) == 49:
            add_circle(e,250,250,0,x,0.01)
        else:
            add_circle(d,250,250,0,x,0.01) 
    x+=0.1


#d = []
#add_edge(d,40,250,0,460,250,0)
#r = make_rotZ(math.pi/2)
#matrix_mult(r,d)

#t = make_translate(0,-500,0)
#matrix_mult(r,t)
#matrix_mult(t,d)

#print d


draw_lines(bg,screen,[237, 201, 175])
draw_lines(center, screen, [200,0,0])
draw_lines(a, screen, [34,139,34])
draw_lines(b, screen, [200,0,0])
draw_lines(c, screen, [0,0,0])
draw_lines(d, screen, [204, 119, 34])
draw_lines(e, screen, [184, 115, 51])
'''
#save_ppm( screen, "hello.ppm" )

parse_file( 'script', edges, transform, screen, color )


