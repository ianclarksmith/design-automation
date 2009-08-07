import py2rhino as p2r

arc1 = p2r.Arc.create_by_3pt((0,0,0), (20,0,0), (10,10,0))
arc2 = p2r.Arc.create_copy_move_by_vec(arc1, (0,0,20))
arc3 = p2r.Arc.create_copy_move_by_vec(arc1, (0,0,40))

srfs = p2r.NurbsSurface.create_by_loft( [arc1, arc2, arc3] )



srf = srfs[0]

u_domain = srf.prop.domain(0)
v_domain = srf.prop.domain(1)
"""
u_step = ( u_domain[1] - u_domain[0] )/ 10.0
v_step = ( v_domain[1] - v_domain[0] )/ 10.0

print u_domain, v_domain
print u_step, v_step

u = 0
v = 0
srf_pt = []
for v_counter in range(11):
    for u_counter in range(11):
        print u,v
        pt = srf.eval.evaluate( [u,v] )
        srf_pt.append(pt)
        p2r.Sphere.create(pt, 0.2)
        u = u + u_step
    u = 0
    v = v + v_step
    
"""

print "done"


