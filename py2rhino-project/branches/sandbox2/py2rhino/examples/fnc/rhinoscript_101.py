import py2rhino.functions as p2r
import math
import random
from datetime import datetime

#------------------------------------------------------------------------------ 
#TODO: Insert page number
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
    
#who_framed_the_surface()

def flat_worm():
    crv_object =p2r.selection.get_objects("Pick a backbone curve", 4, True, False)[0]
    int_samples = p2r.user_interface.get_integer("Number of cross sections", 100, 5)
    bend_radius = p2r.user_interface.get_real("Bend plane radius", 0.5, 0.001)
    perp_radius = p2r.user_interface.get_real("Ribbon plane radius", 2.0, 0.001)
    crv_domain = p2r.curve.curve_domain(crv_object)
    n = -1
    t = crv_domain[0]
    cross_selections = []
    while t <= crv_domain[1]+1e-9:
        n += 1
        crv_curvature =p2r.curve.curve_curvature(crv_object, t)
        pt_o = p2r.point_and_vector
        if crv_curvature== None:
            crv_point = p2r.curve.evaluate_curve(crv_object, t)
            crv_tangent = p2r.curve.curve_tangent(crv_object, t)
            crv_perp = (0,0,1)
            crv_normal = pt_o.vector_cross_product(crv_tangent,crv_perp)
        else:
            crv_point = crv_curvature[0]
            crv_tangent = crv_curvature[1]
            crv_perp = pt_o.vector_unitize(crv_curvature[4])
            crv_normal = pt_o.vector_cross_product(crv_tangent, crv_perp)
        cross_section_plane = p2r.line_and_plane.plane_from_frame(crv_point, crv_perp, crv_normal)
        ellipse = p2r.curve.add_ellipse(cross_section_plane, bend_radius, perp_radius)
        cross_selections.append(ellipse)
        t += (crv_domain[1] - crv_domain[0])/int_samples
    p2r.surface_and_polysurface.add_loft_srf(cross_selections)
    p2r.object.delete_objects(cross_selections)
    
#flat_worm()

def blend_corners():
    id_polyline = p2r.selection.get_objects("Polyline to blend", 4, True, True)[0]
    arr_v = p2r.curve.polyline_vertices(id_polyline)
    new_v = []
    radius = p2r.user_interface.get_real("Blend Radius", 1.0, 1.0)
    n = -1
    def Between(a,b):
        return ((a[0]+b[0])/2, (a[1]+b[1])/2, (a[2]+b[2])/2)
    for i in range(0, len(arr_v)-2):
        a = arr_v[i]
        b = arr_v[i+1]
        vec_segment = p2r.point_and_vector.point_subtract(b, a)
        vec_segment = p2r.point_and_vector.vector_unitize(vec_segment)
        
        if radius < 0.5 * (p2r.math.distance(a, b)):
            vec_segment = p2r.point_and_vector.vector_scale(vec_segment, radius)
        else:
            vec_segment = p2r.point_and_vector.vector_create(vec_segment, 0.5 * p2r.math.distance(a, b))
        
        w1 = p2r.point_and_vector.vector_add(a, vec_segment)
        w2 = p2r.point_and_vector.vector_subtract(b, vec_segment)
        
        new_v.append(a)
        new_v.append(Between(a,w1))
        new_v.append(w1)
        new_v.append(Between(w1,w2))
        new_v.append(w2)
        new_v.append(Between(w2,b))
        n = n + 6
    new_v.append(arr_v[len(arr_v)-1])
    p2r.curve.add_curve(new_v, 5)
    p2r.object.delete_objects(id_polyline)
#blend_corners()

def create_curvature_graph():
    def add_curvature_graph(id_crv,span_samples,scale):
        all_geometry = []
        k = p2r.curve.curve_knots(id_crv)
        print k, "length: ", len(k)
        for i in range(0,len(k)-1):
            print "k:", k[i], "k+1: ", k[i+1]
            tmp_geometry = add_curvature_graph_section(id_crv,k[i],k[i+1],span_samples,scale)
        if not (tmp_geometry == None):
            all_geometry = all_geometry + tmp_geometry
        p2r.group.add_objects_to_group(all_geometry, p2r.group.add_group())
        print "A"
        return all_geometry
    
    def add_curvature_graph_section(id_crv,t0,t1,samples,scale):
        add_curvature_graph_section = None
        arr_a = []
        arr_b = []
        arr_objects = []
        n = -1
        t_step = (t1-t0)/samples
        t = t0
        while t <= (t1+(0.5*t_step)):
            if (t>= t1):
                t = t1-1e-10
            n = n + 1
            c_data = p2r.curve.curve_curvature(id_crv, t)
            print c_data
            if c_data == None:
                a= arr_a.append(p2r.curve.evaluate_curve(id_crv, t))
                arr_b.append(a) 
                arr_objects.append("")
            else:
                c_data_1 = p2r.point_and_vector.vector_scale(c_data[4],scale)
                print "c_data_1: ", c_data_1
                c_data_2 = (c_data[0],c_data[1],c_data[2],c_data[3],c_data_1)
                print "c_data_2: ",c_data_2[0]
                arr_objects.append(p2r.curve.add_line(arr_a.append(c_data_2[0]), arr_b.append(p2r.point_and_vector.vector_subtract(c_data[0], c_data_2[4]))))
            t += t_step
        arr_objects.append.p2r.curve.add_interp_curve(arr_b)    
        print "b"
        return arr_objects
    #---------------------------------------------------------------------------------
    id_curves = p2r.selection.get_objects("Curves for curvature graph", 4, False, True, True)
    print id_curves  
    samples = 10
    scale = 1.0
    arr_preview=[]
    arr_preview_size = len(id_curves)
    cont = True
    while cont == True:
        print arr_preview_size
        p2r.document.enable_redraw(False)
        for i in range(0,arr_preview_size):
            print id_curves[i]
            arr_preview.append(add_curvature_graph(id_curves[i], samples, scale))
        p2r.document.enable_redraw(True)
        b_result = p2r.user_interface.get_string("Curvature settings", "Accept", ("Samples", "Scale", "Accept"))
        if b_result.upper() == "ACCEPT":
            break
        elif b_result.upper() == "SAMPLES":
            b_result = p2r.user_interface.get_integer("Number of samples per knot-span", samples, 3, 100)
            if b_result ==None:
                samples = b_result
        elif b_result.upper() == "SCALES":
            b_result = p2r.user_interface.get_real("Scale of the graph", scale, 0.01, 1000.0)
            if b_result == None:
                scale = b_result
        if i == arr_preview_size-1:
            cont = False
    print "done"              
#create_curvature_graph()

def random_point_in_cone(origin,direction,min_distance,max_distance,max_angle):
    vec_twig = p2r.point_and_vector.vector_unitize(direction)
    vec_twig = p2r.point_and_vector.vector_scale(vec_twig, min_distance + random.random()  * (max_distance - min_distance))
    mutation_plane = p2r.line_and_plane.plane_from_normal((0,0,0), vec_twig)
    vec_twig = p2r.point_and_vector.vector_rotate(vec_twig, random.random() * max_angle, mutation_plane[1])
    vec_twig = p2r.point_and_vector.vector_rotate(vec_twig, random.random() * 360, direction)
    return p2r.point_and_vector.point_add(origin, vec_twig)
    

def add_arc_dir(pt_start, pt_end, vec_dir):
    vec_base = p2r.point_and_vector.point_subtract(pt_end, pt_start)
    if p2r.point_and_vector.vector_length(vec_base) == 0.0:
        return
    if p2r.point_and_vector.is_vector_parallel_to(vec_base, vec_dir):
        return p2r.curve.add_line(pt_start, pt_end)
    vec_base = p2r.point_and_vector.vector_unitize(vec_base)
    vec_dir = p2r.point_and_vector.vector_unitize(vec_dir)
    vec_bisector = p2r.point_and_vector.vector_add(vec_dir, vec_base)
    vec_bisector = p2r.point_and_vector.vector_unitize(vec_bisector)
    dot_prod = p2r.point_and_vector.vector_dot_product(vec_bisector, vec_dir)
    mid_length = (0.5* p2r.math.distance(pt_start, pt_end))/ dot_prod
    vec_bisector = p2r.point_and_vector.vector_scale(vec_bisector,mid_length)
    return p2r.curve.add_arc_3_pt(pt_start, pt_end, p2r.point_and_vector.point_add(pt_start, vec_bisector))

def recursive_growth(pt_start, vec_dir, props, generation):
    if generation > props[2]:
        return
    new_props = [props[0], props[1], props[2]]
    props_1 = props[3] * props[4]
    new_props.append(props_1)
    new_props.append(props[4])
    new_props_1 = props[5] * props[6]
    if new_props_1 > 90:
        new_props.append(90)
    else:
        new_props.append(new_props_1)
    new_props.append(props[6])
    max_n = props[0] + random.random() * (props[1] - props[0])
    n =1
    while n <= max_n:
        pt_grow = random_point_in_cone(pt_start, vec_dir, 0.25*props[3], props[3], props[5])
        new_twig = add_arc_dir(pt_start,pt_grow,vec_dir)
        
        
        if not new_twig == None:
            vec_grow = p2r.curve.curve_tangent(new_twig, p2r.curve.curve_domain(new_twig)[1])
            recursive_growth(pt_grow,vec_grow,new_props,generation+1)
        n +=1
        
def plant_generator():
    pt_root = p2r.user_interface.get_points(message_1="Root point for plant")
    if pt_root == None:
        return
    prop_min_twig_count = 0
    prop_max_twig_count = 8
    prop_max_generations = 5
    prop_max_twig_length = 10.0
    prop_length_mutation = 0.75
    prop_max_twig_angle = 30.0
    prop_angle_mutation = 0.85

    local_value = p2r.user_interface.get_integer("Minimum twig count",prop_min_twig_count)
    if local_value == None:
        return
    prop_min_twig_count = local_value
    
    local_value = p2r.user_interface.get_integer("Maximum twig count",prop_max_twig_count)
    if local_value == None:
        return
    prop_max_twig_count = local_value
    
    local_value = p2r.user_interface.get_integer("Maximum branch generations",prop_max_generations,1,1000)
    if local_value == None:
        return
    prop_max_generations = local_value
    
    local_value = p2r.user_interface.get_real("Maximum twig length",prop_max_twig_length,0.01)
    if local_value == None:
        return
    prop_max_twig_length = local_value
    
    local_value = p2r.user_interface.get_real("Twig length mutation",prop_length_mutation,0.01)
    if local_value == None:
        return
    prop_length_mutation = local_value
    
    local_value = p2r.user_interface.get_real("Maximum twig angle",prop_max_twig_angle,0.0,90.0)
    if local_value == None:
        return
    prop_max_twig_angle = local_value
    
    local_value = p2r.user_interface.get_real("Twig angle mutation", prop_angle_mutation, 0.01)
    if local_value == None:
        return
    prop_angle_mutation = local_value
    
    ##is there a randomize method?

    p2r.document.enable_redraw(False)
    
    growth_props = [prop_min_twig_count,prop_max_twig_count,prop_max_generations,prop_max_twig_length,prop_length_mutation,prop_max_twig_angle,prop_angle_mutation]
    
    recursive_growth((0,0,0),(0,0,1),growth_props,1)
    p2r.document.enable_redraw(True)
    
plant_generator()


