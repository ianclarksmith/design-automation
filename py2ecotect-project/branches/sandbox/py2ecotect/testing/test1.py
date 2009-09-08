import py2ecotect as p2e

p2e.doc.model.new()

p2e.app.draw.set_pen(color = 'OOOOOO', width=5)
p2e.app.draw.draw_lineto((1000,100,10000))
p2e.app.draw.draw_sphere((0,0,0), 10000)


points = ((0,0,0),(10,0,0),(10,0,10),(5,0,20),(5,0,3),)
wall = p2e.obj.Wall.create(points)
wall.state.set_selected(False)

'''
wall.trfm.move_by_vec((0,0,10))

wall.modf.delete()

roof = p2e.obj.Roof.create(points)
r2 = roof.dupl.copy_move_by_vec((20,0,0))
r2.modf.delete()
'''
p2e.doc.calculation.set_dates(0,365)
p2e.doc.calculation.set_times(7,19)

p2e.doc.calculation.update_shading_masks(True, 1, 365, 1, 23)
p2e.doc.calculation.calc_insolation('objects', 0, False, 0)
print p2e.doc.results.solar_direct(15)
print p2e.doc.results.insolation_direct()

print p2e.doc.results.shading_percentange_at_date_time(5, 13)

print "done"