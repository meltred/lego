class Shape:
    vertices: int

    def __init__(self, v: int) -> None:
        self.vertices = v

class Shape3D(Shape):
    pass

def main():
    circle = Shape(0)
    rect = Shape(4)

    cuboid = Shape3D(8)

    print(circle.vertices)
    print(rect.vertices)
    print(cuboid.vertices)

if __name__=="__main__":
    main()