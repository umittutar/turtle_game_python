import random
import turtle as t
from time import sleep

myScore =0
myTime = 20
myT_01= t.Turtle()
myT_01.hideturtle()
myScreen = t.Screen()
myScreen.screensize(800, 600)
myScreen.bgcolor('black')
myScreen.bgcolor('lightblue')
#********* Score Turtle Field ***************
myT_01.teleport(0,280)
myT_01.color('black')
myT_01.write(f"Score : {myScore}", align="center", font=("Arial", 25, "bold"))
#********** Time Turtle Field *****************
myT_02= t.Turtle()
myT_02.hideturtle()
myT_02.teleport(0,250)
myT_02.color('red')
myT_02.write(f"Time : {myTime}", align="center", font=("Arial", 20, "bold"))
#************ Aim Turtle Field **********
myT_03= t.Turtle()
myT_03.shape("turtle")
myT_03.shapesize(3)
myT_03.color('red')







def scoreWriter(x,y):
    myT_03.hideturtle()
    global myScore
    print(f"i am in scorewriter {myScore}")
    x_pos=x
    y_pos=y
    myScore += 10
    myT_01.clear()
    myT_01.write(f"Score : {myScore}", align="center", font=("Arial", 20, "bold"))

def runTurtle():
   if myTime >=0:
       t03_x=  random.randint(-300,300)
       t03_y= random.randint(-250,250)
       myT_03.teleport(t03_x,t03_y)
       myT_03.showturtle()
       sleep(1)
       print(myTime)
       timeWriter()
       myT_03.hideturtle()
       sleep(.5)
       print(myTime)
       timeWriter()
   else:
        myT_03.hideturtle()

   runTurtle()


def timeWriter():
    global myTime
    myTime-= 1
    if myTime > 0:
        # print(myTime)
        myT_02.color('red')
        myT_02.clear()
        myT_02.write(f"Time : {myTime}", align="center", font=("Arial", 20, "bold"))
    else:
        myT_02.teleport(0, 0)
        myT_02.write(f"Game Over !", align="center", font=("courier", 25, "bold"))
        myT_02.teleport(0, 30)
    runTurtle()

# def timeWriter():
#    # global myTime
#    myTime -= 1
#    if myTime > 0:
#         # print(myTime)
#         myT_02.color('red')
#         myT_02.clear()
#         myT_02.write(f"Time : {myTime}", align="center", font=("Arial", 20, "bold"))
#         # myScreen.update()
#
#         t.ontimer(timeWriter, 1000)
#    else:
#        myT_02.teleport(0, 0)
#        myT_02.write(f"Game Over !", align="center", font=("courier", 25, "bold"))
#        myT_02.teleport(0, 30)


# def myTimer():
#     print(myTime)
#     if myTime>0:
#         print(myTime)
#         timeWriter()
#     else:
#         myT_02.teleport(-100,0)
#         myT_02.write(f"Game Over !", align="center", font=("courier", 25, "bold"))



t.listen()
myT_03.onclick(scoreWriter)
runTurtle()
# timeWriter()
# if myTime>0:
#     runTurtle()


# myTimer()
t.mainloop()
