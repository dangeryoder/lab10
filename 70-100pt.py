##########################################
#                                        #
#             Draw a house!              #
#                                        #
##########################################

# Use create_line(), create_rectangle() and create_oval() to make a 
# drawing of a house using the tKinter Canvas widget.

# 70pt: House outline (roof and the house)
# 80pt: Square windows and a door
# 90pt: A door handle plus a chimney!
# 100pt: Green grass on the ground and a red house!

# Minus 5pts if your code has no comments
# Minus 10pts if you only commit once to github

from Tkinter import *
root = Tk()
drawpad = Canvas(root, width=800,height=600, background='white')
drawpad.grid(row=0, column=1)

# house & roof
square = drawpad.create_rectangle(200,200,500,500)
roofline1 = drawpad.create_line(180,220,350,50)
roofline2 = drawpad.create_line(350,50,520,220)

# windows & door
window1 = drawpad.create_rectangle(230,230,310,310)
window1line1 = drawpad.create_line(230,270,310,270)
window1line2 = drawpad.create_line(270,230,270,310)
window2 = drawpad.create_rectangle(470,230,390,310)
window2line1 = drawpad.create_line(470,270,390,270)
window2line2 = drawpad.create_line(430,230,430,310)
window3 = drawpad.create_rectangle(230,390,310,470)
window3line1 = drawpad.create_line(270,390,270,470)
window3line2 = drawpad.create_line(230,430,310,430) 
window4 = drawpad.create_rectangle(470,390,390,470)
window4line1 = drawpad.create_line(430,390,430,470)
window4line2 = drawpad.create_line(390,430,470,430)
door = drawpad.create_rectangle(320,500,380,400)

# handle & chimney
handle = drawpad.create_oval(330,460,340,450)
chimney1 = drawpad.create_line(440,60,440,140)
chimney2 = drawpad.create_line(440,60,480,60)
chimney3 = drawpad.create_line(480,60,480,180)


root.mainloop()
