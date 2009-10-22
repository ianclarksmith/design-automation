import py2ecotect as p2e

p2e.model.time.set_date(10, 3, 13.0)
print p2e.model.sun.position(10, (10,10,0))

p2e.model.time.set_date(25, 3, 13.0)
print p2e.model.sun.position(10, (10,10,0))

print "done"