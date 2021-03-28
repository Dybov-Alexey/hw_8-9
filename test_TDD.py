from TDD_hw3 import *


class Test_prime_numder:
    def test_prime_numder_5(self):
        assert prime_numder(5) == True
    
    def test_prime_numder_100(self):
        assert prime_numder(100) == None

    def test_prime_numder_minus_13(self):
        assert prime_numder(-13) == True


class Test_HOD:
    def test_HOD_12_6(self):
        assert HOD(12,6) == 6
    
    def test_HOD_100_0(self):
        assert HOD(100,0) == 100

    def test_HOD_13_minus_13(self):
        assert HOD(13,-13) == 13


class Test_HOK:
    def test_HOK_12_6(self):
        assert HOK(12,6) == 12
    
    def test_HOK_100_0(self):
        assert HOK(100,0) == 0

    def test_HOK_13_minus_13(self):
        assert HOK(13,-13) == -13


class Test_XOR:
    def test_XOR_123456_3(self):
        assert xor('123456',3) == '210765'
    
    def test_XOR_100_0(self):
        assert xor('210765',3) == '123456'

    def test_XOR_13_minus_13(self):
        assert xor('',3) == ''


class Test_usedigits:
    def test_usedigits_10_20_1(self):
        assert usedigits(10,20,1) == 11
    
    def test_usedigits_5_5_5(self):
        assert usedigits(-5,5,5) == 2

    def test_usedigits_5_minus_5_(self):
        assert usedigits(-5,5,'-') == 5


class Test_usealpha:
    def test_usealpha_aaaaad_a(self):
        assert usealpha('aaaaad','a') == 5
    
    def test_usealpha_555556_6(self):
        assert usealpha(555556,6) == 1

    def test_usealpha(self):
        assert usealpha('  ','') == 3