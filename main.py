from display import *
from draw import *
from parser import *
from matrix import *
import math

screen = new_screen()
color = [ 0, 255, 0 ]
circles = []
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


x = 0
a = []
b = []
c = []
while (x < 215):
    if (x < 15 or x < 100 and x > 85):
        color = [0,0,255]
        add_circle(a, 250, 250, 0, x, 0.01)
    elif (x > 185 and x < 200):

        color = [255,0,0]
        add_circle(b, 250, 250, 0, x, 0.01)
    elif ( x < 215 and x > 200):

        color = [0,255,0]
        add_circle(c,250,250,0,x,0.01)
    x+=1

draw_lines(a, screen, [0,0,255])
draw_lines(b, screen, [255,0,0])
draw_lines(c, screen, [0,0,0])



#edges = []
#add_edge(edges,


#parse_file( 'script', edges, transform, screen, color )
display(screen)

