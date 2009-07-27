'''
Option Explicit
'Draw a sine wave using points
DrawSineWave()
Sub DrawSineWave()
Dim x, y
Dim dblA, dblB, dblStep
dblA = -8.0
dblB = 8.0
dblStep = 0.25
For x = dblA To dblB Step dblStep
y = 2*Sin(x)
Call Rhino.AddPoint(Array(x, y, 0))
Next
End Sub
'''
import py2rhino as p2r
import math
from datetime import datetime

def draw_sine_wave():
    a = -8.0
    b = 8.0
    step = 0.25
    x = a
    while x <= b:
        y = 2 * math.sin(x)
        ge_o = p2r.Geometry()
        ge_o.add_points((x,y,0))
        x += step
    print "done"
    
'''Sub TwistAndShout()
Dim z, a
Dim pi, dblTwistAngle
pi = Rhino.Pi()
dblTwistAngle = 0.0
Call Rhino.EnableRedraw(False)
For z = 0.0 To 5.0 Step 0.5
dblTwistAngle = dblTwistAngle + (pi/30)
For a = 0.0 To 2*pi Step (pi/15)
Dim x, y
x = 5 * Sin(a + dblTwistAngle)
y = 5 * Cos(a + dblTwistAngle)
Call Rhino.AddSphere(Array(x,y,z), 0.5)
Next
Next
Call Rhino.EnableRedraw(True)
End Sub'''
def twist_and_shout():
    pi=math.pi
    twist_angle = 0.0
    en_re = p2r.Document()
    en_re.enable_redraw(False)
    z = 0
    while z <= 5:
        twist_angle = twist_angle + pi/30
        a = 0
        while a <= 2*pi:
            x = 5 * math.sin(a + twist_angle)
            y = 5 * math.cos(a + twist_angle)
            add_sp = p2r.SurfaceAndPolysurface()
            add_sp.add_sphere((x,y,z), 0.5)
            a += pi/15
        z += 0.5
    en_re.enable_redraw(True)  
    print "done"
    
'''Sub PointSpiral()
Dim arrPoint(2)
Dim t, pi
pi = Rhino.Pi()
Call Rhino.EnableRedraw(False)
For t = -5 To 5 Step 0.025
arrPoint(0) = t * Sin(5*t)
arrPoint(1) = t * Cos(5*t)
arrPoint(2) = t
Call Rhino.Print(Rhino.Pt2Str(arrPoint, 3))
Call Rhino.AddPoint(arrPoint)
Next
Call Rhino.EnableRedraw(True)
End Sub
'''

def point_spiral():
    en_re = p2r.Document()
    en_re.enable_redraw(False)
    t = -5
    while t<=5:
        arr_pt = [0,0,0]
        arr_pt[0] = t * math.sin(5 * t)
        arr_pt[1] = t * math.cos(5 * t)
        arr_pt[2] = t
        ut_o = p2r.Utility()
        pr = p2r.Application()
        pr.print_(ut_o.pt2_str(arr_pt, 3))
        ge_o = p2r.Geometry()
        ge_o.add_points(arr_pt)
        
        t+=0.025
    en_re.enable_redraw(True)
    print "done"
    
'''Option Explicit
ViewportClock()
Sub ViewportClock()
Dim strTextObjectID
strTextObjectID = Rhino.AddText(CStr(Time()), Array(0,0,0), 20)
If IsNull(strTextObjectID) Then Exit Sub
Do
Call Rhino.Sleep(1000)
Call Rhino.TextObjectText(strTextObjectID, CStr(Time()))
Loop
End Sub
'''

def view_port_clock():
    str_text_object_id = p2r.Geometry()
    str_text_object_id.add_text((datetime.time(datetime.now())),(0,0,0),20)
    active = True
    while active == True:
        ut_o = p2r.Utility()
        ut_o.sleep(1000)
        ge_o = p2r.Geometry()
        ge_o.text_object_text(str_text_object_id, datetime.time(datetime.now()))
    print "done"  

'''
Dim dblMajorRadius, dblMinorRadius
Dim intSides

dblMajorRadius = Rhino.GetReal("Major radius", 10.0, 1.0, 1000.0)
dblMinorRadius = Rhino.GetReal("Minor radius", 2.0, 0.1, 100.0)
intSides = Rhino.GetInteger("Number of sides", 6, 3, 20)

Dim strPoint1, strPoint2
strPoint1 = " w" & dblMajorRadius & ",0,0"
strPoint2 = " w" & (dblMajorRadius + dblMinorRadius) & ",0,0"

Rhino.Command "_SelNone"
Rhino.Command "_Polygon _NumSides=" & intSides & " w0,0,0" & strPoint1
Rhino.Command "_SelLast"
Rhino.Command "-_Properties _Object _Name Rail _Enter _Enter"
Rhino.Command "_SelNone"
Rhino.Command "_Polygon _NumSides=" & intSides & strPoint1 & strPoint2
Rhino.Command "_SelLast"
Rhino.Command "_Rotate3D w0,0,0 w1,0,0 90"
Rhino.Command "-_Properties _Object _Name Profile _Enter _Enter"
Rhino.Command "_SelNone"
Rhino.Command "-_Sweep1 _SelName Rail _SelName Profile _Enter _Closed=Yes Enter"
Rhino.Command "_SelName Rail"
Rhino.Command "_SelName Profile"
Rhino.Command "_Delete"
'''
#TODO: producing the wrong result
def define_radius():
    ur_o = p2r.UserInterface()
    major_radius = ur_o.get_real("Major radius", 10.0, 1.0, 1000.0)
    minor_radius = ur_o.get_real("Minor radius", 2.0, 0.1, 100.0)
    sides=ur_o.get_integer("Number of sides", 6, 3, 20)
    str_point1 = " w" + str(major_radius) + ",0,0"
    total_radius = major_radius + minor_radius
    str_point2 = " w" + str(total_radius) + ",0,0"    
    ap_o = p2r.Application()
    ap_o.command("_SelNone")
    comm = "_Polygon _NumSides=" + str(sides) + " w0,0,0" + str(str_point1)
    ap_o.command(comm)
    ap_o.command("_SelLast")
    ap_o.command("-_Properties _Object _Name Rail _Enter _Enter")
    ap_o.command("_SelNone")
    comm1 = "_Polygon _NumSides=" + str(sides) + " w0,0,0" + str(str_point1) + str(str_point2)
    ap_o.command(comm1)
    ap_o.command("_SelLast")
    ap_o.command("_Rotate3D w0,0,0 w1,0,0 90")
    ap_o.command("-_Properties _Object _Name Profile _Enter _Enter")
    ap_o.command("_SelNone")
    ap_o.command("-_Sweep1 _SelName Rail _SelName Profile _Enter _Closed=Yes Enter")
    ap_o.command("_SelName Rail")
    ap_o.command("_SelName Profile")
    ap_o.command("_Delete")

#define_radius()
'''Call PlaneExample()
Sub PlaneExample()
    Dim ptOrigin : ptOrigin = Rhino.GetPoint("Plane origin")
    If IsNull(ptOrigin) Then Exit Sub

    Dim ptX : ptX = Rhino.GetPoint("Plane X-axis", ptOrigin)
    If IsNull(ptX) Then Exit Sub

    Dim ptY : ptY = Rhino.GetPoint("Plane Y-axis", ptOrigin)
    If IsNull(ptY) Then Exit Sub
    
    Dim dX : dX = Rhino.Distance(ptOrigin, ptX)
    Dim dY : dY = Rhino.Distance(ptOrigin, ptY)
    Dim arrPlane : arrPlane = Rhino.PlaneFromPoints(ptOrigin, ptX, ptY)

    Call Rhino.AddPlaneSurface(arrPlane, 1.0, 1.0)
    Call Rhino.AddPlaneSurface(arrPlane, dX, dY)
End Sub
'''
def plane_example():
    ui_o = p2r.UserInterface()
    pt_origin = ui_o.get_points("Plane origin")
    pt_x = ui_o.get_points("Plane X-axis")
    pt_y = ui_o.get_points("Plane Y-axis")
    ma_o = p2r.Math()
    d_x = ma_o.distance(pt_origin, pt_x)
    d_y = ma_o.distance(pt_origin, pt_y)
    lp_o = p2r.LineAndPlane()
    arr_plane = lp_o.plane_from_points(pt_origin, pt_x, pt_y)
    sp_o = p2r.SurfaceAndPolysurface()
    sp_o.add_plane_surface(arr_plane, 1.0, 1.0)
    sp_o.add_plane_surface(arr_plane, d_x, d_y)
    
#plane_example()

'''
Option Explicit
'Iteratively scale down a curve until it becomes shorter than a certain length
FitCurveToLength()
Sub FitCurveToLength()
Dim strCurveID
strCurveID = Rhino.GetObject("Select a curve to fit to length", 4, True, True)
'If IsNull(strCurveID) Then Exit Sub
Dim dblLength
dblLength = Rhino.CurveLength(strCurveID)
Dim dblLengthLimit
dblLengthLimit = Rhino.GetReal("Length limit", 0.5 * dblLength, 0.01 * dblLength, dblLength)
'If IsNull(dblLengthLimit) Then Exit Sub
Do
If Rhino.CurveLength(strCurveID) <= dblLengthLimit Then Exit Do
strCurveID = Rhino.ScaleObject(strCurveID, Array(0,0,0), Array(0.95, 0.95, 0.95))
If IsNull(strCurveID) Then
Call Rhino.Print("Something went wrong...")
Exit Sub
End If
Loop
Call Rhino.Print("New curve length: " & Rhino.CurveLength(strCurveID))
End Sub
'''

def fit_curve_to_length():
    sl_o = p2r.Selection()
    cv = sl_o.get_objects("Select a curve to fit to length", 4, True, True)[0]
    cv_o = p2r.Curve()
    length = cv_o.curve_length(cv)
    ui_o = p2r.UserInterface()
    length_limit = ui_o.get_real("Length limit", 0.5 * length, 0.01 * length, length)
    cont = True
    while cont == True:
        if cv_o.curve_length(cv) <= length_limit:
            cont = False
        ob_o = p2r.Object()
        cv = ob_o.scale_objects(cv, (0,0,0), (0.95, 0.95, 0.95))
        
    pr = p2r.Application()
    pr.print_("New curve length:" + str(cv_o.curve_length(cv)))
    print "done"
    
'''Option Explicit

Call WhoFramedTheSurface()
Sub WhoFramedTheSurface()
    Dim idSurface : idSurface = Rhino.GetObject("Surface to frame", 8, True, True)
    If IsNull(idSurface) Then Exit Sub

    Dim intCount : intCount = Rhino.GetInteger("Number of iterations per direction", 20, 2)
    If IsNull(intCount) Then Exit Sub

    Dim uDomain : uDomain = Rhino.SurfaceDomain(idSurface, 0)
    Dim vDomain : vDomain = Rhino.SurfaceDomain(idSurface, 1)
    Dim uStep : uStep = (uDomain(1) - uDomain(0)) / intCount
    Dim vStep : vStep = (vDomain(1) - vDomain(0)) / intCount

    Dim u, v
    Dim pt
    Dim srfFrame

    Call Rhino.EnableRedraw(False)
    For u = uDomain(0) To uDomain(1) Step uStep
        For v = vdomain(0) To vDomain(1) Step vStep
            pt = Rhino.EvaluateSurface(idSurface, Array(u, v))
            
            If Rhino.Distance(pt, Rhino.BrepClosestPoint(idSurface, pt)(0)) < 0.1 Then
                srfFrame = Rhino.SurfaceFrame(idSurface, Array(u, v))
                Call Rhino.AddPlaneSurface(srfFrame, 1.0, 1.0)
            End If
        Next
    Next
    Call Rhino.EnableRedraw(True)
End Sub
'''

def who_framed_the_surface():
    sl_o = p2r.Selection()
    id_surface = sl_o.get_objects("Surface to frame", 8, True, True)[0]
    ur_o = p2r.UserInterface()
    count = ur_o.get_integer("Number of iterations per direction", 20, 2)
    sr_o = p2r.SurfaceAndPolysurface()
    u_domain = sr_o.surface_domain(id_surface, 0)
    v_domain = sr_o.surface_domain(id_surface, 1)
    u_step = (u_domain[1] - u_domain[0]) / count 
    v_step = (v_domain[1] - v_domain[0]) / count 
    en_re = p2r.Document()
    en_re.enable_redraw(False)
    u = u_domain[0]
    v = v_domain[0]
    while u<= u_domain[1]:
        while v <= v_domain[1]:
            pt = sr_o.evaluate_surface(id_surface,(u,v))
            ma_o = p2r.Math()
            if ma_o.distance(pt, sr_o.brep_closest_point(id_surface, pt)[0])< 0.1 :
                srf_frame = sr_o.surface_frame(id_surface, (u,v))
                sr_o.add_plane_surface(srf_frame, 1.0, 1.0)
                v += v_step
        u += u_step
    en_re.enable_redraw(True)
    print "done"
#who_framed_the_surface()

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
def flat_worm():
    sl_o = p2r.Selection()
    crv_object =sl_o.get_objects("Pick a backbone curve", 4, True, False)[0]
    ui_o = p2r.UserInterface()
    int_samples = ui_o.get_integer("Number of cross sections", 100, 5)
    bend_radius = ui_o.get_real("Bend plane radius", 0.5, 0.001)
    perp_radius = ui_o.get_real("Ribbon plane radius", 2.0, 0.001)
    cu_o = p2r.Curve()
    crv_domain = cu_o.curve_domain(crv_object)
    n = -1
    t = crv_domain[0]
    while t <= crv_domain[1]+1e-9:
        n += 1
        crv_curvature =cu_o.curve_curvature(crv_object, t)
        pt_o = p2r.PointAndVector()
        if crv_curvature== None:
            crv_point = cu_o.evaluate_curve(crv_object, t)
            crv_tangent = cu_o.curve_tangent(crv_object, t)
            crv_perp = (0,0,1)
            crv_normal = pt_o.vector_cross_product(crv_tangent,crv_perp)
        else:
            crv_point = crv_curvature[0]
            crv_tangent = crv_curvature[1]
            crv_perp = pt_o.vector_unitize(crv_curvature[4])
            crv_normal = pt_o.vector_cross_product(crv_tangent, crv_perp)
        cross_section_plane = 
        t += (crv_domain[1] - crv_domain[0])/int_samples
        