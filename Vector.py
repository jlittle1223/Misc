import turtle
import math

def get_side_lengths():
    x = float(input("Enter X length: "))
    y = float(input("Enter Y length: "))
    return x, y

def calculate_hypotenuse(x:float, y:float) -> float:
    return float((x**2 + y**2)**(1/2))

def print_side_lengths(x:float, y:float, hypotenuse:float):
    print("X:", x)
    print("Y:", y)
    print("Hypotenuse:", hypotenuse)

def find_angle(x:float, y:float) -> float:
    oa = (x/y)
    angle = math.degrees(math.atan(oa))
    print("Angle:", angle)
    return angle

def draw_triangle(x:float, y:float, hypotenuse:float, angle:float):
    drawingScale = 10
    turtle.forward(x*drawingScale)
    turtle.setheading(90)
    turtle.forward(y*drawingScale)
    turtle.home()
    #turtle.setheading(angle)
    #turtle.forward(hypotenuse*drawingScale)

def find_angle_and_hypotenuse():
    x, y = get_side_lengths()
    hypotenuse = calculate_hypotenuse(x, y)
    print_side_lengths(x, y, hypotenuse)
    angle = find_angle(x, y)
    draw_triangle(x, y, hypotenuse, angle)

def get_hypotenuse_and_angle() -> float:
    hypotenuse = float(input("Enter the hypotenuse length: "))
    angle = float(input("Enter the angle: "))
    return hypotenuse, angle

def find_x_component(hypotenuse:float, angle:float) -> float:
    x = hypotenuse * math.degrees(math.cos(angle))
    return x

def find_y_component(hypotenuse:float, angle:float) -> float:
    y = hypotenuse * math.degrees(math.sin(angle))
    return y


def find_x_and_y_components():
    hypotenuse, angle = get_hypotenuse_and_angle()
    x = find_x_component(hypotenuse, angle)
    y = find_y_component(hypotenuse, angle)
    print_side_lengths(x, y, hypotenuse)
    draw_triangle(x, y, hypotenuse, angle)
    


def main():
    find_angle_and_hypotenuse()
    #find_x_and_y_components()

    
main()
