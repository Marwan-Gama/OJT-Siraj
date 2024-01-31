from app import xbonacci
import unittest

def test_xbonacci_1():
      assert(xbonacci([1,1],10) == [1,1,2,3,5,8,13,21,34,55])

def test_xbonacci_2():
      assert(xbonacci([1,1,1],8) == [1, 1, 1, 3, 5, 9, 17, 31])

def test_xbonacci_3():
      assert(xbonacci([1,1,1,1],10) == [1, 1, 1, 1, 4, 7, 13, 25, 49, 94])

def test_xbonacci_4():
      assert(xbonacci([0,0,0,0,1],10) == [0, 0, 0, 0, 1, 1, 2, 4, 8, 16])