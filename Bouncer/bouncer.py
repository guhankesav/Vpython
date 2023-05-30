from vpython import *
#GlowScript 2.7 VPython

# Set up the scene
scene = display(title="BOUNCE GAME:", width=450)

# Create the ball object
ball = sphere(pos=vec(0,0,0), size=vector(3,3,1), color=vector(1,0,0), radius=5)

# Create the background box
background = box(pos=vector(0,0,0), size=vector(50,44,.1), color=vec(0,1,2))

# Create the borders of the game area
borderTop = box(pos=vector(0,22,0), size=vector(50,3,3), color=color.blue)
borderRight = box(pos=vector(25,0,0), size=vector(3,47,3), color=color.blue)
borderLeft = box(pos=vector(-25,0,0), size=vector(3,47,3), color=color.blue)

# Create the paddle object
paddle = box(pos=vec(0,-20,0), size=vec(10,2,.2), color=vec(100,10,2), height=2)

# Set initial values
dt = .003
runTime = 3000
t = 0
run = True

# Function to display countdown
def countdown():
    for i in range(3):
        countdown = text(pos=vector(ball.pos.x+4,ball.pos.y-1,ball.pos.z+1), text=i+1, align='center', color=color.green)
        sleep(1)
        countdown.visible = False

# Call countdown function
countdown()

# Set initial ball velocity and other variables
ball.velocity = vector(10,10,0)
deltat = .005
score = 0
acceleration = 0.1
gameState = True
dt = .002
time = 0
scene.caption = "Score: " + score + "\n acceleration: " + "{:.2f}".format(acceleration)

# Main game loop
while gameState:
    time += dt
    
    # Update ball velocity based on acceleration
    if ball.velocity.y >= 0:
        ball.velocity.y += (acceleration*dt)
    else:
        ball.velocity.y -= (acceleration*dt)
        
    if ball.velocity.x > 0:
        ball.velocity.x += (acceleration*dt)
    else:
        ball.velocity.x -= (acceleration*dt)
    
    # Update ball position
    ball.pos = ball.pos + (ball.velocity)*dt
    
    # Update score and acceleration display
    scene.caption = "Score: " + score + "\n acceleration: " + "{:.2f}".format(acceleration)
    
    # Check if ball collides with the paddle
    if (ball.pos.x >= paddle.pos.x - paddle.length/2) and (ball.pos.x <= paddle.pos.x + paddle.length/2) and (ball.pos.y <= -18):
        ball.velocity.y = abs(ball.velocity.y)
        acceleration = acceleration + 0.5
        score += 1
    
    # Check if score reaches 5 for winning condition
    if score == 5:
        scene.caption = "Score: " + score + "\n acceleration: " + "{:.2f}".format(acceleration)
        scene.title = "You Win"
        gameState = False
        label(text=' YOU WON ', font='serif')
    
    rate(500)
    

    # Update paddle position based on mouse movement
    if scene.mouse.pos.x < 21 and scene.mouse.pos.x > -21:
        paddle.pos.x = scene.mouse.pos.x
    
    # Call wallCollision function to handle ball collisions with walls
    wallCollision()
    
    # Check if ball is below the paddle (game over condition)
    if ball.pos.y < -21:
        ball.velocity.x = 0
        ball.velocity.y = 0
        label(text='GAME OVER', font='serif')
        gameState = False
    
    # Function to handle ball collisions with walls
    def wallCollision():
        if ball.pos.x > borderRight.pos.x - 1.6:
            ball.velocity.x = -ball.velocity.x
            ball.pos = ball.pos + (ball.velocity)*dt
        if ball.pos.x < borderLeft.pos.x + 1.6:
            ball.velocity.x = -ball.velocity.x
            ball.pos = ball.pos + (ball.velocity)*dt
        if ball.pos.y > borderTop.pos.y - 1.6:
            ball.velocity.y = -ball.velocity.y
            ball.pos = ball.pos + (ball.velocity)*dt
        if ball.pos.y < -23:
            ball.velocity.y = -ball.velocity.y
            ball.pos = ball.pos + (ball.velocity)*dt
