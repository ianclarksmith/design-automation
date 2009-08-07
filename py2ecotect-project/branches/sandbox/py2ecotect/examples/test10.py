import py2ecotect as p2e

points =  [(0,0,0),(2000,0,0),(5000,5000,0)]
p2e.Floor.create(points)

fl = p2e.Floor.create(points)
f2 = p2e.Floor.create(points)