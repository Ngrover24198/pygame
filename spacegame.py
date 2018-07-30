import turtle
import os
import math
import random

wn=turtle.Screen()
wn.bgcolor("black")
wn.title("Space Invaders")

#draw border
border_pen=turtle.Turtle()
border_pen.speed(0) # 0 is the fastest speed here
border_pen.color("white")
border_pen.penup() # here if now we move the turtle in this program
# it will not draw anything as the pen is upward and is not writing anything
# visualise in 3d
border_pen.setposition(-300,-300)
border_pen.pendown()
border_pen.pensize(3)
for side in range(4):
 	border_pen.forward(600)
 	border_pen.left(90)
border_pen.hideturtle()

# SET THE SCORES TO 0
score=0

# Draw the score
score_pen= turtle.Turtle()
score_pen.speed(0)
score_pen.color("white")
score_pen.penup()
score_pen.setposition(-290,275)
scorestring = "Score: %s"%score
score_pen.write(scorestring, False, align="left",font=("Arial",14,"normal"))
score_pen.hideturtle()
#create the player turtle
player=turtle.Turtle()
player.color("blue")
player.shape("triangle")
player.penup()
player.speed(0)
player.setposition(0,-250)
player.setheading(90)

playerspeed=20


#Choose a number of enemies
number_of_enemies = 5
#Create an empty list of enemies
enemies= []

#Add enemies to list
for i in range(number_of_enemies):
	#Create the enemies
	enemies.append(turtle.Turtle())

#creating the enemy
#enemy=turtle.Turtle()
for enemy in enemies:
	enemy.color("red")
	enemy.shape("circle")
	enemy.penup()
	enemy.speed(0)
	x=random.randint(-200,200)
	y=random.randint(100,250)
	enemy.setposition(x,y)

enemyspeed = 2
#Create the player's bullet
bullet=turtle.Turtle()
bullet.color("yellow")
bullet.shape("circle")
bullet.penup()
bullet.speed(0)
bullet.setheading(90)
bullet.shapesize(0.4,0.4)
bullet.hideturtle()

bulletspeed=25

#Define bullet state
#ready- ready to fire
#fire - bullet is firing
bulletstate= "ready"


def move_left():
	x= player.xcor()
	x-=playerspeed
	if x<-280:
		x=-280
	player.setx(x)

def move_right():
	x= player.xcor()
	x+=playerspeed
	if x>280:
		x=280
	player.setx(x)

def fire_bullet():
	#declare bullet state as global if it needs change#create keyboard bindings
	global bulletstate
	if bulletstate== "ready":
		bulletstate="fire"	
		#Move the bullet to the just above the player
		x=player.xcor()
		y=player.ycor()+10
		bullet.setposition(x,y)
		bullet.showturtle()

def iscollision(t1,t2):
	distance= math.sqrt(math.pow(t1.xcor()-t2.xcor(),2)+math.pow(t1.ycor()-t2.ycor(),2))
	if distance<15:
		return True
	else:
		return False


#Create keyboard bindings
turtle.listen()
turtle.onkey(move_left,"Left")
turtle.onkey(move_right,"Right")
turtle.onkey(fire_bullet,"space") #space in this case is a small space instead of a capital one

#Main game loop
while True:# infinite loop
	
	for enemy in enemies:
		# Move the enemy
		x= enemy.xcor()
		x+=enemyspeed
		enemy.setx(x)

		# Move the enemy back and down
		if enemy.xcor()>280:
			# Moves all the enemies down
			for e in enemies:
				y=e.ycor()
				y-=40
				e.sety(y)
			# Change enemies direction
			enemyspeed *= -1
		
		if enemy.xcor() < -280:
			# Move all enemies down
			for e in enemies:
				y=e.ycor()
				y -= 40
				e.sety(y)
			# Change enemy direction	 
			enemyspeed *= -1

			#Check for a collision between the bullet and they enemy
		if iscollision(bullet,enemy):
			#Reset the bullet
			bullet.hideturtle()
			bulletstate="ready"
			bullet.setposition(0,-400)
			#Reset the enemy
			# it will again go to a random spot now
			x=random.randint(-200,200) 
			y=random.randint(100,250)
			enemy.setposition(x,y) 
			# Update the score
			score += 5
			scorestring= "Score: %s"%score
			score_pen.clear()
			score_pen.write(scorestring, False, align="left",font=("Arial",14,"normal"))

		if iscollision(player,enemy):
			player.hideturtle()
			enemy.hideturtle()
			print("GAME OVER...")
			break



	#Move the bullet
	if bulletstate=="fire":
		y = bullet.ycor()
		y += bulletspeed
		bullet.sety(y)

	#Check to see if the bullet has gone to the top
	if bullet.ycor()>275:
		bullet.hideturtle()
		bulletstate="ready"

	





