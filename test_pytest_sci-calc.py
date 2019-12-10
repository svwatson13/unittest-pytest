from sci_calc import *
import math

def test_find_sqrt():
    assert find_sqrt(100) == 10, 'did not find square root'

def test_find_ceil():
    assert find_ceil(12.2) == 13