import py2ecotect as p2e

points =  ((0,0,0),(2,0,0),(5,5,0))

fl = p2e.obj.Floor.create(points)
fl.trfm.move_by_vec((0,0,3))

fl.trfm.copy_by_vec((2,0,0))

filename = "C:\\Program Files\\Autodesk\\Ecotect 2009\\Weather Data\\UK-AberdeenS.wea"
p2e.doc.weather.load_all(filename)

print "Done"