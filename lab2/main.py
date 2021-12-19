from lab_python_oop.rectangle import Rectangle
from lab_python_oop.circle import Circle
from lab_python_oop.square import Square
import sympy


def main():
    r = Rectangle("синего", 13, 13)
    c = Circle("зеленого", 13)
    s = Square("красного", 13)
    print(r)
    print(c)
    print(s)
    x = sympy.Symbol('x')
    print(sympy.integrate(x**2 + x + 1, x))

if __name__ == "__main__":
    main()