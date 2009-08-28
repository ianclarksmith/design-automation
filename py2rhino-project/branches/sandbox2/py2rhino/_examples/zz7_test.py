import py2rhino as p2r

line = p2r.obj.Line.create((0,0,0), (10,0,0))

print line.prop.domain()


