import turtle
ob=turtle.Turtle();
ob.speed(10000)
ob.hideturtle()
turtle.bgcolor("black")
ob.pencolor("teal")
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
    elif i=='r':
        ob.right(90)
    elif i=='l':
        ob.left(90)

