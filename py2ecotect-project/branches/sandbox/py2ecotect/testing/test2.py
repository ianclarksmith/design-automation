import py2ecotect as p2e

p2e.doc.model.new()
p2e.doc.weather.load_all('C:\Program Files\Autodesk\Ecotect 2010\Weather Data\Australia-SydneyNSW-1.wea')

points = ((0,0,0),(10,0,0),(10,0,10),(5,0,20),(5,0,3),)
wall = p2e.obj.Wall.create(points)

wall2 = wall.dupl.copy_move_by_vec((0,10,0))
wall3 = wall.dupl.copy_move_by_vec((0,-10,0))

wall.state.set_selected(True)

p2e.app.view.fit_grid()
p2e.app.view.redraw()

p2e.doc.calculation.calc_shading(shading_type='percentage', cumulative=True, start_day=1, stop_day=365, start_time=1, stop_time=23)

print "shading_percentange_at_date_time = ", p2e.doc.results.shading_percentange_at_date_time(5, 13)

print "done"