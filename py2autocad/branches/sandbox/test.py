import py2autocad
line1 = py2autocad.ms.AddLine((10,0,0), (10,20,0))
line2 = py2autocad.ms.AddLine((0,10,0), (20,10,0))
line3 = line1.Copy()
print line3

line3.Copy()
