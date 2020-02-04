#AutoTraceDraw.py
import turtle as t
t.title('自动轨迹绘制')
t.setup(800,600)
t.pencolor("red")
t.pensize(5)
#数据读取
details = []
f = open("data.txt")
for line in f:
    line = line.replace("\n", "")
    details.append(list(map(eval,line.split(","))))
f.close()
#自动绘制
for i in range(len(details)):
    t.pencolor(details[i][3], details[i][4], details[i][5])
    t.fd(details[i][0])
    if details[i][1]:
        t.right(details[i][2])
    else:
        t.left(details[i][2])