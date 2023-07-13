#!/usr/bin/python3

class Square:
    def __init__(self, side_length=0):
        self.side_length = side_length

    def area(self):
        return self.side_length ** 2

    def perimeter(self):
        return 4 * self.side_length

    def __str__(self):
        return "Square(side_length={})".format(self.side_length)


if __name__ == "__main__":
    s = Square(side_length=12)
    print(s)
    print("Area:", s.area())
    print("Perimeter:", s.perimeter())
