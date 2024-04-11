import math
import Package.Modules as mod

def initialization_equilateral_triangle():
    x = float(input("Enter the x coordinate for the equilateral triangle's bottom-left corner: "))
    y = float(input("Enter the y coordinate for the equilateral triangle's bottom-left corner: "))
    side_length = float(input("Enter the equilateral triangle's side length: "))
    equilateral_triangle = mod.Equilateral(True, x, y, x + side_length, y, (x + side_length) - (side_length / 2), (side_length**2 - (((x + side_length) - side_length / 2) - (x + side_length))**2)**(1/2) + y, 0, 0,
        x, y, x + side_length, y, x + side_length, y, (x + side_length) - (side_length / 2), (side_length**2 - (((x + side_length) - side_length / 2) - (x + side_length))**2)**(1/2) + y, (x + side_length) - (side_length / 2), (side_length**2 - (((x + side_length) - side_length / 2) - (x + side_length))**2)**(1/2) + y, x, y, 0, 0, 0, 0,
        60, 60, 60, 0,
        side_length, (side_length**2 - (side_length / 2)**2)**(1/2))
    print("Perimeter:", equilateral_triangle.compute_perimeter())
    print("Area:", equilateral_triangle.compute_area())
    print("Inner Angles:", equilateral_triangle.compute_inner_angles())
    print("Vertices:", equilateral_triangle.compute_vertices())

def initialization_isosceles_triangle():
    x = float(input("Enter the x coordinate for the isosceles triangle's bottom-left corner: "))
    y = float(input("Enter the y coordinate for the isosceles triangle's bottom-left corner: "))
    base_length = float(input("Enter the isosceles triangle's base length: "))
    equal_side_length = float(input("Enter the isosceles triangle's equal side length: "))
    isosceles_triangle = mod.Isosceles(False, x, y, x + base_length, y, (x + base_length) - ( base_length / 2), y + math.sqrt((equal_side_length)**2 - ((x + base_length) - ( x + base_length - (base_length / 2)))**2), 0, 0,
        x, y, x + base_length, y, x + base_length, y, (x + base_length) - ( base_length / 2), y + math.sqrt((equal_side_length)**2 - ((x + base_length) - ( x + base_length - (base_length / 2)))**2), (x + base_length) - ( base_length / 2), y + math.sqrt((equal_side_length)**2 - ((x + base_length) - ( x + base_length - (base_length / 2)))**2), x, y, 0, 0, 0, 0, 
        0, 0, 0, 0, 
        base_length, math.sqrt(equal_side_length**2 - (base_length / 2)**2))
    print("Area:", isosceles_triangle.compute_area())
    print("Perimeter:", isosceles_triangle.compute_perimeter())
    print("Inner Angles:", isosceles_triangle.compute_inner_angles())
    print("Vertices:", isosceles_triangle.compute_vertices())

def initialization_tri_rectangle():
    x = float(input("Enter the x coordinate for the triangle rectangle's bottom-left corner: "))
    y = float(input("Enter the y coordinate for the triangle rectangle's bottom-left corner: "))
    width = float(input("Enter the triangle rectangle's width: "))
    height = float(input("Enter the triangle rectangle's height: "))
    tri_rectangle = mod.TriRectangle(False, x, y, x + width, y, x, y + height, 0, 0,
        x, y, x + width, y, x + width, y, x, y + height, x, y + height, x, y, 0, 0, 0, 0,
        0, 0, 0, 0,
        width, height)
    print("Area:", tri_rectangle.compute_area())
    print("Perimeter:", tri_rectangle.compute_perimeter())
    print("Inner Angles:", tri_rectangle.compute_inner_angles())
    print("Vertices:", tri_rectangle.compute_vertices())

def initialization_scalene_triangle():
    x1 = float(input("Enter the x coordinate for the scalene triangle's first vertice: "))
    y1 = float(input("Enter the y coordinate for the scalene triangle's first vertice: "))
    x2 = float(input("Enter the x coordinate for the scalene triangle's second vertice: "))
    y2 = float(input("Enter the y coordinate for the scalene triangle's second vertice: "))
    x3 = float(input("Enter the x coordinate for the scalene triangle's third vertice: "))
    y3 = float(input("Enter the y coordinate for the scalene triangle's third vertice: "))
    scalene_triangle = mod.Scalene(False, x1, y1, x2, y2, x3, y3, 0, 0,
        x1, y1, x2, y2, x2, y2, x3, y3, x3, y3, x1, y1, 0, 0, 0, 0,
        0, 0, 0, 0,
        math.sqrt((x2 - x1)**2 + (y2 - y1)**2), 0)
        
    print("Area:", scalene_triangle.compute_area())
    print("Perimeter:", scalene_triangle.compute_perimeter())
    print("Inner Angles:", scalene_triangle.compute_inner_angles())
    print("Vertices:", scalene_triangle.compute_vertices())

def initialization_rectangle():
    x = float(input("Enter the x coordinate for the rectangle's bottom-left corner: "))
    y = float(input("Enter the y coordinate for the rectangle's bottom-left corner: "))
    width = float(input("Enter the rectangle's width: "))
    height = float(input("Enter the rectangle's height: "))

    rectangle = mod(True, x, y, x + width, y, x + width, y + height, x, y + height, #vertices
    x, y, x + width, y, x + width, y, x + width, y + height, x + width, y + height, x , y + height, x, y + height, x, y, #edges
    90, 90, 90, 90, #angles
    width, height) #width, height

    print("Area:", rectangle.compute_area())
    print("Perimeter:", rectangle.compute_perimeter())
    print("Inner Angles:", rectangle.compute_inner_angles())
    print("Vertices:", rectangle.compute_vertices())

    #def is_inside(self, point):
        #return self.vertice1.x <= point.x <= self.vertice3.x and self.vertice1.y <= point.y <= self.vertice3.y

def initialization_square():
    x = float(input("Enter the x coordinate for the square's bottom-left corner: "))
    y = float(input("Enter the y coordinate for the square's bottom-left corner: "))
    width = float(input("Enter the square's width: "))
    height = width
    square = mod.Square(True, x, y, x + width, y, x + width, y + height, x, y + height, #vertices
    x, y, x + width, y, x + width, y, x + width, y + height, x + width, y + height, x , y + height, x, y + height, x, y, #edges
    90, 90, 90, 90, #angles
    width, height) #width, height
    print("Area:", square.compute_area())
    print("Perimeter:", square.compute_perimeter())
    print("Inner Angles:", square.compute_inner_angles())
    print("Vertices:", square.compute_vertices())

if __name__ == "__main__":
    
    method = int(input("Enter the shape you want to create (1 for equilateral, 2 for isosceles, 3 for triangle rectangle, 4 for scalene, 5 for rectangle, 6 for square): "))
    if method == 1:
        initialization_equilateral_triangle()
    elif method == 2:
        initialization_isosceles_triangle()
    elif method == 3:
        initialization_tri_rectangle()
    elif method == 4:
        initialization_scalene_triangle()
    elif method == 5:
        initialization_rectangle()
    elif method == 6:
        initialization_square()
    else:
        print("Invalid option.")
    