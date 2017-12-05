import turtle

turtle.pensize(2)
colors=['red','yellow','blue','green']
turtle.setup(1300,800,0,0)
turtle.bgcolor('black')
turtle.speed(10)

for i in range(400):
    turtle.color(colors[i%4])
    turtle.forward(i*2)
    turtle.left(91)
