import py2ecotect as p2e

p2e.doc.model.new()

p2e.app.draw.set_pen(color = 'OOOOOO', width=5)
p2e.app.draw.draw_line((1000,100,10000))
p2e.app.draw.draw_sphere((0,0,0), 10000)




points = ((0,0,0),(10,0,0),(10,0,10),(5,0,20),(5,0,3),)
wall = p2e.obj.Wall.create(points)
wall.state.set_selected(True)

points2 = ((0,0,0), (10,0,0), (10,10,0), (0,10,0))
collector = p2e.obj.SolarCollector.create(points2)
'''
wall.trfm.move_by_vec((0,0,10))

wall.modf.delete()

roof = p2e.obj.Roof.create(points)
r2 = roof.dupl.copy_move_by_vec((20,0,0))
r2.modf.delete()
'''
p2e.doc.calculation.calc_solar_exposure_one_day(shading=2, ground=1, direct=1)

p2e.doc.weather.load_all('C:\Program Files\Autodesk\Ecotect 2009\Weather Data\Australia-SydneyNSW-1.wea')

p2e.doc.calculation.update_adjacencies(100, True)

p2e.doc.calculation.set_dates(0,365)
p2e.doc.calculation.set_times(7,19)

p2e.doc.calculation.calc_shading(calc_type='percentage', cumulative=True, start_day=1, stop_day=365, start_time=1, stop_time=23)

p2e.doc.calculation.calc_insolation('objects', 0, False, 0)
print "solar_direct = ", p2e.doc.results.solar_direct(15)
print "solar_diffuse = ", p2e.doc.results.solar_diffuse(15)
print "insolation_diffuse = ", p2e.doc.results.insolation_diffuse()

print "shading_percentange_at_date_time = ", p2e.doc.results.shading_percentange_at_date_time(5, 11)

print "done"