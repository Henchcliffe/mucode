from random import randint
from datetime import datetime
from datetime import timedelta

WIDTH = 1920
HEIGHT = 1080

class game:

    def __init__(self):
        self.radius = 0
        self.circlepos = (0, 0)
        self.score = 0
        self.endtime = datetime.now()
        self.timeleft = 0
        self.gametime = 10
        self.delay = 2.0
        self.colour = (0, 128, 0)

    def new_circle(self):
        self.radius = randint(WIDTH//100, WIDTH//10)
        self.circlepos = (randint(0+self.radius, WIDTH-self.radius),
                          randint(0+self.radius, HEIGHT-self.radius))
        clock.schedule_unique(self.new_circle, self.delay)
        return

    def update(self):
        if datetime.now() > self.endtime:
            self.timeleft = 0
            clock.unschedule(self.new_circle)
        else:
            self.timeleft = (self.endtime-datetime.now()).seconds

        if keyboard.a:
            self.endtime = datetime.now() + timedelta(seconds=self.gametime)
            self.score = 0
            self.new_circle()
        return

    def draw(self):
        screen.clear()
        screen.draw.text("Score="+str(self.score), (20, 20))
        screen.draw.text("Time="+str(self.timeleft), (100, 20))
        if self.timeleft > 0:
            screen.draw.filled_circle(self.circlepos, self.radius, self.colour)
        return

    def on_mouse_down(self, pos):
        diffx = pos[0] - self.circlepos[0]
        diffy = pos[1] - self.circlepos[1]
        if diffx**2 + diffy**2 <= self.radius**2:
            self.score += 1
        elif self.timeleft > 0 and self.score > 0:
            self.score -= 1
        self.new_circle()

def draw():
    game.draw()

def update():
    game.update()

def on_mouse_down(pos):
    game.on_mouse_down(pos)

game = game()