import math
from abc import ABC, abstractmethod

class Shape(ABC):
    @abstractmethod
    def getArea(self) -> float:
        pass

    @abstractmethod
    def getPerimeter(self) -> float:
        pass

    @abstractmethod
    def getName(self) -> str:
        pass

class Point2D:
    def __init__(self, x: float, y: float):
        self.x = x
        self.y = y

    def __str__(self):
        return f"({self.x:.2f}, {self.y:.2f})"

class Circle(Shape):
    def __init__(self, center: Point2D, radius: float):
        self.center = center
        self.radius = radius
        self.name = "Circ"

    def getName(self) -> str:
        return self.name

    def getArea(self) -> float:
        return math.pi * (self.radius ** 2)

    def getPerimeter(self) -> float:
        return 2 * math.pi * self.radius

    def __str__(self):
        return f"Circ: C={self.center}, R={self.radius:.2f}"

class Rectangle(Shape):
    def __init__(self, p1: Point2D, p2: Point2D):
        self.p1 = p1
        self.p2 = p2
        self.name = "Rect"

    def getName(self) -> str:
        return self.name

    def getArea(self) -> float:
        width = abs(self.p1.x - self.p2.x)
        height = abs(self.p1.y - self.p2.y)
        return width * height

    def getPerimeter(self) -> float:
        width = abs(self.p1.x - self.p2.x)
        height = abs(self.p1.y - self.p2.y)
        return 2 * (width + height)

    def __str__(self):
        return f"Rect: P1={self.p1} P2={self.p2}"

def main():
    shapes = []

    while True:
        try:
            line = input()
            if not line:
                continue
            
            print("$" + line)
            
            args = line.split()
            cmd = args[0]

            if cmd == "end":
                break
            
            elif cmd == "circle":
                x, y, r = map(float, args[1:])
                shapes.append(Circle(Point2D(x, y), r))

            elif cmd == "rect":
                x1, y1, x2, y2 = map(float, args[1:])
                shapes.append(Rectangle(Point2D(x1, y1), Point2D(x2, y2)))

            elif cmd == "show":
                for s in shapes:
                    print(s)

            elif cmd == "info":
                for s in shapes:
                    print(f"{s.getName()}: A={s.getArea():.2f} P={s.getPerimeter():.2f}")

        except (EOFError, KeyboardInterrupt):
            break

if __name__ == "__main__":
    main()