import turtle
ob=turtle.Turtle();
oc=turtle.Turtle();
od=turtle.Turtle();
oe=turtle.Turtle();

ob.speed(10000)
oc.speed(10000)
od.speed(10000)
oe.speed(10000)

ob.hideturtle()
oc.hideturtle()
od.hideturtle()
oe.hideturtle()

turtle.bgcolor("black")
ob.pencolor("blue")
oc.pencolor("red")
od.pencolor("green")
oe.pencolor("yellow")

oc.left(90)
od.left(180)
oe.left(270)

old=['f','l']
new=['f','l']
steps=[]
k=0
iterations=int(input("Iterations : "))
size=int(input("Size of lines : "))
while(k<iterations):
    for i in range(0,len(old)-1):
        if old[i]=='r':
            old[i]='l'
        elif old[i]=='l':
            old[i]='r'
    for i in range(0,len(old)//2):
        t=old[i]
        old[i]=old[len(old)-i-2]
        old[len(old)-i-2]=t
    for i in old:
        new.append(i)
    for i in old[:]:
        old.remove(i)
    for i in new:
        old.append(i)
    for i in steps[:]:
        steps.remove(i)
    for i in range(0,len(new)):
        steps.append(new[i])
    k+=1
for i in steps:
    if i=='f':
        ob.forward(size)
        oc.forward(size)
        od.forward(size)
        oe.forward(size)
    elif i=='r':
        ob.right(90)
        oc.right(90)
        od.right(90)
        oe.right(90)
    elif i=='l':
        ob.left(90)
        oc.left(90)
        od.left(90)
        oe.left(90)
    
