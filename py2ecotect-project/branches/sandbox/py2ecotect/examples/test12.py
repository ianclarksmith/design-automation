import py2ecotect as p2e
import py2rhino as p2r




p2e.doc.model.set_date(10, 3, 13.0)
print p2e.doc.model.sun_position(10, (10,10,0))


p2e.doc.model.set_date(25, 3, 13.0)
print p2e.doc.model.sun_position(10, (10,10,0))

print "done"