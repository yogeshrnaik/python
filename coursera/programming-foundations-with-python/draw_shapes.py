import turtle

def draw_square(some_turtle):
    for i in range(1,5):
        some_turtle.forward(100)
        some_turtle.right(90)

def draw_circle():
    cir = turtle.Turtle()
    cir.shape("arrow")
    cir.color("green")
    cir.speed(5)
    cir.circle(100)

def draw_triangle():
    angie = turtle.Turtle()
    angie.speed(5)
    angie.shape("turtle")
    angie.color("blue")
    angie.forward(200)
    angie.left(120)
    angie.forward(200)
    angie.left(120)
    angie.forward(200)
    

def draw_shapes():
    window = turtle.Screen()
    window.bgcolor("white")
    
    brad = turtle.Turtle()  # creates a new object of Turtle class
    brad.shape("turtle")
    brad.color("red")
    brad.speed(5)

    for i in range(1,37):
        draw_square(brad)
        brad.right(10)
    
    #draw_circle()
    #draw_triangle()
    window.exitonclick()

draw_shapes()
