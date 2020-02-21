from random import randint
from datetime import datetime
from datetime import timedelta

radius=0
circlepos=(0,0)
score=0
endtime=datetime.now()

WIDTH=1920
HEIGHT=1080

def update():
    global endtime
    global timeleft
    global score
    if datetime.now()>endtime:
        timeleft=0
        clock.unschedule(new_circle)
    else:
        timeleft=(endtime-datetime.now()).seconds

    if keyboard.a:
        endtime=datetime.now()+timedelta(seconds=10)
        score=0
        new_circle()
    return

def draw():
    screen.clear()
    screen.draw.text("Score="+str(score), (20, 20))
    screen.draw.text("Time="+str(timeleft), (100, 20))
    if timeleft>0:
        screen.draw.filled_circle(circlepos, radius, (0, 128, 0))
    return

def new_circle():
    global radius
    global circlepos
    radius=randint(20,200)
    circlepos=(randint(0+radius,WIDTH-radius),randint(0+radius,HEIGHT-radius))
    clock.schedule_unique(new_circle,2.0)
    return

def on_mouse_down(pos):
    global score

    diffx=pos[0]-circlepos[0]
    diffy=pos[1]-circlepos[1]
    if diffx**2+diffy**2<=radius**2:
        score+=1
    else:
        score-=1
        if score<0:
            score=0
    new_circle()



