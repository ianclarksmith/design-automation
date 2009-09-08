import py2ecotect as p2e

p2e.app.draw.set_pen(color = 'OOOOOO', width=5)

p2e.app.draw.draw_lineto((1000,100,10000))
p2e.app.draw.draw_sphere((0,0,0), 10000)

print "done"