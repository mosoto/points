#!/usr/bin/python

from collections import deque
import numpy

def assign_point(arr, point):
    x,y,value = point
    arr[x][y] = value

def assign_points(arr, points):
    yLen = len(arr)
    xLen = len(arr[0])
    queue = deque(points)
    while len(queue) > 0:
        (x,y,v) = queue.popleft()
        new_points = [(x + 1, y, v), (x - 1, y, v), (x, y + 1, v), (x, y - 1, v)]
        for point in new_points:
            (x,y,_) = point
            if 0 <= x < xLen and 0 <= y < yLen and arr[x][y] == 0:
                assign_point(arr, point)
                queue.append(point)




arr = numpy.zeros((5,5))
points = [(1,1,1), (3,3,2), (4,0,3)]

for p in points:
    assign_point(arr, p)

print "BEFORE"
print arr
assign_points(arr, points)
print "AFTER"
print arr



