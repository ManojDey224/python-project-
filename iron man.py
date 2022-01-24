from pywhatkit import image_to_ascii_art as a 
img_path = 'ironman.jpg'
text = 'ironman.txt'        #creating a text file 
a(img_path, text)


import turtle as t 
s_x = -320                  #setting the x and y coordinates
s_y = 250

p = t.Pen()
t.bgcolor('black')
p.up()
p.width(2)
f_m = 0
d_m = 4

# function to select the color
def set_col(c):
    chars = {"*": 'white', "S" : 'green', "#" : 'green', "&" : 'white', "@":'black', "$" : 'white', "%" : 'white', "!":'blue', ":" :'darkgreen', ".":'grey'}
    col = chars[c]
    p.pencolor(col)

def d(m, s_char):
     p.up()
     if s_char != '\n':
         set_col(s_char)

     p.goto(s_x- m, s_y )
     p.down()
     p.forward(1)

text = open(text, 'r')
te = text.readlines()
for i in te:
    for j in i:
        d(f_m, j)
        f_m -= 4
    s_y -= 9
    s_x = -320
    f_m = 0
    d_m = 4

t.done()
print('completed')

