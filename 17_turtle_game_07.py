import math
import random
import turtle as t
from time import sleep
import threading

t.listen()
levelChanged = False
level = 3
myScore = 0
myTime = 25
myScreen = t.Screen()
myScreen.screensize(300, 300)
myScreen.bgcolor("azure4")
#********* Score Turtle Field ***************
myT_01= t.Turtle()
myT_01.hideturtle()
myT_01.teleport(0,280)
myT_01.color("black")
myT_01.write(f"*** Score : {int(myScore)} ***  *** Seviye : {int(4-level)} ***", align="center", font=("Arial", 20, "bold"))
#********** Time Turtle Field *****************
myT_02= t.Turtle()
myT_02.hideturtle()
myT_02.teleport(0,230)
myT_02.color("RosyBrown1")
myT_02.write(f"Time : {myTime}", align="center", font=("Arial", 20, "bold"))
#************ Aim Turtle Field **********
myT_03= t.Turtle()
myT_03.shape("turtle")
myT_03.color("green")
myT_03.shapesize(4)
#*********************************
myT_04 = t.Turtle()
myT_04.hideturtle()
#*********************************
def gamePlatform(platformColor="red"):
    myT_04.speed(0)
    myT_04.penup()
    myPenSize = 2
    myT_04.pensize(myPenSize)
    pRange = 230
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




gamePlatform("NavajoWhite")
def exitGame():
    t.bye()
def myTimeCounter():
  global myTime
  myTimeThread= threading.Timer(1.0, myTimeCounter)
  myTimeThread.daemon = True
  myTimeThread.start()
  if levelChanged:
      myT_02.clear()
  if not levelChanged:
      if myTime<0:
          myT_02.clear()
          myT_02.teleport(0, 30)
          myT_02.color("red")
          myT_02.write(f"Game Over !", align="center", font=("courier", 25, "bold"))
          myT_02.teleport(0, -300)
          t.listen()
          myT_02.color("blue")
          myT_02.write(f"Çıkış için 'Space' tuşunu kullanabilirsiniz !", align="center", font=("courier", 15))
          myScreen.onkey(exitGame, "space")
          myTimeThread.join()

      if myTime >= 0:
          print(f" in myTimeCounter : {myTime}")
          myT_02.clear()
          myT_02.write(f"Time : {myTime}", align="center", font=("Arial", 20, "bold"))
          myTime -= 1


def levelChangedFunction():
    gamePlatform("HotPink")
    global levelChanged
    levelChanged = True
    print(f"Level Changed in function : {levelChanged}")
    colorList = ["red", "pink","yellow","snow", "snow","yellow","pink","red"]
    for repeatPlatform in range(4):
        plusColor = 1

        for clr in colorList:
            print(f"color : {clr}")
            myT_03.hideturtle()
            myT_04.color(clr+str(plusColor))
            myT_04.teleport(0,-70)
            myT_04.write("\n\n\n\n\n   Tebrikler !!\n\nBir Üst Seviyeye\n\n    Geçtiniz", align="center", font=("Courier", 20, "bold"))
            sleep(.05)
            # myT_04.clear()
            myT_02.clear()
            myT_03.hideturtle()
            # myT_02.clear()
            myT_03.hideturtle()
        plusColor += 1

    myT_04.clear()



def level2():
    global levelChanged
    print("in now level2")
    myT_04.teleport(0,0)
    global level
    global myTime
    level = 2
    myT_03.clear()
    # myT_03.hideturtle()
    myT_02.clear()
    #**********************
    myTime= 20
    levelChangedFunction()
    # myTimeCounter()
    # runTurtle()
    myT_03.clear()
    myT_03.color("yellow")
    myT_03.shapesize(4)
    myT_01.clear()
    myT_01.color("darkblue")
    print(f"Level 2 level: {(4 - (math.floor(level)))}")
    myT_01.write(f"*** Score : {int(myScore)} ***  *** Seviye : {int(4-level)} ***", align="center", font=("Arial", 20, "bold"))
    myT_02.clear()
    levelChanged = False
    gamePlatform("LightSkyBlue")
    myTime= 20

def level3():
    global levelChanged
    levelChanged= True
    print("in now level3")
    myT_04.teleport(0,0)
    global  level
    global myTime
    level = 1.48
    myT_03.clear()
    myT_02.clear()
    myTime= 20
    #**********************#**********************
    levelChangedFunction()
    # myTimeCounter()
    # runTurtle()
    myT_03.color("red")
    myT_03.shapesize(4)
    myT_01.clear()
    myT_01.color("white")
    print(f"Level 3 level number: {level}")
    myT_01.write(f"*** Score : {int(myScore)} ***  *** Seviye : {(4-(math.floor(level)))} ***", align="center", font=("Arial", 20, "bold"))
    myT_02.clear()
    levelChanged = False
    gamePlatform("azure")
    myTime= 30


def scoreWriter(x,y):
    myT_03.hideturtle()
    global myScore
    myScore += 30/level
    myT_01.clear()
    myT_01.write(f"*** Score : {int(myScore)} ***  *** Seviye : {int(4-(math.floor(level)))} ***", align="center", font=("Arial", 20, "bold"))
    print(f"i am in scorewriter {myScore}")
    if myScore == 50:
        level2()
    if myScore == 110:
        level3()
    x_pos=x
    y_pos=y

def runTurtle():
   global levelChanged
   global level
   print("level changed in runTurtle(): {}".format(levelChanged))
   myTurtleThread= threading.Timer(level, runTurtle)
   myTurtleThread.daemon = True
   myTurtleThread.start()
   if levelChanged == True:
       myT_03.hideturtle()
   if levelChanged == False and myTime >=0:
           t03_x=  random.randint(-int(200/level),int(200/level))
           if t03_x >295:
               t03_x = 280
           if t03_x <-295:
               t03_x = -280
           t03_y= random.randint(-int(200/level),int(200/level))
           myT_03.teleport(t03_x,t03_y)
           myT_03.showturtle()
           sleep(level/2)
           myT_03.hideturtle()
   if levelChanged == False and myTime<0:
           myTurtleThread.join()





myTimeCounter()
myT_03.onclick(scoreWriter)

runTurtle()

t.mainloop()
