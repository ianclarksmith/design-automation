from py2autocad.acad_application import AcadApplication

app = AcadApplication()
doc = app.active_document
ms = doc.model_space

line1 = ms.add_line((10,0,0), (10,20,0))
#===============================================================================
# testing AcadLine
#===============================================================================
print line1

#testing AcadLine methods
#offset

#testing AcadLine Properties
#TODO: test setters as well
print line1.start_point
print line1.end_point
print line1.normal
print line1.thickness
print line1.delta
print line1.length
print line1.angle
#===============================================================================
# testing AcadEntity
#===============================================================================
#test AcadEntity methods

#array_polar
#array_rectangular
line1.highlight(True)
line1.copy()
line1.move((0,0,0),(20,0,0))
line1.rotate((0,0,0),30.0)
line1.rotate_3d((0,0,0),(20,0,0),30.0)
line1.mirror((0,0,0),(20,0,0))
line1.mirror_3d((0,0,0),(10,0,0),(0,10,10))
line1.scale_entity((0,0,0),2)
#line1.transform_by
line1.update()
line1.get_bounding_box()

#TODO: test AcadEntity properties

#===============================================================================
# testing AcadObject
#===============================================================================
#TODO: test AcadObject methods

#TODO: test AcadObject properties


#===============================================================================
# testing some other stuff
#===============================================================================
app.update()
doc.regen(1)
print "done"

