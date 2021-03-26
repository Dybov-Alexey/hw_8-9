from math import sqrt, pi


class quadrangle():
    def perimeter(A,B):
        return (A + B)*2
    
    def area(A,B):
        return A * B

    def volume(A,B,C):
        return quadrangle.area(A,B) * C


class triangle():
    def perimeter(A,B,C):
        return A + B + C

    def area(A,B,C):
        p = triangle.perimeter(A,B,C)/2
        return sqrt(p*(p-A)*(p-B)*(p-C))

    def volume(A,B,C,h):
        if A != B or B != C:
            print('Для вычисления объема правильной пирамиды нужен правильный треугольник')
            return None
        return triangle.area(A,B,C)/3*h


class circle():
    def long(r):
        return 2*pi*r

    def area(r):
        return pi*r*r

    def volume(r):
        return 4/3*pi*r*r*r