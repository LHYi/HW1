alarmhour,alarmmin=eval(input("请输入响铃时间（时,分）："))
print("时钟启动，闹钟将在{}:{}时响起".format(alarmhour,alarmmin))
import turtle
import time
import random
import winsound
R=0.00
G=0.00
B=0.00
def changecolor():
    global R
    global G
    global B
    i = time.time()
    random.seed(i)
    R=random.random()
    random.seed(i+1)
    G=random.random()
    random.seed(i+2)
    B=random.random()
    return R,G,B
def drawgap():
    turtle.penup()
    turtle.fd(5)
def drawline(draw):
    drawgap()
    turtle.pendown() if draw else turtle.penup()
    turtle.pencolor(changecolor())
    turtle.fd(40)
    drawgap()
    turtle.right(90)
def drawdigit(digit):
    drawgap()
    drawline(True) if digit in [2,3,4,5,6,8,9] else drawline(False)
    drawline(True) if digit in [0,1,3,4,5,6,7,8,9] else drawline(False)
    drawline(True) if digit in [0,2,3,5,6,8,9] else drawline(False)
    drawline(True) if digit in [0,2,6,8,] else drawline(False)
    turtle.left(90)
    drawline(True) if digit in [0,4,5,6,8,9] else drawline(False)
    drawline(True) if digit in [0,2,3,5,6,7,8,9] else drawline(False)
    drawline(True) if digit in [0,1,2,3,4,7,8,9] else drawline(False)
    turtle.left(180)
    turtle.penup()
    turtle.fd(20)
def drawdate(date):
    turtle.pencolor(changecolor())
    for i in date:
        if i == '-':
            turtle.write('：',font = ("Arial",36, "normal"))
            turtle.pencolor(changecolor())
            turtle.fd(40)
        elif i == '+':
            turtle.write('：',font = ("Arial",36, "normal"))
            turtle.pencolor(changecolor())
            turtle.fd(40)
        elif i == '=':
            #turtle.write('：',font = ("Arial",36, "normal"))
            turtle.fd(40)
        else :
            drawdigit(eval(i))
def main():
    turtle.setup(800,350,200,200)
    turtle.penup()
    turtle.fd(-340)
    turtle.pensize(5)
    turtle.speed(7)
    turtle.hideturtle()
    while True:
        drawdate(time.strftime('%H-%M+%S=',time.localtime()))
        timenow=list(time.localtime())
        nowhour=timenow[3]
        nowmin=timenow[4]
        if nowhour==alarmhour and nowmin ==alarmmin:
            print("时间到")
            winsound.PlaySound('Intro',winsound.SND_ALIAS)
            break
        turtle.penup()
        turtle.fd(-570)
        turtle.clear()
main()
