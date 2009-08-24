import py2ecotect as p2e
import py2rhino as p2r

sp = p2r.obj.Sphere.create((0,0,0), 5)
domain_u = sp.prop.domain(0)
domain_v = sp.prop.domain(1)
print domain_u
print domain_v
step_u = (domain_u[1] - domain_u[0])/10.0
step_v = (domain_v[1] - domain_v[0])/10.0


corner_points = []
walls = []
for v_num in range(10):
    for u_num in range(10):
        
        #get the points
        param = domain_u[0] + (step_u * u_num), domain_v[0] + (step_v * v_num)
        pt1 = sp.eval.evaluate(param)
        pt2 = sp.eval.evaluate((param[0]+ step_u, param[1]))
        pt3 = sp.eval.evaluate((param[0]+ step_u, param[1]+ step_v))
        pt4 = sp.eval.evaluate((param[0], param[1]+ step_v))
        
        #draw in Rhino
        p2r.obj.NurbsSurface.create_by_corner_pnts((pt1, pt2, pt3))
        p2r.obj.NurbsSurface.create_by_corner_pnts((pt1, pt3, pt4))  
        
        #draw in Ecotect
        wall1 = p2e.obj.Wall.create((pt1, pt2, pt3))
        wall2 = p2e.obj.Wall.create((pt1, pt3, pt4))
        
        #save the dats
        corner_points.append((pt1, pt2, pt3, pt4))
        walls.append((wall1, wall2))