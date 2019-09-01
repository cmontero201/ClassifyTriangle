"""
Created by Christian Montero
August 29, 2019

This file shows code to solve the Triangles assignment.   

"""

import unittest
import math

def classify_triangle(a,b,c):
    sum = a**2 + b**2
    check = math.floor(c**2)

    if (a < 0 or b < 0 or c < 0):
        return "Not a Triangle"

    if (a == b) and (a == c) and (b == c):
        return 'Equilateral'
    elif (a != b) and (b != c) and (c != a):
        return "Scalene"
    elif (sum == check):
        return "Right"
    elif (a == b) or (b == c) or (c == a):
        return "Isosceles"
    else:
        return "Not a Triangle"


def runClassify_Triangle(a, b, c):
    print('classify_triangle(',a, ',', b, ',', c, ') = ',classify_triangle(a,b,c),sep = "")


class TestTriangles(unittest.TestCase):

    def testSet1(self): # test invalid inputs
        self.assertEqual(classify_triangle(1,1, math.sqrt(2)),'Right','Should be a Right triangle')
        self.assertEqual(classify_triangle(2,2,2),'Equilateral','2,2,2 should be equilateral')
        self.assertEqual(classify_triangle(1,2,3), 'Scalene', '1,2,3 should be scalene')
        self.assertEqual(classify_triangle(2,2,5), 'Isosceles', '2,2,5 shoud be isosceles')
        self.assertEqual(classify_triangle(10,5,-2), 'Not a Triangle', "Should not be a triangle")


if __name__ == '__main__':
    # examples of running the code
    runClassify_Triangle(2,3,5)
    runClassify_Triangle(3,4,4)
    runClassify_Triangle(4,2,-1)

    suite = unittest.TestLoader().loadTestsFromTestCase(TestTriangles)
    unittest.TextTestRunner(verbosity = 2).run(suite)
    
    unittest.main()