from math_series.series import fibonacci_series
from math_series.series import lucas_series
from math_series.series import sum_series
"""
Fibonacci test :
     0 => 0
     1 => 1
     5 => 5
     6 => 8
"""
def test_fibonacci1():
    assert fibonacci_series(0) == 0

def test_fibonacci2():
    assert fibonacci_series(1) == 1

def test_fibonacci3():
    assert fibonacci_series(5) == 5

def test_fibonacci4():
    assert fibonacci_series(6) == 8
def test_five():
    assert fibonacci_series(5) == 5
    assert lucas_series(5) == 11
   


def test_one():
    assert fibonacci_series(1) == 1
    assert lucas_series(1) == 1

def test_zero():
    assert fibonacci_series(0) == 0
    assert lucas_series(0) == 2

def test_sum():
    assert sum_series(5,5,5) == 40    #new series 
    assert sum_series(5) == 5         #same lucas
    assert sum_series(5,0,1) == 5 
    assert sum_series(5,2,1) == 11    #same fibonacci