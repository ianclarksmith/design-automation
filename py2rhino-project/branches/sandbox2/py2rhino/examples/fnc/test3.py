import py2rhino.functions as p2r
import math
import random
from datetime import datetime

def draw_fillet_curve():
    arc1 = p2r.curve.add_arc((0,0,0), 10, 40)
    arc2 = p2r.curve.add_arc((10,0,0), 15, 95)
    print arc1
    print arc2
    curve1 = p2r.curve.add_fillet_curve(arc1, arc2,1, p2r.curve.curve_start_point(arc1), p2r.curve.curve_start_point(arc2))
    print curve1
    print p2r.curve.curve_start_point(arc1)
#draw_fillet_curve()
 
def density():
    arc4 = p2r.object.add_object_mesh(p2r.curve.add_arc_3_pt((10,0,0), (20,0,0), (10,10,0)))
    print p2r.object.object_mesh_density(arc4)
#density()    

def extrude_curve():
    str_curve = p2r.curve.add_circle(((0,0,0),(1,0,0),(0,1,0)), 5)
    str_path = p2r.curve.add_line((5,0,0), (10,0,10))
    print p2r.surface_and_polysurface.extrude_curve(str_curve, str_path)
    print p2r.surface_and_polysurface.extrude_curve_point(str_curve, (0,0,10))
#extrude_curve()

def extrude_surface():
    str_surface = p2r.surface_and_polysurface.add_srf_pt(((0,0,0),(5,0,0),(5,5,0), (0,5,0)))
    str_curve = p2r.curve.add_line((5,0,0), (10,0,10))
    #print p2r.surface_and_polysurface.extrude_curve(str_curve, str_path)
    print p2r.surface_and_polysurface.extrude_surface(str_surface,str_curve)
#extrude_surface()

def join_surface():
    line1 = p2r.curve.add_line((5,0,0), (10,0,10))
    nurve_surface1 = p2r.surface_and_polysurface.add_rev_srf(line1,((0,0,0),(0,0,3)))[0]
    nurve_surface2 = p2r.surface_and_polysurface.add_rev_srf(line1,((0,0,5),(0,0,4)))[0]
    arr_obj = []
    arr_obj.append(nurve_surface1)
    arr_obj.append(nurve_surface2)
    if len(arr_obj) >0:
        p2r.surface_and_polysurface.join_surfaces(arr_obj)
#join_surface()    

def line():
    print p2r.curve.line_fit_from_points(((0,0,0),(10,10,10)))
#line()
 
def cone():
    print p2r.surface_and_polysurface.add_cone((0,0,0), 10, 5)  
    
#cone()

def ns1():
    #ns = p2r.surface_and_polysurface.add_srf_pt(((0,0,0),(0,0,5),(0,0,4)))
    sphere1 = p2r.surface_and_polysurface.add_sphere((0,0,0), 5)
    #print p2r.surface_and_polysurface.make_surface_non_periodic(sphere1,0)
    #print p2r.surface_and_polysurface.fit_surface(ns)
    #print p2r.surface_and_polysurface.rebuild_surface(ns)
    #print p2r.surface_and_polysurface.insert_surface_knot(ns, (0,0,0), 0)
    print p2r.surface_and_polysurface.is_poly_surface(sphere1[0])
ns1()

def knot():
    sphere1 = p2r.surface_and_polysurface.add_sphere((0,0,0), 5)
    str = p2r.selection.get_objects("Select surface:", 8)[0]
    arr_pt = p2r.user_interface.get_point_on_surface(str, "Point on surface")
    arr_para = p2r.surface_and_polysurface.surface_closest_point(str, arr_pt)
    print arr_para
    print p2r.surface_and_polysurface.insert_surface_knot(str, arr_para,0)
#knot()
def cylinder():
    print p2r.surface_and_polysurface.add_cylinder((0,0,1), 5, 2) 
def interp_curv_on_srf():
    line1 = p2r.curve.add_line((5,0,0), (10,0,10))
    nurve_surface11 = p2r.surface_and_polysurface.add_rev_srf(line1,((0,0,0),(0,0,3)))[0]
    nurve_curve2 = p2r.curve.add_interp_crv_on_srf(nurve_surface11,((0,0,1),(0,0,2)))
    print nurve_curve2

#interp_curv_on_srf()