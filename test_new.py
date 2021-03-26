from new import *

class Test_quadrangle:
    def test_perimeter_5_10(self):
        assert quadrangle.perimeter(5,10) == 30
    
    def test_perimeter_100_0_point_5(self):
        assert quadrangle.perimeter(100,0.5) == 201

    def test_perimeter_2_2(self):
        assert quadrangle.perimeter(2,2) == 8

    def test_area_5_10(self):
        assert quadrangle.area(5,10) == 50
    
    def test_area_100_0_point_5(self):
        assert quadrangle.area(100,0.5) == 50

    def test_area_2_2(self):
        assert quadrangle.area(2,2) == 4

    def test_volume_5_10_2(self):
        assert quadrangle.volume(5,10,2) == 100
    
    def test_volume_100_0_point_5_100(self):
        assert quadrangle.volume(100,0.5,100) == 5000

    def test_volume_2_2_2(self):
        assert quadrangle.volume(2,2,2) == 8
    


class Test_triangle:
    def test_perimeter_5_10_20(self):
        assert triangle.perimeter(5,10,20) == 35
    
    def test_perimeter_100_0_point_5_3(self):
        assert triangle.perimeter(100,0.5,3) == 103.5

    def test_perimeter_2_2_2(self):
        assert triangle.perimeter(2,2,2) == 6

    def test_area_2_2_2(self):
        assert triangle.area(2,2,2) == sqrt(3)

    def test_volume_2_2_2_100(self):
        assert triangle.volume(2,2,2,100) == sqrt(3)*100/3

    def test_volume_2_3_2_2(self):
        assert triangle.volume(2,3,2,2) == None



class Test_circle:
    def test_perimeter_5(self):
        assert circle.long(5) == 10*pi
    
    def test_perimeter_100(self):
        assert circle.long(100) == 200*pi

    def test_perimeter_2(self):
        assert circle.long(2) == 4*pi

    def test_area_2(self):
        assert circle.area(2) == 4*pi

    def test_volume_3(self):
        assert circle.volume(3) == 36*pi

    def test_volume_6(self):
        assert circle.volume(6) == 288*pi