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
myScreen.screensize(800, 600)
myScreen.bgcolor("lightblue")
#********* Score Turtle Field ***************
myT_01= t.Turtle()
myT_01.hideturtle()
myT_01.teleport(0,280)
myT_01.color("black")
myT_01.write(f"*** Score : {int(myScore)}   *** Seviye : {int(4-level)}", align="center", font=("Arial", 20, "bold"))
#********** Time Turtle Field *****************
myT_02= t.Turtle()
myT_02.hideturtle()
myT_02.teleport(0,230)
myT_02.color("red")
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
          myT_02.teleport(0, -50)
          t.listen()
          myT_02.color("gray")
          myT_02.write(f"Çıkış için 'Space' tuşunu kullanabilirsiniz !", align="center", font=("courier", 15))
          myScreen.onkey(exitGame, "space")
          myTimeThread.join()

      if myTime >= 0:
          print(f" in myTimeCounter : {myTime}")
          myT_02.clear()
          myT_02.write(f"Time : {myTime}", align="center", font=("Arial", 20, "bold"))
          myTime -= 1


def levelChangedFunction():
    global levelChanged
    levelChanged= True
    print(f"Level Changed in function : {levelChanged}")
    colorList = ["red", "brown", "yellow", "blue", "pink"]
    for clr in colorList:
        print(f"color : {clr}")
        for i in range(3):
            myT_03.hideturtle()
            myT_04.color(str(clr)+str(i+1))
            myT_04.write("Tebrikler\nBir Üst Seviyeye\nGeçtiniz", align="center", font=("Courier", 20, "bold"))
            sleep(.1)
            myT_04.clear()
            myT_02.clear()
            myT_03.hideturtle()
        myT_04.clear()
        myT_02.clear()
        myT_03.hideturtle()



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
    myT_01.write(f"*** Score : {int(myScore)}   *** Seviye : {4 - int(level)}", align="center", font=("Arial", 20, "bold"))
    myT_02.clear()
    # myT_03.showturtle()
    levelChanged = False
    myTime= 20

def level3():
    global levelChanged
    levelChanged= True
    print("in now level3")
    myT_04.teleport(0,0)
    global  level
    global myTime
    level = 1.4
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
    myT_01.write(f"*** Score : {int(myScore)}   *** Seviye : {4 - int(level)}", align="center", font=("Arial", 20, "bold"))
    myT_02.clear()
    levelChanged = False
    myTime= 30
    # myT_03.showturtle()


def scoreWriter(x,y):
    global myScore
    myScore += 30/level
    myT_01.clear()
    myT_01.write(f"*** Score : {int(myScore)}   *** Seviye : {4-int(level)}", align="center", font=("Arial", 20, "bold"))
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
           t03_x=  random.randint(-int(300/level),int(300/level))
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

