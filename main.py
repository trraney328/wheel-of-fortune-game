import turtle
import math
import random
from threading import Timer

#TurtleCode

screen = turtle.Screen()                                                                                            
screen.tracer(False)
screen.colormode(1)
screen.setup(width = 1.0, height = 1.0)

canvas = turtle.getcanvas()

section_list = []

angle_list = [[-75.5,99.5],[15-75.5,15+99.5],[30-75.5,30+99.5],[45-75.5,45+99.5],                                   
              [60-75.5,60+99.5],[75-75.5,75+99.5],[90-75.5,90+99.5],[105-75.5,105+99],
              [120-75.5,120+99],[135-75.5,135+99],[150-75.5,150+99.5],[165-75.5,165+99.5],
              [180-75.5,180+99.5],[195-75.5,195+99.5],[210-75.5,210+99.5],[225-75.5,225+99.5],
              [240-75.5,240+99.5],[255-75.5,255+99.5],[270-75.5,270+99.5],[285-75.5,285+99.5],
              [300-75.5,300+99.5],[315-75.5,315+99.5],[330-75.5,330+99],[345-75.5,345+99.5]]

turtle.title("WHEEL OF FORTUNE")

screen.bgpic("GET A LIFE.png")

txt = canvas.create_text(480, -320, text = "GUESS", angle = 0, font = ("Arial", 25, "bold"),anchor = "center")      
txt = canvas.create_text(380, -328, text = "|", angle = 0, font = ("Arial", 20, "bold"),anchor = "center")
txt = canvas.create_text(380, -310, text = "V", angle = 0, font = ("Arial", 18, "bold"),anchor = "center")
txt = canvas.create_text(580, -328, text = "|", angle = 0, font = ("Arial", 20, "bold"),anchor = "center")
txt = canvas.create_text(580, -310, text = "V", angle = 0, font = ("Arial", 18, "bold"),anchor = "center")

tur = turtle.Turtle(visible = False)                                                                                
tur.begin_poly()
tur.sety(turtle.ycor()-300)
tur.circle(300,extent=15)
tur.home()
tur.end_poly()
screen.register_shape("section", tur.get_poly())
tur.clear()

tur = turtle.Turtle(visible = False)                                                                               
tur.begin_poly()
tur.circle(50)
tur.end_poly()
screen.register_shape("center", tur.get_poly())
tur.clear()

tur = turtle.Turtle(visible = False)                                                                               
tur.begin_poly()
tur.right(135)
tur.forward(30)
tur.right(135)
tur.forward(40)
screen.register_shape("pointer", tur.get_poly())
tur.clear()

tur = turtle.Turtle(visible = False)                                                                               
tur.begin_poly()
tur.right(90)
tur.forward(20)
tur.right(90)
tur.forward(30)
tur.right(90)
tur.forward(20)
screen.register_shape("box", tur.get_poly())
tur.clear()

def box(xaxis,yaxis):                                                                                              
  tur = turtle.Turtle("box")
  tur.penup()
  tur.goto(xaxis,yaxis)
  tur.fillcolor(0.2352,0.70196,0.44314)
  
def pointer():                                                                                                     
  tur = turtle.Turtle("pointer")
  tur.penup()
  tur.goto(0,306)
  tur.fillcolor(0.54510,0.27059,0.07451)
  screen.update()
    
def center():                                                                                                       
  tur = turtle.Turtle("center")
  tur.goto(-50,0)
  tur.fillcolor(0.40000,0.80392,0.66667)
  screen.update()
   
def wheel():                                                                                                       
  tur = turtle.Turtle("section")
  tur.setheading(7.5)
  tur.fillcolor(0,0.50196,0)
  section_list.append(tur)

  tur = turtle.Turtle("section")
  tur.setheading(22.5)
  tur.fillcolor(0.85490,0.43922,0.83922)
  section_list.append(tur)
  
  tur = turtle.Turtle("section")
  tur.setheading(37.5)
  tur.fillcolor(0,0,0)
  section_list.append(tur)

  tur = turtle.Turtle("section")
  tur.setheading(52.5)
  tur.fillcolor(0.85882,0.43922,0.57647)
  section_list.append(tur)

  tur = turtle.Turtle("section")
  tur.setheading(67.5)
  tur.fillcolor(0.13333,0.54510,0.13333)
  section_list.append(tur)

  tur = turtle.Turtle("section")
  tur.setheading(82.5)
  tur.fillcolor(0.00000,0.74902,1.00000)
  section_list.append(tur)

  tur = turtle.Turtle("section")
  tur.setheading(97.5)
  tur.fillcolor(0.86275,0.07843,0.23529)
  section_list.append(tur)

  tur = turtle.Turtle("section")
  tur.setheading(112.5)
  tur.fillcolor(0.85882,0.43922,0.57647)
  section_list.append(tur)

  tur = turtle.Turtle("section")
  tur.setheading(127.5)
  tur.fillcolor(0.88235,0.88235,0.00000)
  section_list.append(tur)

  tur = turtle.Turtle("section")
  tur.setheading(142.5)
  tur.fillcolor(0.85490,0.43922,0.83922)
  section_list.append(tur)
  
  tur = turtle.Turtle("section")
  tur.setheading(157.5)
  tur.fillcolor(1.00000,0.54902,0.00000)
  section_list.append(tur)

  tur = turtle.Turtle("section")
  tur.setheading(172.5)
  tur.fillcolor(0.00000,0.74902,1.00000)
  section_list.append(tur)

  tur = turtle.Turtle("section")
  tur.setheading(187.5)
  tur.fillcolor(0.86275,0.07843,0.23529)
  section_list.append(tur)

  tur = turtle.Turtle("section")
  tur.setheading(202.5)
  tur.fillcolor(0.88235,0.88235,0.00000)
  section_list.append(tur)

  tur = turtle.Turtle("section")
  tur.setheading(217.5)
  tur.fillcolor(0.13333,0.54510,0.13333)
  section_list.append(tur)

  tur = turtle.Turtle("section")
  tur.setheading(232.5)
  tur.fillcolor(0.75294,0.75294,0.75294)
  section_list.append(tur)

  tur = turtle.Turtle("section")
  tur.setheading(247.5)
  tur.fillcolor(0,0,0)
  section_list.append(tur)
  
  tur = turtle.Turtle("section")
  tur.setheading(262.5)
  tur.fillcolor(1.00000,0.54902,0.00000)
  section_list.append(tur)

  tur = turtle.Turtle("section")
  tur.setheading(277.5)
  tur.fillcolor(0.13333,0.54510,0.13333)
  section_list.append(tur)

  tur = turtle.Turtle("section")
  tur.setheading(292.5)
  tur.fillcolor(0.85882,0.43922,0.57647)
  section_list.append(tur)

  tur = turtle.Turtle("section")
  tur.setheading(307.5)
  tur.fillcolor(0.85490,0.43922,0.83922)
  section_list.append(tur)

  tur = turtle.Turtle("section")
  tur.setheading(322.5)
  tur.fillcolor(0.86275,0.07843,0.23529)
  section_list.append(tur)

  tur = turtle.Turtle("section")
  tur.setheading(337.5)
  tur.fillcolor(1.00000,1.00000,1.00000)
  section_list.append(tur)

  tur = turtle.Turtle("section")
  tur.setheading(352.5)
  tur.fillcolor(0.00000,0.74902,1.00000)
  section_list.append(tur)
  
def word(angle_list):                                                                                                                            
  txt = canvas.create_text(280*math.sin((angle_list[0][0])/180*math.pi), 280*math.cos((angle_list[0][0])/180*math.pi), text = 'Free', angle = (angle_list[0][1]), font = ("Arial", 10, "bold"),fill = "yellow",anchor = "center",tags = "word")
  txt = canvas.create_text(260*math.sin((angle_list[0][0])/180*math.pi), 260*math.cos((angle_list[0][0])/180*math.pi), text = 'PLAY', angle = (angle_list[0][1]), font = ("Arial", 14, "bold"),fill = "white",anchor = "center",tags = "word")

  txt = canvas.create_text(260*math.sin((angle_list[1][0])/180*math.pi), 260*math.cos((angle_list[1][0])/180*math.pi), text = '$', angle = (angle_list[1][1]), font = ("Arial", 11, "bold"),anchor = "center",tags = "word")
  txt = canvas.create_text(220*math.sin((angle_list[1][0])/180*math.pi), 220*math.cos((angle_list[1][0])/180*math.pi), text = '6', angle = (angle_list[1][1]), font = ("Arial", 18, "bold"),anchor = "center",tags = "word")
  txt = canvas.create_text(180*math.sin((angle_list[1][0])/180*math.pi), 180*math.cos((angle_list[1][0])/180*math.pi), text = '5', angle = (angle_list[1][1]), font = ("Arial", 18, "bold"),anchor = "center",tags = "word")
  txt = canvas.create_text(140*math.sin((angle_list[1][0])/180*math.pi), 140*math.cos((angle_list[1][0])/180*math.pi), text = '0', angle = (angle_list[1][1]), font = ("Arial", 18, "bold"),anchor = "center",tags = "word")

  txt = canvas.create_text(260*math.sin((angle_list[2][0])/180*math.pi), 260*math.cos((angle_list[2][0])/180*math.pi), text = 'B', angle = (angle_list[2][1]), font = ("Arial", 15, "bold"),fill = "white",anchor = "center",tags = "word")
  txt = canvas.create_text(240*math.sin((angle_list[2][0])/180*math.pi), 240*math.cos((angle_list[2][0])/180*math.pi), text = 'A', angle = (angle_list[2][1]), font = ("Arial", 14, "bold"),fill = "white",anchor = "center",tags = "word")
  txt = canvas.create_text(220*math.sin((angle_list[2][0])/180*math.pi), 220*math.cos((angle_list[2][0])/180*math.pi), text = 'N', angle = (angle_list[2][1]), font = ("Arial", 13, "bold"),fill = "white",anchor = "center",tags = "word")
  txt = canvas.create_text(200*math.sin((angle_list[2][0])/180*math.pi), 200*math.cos((angle_list[2][0])/180*math.pi), text = 'K', angle = (angle_list[2][1]), font = ("Arial", 12, "bold"),fill = "white",anchor = "center",tags = "word")
  txt = canvas.create_text(180*math.sin((angle_list[2][0])/180*math.pi), 180*math.cos((angle_list[2][0])/180*math.pi), text = 'R', angle = (angle_list[2][1]), font = ("Arial", 11, "bold"),fill = "white",anchor = "center",tags = "word")
  txt = canvas.create_text(160*math.sin((angle_list[2][0])/180*math.pi), 160*math.cos((angle_list[2][0])/180*math.pi), text = 'U', angle = (angle_list[2][1]), font = ("Arial", 10, "bold"),fill = "white",anchor = "center",tags = "word")
  txt = canvas.create_text(140*math.sin((angle_list[2][0])/180*math.pi), 140*math.cos((angle_list[2][0])/180*math.pi), text = 'P', angle = (angle_list[2][1]), font = ("Arial", 9, "bold"),fill = "white",anchor = "center",tags = "word")
  txt = canvas.create_text(120*math.sin((angle_list[2][0])/180*math.pi), 120*math.cos((angle_list[2][0])/180*math.pi), text = 'T', angle = (angle_list[2][1]), font = ("Arial", 8, "bold"),fill = "white",anchor = "center",tags = "word")

  txt = canvas.create_text(260*math.sin((angle_list[3][0])/180*math.pi), 260*math.cos((angle_list[3][0])/180*math.pi), text = '$', angle = (angle_list[3][1]), font = ("Arial", 11, "bold"),anchor = "center",tags = "word")
  txt = canvas.create_text(220*math.sin((angle_list[3][0])/180*math.pi), 220*math.cos((angle_list[3][0])/180*math.pi), text = '9', angle = (angle_list[3][1]), font = ("Arial", 18, "bold"),anchor = "center",tags = "word")
  txt = canvas.create_text(180*math.sin((angle_list[3][0])/180*math.pi), 180*math.cos((angle_list[3][0])/180*math.pi), text = '0', angle = (angle_list[3][1]), font = ("Arial", 18, "bold"),anchor = "center",tags = "word")
  txt = canvas.create_text(140*math.sin((angle_list[3][0])/180*math.pi), 140*math.cos((angle_list[3][0])/180*math.pi), text = '0', angle = (angle_list[3][1]), font = ("Arial", 18, "bold"),anchor = "center",tags = "word")

  txt = canvas.create_text(260*math.sin((angle_list[4][0])/180*math.pi), 260*math.cos((angle_list[4][0])/180*math.pi), text = '$', angle = (angle_list[4][1]), font = ("Arial", 11, "bold"),anchor = "center",tags = "word")
  txt = canvas.create_text(220*math.sin((angle_list[4][0])/180*math.pi), 220*math.cos((angle_list[4][0])/180*math.pi), text = '5', angle = (angle_list[4][1]), font = ("Arial", 18, "bold"),anchor = "center",tags = "word")
  txt = canvas.create_text(180*math.sin((angle_list[4][0])/180*math.pi), 180*math.cos((angle_list[4][0])/180*math.pi), text = '0', angle = (angle_list[4][1]), font = ("Arial", 18, "bold"),anchor = "center",tags = "word")
  txt = canvas.create_text(140*math.sin((angle_list[4][0])/180*math.pi), 140*math.cos((angle_list[4][0])/180*math.pi), text = '0', angle = (angle_list[4][1]), font =( "Arial", 18, "bold"),anchor = "center",tags = "word")

  txt = canvas.create_text(260*math.sin((angle_list[5][0])/180*math.pi), 260*math.cos((angle_list[5][0])/180*math.pi), text = '$', angle = (angle_list[5][1]), font = ("Arial", 11, "bold"),anchor = "center",tags = "word")
  txt = canvas.create_text(220*math.sin((angle_list[5][0])/180*math.pi), 220*math.cos((angle_list[5][0])/180*math.pi), text = '3', angle = (angle_list[5][1]), font = ("Arial", 18, "bold"),anchor = "center",tags = "word")
  txt = canvas.create_text(180*math.sin((angle_list[5][0])/180*math.pi), 180*math.cos((angle_list[5][0])/180*math.pi), text = '5', angle = (angle_list[5][1]), font = ("Arial", 18, "bold"),anchor = "center",tags = "word")
  txt = canvas.create_text(140*math.sin((angle_list[5][0])/180*math.pi), 140*math.cos((angle_list[5][0])/180*math.pi), text = '0', angle = (angle_list[5][1]), font = ("Arial", 18, "bold"),anchor = "center",tags = "word")

  txt = canvas.create_text(260*math.sin((angle_list[6][0])/180*math.pi), 260*math.cos((angle_list[6][0])/180*math.pi), text = '$', angle = (angle_list[6][1]), font = ("Arial", 11, "bold"),anchor = "center",tags = "word")
  txt = canvas.create_text(220*math.sin((angle_list[6][0])/180*math.pi), 220*math.cos((angle_list[6][0])/180*math.pi), text = '6', angle = (angle_list[6][1]), font = ("Arial", 18, "bold"),anchor = "center",tags = "word")
  txt = canvas.create_text(180*math.sin((angle_list[6][0])/180*math.pi), 180*math.cos((angle_list[6][0])/180*math.pi), text = '0', angle = (angle_list[6][1]), font = ("Arial", 18, "bold"),anchor = "center",tags = "word")
  txt = canvas.create_text(140*math.sin((angle_list[6][0])/180*math.pi), 140*math.cos((angle_list[6][0])/180*math.pi), text = '0', angle = (angle_list[6][1]), font = ("Arial", 18, "bold"),anchor = "center",tags = "word")

  txt = canvas.create_text(260*math.sin((angle_list[7][0])/180*math.pi), 260*math.cos((angle_list[7][0])/180*math.pi), text = '$', angle = (angle_list[7][1]), font = ("Arial", 11, "bold"),anchor = "center",tags = "word")
  txt = canvas.create_text(220*math.sin((angle_list[7][0])/180*math.pi), 220*math.cos((angle_list[7][0])/180*math.pi), text = '5', angle = (angle_list[7][1]), font = ("Arial", 18, "bold"),anchor = "center",tags = "word")
  txt = canvas.create_text(180*math.sin((angle_list[7][0])/180*math.pi), 180*math.cos((angle_list[7][0])/180*math.pi), text = '0', angle = (angle_list[7][1]), font = ("Arial", 18, "bold"),anchor = "center",tags = "word")
  txt = canvas.create_text(140*math.sin((angle_list[7][0])/180*math.pi), 140*math.cos((angle_list[7][0])/180*math.pi), text = '0', angle = (angle_list[7][1]), font = ("Arial", 18, "bold"),anchor = "center",tags = "word")
  
  txt = canvas.create_text(260*math.sin((angle_list[8][0])/180*math.pi), 260*math.cos((angle_list[8][0])/180*math.pi), text = '$', angle = (angle_list[8][1]), font = ("Arial", 11, "bold"),anchor = "center",tags = "word")
  txt = canvas.create_text(220*math.sin((angle_list[8][0])/180*math.pi), 220*math.cos((angle_list[8][0])/180*math.pi), text = '4', angle = (angle_list[8][1]), font = ("Arial", 18, "bold"),anchor = "center",tags = "word")
  txt = canvas.create_text(180*math.sin((angle_list[8][0])/180*math.pi), 180*math.cos((angle_list[8][0])/180*math.pi), text = '0', angle = (angle_list[8][1]), font = ("Arial", 18, "bold"),anchor = "center",tags = "word")
  txt = canvas.create_text(140*math.sin((angle_list[8][0])/180*math.pi), 140*math.cos((angle_list[8][0])/180*math.pi), text = '0', angle = (angle_list[8][1]), font = ("Arial", 18, "bold"),anchor = "center",tags = "word")

  txt = canvas.create_text(260*math.sin((angle_list[9][0])/180*math.pi), 260*math.cos((angle_list[9][0])/180*math.pi), text = '$', angle = (angle_list[9][1]), font = ("Arial", 11, "bold"),anchor = "center",tags = "word")
  txt = canvas.create_text(220*math.sin((angle_list[9][0])/180*math.pi), 220*math.cos((angle_list[9][0])/180*math.pi), text = '5', angle = (angle_list[9][1]), font = ("Arial", 18, "bold"),anchor = "center",tags = "word")
  txt = canvas.create_text(180*math.sin((angle_list[9][0])/180*math.pi), 180*math.cos((angle_list[9][0])/180*math.pi), text = '5', angle = (angle_list[9][1]), font = ("Arial", 18, "bold"),anchor = "center",tags = "word")
  txt = canvas.create_text(140*math.sin((angle_list[9][0])/180*math.pi), 140*math.cos((angle_list[9][0])/180*math.pi), text = '0', angle = (angle_list[9][1]), font = ("Arial", 18, "bold"),anchor = "center",tags = "word")

  txt = canvas.create_text(260*math.sin((angle_list[10][0])/180*math.pi), 260*math.cos((angle_list[10][0])/180*math.pi), text = '$', angle = (angle_list[10][1]), font = ("Arial", 11, "bold"),anchor = "center",tags = "word")
  txt = canvas.create_text(220*math.sin((angle_list[10][0])/180*math.pi), 220*math.cos((angle_list[10][0])/180*math.pi), text = '8', angle = (angle_list[10][1]), font = ("Arial", 18, "bold"),anchor = "center",tags = "word")
  txt = canvas.create_text(180*math.sin((angle_list[10][0])/180*math.pi), 180*math.cos((angle_list[10][0])/180*math.pi), text = '0', angle = (angle_list[10][1]), font = ("Arial", 18, "bold"),anchor = "center",tags = "word")
  txt = canvas.create_text(140*math.sin((angle_list[10][0])/180*math.pi), 140*math.cos((angle_list[10][0])/180*math.pi), text = '0', angle = (angle_list[10][1]), font = ("Arial", 18, "bold"),anchor = "center",tags = "word")

  txt = canvas.create_text(260*math.sin((angle_list[11][0])/180*math.pi), 260*math.cos((angle_list[11][0])/180*math.pi), text = '$', angle = (angle_list[11][1]), font = ("Arial", 11, "bold"),anchor = "center",tags = "word")
  txt = canvas.create_text(220*math.sin((angle_list[11][0])/180*math.pi), 220*math.cos((angle_list[11][0])/180*math.pi), text = '3', angle = (angle_list[11][1]), font = ("Arial", 18, "bold"),anchor = "center",tags = "word")
  txt = canvas.create_text(180*math.sin((angle_list[11][0])/180*math.pi), 180*math.cos((angle_list[11][0])/180*math.pi), text = '0', angle = (angle_list[11][1]), font = ("Arial", 18, "bold"),anchor = "center",tags = "word")
  txt = canvas.create_text(140*math.sin((angle_list[11][0])/180*math.pi), 140*math.cos((angle_list[11][0])/180*math.pi), text = '0', angle = (angle_list[11][1]), font = ("Arial", 18, "bold"),anchor = "center",tags = "word")

  txt = canvas.create_text(260*math.sin((angle_list[12][0])/180*math.pi), 260*math.cos((angle_list[12][0])/180*math.pi), text = '$', angle = (angle_list[12][1]), font = ("Arial", 11, "bold"),anchor = "center",tags = "word")
  txt = canvas.create_text(220*math.sin((angle_list[12][0])/180*math.pi), 220*math.cos((angle_list[12][0])/180*math.pi), text = '7', angle = (angle_list[12][1]), font = ("Arial", 18, "bold"),anchor = "center",tags = "word")
  txt = canvas.create_text(180*math.sin((angle_list[12][0])/180*math.pi), 180*math.cos((angle_list[12][0])/180*math.pi), text = '0', angle = (angle_list[12][1]), font = ("Arial", 18, "bold"),anchor = "center",tags = "word")
  txt = canvas.create_text(140*math.sin((angle_list[12][0])/180*math.pi), 140*math.cos((angle_list[12][0])/180*math.pi), text = '0', angle = (angle_list[12][1]), font = ("Arial", 18, "bold"),anchor = "center",tags = "word")
  
  txt = canvas.create_text(260*math.sin((angle_list[13][0])/180*math.pi), 260*math.cos((angle_list[13][0])/180*math.pi), text = '$', angle = (angle_list[13][1]), font = ("Arial", 11, "bold"),anchor = "center",tags = "word")
  txt = canvas.create_text(220*math.sin((angle_list[13][0])/180*math.pi), 220*math.cos((angle_list[13][0])/180*math.pi), text = '9', angle = (angle_list[13][1]), font = ("Arial", 18, "bold"),anchor = "center",tags = "word")
  txt = canvas.create_text(180*math.sin((angle_list[13][0])/180*math.pi), 180*math.cos((angle_list[13][0])/180*math.pi), text = '0', angle = (angle_list[13][1]), font = ("Arial", 18, "bold"),anchor = "center",tags = "word")
  txt = canvas.create_text(140*math.sin((angle_list[13][0])/180*math.pi), 140*math.cos((angle_list[13][0])/180*math.pi), text = '0', angle = (angle_list[13][1]), font = ("Arial", 18, "bold"),anchor = "center",tags = "word")    

  txt = canvas.create_text(260*math.sin((angle_list[14][0])/180*math.pi), 260*math.cos((angle_list[14][0])/180*math.pi), text = '$', angle = (angle_list[14][1]), font = ("Arial", 11, "bold"),anchor = "center",tags = "word")
  txt = canvas.create_text(220*math.sin((angle_list[14][0])/180*math.pi), 220*math.cos((angle_list[14][0])/180*math.pi), text = '5', angle = (angle_list[14][1]), font = ("Arial", 18, "bold"),anchor = "center",tags = "word")
  txt = canvas.create_text(180*math.sin((angle_list[14][0])/180*math.pi), 180*math.cos((angle_list[14][0])/180*math.pi), text = '0', angle = (angle_list[14][1]), font = ("Arial", 18, "bold"),anchor = "center",tags = "word")
  txt = canvas.create_text(140*math.sin((angle_list[14][0])/180*math.pi), 140*math.cos((angle_list[14][0])/180*math.pi), text = '0', angle = (angle_list[14][1]), font = ("Arial", 18, "bold"),anchor = "center",tags = "word")

  txt = canvas.create_text(260*math.sin((angle_list[15][0])/180*math.pi), 260*math.cos((angle_list[15][0])/180*math.pi), text = '$', angle = (angle_list[15][1]), font = ("Arial", 11, "bold"),anchor = "center",tags = "word")
  txt = canvas.create_text(220*math.sin((angle_list[15][0])/180*math.pi), 220*math.cos((angle_list[15][0])/180*math.pi), text = '5', angle = (angle_list[15][1]), font = ("Arial", 18, "bold"),anchor = "center",tags = "word")
  txt = canvas.create_text(180*math.sin((angle_list[15][0])/180*math.pi), 180*math.cos((angle_list[15][0])/180*math.pi), text = '0', angle = (angle_list[15][1]), font = ("Arial", 18, "bold"),anchor = "center",tags = "word")
  txt = canvas.create_text(140*math.sin((angle_list[15][0])/180*math.pi), 140*math.cos((angle_list[15][0])/180*math.pi), text = '0', angle = (angle_list[15][1]), font = ("Arial", 18, "bold"),anchor = "center",tags = "word")
  txt = canvas.create_text(100*math.sin((angle_list[15][0])/180*math.pi), 100*math.cos((angle_list[15][0])/180*math.pi), text = '0', angle = (angle_list[15][1]), font = ("Arial", 18, "bold"),anchor = "center",tags = "word")

  txt = canvas.create_text(260*math.sin((angle_list[16][0])/180*math.pi), 260*math.cos((angle_list[16][0])/180*math.pi), text = 'B', angle = (angle_list[16][1]), font = ("Arial", 15, "bold"),fill="white",anchor = "center",tags = "word")
  txt = canvas.create_text(240*math.sin((angle_list[16][0])/180*math.pi), 240*math.cos((angle_list[16][0])/180*math.pi), text = 'A', angle = (angle_list[16][1]), font = ("Arial", 14, "bold"),fill="white",anchor = "center",tags = "word")
  txt = canvas.create_text(220*math.sin((angle_list[16][0])/180*math.pi), 220*math.cos((angle_list[16][0])/180*math.pi), text = 'N', angle = (angle_list[16][1]), font = ("Arial", 13, "bold"),fill="white",anchor = "center",tags = "word")
  txt = canvas.create_text(200*math.sin((angle_list[16][0])/180*math.pi), 200*math.cos((angle_list[16][0])/180*math.pi), text = 'K', angle = (angle_list[16][1]), font = ("Arial", 12, "bold"),fill="white",anchor = "center",tags = "word")
  txt = canvas.create_text(180*math.sin((angle_list[16][0])/180*math.pi), 180*math.cos((angle_list[16][0])/180*math.pi), text = 'R', angle = (angle_list[16][1]), font = ("Arial", 11, "bold"),fill="white",anchor = "center",tags = "word")
  txt = canvas.create_text(160*math.sin((angle_list[16][0])/180*math.pi), 160*math.cos((angle_list[16][0])/180*math.pi), text = 'U', angle = (angle_list[16][1]), font = ("Arial", 10, "bold"),fill="white",anchor = "center",tags = "word")
  txt = canvas.create_text(140*math.sin((angle_list[16][0])/180*math.pi), 140*math.cos((angle_list[16][0])/180*math.pi), text = 'P', angle = (angle_list[16][1]), font = ("Arial", 9, "bold"),fill="white",anchor = "center",tags = "word")
  txt = canvas.create_text(120*math.sin((angle_list[16][0])/180*math.pi), 120*math.cos((angle_list[16][0])/180*math.pi), text = 'T', angle = (angle_list[16][1]), font = ("Arial", 8, "bold"),fill="white",anchor = "center",tags = "word")

  txt = canvas.create_text(260*math.sin((angle_list[17][0])/180*math.pi), 260*math.cos((angle_list[17][0])/180*math.pi), text = '$', angle = (angle_list[17][1]), font = ("Arial", 11, "bold"),anchor = "center",tags = "word")
  txt = canvas.create_text(220*math.sin((angle_list[17][0])/180*math.pi), 220*math.cos((angle_list[17][0])/180*math.pi), text = '3', angle = (angle_list[17][1]), font = ("Arial", 18, "bold"),anchor = "center",tags = "word")
  txt = canvas.create_text(180*math.sin((angle_list[17][0])/180*math.pi), 180*math.cos((angle_list[17][0])/180*math.pi), text = '0', angle = (angle_list[17][1]), font = ("Arial", 18, "bold"),anchor = "center",tags = "word")
  txt = canvas.create_text(140*math.sin((angle_list[17][0])/180*math.pi), 140*math.cos((angle_list[17][0])/180*math.pi), text = '0', angle = (angle_list[17][1]), font = ("Arial", 18, "bold"),anchor = "center",tags = "word")

  txt = canvas.create_text(260*math.sin((angle_list[18][0])/180*math.pi), 260*math.cos((angle_list[18][0])/180*math.pi), text = '$', angle = (angle_list[18][1]), font = ("Arial", 11, "bold"),anchor = "center",tags = "word")
  txt = canvas.create_text(220*math.sin((angle_list[18][0])/180*math.pi), 220*math.cos((angle_list[18][0])/180*math.pi), text = '5', angle = (angle_list[18][1]), font = ("Arial", 18, "bold"),anchor = "center",tags = "word")
  txt = canvas.create_text(180*math.sin((angle_list[18][0])/180*math.pi), 180*math.cos((angle_list[18][0])/180*math.pi), text = '0', angle = (angle_list[18][1]), font = ("Arial", 18, "bold"),anchor = "center",tags = "word")
  txt = canvas.create_text(140*math.sin((angle_list[18][0])/180*math.pi), 140*math.cos((angle_list[18][0])/180*math.pi), text = '0', angle = (angle_list[18][1]), font = ("Arial", 18, "bold"),anchor = "center",tags = "word")   

  txt = canvas.create_text(260*math.sin((angle_list[19][0])/180*math.pi), 260*math.cos((angle_list[19][0])/180*math.pi), text = '$', angle = (angle_list[19][1]), font = ("Arial", 11, "bold"),anchor = "center",tags = "word")
  txt = canvas.create_text(220*math.sin((angle_list[19][0])/180*math.pi), 220*math.cos((angle_list[19][0])/180*math.pi), text = '4', angle = (angle_list[19][1]), font = ("Arial", 18, "bold"),anchor = "center",tags = "word")
  txt = canvas.create_text(180*math.sin((angle_list[19][0])/180*math.pi), 180*math.cos((angle_list[19][0])/180*math.pi), text = '5', angle = (angle_list[19][1]), font = ("Arial", 18, "bold"),anchor = "center",tags = "word")
  txt = canvas.create_text(140*math.sin((angle_list[19][0])/180*math.pi), 140*math.cos((angle_list[19][0])/180*math.pi), text = '0', angle = (angle_list[19][1]), font = ("Arial", 18, "bold"),anchor = "center",tags = "word")

  txt = canvas.create_text(260*math.sin((angle_list[20][0])/180*math.pi), 260*math.cos((angle_list[20][0])/180*math.pi), text = '$', angle = (angle_list[20][1]), font = ("Arial", 11, "bold"),anchor = "center",tags = "word")
  txt = canvas.create_text(220*math.sin((angle_list[20][0])/180*math.pi), 220*math.cos((angle_list[20][0])/180*math.pi), text = '5', angle = (angle_list[20][1]), font = ("Arial", 18, "bold"),anchor = "center",tags = "word")
  txt = canvas.create_text(180*math.sin((angle_list[20][0])/180*math.pi), 180*math.cos((angle_list[20][0])/180*math.pi), text = '0', angle = (angle_list[20][1]), font = ("Arial", 18, "bold"),anchor = "center",tags = "word")
  txt = canvas.create_text(140*math.sin((angle_list[20][0])/180*math.pi), 140*math.cos((angle_list[20][0])/180*math.pi), text = '0', angle = (angle_list[20][1]), font = ("Arial", 18, "bold"),anchor = "center",tags = "word")

  txt = canvas.create_text(260*math.sin((angle_list[21][0])/180*math.pi), 260*math.cos((angle_list[21][0])/180*math.pi), text = '$', angle = (angle_list[21][1]), font = ("Arial", 11, "bold"),anchor = "center",tags = "word")
  txt = canvas.create_text(220*math.sin((angle_list[21][0])/180*math.pi), 220*math.cos((angle_list[21][0])/180*math.pi), text = '8', angle = (angle_list[21][1]), font = ("Arial", 18, "bold"),anchor = "center",tags = "word")
  txt = canvas.create_text(180*math.sin((angle_list[21][0])/180*math.pi), 180*math.cos((angle_list[21][0])/180*math.pi), text = '0', angle = (angle_list[21][1]), font = ("Arial", 18, "bold"),anchor = "center",tags = "word")
  txt = canvas.create_text(140*math.sin((angle_list[21][0])/180*math.pi), 140*math.cos((angle_list[21][0])/180*math.pi), text = '0', angle = (angle_list[21][1]), font = ("Arial", 18, "bold"),anchor = "center",tags = "word")

  txt = canvas.create_text(260*math.sin((angle_list[22][0])/180*math.pi), 260*math.cos((angle_list[22][0])/180*math.pi), text = 'LOSE', angle = (angle_list[22][1]), font = ("Arial", 11, "bold"),anchor = "center",tags = "word")
  txt = canvas.create_text(240*math.sin((angle_list[22][0])/180*math.pi), 240*math.cos((angle_list[22][0])/180*math.pi), text = 'A', angle = (angle_list[22][1]), font = ("Arial", 9, "bold"),anchor = "center",tags = "word")
  txt = canvas.create_text(210*math.sin((angle_list[22][0])/180*math.pi), 210*math.cos((angle_list[22][0])/180*math.pi), text = 'T', angle = (angle_list[22][1]), font = ("Arial", 18, "bold"),anchor = "center",tags = "word")
  txt = canvas.create_text(180*math.sin((angle_list[22][0])/180*math.pi), 180*math.cos((angle_list[22][0])/180*math.pi), text = 'U', angle = (angle_list[22][1]), font = ("Arial", 16, "bold"),anchor = "center",tags = "word")
  txt = canvas.create_text(160*math.sin((angle_list[22][0])/180*math.pi), 160*math.cos((angle_list[22][0])/180*math.pi), text = 'R', angle = (angle_list[22][1]), font = ("Arial", 13, "bold"),anchor = "center",tags = "word")
  txt = canvas.create_text(140*math.sin((angle_list[22][0])/180*math.pi), 140*math.cos((angle_list[22][0])/180*math.pi), text = 'N', angle = (angle_list[22][1]), font = ("Arial", 12, "bold"),anchor = "center",tags = "word")
  
  txt = canvas.create_text(260*math.sin((angle_list[23][0])/180*math.pi), 260*math.cos((angle_list[23][0])/180*math.pi), text = '$', angle = (angle_list[23][1]), font = ("Arial", 11, "bold"),anchor = "center",tags = "word")
  txt = canvas.create_text(218*math.sin((angle_list[23][0])/180*math.pi), 218*math.cos((angle_list[23][0])/180*math.pi), text = '7', angle = (angle_list[23][1]), font = ("Arial", 18, "bold"),anchor = "center",tags = "word")
  txt = canvas.create_text(180*math.sin((angle_list[23][0])/180*math.pi), 180*math.cos((angle_list[23][0])/180*math.pi), text = '0', angle = (angle_list[23][1]), font = ("Arial", 18, "bold"),anchor = "center",tags = "word")
  txt = canvas.create_text(140*math.sin((angle_list[23][0])/180*math.pi), 140*math.cos((angle_list[23][0])/180*math.pi), text = '0', angle = (angle_list[23][1]), font = ("Arial", 18, "bold"),anchor = "center",tags = "word")

def username(name1,name2,name3):                                                                                   
  txt = canvas.create_text(-500, -300, text = name1, angle = 0, font = ("Arial", 18),anchor = "center")
  txt = canvas.create_text(-500, -50, text = name2, angle = 0, font = ("Arial", 18),anchor = "center")
  txt = canvas.create_text(-500, 200, text = name3, angle = 0, font = ("Arial", 18),anchor = "center")

def cash_display(cash1,cash2,cash3):                                                                                
  txt = canvas.create_text(-500, -250, text = "$"+str(cash1), angle = 0, font = ("Arial", 25, "bold"), fill = "red", anchor = "center", tags = "cash")
  txt = canvas.create_text(-500, 0, text = "$"+str(cash2), angle = 0, font = ("Arial", 25, "bold"), fill = "red", anchor = "center", tags = "cash")
  txt = canvas.create_text(-500, 250, text = "$"+str(cash3), angle = 0, font = ("Arial", 25, "bold"), fill = "red", anchor = "center", tags = "cash")

def draw_letter(letter_list):                                                                                      
  for i in letter_list:
    txt = canvas.create_text(i[0] - 10, - i[1] - 15, text = i[2], angle = 0, font = ("Arial", 13),anchor = "center")
  canvas.update()
       
def draw_box(num_charlist):                                                                                         
  box_list = []
  yaxis = 250
  for e in num_charlist:
    yaxis -= 50
    xaxis = 335
    for num_box in range(0,e):
      xaxis += 23
      box(xaxis,yaxis)
      box_list.append([xaxis,yaxis])
  screen.update()
  return box_list

def turn_word():                                                                                                   
  a = angle_list[23]
  for i,e in reversed(list(enumerate(angle_list))):
    if i == 0:
      angle_list[0] = a
    else:
      angle_list[i] = angle_list[i - 1]
  word(angle_list)
  canvas.update()
  canvas.after(40,canvas.delete("word"))
  return angle_list
    
def turn_wheel(letter_list):                                                                                       
  a = section_list[0].color()
  for i,e in enumerate(section_list):
    if i == 23:
      section_list[23].color(*a)
    else:
      e.color(*section_list[(i + 1) % 24].color())
  screen.update()
  draw_letter(letter_list)

def all_turn(letter_list):                                                                                     
  max_section = random.randint(1,24)
  for section in range(0,24):
    turn_wheel(letter_list)
    angle_list = turn_word()
  for section in range(0,max_section):
    turn_wheel(letter_list)
    angle_list = turn_word()
  word(angle_list)
  canvas.update()
  return max_section

#GameCode

name_list = []

letter_list = []

total_section = 0

guess_consonant = 0

guess_vowel = 0

def time_up(time):                                                                                                 
  time[0] = True
    
def get_word():                                                                                                    
  player_continue = False
  while player_continue == False:
    player_ans = input("Get word? Y/N   ").lower()
    if player_ans == "y":
      player_continue = True
    else:
      player_continue = False
  num_charlist, phrase_charlist, vowel, consonant, phrase = choose_word()
  box_list = draw_box(num_charlist)
  word(angle_list)
  canvas.update()
  return player_continue, phrase_charlist, box_list, vowel, consonant, phrase

def spin_wheel(cash,can_play,total_section,letter_list):                                                        
  player_continue = False
  while player_continue == False:
    print("RULES: You only have 20 seconds to guess after spinning")
    print("")
    player_ans = input("Ready to SPIN WHEEL? Y/N   ").lower()
    if player_ans == "y":
      player_continue = True
    else:
      player_continue = False
  max_section = all_turn(letter_list)
  total_section += max_section
  true_section = total_section%24
  cash, cash_onhold, can_play = spin_result(true_section,cash,can_play)
  return cash, cash_onhold, can_play, total_section, true_section
  
def choose_word():                                                                                                 
  vowel = 0
  consonant = 0
  num_charlist = []
  num_char = 0
  word_count = 0
  file = open("WofFPhrases.txt","r")
  phrase_num = random.randint(0,74)
  for i,e in enumerate(file):
    if i == phrase_num:
      phrase = e.rstrip("\n")
  phrase_wordlist = phrase.split()
  phrase_charlist = list(phrase)
  for i in range(0,len(phrase_wordlist)):
    num_charlist.append(0)
  for e in phrase_charlist:
    if e.isupper() or e.islower():
      num_char += 1
      num_charlist[word_count] = num_char
    elif e == " ":
      word_count += 1
      num_char = num_char*0
  for e in phrase_charlist:
    if e == "a" or e == "e" or e == "i" or e == "o" or e == "u" or e == "A" or e == "E" or e == "I" or e == "O" or e == "U":
      vowel += 1
    elif e == " ":
      pass
    else:
      consonant += 1
  return num_charlist, phrase_charlist, vowel, consonant, phrase

def ask_consonant(phrase_charlist,box_list,cash,cash_onhold,can_play,letter_list,guess_consonant):         
  time = [False]
  num_consonant = 0
  player_correctinput = False
  t = Timer(20,time_up,args=(time,)) 
  t.start()
  while player_correctinput == False:
    player_guess = input("Enter a consonant:   ").upper()
    if player_guess != "A" and player_guess != "E" and player_guess != "I" and player_guess != "O" and player_guess != "U" and len(player_guess) == 1 and player_guess.isupper():
      player_correctinput = True
    else:
      print("Invalid, enter a consonant!")
      player_correctinput = False
  if time[0] == True :
    can_play = False
    return letter_list, cash, cash_onhold, can_play, time, guess_consonant
  else:
    t.cancel()
  for e in phrase_charlist:
    if e == " ":
      phrase_charlist.remove(e)
  if player_guess not in [j for i in letter_list for j in i]:
    for i,e in enumerate(phrase_charlist):
      if e == player_guess:
        guess_consonant += 1
        num_consonant += 1
        xaxis = box_list[i][0]
        yaxis = box_list[i][1]
        letter_list.append([xaxis,yaxis,e])
  if num_consonant >= 1:
    can_play = True
    cash = cash + cash_onhold*num_consonant
  else:
    can_play = False
  cash_onhold = cash_onhold*0
  draw_letter(letter_list)
  return letter_list, cash, cash_onhold, can_play, time, guess_consonant

def ask_anyletter(phrase_charlist,box_list,can_play,letter_list,guess_consonant,guess_vowel):                      
  time = [False]
  num_letter = 0
  t = Timer(20,time_up,args=(time,)) 
  t.start()
  player_correctinput = False
  while player_correctinput == False:
    player_guess = input("Enter a letter:   ").upper()
    if len(player_guess) == 1 and player_guess.isupper():
      player_correctinput = True
    else:
      print("Invalid, enter a letter!")
      player_correctinput = False
  if time[0] == True :
    can_play = False
    return letter_list, can_play, time, guess_consonant, guess_vowel
  else:
    t.cancel()
  for e in phrase_charlist:
    if e == " ":
      phrase_charlist.remove(e)
  if player_guess not in [j for i in letter_list for j in i]:
    for i,e in enumerate(phrase_charlist):
      if e == player_guess:
        num_letter += 1
        xaxis = box_list[i][0]
        yaxis = box_list[i][1]
        letter_list.append([xaxis,yaxis,e])
        if e == "A" or e == "E" or e == "I" or e == "O" or e == "U":
          guess_vowel += 1
        else:
          guess_consonant += 1            
  if num_letter >= 1:
    can_play = True
  else:
    can_play = False
  draw_letter(letter_list)
  return letter_list, can_play, time, guess_consonant, guess_vowel

def ask_vowel(phrase_charlist,box_list,cash,can_play,letter_list,guess_vowel):                                      
  time = [False]
  num_vowel = 0
  t = Timer(20,time_up,args=(time,)) 
  t.start()
  player_correctinput = False
  while player_correctinput == False:
    player_guess = input("Enter a vowel:   ").upper()
    if (player_guess == "A" or player_guess == "E" or player_guess == "I" or player_guess == "O" or player_guess == "U") and len(player_guess) == 1 and player_guess.isupper():
      player_correctinput = True
    else:
      print("Invalid, enter a vowel!")
      player_correctinput = False
  if time[0] == True :
    can_play = False
    return letter_list, cash, can_play, time, guess_vowel
  else:
    t.cancel()
  for e in phrase_charlist:
    if e == " ":
      phrase_charlist.remove(e)
  if player_guess not in [j for i in letter_list for j in i]:
    for i,e in enumerate(phrase_charlist):
      if e == player_guess:
        guess_vowel += 1
        num_vowel += 1
        xaxis = box_list[i][0]
        yaxis = box_list[i][1]
        letter_list.append([xaxis,yaxis,e])
  if num_vowel >= 1:
    can_play = True
    cash -= 250
  else:
    can_play = False
    cash -= 250
  draw_letter(letter_list)
  return letter_list, cash, can_play, time, guess_vowel

def solve_puzzle(phrase,phrase_charlist,box_list,can_play,letter_list):                                             
  time = [False]
  t = Timer(20,time_up,args=(time,)) 
  t.start()
  player_guess = input("Enter the whole phrase with spacing:   ").upper()
  if time[0] == True :
    can_play = False
    return letter_list, can_play, time
  else:
    t.cancel()
  if player_guess == phrase:
    for i,e in enumerate(phrase_charlist):
      xaxis = box_list[i][0]
      yaxis = box_list[i][1]
      letter_list.append([xaxis,yaxis,e])
    can_play = True
  else:
    can_play = False
  draw_letter(letter_list)
  return letter_list, can_play, time
            
def spin_result(section,cash,can_play):                                                                             
  cash_onhold = 0
  if section == 0:
    cash_onhold = 300
    can_play = True
  elif section == 1:
    cash_onhold = 500
    can_play = True
  elif section == 2:
    cash_onhold = 450
    can_play = True
  elif section == 3:
    cash_onhold = 500
    can_play = True
  elif section == 4:
    cash_onhold = 800
    can_play = True
  elif section == 6:
    cash_onhold = 700
    can_play = True
  elif section == 8:
    cash_onhold = 650
    can_play = True
  elif section == 10:
    cash_onhold = 900
    can_play = True
  elif section == 11:
    cash_onhold = 500
    can_play = True
  elif section == 12:
    cash_onhold = 350
    can_play = True
  elif section == 13:
    cash_onhold = 600
    can_play = True
  elif section == 14:
    cash_onhold = 500
    can_play = True
  elif section == 15:
    cash_onhold = 400
    can_play = True
  elif section == 16:
    cash_onhold = 550
    can_play = True
  elif section == 17:
    cash_onhold = 800
    can_play = True
  elif section == 18:
    cash_onhold = 300
    can_play = True
  elif section == 19:
    cash_onhold = 700
    can_play = True
  elif section == 20:
    cash_onhold = 900
    can_play = True
  elif section == 21:
    cash_onhold = 500
    can_play = True
  elif section == 22:
    cash_onhold = 5000
    can_play = True
  elif section == 23:
    cash = cash*0
    can_play = False
  elif section == 9:
    cash = cash*0
    can_play = False
  elif section == 5:
    can_play = False
  elif section == 7:
    can_play = True
  return cash, cash_onhold, can_play  

def option_one(e,total_section,letter_list,guess_consonant,guess_vowel):                                            
  cash, cash_onhold, can_play, total_section, true_section = spin_wheel(cash_d[e],canplay_d[e],total_section,letter_list)
  print("")
  cash_d[e] = cash
  cashonhold_d[e] = cash_onhold
  canplay_d[e] = can_play
  if true_section == 9 or true_section == 23:                                                                     
    print(">>> Oh No, you lost ALL your money and turn. Better luck next time! <<<")
    print("")
    canplay_d[name_list[(i+1)%3]] = True
    canvas.delete("cash")
    cash_display(cash_d[name1],cash_d[name2],cash_d[name3])
    canvas.update()
  elif true_section == 5:                                                                                         
    print(">>> You lost your turn, next player! <<<")
    print("")
    canplay_d[name_list[(i+1)%3]] = True
  elif true_section == 7:                                                                                     
    print(">>> Lucky you, guess ANY letter! <<<")
    print("")
    letter_list, can_play, time, guess_consonant, guess_vowel = ask_anyletter(phrase_charlist,box_list,canplay_d[e],letter_list,guess_consonant,guess_vowel)
    print("")
    canplay_d[e] = can_play
    if can_play == False and time[0] == False:
      print(">>> Wrong letter, but you may continue! <<<")
      print("")
      canplay_d[e] = True
    elif can_play == False and time[0] == True:
      print(">>> You've exceeded 20 seconds, next player! <<<")
      print("")
      canplay_d[e] = True
    else:
      print(">>> Way to go, your turn again! <<<")
      print("")
  else:                                                                                                         
    print(">>> You've hit [ $"+str(cash_onhold)+" ] <<<")
    print("")
    letter_list, cash, cash_onhold, can_play, time, guess_consonant = ask_consonant(phrase_charlist,box_list,cash_d[e],cashonhold_d[e],canplay_d[e],letter_list,guess_consonant)
    print("")
    cash_d[e] = cash
    cashonhold_d[e] = cash_onhold
    canplay_d[e] = can_play
    if can_play == False and time[0] == False:
      print(">>> Wrong consonant, next player! <<<")
      print("")
      canplay_d[name_list[(i+1)%3]] = True
    elif can_play == False and time[0] == True:
      print(">>> You've exceeded 20 seconds, next player! <<<")
      print("")
      canplay_d[name_list[(i+1)%3]] = True
    else:
      print(">>> Good guess, keep it rolling! <<<")
      print("")
      canvas.delete("cash")
      cash_display(cash_d[name1],cash_d[name2],cash_d[name3])
      canvas.update()
  return total_section, guess_consonant, guess_vowel

def option_two(e,total_section,letter_list,guess_vowel):                                                 
  letter_list, cash, can_play, time, guess_vowel = ask_vowel(phrase_charlist,box_list,cash_d[e],canplay_d[e],letter_list,guess_vowel)
  print("")
  cash_d[e] = cash
  canplay_d[e] = can_play
  if can_play == False and time[0] == False:
    print(">>> Wrong vowel, next player! <<<")
    print("")
    canplay_d[name_list[(i+1)%3]] = True
    canvas.delete("cash")
    cash_display(cash_d[name1],cash_d[name2],cash_d[name3])
    canvas.update()
  elif can_play == False and time[0] == True:
    print(">>> You've exceeded 20 seconds, next player! <<<")
    print("")
    canplay_d[name_list[(i+1)%3]] = True
  else:
    print(">>> You got it right! <<<")
    print("")
    canvas.delete("cash")
    cash_display(cash_d[name1],cash_d[name2],cash_d[name3])
    canvas.update()
  return total_section, guess_vowel

def option_three(e,phrase,player_continue,letter_list):                                                             
  letter_list, can_play, time = solve_puzzle(phrase,phrase_charlist,box_list,canplay_d[e],letter_list)
  print("")
  canplay_d[e] = can_play
  if can_play == False and time[0] == False:
    print(">>> Good try, but that's not the word! <<<")
    print("")
    canplay_d[name_list[(i+1)%3]] = True
  elif can_play == False and time[0] == True:
    print(">>> You've exceeded 20 seconds, next player! <<<")
    print("")
    canplay_d[name_list[(i+1)%3]] = True
  else:
    print(">>> CONGRATULATIONS!!!! <<<")
    print("")
    print(">>> "+e+" is the WINNER <<<")
    cash_d[name_list[(i+1)%3]] = cash_d[name_list[(i+1)%3]]*0
    cash_d[name_list[(i+2)%3]] = cash_d[name_list[(i+1)%3]]*0
    canvas.delete("cash")
    cash_display(cash_d[name1],cash_d[name2],cash_d[name3])
    canvas.update()
    player_continue = False
  return player_continue

#CoreCode        

print("")
print("                          Welcome to Wheel Of Fortune")
print("")

wheel()
pointer()
center()
screen.update()
word(angle_list)
canvas.update()

name1 = input("Please enter Player 1's name:   ")
name2 = input("Please enter Player 2's name:   ")
name3 = input("Please enter Player 3's name:   ")
print("")

cash_d = {name1:0,name2:0,name3:0}                                                                                  
cashonhold_d = {name1:0,name2:0,name3:0}
canplay_d = {name1:True,name2:False,name3:False}

username(name1,name2,name3)
cash_display(cash_d[name1],cash_d[name2],cash_d[name3])

name_list.append(name1)
name_list.append(name2)
name_list.append(name3)

player_continue, phrase_charlist, box_list, vowel, consonant, phrase = get_word()
print("")

for i,e in enumerate(name_list):                                                                                  
  if canplay_d[e] == True:
    print("-------------------------------------------------")
    print("")
    print("*** "+e+"'s Turn ***")
    print("")
    total_section, guess_consonant, guess_vowel = option_one(e,total_section,letter_list,guess_consonant,guess_vowel)
    break
    
while player_continue is True:
  for i,e in enumerate(name_list):
    if canplay_d[e] == True:
      print("-------------------------------------------------")
      print("")
      print("*** "+e+"'s Turn ***")
      print("")
      player_correctoption = False
      if consonant == guess_consonant and vowel != guess_vowel:                                               
        while player_correctoption == False:
          player_option = input("What do you want to do? \n1: (No more consonants) \n2: Buy vowel \n3: Solve the puzzle \nEnter number given:   ")
          print("")
          if player_option == "2" or player_option == "3":
            player_correctoption = True
          else:
            print("Invalid, enter an applicable number!")
            print("")
            player_correctoption == False
      elif vowel == guess_vowel and consonant != guess_consonant:                                            
        while player_correctoption == False:
          player_option = input("What do you want to do? \n1: Spin wheel \n2: (No more vowels) \n3: Solve the puzzle \nEnter number given:   ")
          print("")
          if player_option == "1" or player_option == "3":
            player_correctoption = True
          else:
            print("Invalid, enter an applicable number!")
            print("")
            player_correctoption == False
      else:
        while player_correctoption == False:
          player_option = input("What do you want to do? \n1: Spin wheel \n2: Buy vowel \n3: Solve the puzzle \nEnter number given:   ")
          print("")
          if player_option == "1" or player_option == "2" or player_option == "3":
            player_correctoption = True
          else:
            print("Invalid, enter number given!")
            print("")
            player_correctoption == False
      if player_option == "1":
        total_section, guess_consonant, guess_vowel = option_one(e,total_section,letter_list,guess_consonant,guess_vowel)
      elif player_option == "2" and cash_d[e] >= 250:
        total_section, guess_vowel = option_two(e,total_section,letter_list,guess_vowel)
      elif player_option == "2" and cash_d[e] < 250 and consonant != guess_consonant :
        print("You do not have enough money to buy a vowel!")
        print("")
        total_section, guess_consonant, guess_vowel = option_one(e,total_section,letter_list,guess_consonant,guess_vowel)
      elif player_option == "2" and cash_d[e] < 250 and consonant == guess_consonant :
        print("You do not have enough money to buy a vowel!")
        print("")
        player_continue = option_three(e,phrase,player_continue,letter_list)
      elif player_option == "3":
        player_continue = option_three(e,phrase,player_continue,letter_list)
      if consonant == guess_consonant and vowel == guess_vowel:
        print("-------------------------------------------------")
        print(">>> CONGRATULATIONS!!!! <<<")
        print("")
        print(">>> "+e+" is the WINNER <<<")
        cash_d[name_list[(i+1)%3]] = cash_d[name_list[(i+1)%3]]*0
        cash_d[name_list[(i+2)%3]] = cash_d[name_list[(i+1)%3]]*0
        canvas.delete("cash")
        cash_display(cash_d[name1],cash_d[name2],cash_d[name3])
        canvas.update()
        player_continue = False
