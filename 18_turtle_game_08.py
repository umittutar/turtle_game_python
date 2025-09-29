import math
import random
import turtle as t
from time import sleep

levelChanged = False
level = 3
myScore = 0
myTime = 20
myScreen = t.Screen()
myScreen.screensize(300, 300)
print(f"myScreen.window_height(): {myScreen.window_height()}")
print(f"myScreen.window_width() : {myScreen.window_width()}")
myScreen.bgcolor("azure4")
myScreen.title("Kaplumbağa Yakalamaca")
#********* Score Turtle Field ***************
myT_01= t.Turtle()
myT_01.hideturtle()
myT_01.teleport(0,280)
myT_01.color("black")
myT_01.write(f"*** Puan : {int(myScore)} ***  *** Seviye : {int(4-level)} ***", align="center", font=("Arial", 20, "bold"))
#********** Time Turtle Field *****************
myT_02= t.Turtle()
myT_02.hideturtle()
myT_02.teleport(0,250)
myT_02.color("RosyBrown1")
myT_02.write(f"Kalan Süre : {myTime}", align="center", font=("Arial", 20, "bold"))
#************ Aim Turtle Field **********
myT_03= t.Turtle()
myT_03.shape("turtle")
myT_03.color("green")
myT_03.shapesize(4)
#*********************************
myT_04 = t.Turtle()
myT_04.hideturtle()
myT_05= t.Turtle()

#*********************************

def gamePlatform(platformColor="red"):
    myT_04.clear()
    myT_04.teleport(0,0)
    global pRange
    myT_04.speed(0)
    myT_04.penup()
    pRange = 230
    myPenSize = 2
    myT_04.pensize(myPenSize)
    for repeatPlatform in range(4):
        myT_04.penup()
        myT_04.pensize(myPenSize)
        myColor = str(platformColor+str(4-repeatPlatform))
        myT_04.begin_fill()
        myT_04.color("Dodgerblue3",myColor)
        myT_04.goto(-pRange,pRange)
        myT_04.pendown()
        myT_04.forward(2*pRange)
        myT_04.right(90)
        myT_04.forward(2*pRange)
        myT_04.right(90)
        myT_04.forward(2*pRange)
        myT_04.right(90)
        myT_04.forward(2*pRange)
        myT_04.right(90)
        myT_04.end_fill()
        pRange -= 15
        myPenSize += 2
    myT_04.teleport(0,0)
def exitGame():
    t.bye()
def myTimeCounter():
  global myTime
  if levelChanged:
      myT_02.clear()
  if not levelChanged:
      if myTime<0:
          myT_03.hideturtle()
          myT_02.clear()
          myT_02.teleport(0, 30)
          myT_02.color("red")
          myT_02.teleport(0,-50)
          myT_02.write(f"\nOyun\nSonu", align="center", font=("courier", 30, "bold"))
          myT_02.teleport(0, -300)
          t.listen()
          myT_02.color("blue")
          myT_02.write(f"Çıkış için 'Space' tuşunu kullanabilirsiniz !", align="center", font=("courier", 15))
          myScreen.onkey(exitGame, "space")

      if myTime >= 0:
          print(f" in myTimeCounter : {myTime}")
          myT_02.clear()
          myT_02.write(f"Kalan Süre : {myTime}", align="center", font=("Arial", 20, "bold"))
          myTime -= 1
          t.ontimer(myTimeCounter, 1000)
def levelChangedFunction():
    gamePlatform("HotPink")
    global levelChanged
    levelChanged = True
    print(f"Level Changed in function : {levelChanged}")
    myT_04.teleport(0,-70)
    colorList = ["red", "pink","yellow","snow", "snow","yellow","pink","red"]
    for repeatPlatform in range(4):
        plusColor = 1

        for clr in colorList:
            myT_03.hideturtle()
            myT_04.color(clr+str(plusColor))
            myT_04.write("\n\n\n\n\n   Tebrikler !!\n\nBir Üst Seviyeye\n\n    Geçtiniz", align="center", font=("Courier", 20, "bold"))
            sleep(.05)
            myT_02.clear()
            myT_03.hideturtle()
        plusColor += 1
    myT_04.clear()
def level2():
    global levelChanged,level, myTime, pRange
    levelChanged = True
    myT_04.teleport(0,0)
    myT_03.hideturtle()
    myT_03.clear()
    myT_03.color("yellow")
    myT_03.shapesize(3)
    print("in now level2")
    level = 2
    myT_02.clear()
    myT_02.teleport(0, 250)
    #**********************
    levelChangedFunction()
    #**********************
    myT_01.clear()
    myT_01.color("darkblue")
    print(f"Level 2 level: {(4 - (math.floor(level)))}")
    myT_01.write(f"*** Puan : {int(myScore)} ***  *** Seviye : {int(4-(math.floor(level)))} ***", align="center", font=("Arial", 20, "bold"))
    levelChanged = False
    pRange =240
    gamePlatform("LightSkyBlue")
    myTime= 20
def level3():
    global levelChanged, level, myTime
    levelChanged= True
    myT_04.teleport(0,0)
    myT_03.hideturtle()
    myT_03.clear()
    myT_03.color("red")
    myT_03.shapesize(2)
    print("in now level3")
    level = 1.48
    myT_02.clear()
    myT_02.teleport(0, 250)
    #**********************#**********************
    levelChangedFunction()
    #**********************#**********************
    myT_01.clear()
    myT_01.color("white")
    print(f"Level 3 level number: {4-(math.floor(level))}")
    myT_01.write(f"*** Puan : {int(myScore)} ***  *** Seviye : {(4-(math.floor(level)))} ***", align="center", font=("Arial", 20, "bold"))
    levelChanged = False
    gamePlatform("azure")
    myTime= 25
def level4():
    global levelChanged, level, myTime
    levelChanged= True
    myT_04.teleport(0,0)
    myT_03.hideturtle()
    myT_03.clear()
    myT_03.color("black")
    myT_03.shapesize(2)
    print("in now level4")
    level = .6
    myT_02.clear()
    myT_02.teleport(0, 250)
    #**********************#**********************
    levelChangedFunction()
    #**********************#**********************
    myT_01.clear()
    myT_01.color("pink")
    print(f"Level 4 level number: {4-(math.floor(level))}")
    myT_01.write(f"*** Puan : {int(myScore)} ***  *** Seviye : {(4-(math.floor(level)))} ***", align="center", font=("Arial", 20, "bold"))
    levelChanged = False
    gamePlatform("honeydew")
    myTime= 25

def scoreWriter(x,y):
    myT_03.hideturtle()
    global myScore
    print(f"level {(4-(math.floor(level)))} Hit Value is: {math.floor(30/level)}")
    myScore += math.floor(30/level)
    print(f"Score : {myScore}")
    myT_01.clear()
    myT_01.write(f"*** Puan : {int(myScore)} ***  *** Seviye : {int(4-(math.floor(level)))} ***", align="center", font=("Arial", 20, "bold"))
    print(f"i am in scorewriter {myScore}")
    if myScore == 100:
        level2()
        myTimeCounter()
    if myScore == 220:
        level3()
        myTimeCounter()
    if myScore == 360:
        level4()
        myTimeCounter()
    x_pos=x
    y_pos=y
def runTurtle():
   myT_03.hideturtle()
   global levelChanged
   global level
   print("level changed in runTurtle(): {}".format(levelChanged))
   t.ontimer(runTurtle,(int(level*750)))
   if levelChanged == True:
       myT_03.hideturtle()
   if levelChanged == False and myTime >=0:
           t03_x=  random.randint(-int(200/round(level)),int(200/round(level)))
           if t03_x >150:
               t03_x = 150
           if t03_x <-150:
               t03_x = -150
           t03_y= random.randint(-int(200/round(level)),int(200/round(level)))
           if t03_y>150:
               t03_y = 150
           if t03_y <-150:
               t03_y = -150
           myT_03.teleport(t03_x,t03_y)
           print(f"t03_x : {t03_x}")
           print(f"t03_y : {t03_y}")
           myT_03.showturtle()

   if levelChanged == False and myTime<0:
       myTimeCounter()


gamePlatform("NavajoWhite")
myTimeCounter()
myT_03.onclick(scoreWriter)
runTurtle()
t.mainloop()