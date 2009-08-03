import py2rhino.functions as p2r
import math
def annotate_curve_end_points():
    str_object = p2r.selection.get_objects("Select curve: ", 4)[0]
    print str_object
    if str_object == None:
        return
    arr_point = p2r.curve.curve_start_point(str_object)
    print arr_point
    p2r.geometry.add_points(arr_point)
    p2r.geometry.add_text_dot(p2r.utility.pt_2_str(arr_point, 3), arr_point)
    if not p2r.curve.is_curve_closed(str_object):
        arr_point = p2r.curve.curve_end_point(str_object)
        print arr_point
        p2r.geometry.add_points(arr_point)
        p2r.geometry.add_text_dot(p2r.utility.pt_2_str(arr_point, 3), arr_point)

#annotate_curve_end_points()

def array_points_on_surface():
    arr_point=[]
    str_object = p2r.selection.get_objects("Select surface: ", 8)[0]
    if str_object == None:
        return
    n_rows = p2r.user_interface.get_integer("Number of rows", 2, 2)
    if n_rows == None:
        return
    n_rows = n_rows - 1
    n_columns = p2r.user_interface.get_integer("Number of columns", 2, 2)
    if n_columns == None:
        return
    n_columns = n_columns -1
    u = p2r.surface_and_polysurface.surface_domain(str_object, 0)
    v = p2r.surface_and_polysurface.surface_domain(str_object, 1)
    print n_rows, n_columns
    i =0
    while i <= n_rows:
        j = 0
        while j <= n_columns:
            arr_param=[]
            arr_param.append(u[0] + (((u[1] - u[0]) / n_rows) * i))
            arr_param.append(v[0] + ((v[1]-v[0])/n_columns * j))
            arr_point.append(p2r.surface_and_polysurface.evaluate_surface(str_object, arr_param))
            p2r.geometry.add_points(arr_point)
            j +=1
        i+=1
#array_points_on_surface()

def circle_from_length():
        arr_center = p2r.user_interface.get_points(message_1="Center point of circle")
        arr_plane = p2r.line_and_plane.move_plane(p2r.view.view_c_plane(), arr_center)
        length = p2r.user_interface.get_real("Circle circumference")
        if length > 0.0:
            radius = length / (2* math.pi)
            str_object = p2r.curve.add_circle(arr_plane, radius)
            p2r.object.select_objects(str_object)
#circle_from_length()

def copy_objects_to_layer():
    arr_objects = p2r.selection.get_objects("Select objects")
    p2r.object.unselect_objects(arr_objects)
    arr_layers = p2r.layer.layer_names()
    str_layer = p2r.user_interface.combo_list_box(arr_layers, "Destination Layer" + p2r.layer.current_layer())
    if not str_layer == None:
        if not p2r.layer.is_layer(str_layer):
            p2r.layer.add_layer(str_layer)
    arr_new = p2r.object.copy_objects(arr_objects)
    for i in range (0, len(arr_new)):
        p2r.object.object_layer(arr_new[i], str_layer)
    p2r.object.select_objects(arr_new)

#copy_objects_to_layer()

def curve_length():
    length = 0.0
    count = 0
    arr_objects = p2r.selection.get_objects("Select objects", 4, True, True)
    p2r.object.unselect_objects(arr_objects)
    for i in range (0, len(arr_objects)):
        if p2r.curve.is_curve(arr_objects[i]):
            length = length + p2r.curve.curve_length(arr_objects[i])
            count = count + 1
    if count > 0:
        curve_sec = "Curves selected: ", count, "Total length: ", length
        p2r.application.print_(curve_sec)
        
#curve_length()

def draw_parametric_curve():
    def calculate_point(t):
        calculate_point = [0,0,0]
        calculate_point[0]= (4 * (1 - t) + 1 * t) * math.sin(3 * 6.2832 * t)
        calculate_point[1] = (4 * (1 - t) + 1 * t) * math.cos(3 * 6.2832 * t)
        calculate_point[2] = 5 * t
        return calculate_point
#====================================================================================================
    t0 = p2r.user_interface.get_real("Minimum t value", 0.0)
    if t0 == None:
        return
    t1 = p2r.user_interface.get_real("Maximum t value", 1.0)
    if t1 == None:
        return
    count  = p2r.user_interface.get_integer("Number of points", 50, 2)
    if count == None:
        return
    arr_points = []
    arr_points.append(calculate_point(t0))
    x = 1
    while x <= count-2:
        t = (1.0 - (float(x) / count) ) * t0 + (float(x) / count) * t1
        arr_points.append(calculate_point(t))
        x += 1
    arr_points.append(calculate_point(t1))
    p2r.curve.add_interp_curve(arr_points)

#draw_parametric_curve()

'''def current_mode_info():
    str_name = p2r.document.document_name()
    str_path = p2r.document.document_path()
    str_file_spec = str_path + str_name
    obj_fso 
'''

def garden_path():
    sp = p2r.user_interface.get_points(message_1="Start point of path")
    ep = p2r.user_interface.get_points(message_1="End point of path", base_point=sp)
    hwidth = p2r.user_interface.get_distance(sp, message_1="Half width of path")
    trad = p2r.user_interface.get_distance(sp, 1.0, message_1="Radius of tiles")
    tspac = p2r.user_interface.get_distance(sp, 1.0, message_1="Distance between tiles")
    temp = p2r.math.angle(sp, ep)
    pangle = temp [0]
    plength = p2r.math.distance(sp, ep)
    width = hwidth * 2
    angp90 = pangle + 90.0
    angm90 = pangle - 90.0
    p2r.document.enable_redraw(False)
    pline = [0,0,0,0,0]
    pline[0] = p2r.math.polar(sp, angm90, hwidth)
    pline[1] = p2r.math.polar(pline[0], pangle, plength)
    pline[2] = p2r.math.polar(pline[1], angp90, width)
    pline[3] = p2r.math.polar(pline[2], pangle + 180.0, plength)
    pline[4] = pline[0]
    p2r.curve.add_polyline(pline)
    plane = p2r.line_and_plane.world_x_y_plane()
    pdist = trad + tspac
    off = 0.0
    while (pdist <= (plength - trad)):
        pfirst = p2r.math.polar(sp, pangle, pdist)
        pctile = p2r.math.polar(pfirst,angp90,off)
        pltile = pctile
        while (p2r.math.distance(pfirst, pltile) < hwidth - trad):
            plane = p2r.line_and_plane.move_plane(plane, pltile)
            p2r.curve.add_circle(plane,trad)
            pltile = p2r.math.polar(pltile,angm90,tspac + trad + trad)
        pltile = p2r.math.polar(pctile, angm90, tspac + trad + trad)
        while (p2r.math.distance(pfirst, pltile)) < (hwidth - trad):
            plane = p2r.line_and_plane.move_plane(plane, pltile)
            p2r.curve.add_circle(plane,trad)
            pltile = p2r.math.polar(pltile, angm90, tspac + trad + trad)
        pdist = pdist + ((tspac + trad + trad) * math.sin(math.radians(60)))
        if off == 0.0:
            off = (tspac + trad + trad) * math.cos(math.radians(60))
        else:
            off =0.0
    p2r.document.enable_redraw(True)

#garden_path()

#ring_torus_1 and ring_torus_2 produce the same result but asked in a different way only.

def ring_torus_1():
    arr_point = p2r.user_interface.get_points(message_1="Center of ring")
    inner = p2r.user_interface.get_real("Inner diameter of ring")
    if inner == None:
        return
    outer = inner
    while outer <= inner:
        outer = p2r.user_interface.get_real("Outer diameter of ring")
        if outer <= inner:
            p2r.application.print_("Outer diameter must be greater than inner diameter")
    first = outer - ((outer - inner) / 2)
    second = (outer - inner) /2
    p2r.surface_and_polysurface.add_torus(arr_point, first/2, second/2)
    
#ring_torus_1()

def ring_torus_2():
    arr_point = p2r.user_interface.get_points(message_1="Center of ring")
    inner = p2r.user_interface.get_real("Inner diameter of ring")
    if inner == None:
        return
    tube = inner
    while (tube >= inner):
        tube = p2r.user_interface.get_real("Tube diameter of ring")
        if tube <= inner:
            p2r.application.print_("Tube diameter must be greater than inner diameter")
    inner = (inner + tube) / 2
    tube = tube /2
    p2r.surface_and_polysurface.add_torus(arr_point, inner, tube)
#ring_torus_2()

def make_nurbs_curve():
    degree = 3
    arr_control_points = [0,0,0,0,0,0,0,0,0,0]
    arr_control_points[0] = (0.0, 0.0, 0.0)
    arr_control_points[1] = (1.0, 2.0, 3.0)
    arr_control_points[2] = (5.0, 8.0, 9.0)
    arr_control_points[3] = (4.0, 7.0, 2.0)
    arr_control_points[4] = (8.0, 5.0, 6.0)
    arr_control_points[5] = (9.0, 5.0, 2.0)
    arr_control_points[6] = (5.0, 3.0, 2.0)
    arr_control_points[7] = (6.0, 2.0, 3.0)
    arr_control_points[8] = (7.0, 4.0, 2.0)
    arr_control_points[9] = (8.0, 5.0, 3.0)
    
    arr_weights = [0,0,0,0,0,0,0,0,0,0]
    arr_weights[0] = 1.0
    arr_weights[1] = 1.1 
    arr_weights[2] = 0.7
    arr_weights[3] = 2.0
    arr_weights[4] = 1.8
    arr_weights[5] = 0.9
    arr_weights[6] = 2.0
    arr_weights[7] = 1.3
    arr_weights[8] = 0.8
    arr_weights[9] = 1.0
    
    arr_knots= [0,0,0,0,0,0,0,0,0,0,0,0]
    arr_knots[0] = 0.0
    arr_knots[1] = 0.0
    arr_knots[2] = 0.0
    arr_knots[3] = 1.0
    arr_knots[4] = 3.0
    arr_knots[5] = 5.0
    arr_knots[6] = 5.0
    arr_knots[7] = 5.0
    arr_knots[8] = 7.12345
    arr_knots[9] = 9.0
    arr_knots[10] = 9.0
    arr_knots[11] = 9.0
    
    p2r.curve.add_nurbs_curve(arr_control_points,arr_knots,degree,arr_weights)
    
#make_nurbs_curve()