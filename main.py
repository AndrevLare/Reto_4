from math import (acos, pi)

class Point:
  def __init__(self, x=0, y=0):
    self.x = x
    self.y = y 
  def compute_distance(self, point: "Point")-> float:
    distance = ((self.x - point.x)**2+(self.y - point.y)**2)**(0.5)
    return distance
  def __str__(self):
      return f"({self.x}, {self.y})"


class Line():
    def __init__(self, start:"Point", end:"Point"):
        self.start = start
        self.end = end
        self.__lenght = ((end.x - start.x)**2 + (end.y - start.y)**2)**0.5
        self.__slope = (end.y - start.y)/(end.x - start.x) if (end.x - start.x) != 0 else "indefinida"
    def compute_length(self):
        return self.__lenght
    def __str__(self):
        return f"Line from {self.start} to {self.end}, length: {self.__lenght}, slope: {self.__slope}"
    
class Shape():
   def __init__(self, is_regular:bool, vertices:list["Point"], edges:list["Line"]):
      self._is_regular = is_regular
      self._edges = edges
      self._vertices = vertices
      self._inner_angles = self.compute_inner_angles()
      self._perimeter = self.compute_perimeter()
      self._area = self.compute_area()

   def get_edges(self):
      return self._edges
   def get_vertices(self):
      return self._vertices
   def get_is_regular(self):
      return self._is_regular
   def get_inner_angles(self):
      return self._inner_angles
   def get_perimeter(self):
      self._inner_angles = self.compute_perimeter()
   def get_area(self):
      self._perimeter = self.compute_area()
   
   def set_edges(self, edges:list["Line"]):
      self._edges = edges
   def set_vertices(self, vertices:list["Point"]):
      self._vertices = vertices
   def set_is_regular(self, is_regular:bool):
      self._is_regular = is_regular
   def set_inner_angles(self, inner_angles:list[float]):
      self._inner_angles = self.compute_inner_angles()
    
   def compute_perimeter(self):
      return sum([edge.compute_length() for edge in self._edges])
   def compute_area(self):
      pass
   def compute_inner_angles(self):
      pass
   def __str__(self):
        return (f"Vertices: {self._vertices},\n"
                f"Edges: {self._edges},\n"
                f"Is regular: {self._is_regular},\n"
                f"Inner angles: {self._inner_angles},\n"
                f"Perimeter: {self._perimeter},\nArea: {self._area}")
class Rectangle(Shape):
   def __init__(self, vertices:list["Point"], edges:list["Line"], is_regular = False):
      super().__init__(is_regular, vertices, edges)
   def compute_inner_angles(self):
        return [90, 90, 90, 90]
   def compute_area(self):
      return self._edges[0].compute_length() * self._edges[1].compute_length()
    
class Square(Rectangle):
    def __init__(self, vertices, edges):
       super().__init__(vertices, edges, True)
       
class Triangle(Shape):
    def __init__(self, is_regular, vertices, edges:list["Line"]):
       super().__init__(is_regular, vertices, edges)
    def compute_area(self):
        return (self._edges[0].compute_length() * self._edges[1].compute_length())/2
    def compute_inner_angles(self):
      alpha = ((acos(((self._edges[1].compute_length()**2)
                    +(self._edges[2].compute_length()**2)
                    -(self._edges[0].compute_length()**2))
                    /(2*self._edges[1].compute_length()*self._edges[2].compute_length())))
                    *(180/pi))
      betha = ((acos(((self._edges[2].compute_length()**2)
                    +(self._edges[0].compute_length()**2)
                    -(self._edges[1].compute_length()**2))
                    /(2*self._edges[2].compute_length()*self._edges[0].compute_length())))
                    *(180/pi))
      gamma = ((acos(((self._edges[1].compute_length()**2)
                    +(self._edges[0].compute_length()**2)
                    -(self._edges[2].compute_length()**2))
                    /(2*self._edges[1].compute_length()*self._edges[0].compute_length())))
                    *(180/pi))
      return [alpha, betha, gamma, alpha+betha+gamma]
    def compute_area(self) -> float:
        a = self._edges[0].compute_length()
        b = self._edges[1].compute_length()
        c = self._edges[2].compute_length()
        s = (a + b + c) / 2
        area = (s * (s - a) * (s - b) * (s - c))**0.5
        return area

class Equilateral(Triangle):
   def __init__(self, vertices, edge):
      super().__init__(True, vertices, [edge]*3)
class Isosceles(Triangle):
   def __init__(self, vertices, edge):
      super().__init__(False, vertices, [edge]*2 + [Line(vertices[0], vertices[2])])
class Scalene(Triangle):
   def __init__(self, vertices, edges):
      super().__init__(False, vertices, edges)
class TriRectangle(Triangle):
      def __init__(self, vertices, edges):
         super().__init__(False, vertices, edges)
      
rectangle = Rectangle([Point(0,0), Point(1,0), Point(1,1), Point(0,1)], [Line(Point(0,0), Point(1,0)), Line(Point(1,0), Point(1,1)), Line(Point(1,1), Point(0,1)), Line(Point(0,1), Point(0,0))])
print("Rectangle: ",rectangle, "\n\n\n")
square = Square([Point(0,0), Point(1,0), Point(1,1), Point(0,1)], [Line(Point(0,0), Point(1,0)), Line(Point(1,0), Point(1,1)), Line(Point(1,1), Point(0,1)), Line(Point(0,1), Point(0,0))])
print("Cuadrado: ",square, "\n\n\n")
triangle = Triangle(False, [Point(0,0), Point(1,0), Point(0,1)], [Line(Point(0,0), Point(1,0)), Line(Point(1,0), Point(0,1)), Line(Point(0,1), Point(0,0))])
print("Triángulo: ",triangle, "\n\n\n")
equilateral = Equilateral([Point(0,0), Point(1,0), Point(0.5, (3**0.5)/2)], Line(Point(0,0), Point(1,0)))
print("Equilátero: ",equilateral, "\n\n\n")
isosceles = Isosceles([Point(0,0), Point(1,0), Point(0.5, (3**0.5)/2)], Line(Point(0,0), Point(1,0)))
print("Isósceles: ",isosceles, "\n\n\n")
scalene = Scalene([Point(0,0), Point(1,0), Point(0.5, (3**0.5)/2)], [Line(Point(0,0), Point(1,0)), Line(Point(1,0), Point(0.5, (3**0.5)/2)), Line(Point(0.5, (3**0.5)/2), Point(0,0))])
print("Escaleno: ",scalene, "\n\n\n")