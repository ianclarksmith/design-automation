#http://starship.python.net/crew/theller/comtypes/

import array
import comtypes.client

#Get running instance of the AutoCAD application
app = comtypes.client.GetActiveObject("AutoCAD.Application")

#Create a new  document
ad = app.Documents.Add()

#Get the ModelSpace object
ms = ad.ModelSpace

#Add a POINT in ModelSpace
pt = array.array('d', [0,0,0])
point = ms.AddPoint(pt)

#Add a LINE in ModelSpace
pt1 = array.array('d', [1.0,1.0,0])
pt2 = array.array('d', [200.0,200.0,0])
line = ms.AddLine(pt1, pt2)
line2 = line.Copy()
line2.Move(pt1, pt2)
pt1, pt2 = line2.GetBoundingBox()

print type(line)

#xx = line2.Angle()


#line2.StartPoint()

#Should return a Variant Array (array of objects) - but throws an error
#test += line.ArrayRectangular(2,3,4,10,20,10)

#Add a 3d Polyline
pla = array.array('d', [100.0,200.0,0,200.0,50.0,100,300.0,200.0,0])
pline = ms.Add3Dpoly(pla)

#Add an integer type xdata to the point.
point.SetXData(array.array("h", [1001, 1070]), ['Test_Application1', 600])

#Add a double type xdata to the line.
line.SetXData(array.array("h", [1001, 1040]), ['Test_Application2', 132.65])

#Add a string type xdata to the line.
line.SetXData(array.array("h", [1001, 1000]), ['Test_Application3', 'TestData'])

#Add a list type (a point coordinate in this case) xdata to the line.
line.SetXData(array.array("h", [1001, 1010]),
              ['Test_Application4', array.array('d', [2.0,0,0])])

#ad.SaveAs("d:/temp/mytest998.dwg")
print line
print "done"