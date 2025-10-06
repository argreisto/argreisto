import turtle
import time
import random

# Pengaturan awal
delay = 0.1
score = 0
high_score = 0

# Setup layar
wn = turtle.Screen()
wn.title("😱 Multo Game by Argreisto")
wn.bgcolor("black")
wn.setup(width=600, height=600)
wn.tracer(0)

# Pemain (Ular)
player = turtle.Turtle()
player.speed(0)
player.shape("square")
player.color("green")
player.penup()
player.goto(0, 0)
player.direction = "stop"

# Hantu (Multo)
ghost = turtle.Turtle()
ghost.speed(0)
ghost.shape("circle")
ghost.color("white")
ghost.penup()
ghost.goto(random.randint(-200, 200), random.randint(-200, 200))

# Skor
pen = turtle.Turtle()
pen.speed(0)
pen.color("white")
pen.penup()
pen.hideturtle()
pen.goto(0, 260)
pen.write("Score: 0  High Score: 0", align="center", font=("Courier", 16, "normal"))

# Fungsi gerak pemain
def go_up():
    if player.direction != "down":
        player.direction = "up"
def go_down():
    if player.direction != "up":
        player.direction = "down"
def go_left():
    if player.direction != "right":
        player.direction = "left"
def go_right():
    if player.direction != "left":
        player.direction = "right"

def move():
    if player.direction == "up":
        y = player.ycor()
        player.sety(y + 20)
    if player.direction == "down":
        y = player.ycor()
        player.sety(y - 20)
    if player.direction == "left":
        x = player.xcor()
        player.setx(x - 20)
    if player.direction == "right":
        x = player.xcor()
        player.setx(x + 20)

# Keyboard binding
wn.listen()
wn.onkeypress(go_up, "Up")
wn.onkeypress(go_down, "Down")
wn.onkeypress(go_left, "Left")
wn.onkeypress(go_right, "Right")

# Fungsi gerak hantu (ke arah pemain)
def move_ghost():
    gx, gy = ghost.xcor(), ghost.ycor()
    px, py = player.xcor(), player.ycor()

    if gx < px:
        gx += 10
    elif gx > px:
        gx -= 10
    if gy < py:
        gy += 10
    elif gy > py:
        gy -= 10
    ghost.goto(gx, gy)

# Game loop
while True:
    wn.update()

    # Gerak pemain
    move()
    move_ghost()

    # Tabrak dinding
    if player.xcor()>290 or player.xcor()<-290 or player.ycor()>290 or player.ycor()<-290:
        pen.clear()
        pen.write("💀 Kamu Nabrak Tembok! GAME OVER 💀", align="center", font=("Courier", 18, "bold"))
        time.sleep(2)
        player.goto(0,0)
        player.direction = "stop"
        ghost.goto(random.randint(-200, 200), random.randint(-200, 200))
        score = 0
        delay = 0.1
        pen.clear()
        pen.write(f"Score: {score}  High Score: {high_score}", align="center", font=("Courier", 16, "normal"))

    # Jika hantu menyentuh pemain
    if player.distance(ghost) < 20:
        pen.clear()
        pen.write("👻 Kena Multo! GAME OVER 👻", align="center", font=("Courier", 18, "bold"))
        time.sleep(2)
        player.goto(0,0)
        player.direction = "stop"
        ghost.goto(random.randint(-200, 200), random.randint(-200, 200))
        score = 0
        delay = 0.1
        pen.clear()
        pen.write(f"Score: {score}  High Score: {high_score}", align="center", font=("Courier", 16, "normal"))

    # Tambah skor tiap detik bertahan hidup
    score += 1
    if score > high_score:
        high_score = score

    pen.clear()
    pen.write(f"Score: {score}  High Score: {high_score}", align="center", font=("Courier", 16, "normal"))
    time.sleep(delay)

wn.mainloop()
