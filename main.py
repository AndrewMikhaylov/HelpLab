import math


class Figure:
    is_two_dimensional = True
    figure_perimetr = 0
    figure_square = 0
    figure_square_surface=0
    figure_square_base=0
    figure_height = 0
    figure_volume = 0

    def dimention(self):
        return self.is_two_dimensional

    def perimetr(self):
        if not self.is_two_dimensional:
            return None
        if self.figure_perimetr != 0:
            return self.figure_perimetr

    def square(self):
        if not self.is_two_dimensional:
            return None
        if self.figure_square != 0:
            return self.figure_square

    def squareSurface(self):
        if self.is_two_dimensional:
            return None
        if self.figure_square_surface!=0:
            return self.figure_square_surface

    def squareBase(self):
        if self.is_two_dimensional:
            return None
        if self.figure_square_base!=0:
            return self.figure_square_base

    def height(self):
        if self.is_two_dimensional:
            return None
        if self.figure_height!=0:
            return self.figure_height

    def volume(self):
        if self.figure_volume!=0:
            return self.figure_volume

class Triangle(Figure):
    def __init__(self, first_side: int, second_side: int, third_side: int):
        self.first_side = first_side
        self.second_side = second_side
        self.third_side=third_side
        self.is_two_dimensional = True

    def perimetr(self):
        super().perimetr()
        self.figure_perimetr = self.first_side+self.second_side+self.third_side
        return self.figure_perimetr

    def square(self):
        super().square()
        self.figure_square = math.sqrt(self.perimetr() * (self.perimetr() - self.first_side)* (self.perimetr() - self.second_side)* (self.perimetr() - self.third_side))
        return self.figure_square


class Rectangular(Figure):
    def __init__(self, first_side:int, second_side:int):
        self.first_side = first_side
        self.second_side = second_side
        self.is_two_dimensional = True

    def perimetr(self):
        super().perimetr()
        self.figure_perimetr = 2*self.first_side+2*self.second_side
        return self.figure_perimetr

    def square(self):
        super().square()
        self.figure_square = self.first_side*self.second_side
        return self.figure_square


class Trapeze(Figure):
    def __init__(self, first_base:int, second_base:int, right_side:int, left_side:int):
        self.first_base = first_base
        self.second_base=second_base
        self.right_side=right_side
        self.left_side=left_side
        self.is_two_dimensional = True

    def perimetr(self):
        super().perimetr()
        self.figure_perimetr = self.first_base+self.second_base+self.right_side+self.left_side
        return self.figure_perimetr

    def square(self):
        super().square()
        self.figure_square = ((self.first_base+self.second_base)/(self.second_base-self.first_base)/4) \
                             *math.sqrt((-self.first_base+self.second_base+self.right_side+self.left_side) \
                                        *(self.first_base-self.second_base+self.left_side-self.right_side) \
                                        *(self.first_base-self.second_base-self.left_side+self.right_side))
        return self.figure_square


class Parallelogram(Figure):
    def __init__(self, base:int, side:int, altitude_to_base:int):
        self.base = base
        self.side = side
        self. altitude_to_base = altitude_to_base
        self. is_two_dimensional = True


    def perimetr(self):
        super().perimetr()
        self.figure_perimetr = 2*self.base+2*self.side
        return self.figure_perimetr

    def square(self):
        super().square()
        self.figure_square = self.base*self.altitude_to_base
        return self.figure_square


class Circle(Figure):
    def __init__(self, radius:int):
        self.radius = radius
        self.is_two_dimensional=True

    def perimetr(self):
        super().perimetr()
        self.figure_perimetr = 2*math.pi*self.radius
        return self.figure_perimetr

    def square(self):
        super().square()
        self.figure_square = math.pi*self.radius*self.radius
        return  self.figure_square


class Ball(Figure):
    def __init__(self, radius:int):
        self.radius=radius
        self.is_two_dimensional = False

    def squareSurface(self):
        super().squareSurface()
        self.figure_square_surface = 4*math.pi*self.radius*self.radius
        return self.figure_square_surface

    def squareBase(self):
        super().squareBase()
        self.figure_square_base = 4 * math.pi * self.radius * self.radius
        return self.figure_square_base

    def height(self):
        super().height()
        self.figure_height = self.radius
        return self.figure_height

    def volume(self):
        super().volume()
        self.figure_volume = (4/3)*math.pi*self.radius*self.radius*self.radius
        return self.figure_volume


class TrianglePyramid(Triangle):
    def __init__(self, side:int, altitude:int):
        self.side = side
        self.altitude = altitude
        self.is_two_dimensional = False

    def squareSurface(self):
        super().squareSurface()
        self.figure_square_surface = 3*(math.sqrt(3)/4)*self.side*self.side
        return self.figure_square_surface

    def squareBase(self):
        super().squareBase()
        self.figure_square_base = (math.sqrt(3)/4)*self.side*self.side
        return self.figure_square_base

    def height(self):
        super().height()
        self.figure_height = self.altitude
        return self.figure_height

    def volume(self):
        super().volume()
        self.figure_volume = (self.altitude*self.side*self.side)/(4/math.sqrt(3))
        return self.figure_volume


class RectangularPyramid(Rectangular):
    def __init__(self, side: int, altitude: int):
        self.side = side
        self.altitude = altitude
        self.is_two_dimensional = False

    def squareSurface(self):
        super().squareSurface()
        self.figure_square_surface = 0.5*self.side*4*(self.altitude*self.altitude+0.25*self.side*self.side)
        return self.figure_square_surface

    def squareBase(self):
        super().squareBase()
        self.figure_square_base = self.side*self.side
        return self.figure_square_base

    def height(self):
        super().height()
        self.figure_height = self.altitude
        return self.figure_height

    def volume(self):
        super().volume()
        self.figure_volume = (1/3)*(self.altitude * self.side * self.side)
        return self.figure_volume


class RectangularParallelepiped(Rectangular):
    def __init__(self, first_base_side: int, second_base_side:int, altitude: int):
        self.first_base_side = first_base_side
        self.second_base_side=second_base_side
        self.altitude = altitude
        self.is_two_dimensional = False

    def squareSurface(self):
        super().squareSurface()
        self.figure_square_surface = 2*self.first_base_side*self.altitude+2*self.second_base_side*self.altitude
        return self.figure_square_surface

    def squareBase(self):
        super().squareBase()
        self.figure_square_base = self.first_base_side*self.second_base_side
        return self.figure_square_base

    def height(self):
        super().height()
        self.figure_height = self.altitude
        return self.figure_height

    def volume(self):
        super().volume()
        self.figure_volume = self.first_base_side*self.second_base_side*self.altitude
        return self.figure_volume


class Cone(Circle):
    def __init__(self, radius: int, altitude: int):
        self.radius = radius
        self.altitude = altitude
        self.is_two_dimensional =False

    def squareSurface(self):
        super().squareSurface()
        self.figure_square_surface = math.pi*self.radius*math.sqrt(self.radius*self.radius+self.altitude*self.altitude)
        return self.figure_square_surface

    def squareBase(self):
        super().squareBase()
        self.figure_square_base = math.pi*self.radius * self.radius
        return self.figure_square_base

    def height(self):
        super().height()
        self.figure_height = self.altitude
        return self.figure_height

    def volume(self):
        super().volume()
        self.figure_volume = (1/3)*math.pi*self.radius*self.radius*self.altitude
        return self.figure_volume


class TrianglePrism(Triangle):
    def __init__(self, first_base_side:int, second_base_side:int, third_base_side:int, altitude:int):
        self.first_base_side=first_base_side
        self.second_base_side=second_base_side
        self.third_base_side=third_base_side
        self.altitude = altitude
        self.is_two_dimensional = False

    def squareSurface(self):
        super().squareSurface()
        self.figure_square_surface = self.first_base_side*self.altitude+self.second_base_side*self.altitude+self.third_base_side*self.altitude
        return self.figure_square_surface

    def squareBase(self):
        super().squareBase()
        self.figure_square_base = math.sqrt((self.first_base_side+self.second_base_side+self.third_base_side)
                                            * ((self.first_base_side+self.second_base_side+self.third_base_side) - self.first_base_side)
                                            * ((self.first_base_side+self.second_base_side+self.third_base_side) - self.second_base_side)
                                            * ((self.first_base_side+self.second_base_side+self.third_base_side) - self.third_base_side))
        return self.figure_square_base

    def height(self):
        super().height()
        self.figure_height = self.altitude
        return self.figure_height

    def volume(self):
        super().volume()
        self.figure_volume = self.altitude*self.squareBase()
        return self.figure_volume

