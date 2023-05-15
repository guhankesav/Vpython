GlowScript 3.0 VPython


scene = display(title="TABLE TENNIS :",width=450)

table_top = box (pos=vector(0,0,0), length=27.4, height=0.2, width=15.2, color=color.green) 

table_leg1 = box (pos = vector(13.7,-3.8,-7.6), length=0.5, height =7.6, width=0.5, color=color.red)
table_leg2 = box (pos = vector(13.7,-3.8,7.6), length = 0.5, height = 7.6, width=0.5, color=color.red)
table_leg3 = box (pos = vector(-13.7,-3.8,-7.6), length=0.5, height =7.6, width=0.5, color=color.red)
table_leg4 = box (pos = vector(-13.7,-3.8,7.6), length = 0.5, height = 7.6, width=0.5, color=color.red)

center_line = box (pos = vector(0, 0.1,0),length=27.4, height=0.01, width=0.5, color=color.white)
left_line = box (pos = vector(0, 0.1,7.5),length=27.4, height=0.01, width=0.5, color=color.white)
right_line = box (pos = vector(0, 0.1,-7.5),length=27.4, height=0.01, width=0.5, color=color.white)
bor_right_line = box (pos = vector(13.5, 0.1,0),length=0.5, height=0.01, width=15.2, color=color.white)
left_right_line = box (pos = vector(-13.5, 0.1,0),length=0.5, height=0.01, width=15.2, color=color.white)
bor_right_line = box (pos = vector(2, 0.1,0),length=0.5, height=0.01, width=15.2, color=color.white)
left_right_line = box (pos = vector(-2, 0.1,0),length=0.5, height=0.01, width=15.2, color=color.white)

scene.caption = "Score 5 points to win , don't leave the ball out of the table " 




net = box (pos= vector (0.1,1.7,0),length=0.1, height=0.3, width=15.2, color=vector(0,2,2))
net = box (pos= vector (-0.1,1.7,0),length=0.1, height=0.3, width=15.2, color=vector(0,2,2))
net = box (pos= vector (0.1,1.1,0),length=0.1, height=0.3, width=15.2, color=vector(0,2,2))
net = box (pos= vector (-0.1,1.1,0),length=0.1, height=0.3, width=15.2, color=vector(0,2,2))
net = box (pos= vector (0.1,.5,0),length=0.1, height=0.3, width=15.2, color=vector(0,2,2))
net = box (pos= vector (-0.1,.5,0),length=0.1, height=0.3, width=15.2, color=vector(0,2,2))


net_bar = box (pos= vector (0,.87,0),length=0.3, height=1.9, width=0.4, color=color.black)
net_barl = box (pos= vector (0,.87,-7.6),length=0.3, height=1.9, width=0.4, color=color.black)
net_barr = box (pos= vector (0,.87,7.6),length=0.3, height=1.9, width=0.4, color=color.black)



floor = box (pos = vector(0,-7.6,0), length=35.4, height=0.5, width=18, color = color.orange)

racket_face = box (pos=vector(13,2.1,-2), length=0.5, height=2.5, width=1.5, color=color.red)
racket_face1 = box (pos=vector(-13,2.1,-2), length=0.5, height=2.5, width=1.5, color=color.yellow)


ball = sphere (pos=vector(11,3,-3), radius=0.2, color=color.white)


racket_face.velocity = vector(0,0,0)

ball.velocity = vector(-10,-1,2)

dt = 0.01
Flag = 1

def countdown():
    for i in range(3):
        countdown = text(pos = vector(ball.pos.x+4,ball.pos.y-1,ball.pos.z+1),text=i+1,align='center', color=color.green)
        sleep(1)
        countdown.visible = False
countdown()
whileflag = 0
scoree = 0
while whileflag == 0:


    rate (75)
    ball.pos = ball.pos + ball.velocity*dt
    scene.caption = "Score: " + scoree

    if ball.pos.y < ball.radius:
        ball.velocity.y = abs(ball.velocity.y)
    else:
        ball.velocity.y = ball.velocity.y - 9.8*dt

#    if ball.pos.x <= racket_face.pos.x :
#        ball.velocity.x = ball.velocity.x + racket_face.velocity.x 
        
    if scene.mouse.pos.z<21 and scene.mouse.pos.z>-21:
        racket_face.pos.z  = - scene.mouse.pos.z
        racket_face1.pos.z  = scene.mouse.pos.z

    if (ball.pos.x == net.pos.x) and (ball.pos.y < net.pos.y):
        ball.velocity.x = abs(ball.velocity.x)
    
#    if racket_face.pos.x < 10:
#        racket_face.velocity = vector(0,0,0)
    

    if ball.pos.x > racket_face.pos.x - 1: 
        if ball.pos.z > racket_face.pos.z - racket_face.width/2:
            if ball.pos.z < racket_face.pos.z + racket_face.width/2 :
                ball.velocity.x = -(ball.velocity.x)
                ball.velocity.z = -(ball.velocity.z)
                scoree = scoree + 1
                if scoree == 5:
                    label(text='WIN',font='serif')
                    scene.caption = "Win " 
                    whileflag = 1
        else:
            Flag = 0

    if ball.pos.x < racket_face1.pos.x + 0.4: 
        if ball.pos.z > racket_face1.pos.z - racket_face1.width/2:
            if ball.pos.z < racket_face1.pos.z + racket_face1.width/2 :
                ball.velocity.x = -(ball.velocity.x)
                ball.velocity.z = -(ball.velocity.z)
                scoree = scoree +1
                if scoree == 5:
                    label(text='WIN',font='serif')
                    scene.caption = "Win " 
                    whileflag = 1
        else:
            Flag = 0

            
    if Flag == 0:
        label(text='GAME OVER: ',font='serif')
        whileflag = 1
        scene.caption = "Score: " + scoree + ": YOU LOSE "
        
    if ball.pos.x > 15:        
        ball.velocity = vector(0,0,0)
        whileflag = 1
        label(text='GAME OVER: ',font='serif')
        
    if ball.pos.x < -15:        
        ball.velocity = vector(0,0,0)
        whileflag = 1
        label(text='GAME OVER: ',font='serif')

        
    
        
        



   

    
