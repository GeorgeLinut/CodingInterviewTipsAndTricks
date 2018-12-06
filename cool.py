"""
    You are given an n x n 2D matrix representing an image.

    Rotate the image by 90 degrees (clockwise).

"""

def rotate(matrix):

    return [list(x[::-1]) for x in zip(*matrix)]


print(rotate([[1, 2, 3], [4, 5, 6], [7, 8, 9]]))

""" 
  [1, 2, 3], [4, 5, 6], [7, 8, 9]]  ---->  [[7, 4, 1], [8, 5, 2], [9, 6, 3]]

"""
