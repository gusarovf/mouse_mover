import mouse
import time

def move(x, y):
    mouse.move(x,y, absolute=True, duration=0.5)

MOVE_POS = 5
OUTBOUNDS_POS = 7
ENABLE_MOVE_TIME = 3000
start_x, start_y = mouse.get_position()
sleeping_time = 0
outbounds = False

while(True):
    if not outbounds:
        current_x, current_y = mouse.get_position()
        new_x = start_x + MOVE_POS if int(start_x) == int(current_x) else start_x  

        diff_x = int(current_x) - int(start_x)
        diff_y = int(current_y) - int(start_y)
        outbounds = diff_x > OUTBOUNDS_POS or diff_y > OUTBOUNDS_POS 

        move(new_x, start_y)
    else:
        sleeping_time += 1000
        time.sleep(1)
        if(sleeping_time >= ENABLE_MOVE_TIME):
            pos = mouse.get_position()
            outbounds = False
            start_x = pos[0]
            start_y = pos[1]
            sleeping_time = 0

            