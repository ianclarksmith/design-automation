import py2rhino.functions as p2r
import math
from datetime import datetime

def draw_sine_wave():
    a = -8.0
    b = 8.0
    step = 0.25
    x = a
    while x <= b:
        y = 2 * math.sin(x)
        p2r.geometry.add_points((x,y,0))
        x += step
    print "done"

#draw_sine_wave()

def twist_and_shout():
    pi=math.pi
    twist_angle = 0.0
    p2r.document.enable_redraw(False)
    z = 0
    while z <= 5:
        twist_angle = twist_angle + pi/30
        a = 0
        while a <= 2*pi:
            x = 5 * math.sin(a + twist_angle)
            y = 5 * math.cos(a + twist_angle)
            p2r.surface_and_polysurface.add_sphere((x,y,z), 0.5)
            a += pi/15
        z += 0.5
    p2r.document.enable_redraw(True)  
    print "done"

#twist_and_shout()

#TODO: PROBLEM: no result, negative numbers were generated.
def point_spiral():
    p2r.document.enable_redraw(False)
    t = -5
    while t<=5:
        arr_pt = [0,0,0]
        arr_pt[0] = t * math.sin(5 * t)
        arr_pt[1] = t * math.cos(5 * t)
        arr_pt[2] = t
        p2r.application.print_(p2r.utility.pt_2_str(arr_pt, 3))
        p2r.geometry.add_points(arr_pt)
        t+=0.025
    p2r.document.enable_redraw(False)
    print "done"
#point_spiral()    

def view_port_clock():
    active = True
    while active == True:
        date_id = p2r.geometry.add_text((datetime.time(datetime.now())),(0,0,0),20)
        print date_id
        p2r.utility.sleep(1000)
        p2r.geometry.text_object_text(date_id, datetime.time(datetime.now()))
    print "done"

#view_port_clock()

#TODO: producing the wrong result, same as previous one.
def define_radius():
    major_radius = p2r.user_interface.get_real("Major radius", 10.0, 1.0, 1000.0)
    minor_radius = p2r.user_interface.get_real("Minor radius", 2.0, 0.1, 100.0)
    sides=p2r.user_interface.get_integer("Number of sides", 6, 3, 20)
    str_point1 = " w" + str(major_radius) + ",0,0"
    total_radius = major_radius + minor_radius
    str_point2 = " w" + str(total_radius) + ",0,0"    
    p2r.application.command("_SelNone")
    comm = "_Polygon _NumSides=" + str(sides) + " w0,0,0" + str(str_point1)
    p2r.application.command(comm)
    p2r.application.command("_SelLast")
    p2r.application.command("-_Properties _Object _Name Rail _Enter _Enter")
    p2r.application.command("_SelNone")
    comm1 = "_Polygon _NumSides=" + str(sides) + " w0,0,0" + str(str_point1) + str(str_point2)
    p2r.application.command(comm1)
    p2r.application.command("_SelLast")
    p2r.application.command("_Rotate3D w0,0,0 w1,0,0 90")
    p2r.application.command("-_Properties _Object _Name Profile _Enter _Enter")
    p2r.application.command("_SelNone")
    p2r.application.command("-_Sweep1 _SelName Rail _SelName Profile _Enter _Closed=Yes Enter")
    p2r.application.command("_SelName Rail")
    p2r.application.command("_SelName Profile")
    p2r.application.command("_Delete")
    
#define_radius()
def fit_curve_to_length():
    cv = p2r.selection.get_objects("Select a curve to fit to length", 4, True, True)[0]
    length = p2r.curve.curve_length(cv)
    length_limit = p2r.user_interface.get_real("Length limit", 0.5 * length, 0.01 * length, length)
    cont = True
    while cont == True:
        if p2r.curve.curve_length(cv) <= length_limit:
            cont = False
        cv = p2r.object.scale_objects(cv, (0,0,0), (0.95, 0.95, 0.95))
    p2r.application.print_("New curve length:" + str(p2r.curve.curve_length(cv)))
    print "done"
    
#fit_curve_to_length()
def plane_example():
    
    pt_origin = p2r.user_interface.get_points(message_1="Plane origin")
    pt_x = p2r.user_interface.get_points(message_1="Plane X-axis")
    pt_y = p2r.user_interface.get_points(message_1="Plane Y-axis")
    d_x = p2r.math.distance(pt_origin, pt_x)
    d_y = p2r.math.distance(pt_origin, pt_y)
    arr_plane = p2r.line_and_plane.plane_from_points(pt_origin, pt_x, pt_y)
    p2r.surface_and_polysurface.add_plane_surface(arr_plane, 1.0, 1.0)
    p2r.surface_and_polysurface.add_plane_surface(arr_plane, d_x, d_y)
    
#plane_example()

#TODO: end result is different from actual, same as previous test
def who_framed_the_surface():
    id_surface = p2r.selection.get_objects("Surface to frame", 8, True, True)[0]
    count = p2r.user_interface.get_integer("Number of iterations per direction", 20, 2)
    u_domain = p2r.surface_and_polysurface.surface_domain(id_surface, 0)
    v_domain = p2r.surface_and_polysurface.surface_domain(id_surface, 1)
    u_step = (u_domain[1] - u_domain[0]) / count 
    v_step = (v_domain[1] - v_domain[0]) / count 
    p2r.document.enable_redraw(False)
    u = u_domain[0]
    v = v_domain[0]
    while u<= u_domain[1]:
        while v <= v_domain[1]:
            pt = p2r.surface_and_polysurface.evaluate_surface(id_surface,(u,v))
            if p2r.math.distance(pt, p2r.surface_and_polysurface.brep_closest_point(id_surface, pt)[0])< 0.1 :
                srf_frame = p2r.surface_and_polysurface.surface_frame(id_surface, (u,v))
                p2r.surface_and_polysurface.add_plane_surface(srf_frame, 1.0, 1.0)
            v += v_step
        u += u_step
    p2r.document.enable_redraw(True)
    print "done"
    
who_framed_the_surface()

'''Call FlatWorm()
Sub FlatWorm()
    Dim crvObject : crvObject = Rhino.GetObject("Pick a backbone curve", 4, True, False)
    If IsNull(crvObject) Then Exit Sub

    Dim intSamples : intSamples = Rhino.GetInteger("Number of cross sections", 100, 5)
    If IsNull(intSamples) Then Exit Sub

    Dim dblBendRadius : dblBendRadius = Rhino.GetReal("Bend plane radius", 0.5, 0.001)
    If IsNull(dblBendRadius) Then Exit Sub

    Dim dblPerpRadius : dblPerpRadius = Rhino.GetReal("Ribbon plane radius", 2.0, 0.001)
    If IsNull(dblPerpRadius) Then Exit Sub

    Dim crvDomain : crvDomain = Rhino.CurveDomain(crvObject)
    Dim t, N

    Dim arrCrossSections(), CrossSectionPlane
    Dim crvCurvature, crvPoint, crvTangent, crvPerp, crvNormal
    
    N = -1
    For t = crvDomain(0) To crvDomain(1) + 1e-9 Step (crvDomain(1)-crvDomain(0))/intSamples
        N = N+1
        crvCurvature = Rhino.CurveCurvature(crvObject, t)
        If IsNull(crvCurvature) Then
            crvPoint = Rhino.EvaluateCurve(crvObject, t)
            crvTangent = Rhino.CurveTangent(crvObject, t)
            crvPerp = Array(0,0,1)
            crvNormal = Rhino.VectorCrossProduct(crvTangent, crvPerp)
        Else
            crvPoint = crvCurvature(0)
            crvTangent = crvCurvature(1)
            crvPerp = Rhino.VectorUnitize(crvCurvature(4))
            crvNormal = Rhino.VectorCrossProduct(crvTangent, crvPerp)
        End If
        
        CrossSectionPlane = Rhino.PlaneFromFrame(crvPoint, crvPerp, crvNormal)
        
        ReDim Preserve arrCrossSections(N)
        arrCrossSections(N) = Rhino.AddEllipse(CrossSectionPlane, dblBendRadius, dblPerpRadius)
    Next

    If N < 1 Then Exit Sub
    
    Call Rhino.AddLoftSrf(arrCrossSections)
    Call Rhino.DeleteObjects(arrCrossSections)
End Sub
'''
