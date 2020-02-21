WIDTH=1920
HEIGHT=1080

def draw():
    return

def on_mouse_move(pos, buttons):
    if mouse.LEFT in buttons:
        #screen.clear()
        radius=20
        screen.draw.filled_circle(pos, radius, (128, 0, 0))