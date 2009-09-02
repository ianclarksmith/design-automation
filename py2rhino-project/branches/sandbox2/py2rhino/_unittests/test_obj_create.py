import unittest
import py2rhino as p2r

class obj_test(unittest.TestCase):
    
    def testCreateArc(self):
        arc1 = p2r.obj.Arc.create((0,0,0), 5, 45)
        self.assertEqual(type(arc1), p2r.obj.Arc)
    
    def testCreateArcByPt(self):
        arc1 = p2r.obj.Arc.create_by_3pt((0,0,0), (20,0,0), (10,10,0))
        self.assertEqual(type(arc1),p2r.obj.Arc)
        
    def testCreateArcByFillet(self):
        arc1 = p2r.obj.Arc.create_by_3pt((0,0,0), (20,0,0), (10,10,0))
        arc2 = p2r.obj.Arc.create((0,0,0), 5, 45)
        arc3 = arc2.create_by_fillet(arc1,arc2)
        self.assertEqual(type(arc3),p2r.obj.Arc)
    
    def testBox(self):
        box1 = p2r.obj.Box.create(((0,0,0),(0,0,1),(5,0,0),(10,0,0),(20,0,0),(20,0,1),(8,0,0),(20,10,0)))
        self.assertEqual(type(box1),p2r.obj.Box)
        
    def testCircleByPt(self):
        circle1 = p2r.obj.Circle.create_by_3pt((0,0,0),(0,1,0),(1,0,0))
        self.assertEqual(type(circle1),p2r.obj.Circle)
    
    def testCircle(self):
        circle1 = p2r.obj.Circle.create((0,0,0), 45)
        self.assertEqual(type(circle1),p2r.obj.Circle)
        
    def testCreateCone(self):
        cone1 = p2r.obj.Cone.create((0,0,0), (1,1,1), 5)
        self.assertEqual(type(cone1),p2r.obj.Cone)
        
    def testCreateConeByPlane(self):
        cone1 = p2r.obj.Cone.create_by_plane(((10,0,0),(1,0,0),(0,1,0)), 3, 5)
        self.assertEqual(type(cone1),p2r.obj.Cone)
    
    def testCreateCylinder(self):
        cylinder1 = p2r.obj.Cylinder.create((0,0,0),(1,1,1), 5)
        self.assertEqual(type(cylinder1),p2r.obj.Cylinder)
        
    def testCreateCylinderbyPlane(self):
        cylinder1 = p2r.obj.Cylinder.create_by_plane(((10,0,0),(1,0,0),(0,1,0)),2, 5)
        self.assertEqual(type(cylinder1),p2r.obj.Cylinder)
        
    def testCreateEllipse(self):
        ellipse1 = p2r.obj.Ellipse.create(((0,0,0),(0,1,0),(1,0,0)), 5, 10)
        self.assertEqual(type(ellipse1),p2r.obj.Ellipse)
        
    def testCreateEllipseByPt(self):
        ellipse1 = p2r.obj.Ellipse.create_by_3pt((0,0,0),(0,1,0),(1,0,0))
        self.assertEqual(type(ellipse1),p2r.obj.Ellipse)
        
    def testCreateLine(self):
        line1 = p2r.obj.Line.create((0,0,0), (0,0,1))
        self.assertEqual(type(line1),p2r.obj.Line)
        
    def testCreateMesh(self):
        mesh1 = p2r.obj.Mesh.create(((0,0,0),(5,0,0),(10,0,0),(0,5,0),(5,5,0),(10,5,0),(0,10,0),(5,10,0),(10,10,0)), ((0,1,4,4),(2,4,1,1),(0,4,3,3),(2,5,4,4),(3,4,6,6),(5,8,4,4),(6,4,7,7),(8,7,4,4)))
        self.assertEqual(type(mesh1),p2r.obj.Mesh)
        
    def testCreateMeshByPolyline(self):
        polyline1 = p2r.obj.Polyline.create(((0,0,0),(10,0,0),(10,10,0),(0,10,0)))
        mesh1 = p2r.obj.Mesh.create_by_polyline(polyline1)
        self.assertEqual(type(mesh1),p2r.obj.Mesh)
        
    def testCreateNurbsCurveByPt(self):
        nurbscurve1 = p2r.obj.NurbsCurve.create_by_pnts(((0,0,0),(1,0,0),(5,0,0)))
        self.assertEqual(type(nurbscurve1),p2r.obj.NurbsCurve)
        
    def testCreateInterpCrvOnSrf(self):        
        nurvesurface1  = p2r.obj.NurbsSurface.create_by_corner_pnts(((0,0,0),(5,0,0),(5,5,0),(0,5,0)))
        nurbscurve1 = p2r.obj.NurbsCurve.create_interp_crv_on_srf(nurvesurface1,((0,0,0),(5,0,0)))
        self.assertEqual(type(nurbscurve1),p2r.obj.NurbsCurve)
        
    def testCreateInterpCrvOnSrfUV(self):        
        nurvesurface1  = p2r.obj.NurbsSurface.create_by_corner_pnts(((0,0,0),(5,0,0),(5,5,0),(0,5,0)))
        nurbscurve1 = p2r.obj.NurbsCurve.create_interp_crv_on_srf_uv(nurvesurface1,((0,0,0),(5,0,0)))
        self.assertEqual(type(nurbscurve1),p2r.obj.NurbsCurve)
        
    def testCreateInterpCrv(self):
        nurbscurve1 = p2r.obj.NurbsCurve.create_interp_crv(((0,0,0),(1,0,0),(5,0,0)))
        self.assertEqual(type(nurbscurve1),p2r.obj.NurbsCurve)
        
    def testCreateInterpCrvEx(self):
        nurbscurve1 = p2r.obj.NurbsCurve.create_interp_crv_ex(((0,0,0),(1,0,0),(5,0,0)))
        self.assertEqual(type(nurbscurve1),p2r.obj.NurbsCurve)
        
    def testCreateNurbsCurve(self):
        nurbscurve1 = p2r.obj.NurbsCurve.create(((5,0,0),(5,2,0),(3.5,3.5,0)),(0,0,4,4),2)
        self.assertEqual(type(nurbscurve1),p2r.obj.NurbsCurve)
        
    def testCreateNurbsCurveBySurfaceContour(self):
        nurvesurface1  = p2r.obj.NurbsSurface.create_by_corner_pnts(((0,0,0),(5,0,0),(5,5,0),(0,5,0)))
        nurbscurve1 = p2r.obj.NurbsCurve.create_by_srf_contour(nurvesurface1, (0,0,0), (5,0,0))
        self.assertEqual(type(nurbscurve1[0]),p2r.obj.NurbsCurve)
        
    def testCreateNurbsCurveBySurfaceContourCutPlane(self):
        nurvesurface1  = p2r.obj.NurbsSurface.create_by_corner_pnts(((0,0,0),(5,0,0),(5,5,0),(0,5,0)))
        nurbscurve1 = p2r.obj.NurbsCurve.create_by_srf_contour_cut_plane(nurvesurface1, ((0,0,0),(1,0,0),(5,0,0)))
        self.assertEqual(type(nurbscurve1),p2r.obj.NurbsCurve)
        
    def testCreateNurbsCurveBySurfaceSection(self):
        nurvesurface1  = p2r.obj.NurbsSurface.create_by_corner_pnts(((0,0,0),(5,0,0),(5,5,0),(0,5,0)))
        nurbscurve1 = p2r.obj.NurbsCurve.create_by_srf_section(nurvesurface1, ((0,0,0),(1,0,0),(-0.7,0,0.7),(0.7,0,0.7)))
        self.assertEqual(type(nurbscurve1[0]),p2r.obj.NurbsCurve)
        
    def testCreateNurbsCurveBySurfaceEdge(self):
        nurvesurface1  = p2r.obj.NurbsSurface.create_by_corner_pnts(((0,0,0),(5,0,0),(5,5,0),(0,5,0)))
        nurbscurve1 = p2r.obj.NurbsCurve.create_by_srf_edge(nurvesurface1)
        self.assertEqual(type(nurbscurve1[0]),p2r.obj.NurbsCurve)
        
    def testCreateNurbsCurveBySurfaceBorder(self):
        nurvesurface1  = p2r.obj.NurbsSurface.create_by_corner_pnts(((0,0,0),(5,0,0),(5,5,0),(0,5,0)))
        nurbscurve1 = p2r.obj.NurbsCurve.create_by_srf_border(nurvesurface1)
        self.assertEqual(type(nurbscurve1[0]),p2r.obj.NurbsCurve)
        
    def testCreateNurbsCurveBySurfaceISOCurve(self):
        nurvesurface1  = p2r.obj.NurbsSurface.create_by_corner_pnts(((0,0,0),(5,0,0),(5,5,0),(0,5,0)))
        nurbscurve1 = p2r.obj.NurbsCurve.create_by_srf_iso_curve(nurvesurface1,2,0)
        self.assertEqual(type(nurbscurve1),p2r.obj.NurbsCurve)
        
    def testCreateNurbsCurveByFit(self):
        nurvesurface1  = p2r.obj.NurbsSurface.create_by_corner_pnts(((0,0,0),(5,0,0),(5,5,0),(0,5,0)))
        nurbscurve1 = p2r.obj.NurbsCurve.create_by_fit(nurvesurface1)
        self.assertEqual(type(nurbscurve1),p2r.obj.NurbsCurve)
        
    def testCreateNurbsCurveProjectionToMesh(self):
        pl = p2r.obj.Polyline.create(((-20,-20,0),(20,-20,0),(20,20,0),(-20,20,0),(-20,-20,0)))
        mesh1 = p2r.obj.Mesh.create_by_polyline(pl)
        nurbscurve1 = p2r.obj.NurbsCurve.create_by_pnts( ((0,0,10),(10,0,10),(10,10,10),(0,10,10) ), 3)
        nurbscurve2 = p2r.obj.NurbsCurve.create_by_projection_to_mesh(nurbscurve1, mesh1, (0,0,1))
        self.assertEqual(type(nurbscurve2[0]),p2r.obj.NurbsCurve)
        
    def testCreateNurbsCurveProjectionToSurface(self):
        planesurface1 = p2r.obj.PlaneSurface.create(((0,0,0),(0,1,0),(1,0,0)),3,5)
        nurbscurve1 = p2r.obj.NurbsCurve.create(((5,0,0),(5,2,0),(3.5,3.5,0)),(0,0,4,4),2)
        nurbscurve2 = p2r.obj.NurbsCurve.create_by_projection_to_srf(nurbscurve1, planesurface1, (0,0,1))
        self.assertEqual(type(nurbscurve2[0]),p2r.obj.NurbsCurve)
        
    def testCreateNurbsCurveBySurfacePull(self):
        planesurface1 = p2r.obj.PlaneSurface.create(((0,0,0),(0,1,0),(1,0,0)),3,5)
        nurbscurve1 = p2r.obj.NurbsCurve.create(((5,0,0),(5,2,0),(3.5,3.5,0)),(0,0,4,4),2)
        nurbscurve2 = p2r.obj.NurbsCurve.create_by_srf_pull(planesurface1, nurbscurve1)
        self.assertEqual(type(nurbscurve2[0]),p2r.obj.NurbsCurve)   
        
    def testCreateNurbsCurveByShortPath(self):
        planesurface1 = p2r.obj.PlaneSurface.create(((0,0,0),(0,1,0),(1,0,0)),3,5)
        nurbscurve1 = p2r.obj.NurbsCurve.create_by_srf_short_path(planesurface1, (0,0,0), (5,5,5))
        self.assertEqual(type(nurbscurve1),p2r.obj.NurbsCurve)
        
    def testCreateNurbsCurveBySurfacePrincipalCurvature(self):
        nurvesurface1  = p2r.obj.NurbsSurface.create_by_corner_pnts(((0,0,0),(5,0,0),(5,5,0),(0,5,0)))
        nurbscurve1 = p2r.obj.NurbsCurve.create_by_srf_principal_curvature(nurvesurface1, (0,0,0))
        self.assertEqual(type(nurbscurve1[0]),p2r.obj.NurbsCurve)
        
    def testCreatePlanarMeshByCrv(self):
        circle1 = p2r.obj.Circle.create_by_3pt((0,0,0),(0,1,0),(1,0,0))
        planarmesh1 = p2r.obj.PlanarMesh.create_by_crv(circle1,False)
        self.assertEqual(type(planarmesh1),p2r.obj.PlanarMesh)
        
    def testCreateNurbsSurfaceByCutPlane(self):
        circle1 = p2r.obj.Circle.create_by_3pt((0,0,0),(0,1,0),(1,0,0))
        nurbsurface1 = p2r.obj.NurbsSurface.create_by_cut_plane(circle1, (0,0,0), (1,0,0))
        self.assertEqual(type(nurbsurface1),p2r.obj.NurbsSurface)
    
    def testCreateNurbsSurfaceByEdge(self):
        circle1 = p2r.obj.Circle.create_by_3pt((0,0,0),(0,1,0),(1,0,0))        
        circle2 = p2r.obj.Circle.create_by_3pt((0,0,0),(0,5,0),(5,0,0))
        nurbsurface1 = p2r.obj.NurbsSurface.create_by_edge((circle1,circle2))
        self.assertEqual(type(nurbsurface1),p2r.obj.NurbsSurface)
    
    def testCreateNurbsSurfaceByLoft(self):
        circle1 = p2r.obj.Circle.create_by_3pt((0,0,0),(0,1,0),(1,0,0))        
        circle2 = p2r.obj.Circle.create_by_3pt((0,0,0),(0,5,0),(5,0,0))
        nurbsurface1 = p2r.obj.NurbsSurface.create_by_loft((circle1,circle2))
        self.assertEqual(type(nurbsurface1),p2r.obj.NurbsSurface)
    
    def testCreateNurbsSurfaceByPlanarCrv(self):
        circle1 = p2r.obj.Circle.create_by_3pt((0,0,0),(0,1,0),(1,0,0))        
        circle2 = p2r.obj.Circle.create_by_3pt((0,0,0),(0,5,0),(5,0,0))
        nurbsurface1 = p2r.obj.NurbsSurface.create_by_planar_crv((circle1,circle2))
        self.assertEqual(type(nurbsurface1),p2r.obj.NurbsSurface)
        
    def testCreatePlaneSurface(self):
        planesurface1 = p2r.obj.PlaneSurface.create(((0,0,0),(0,1,0),(1,0,0)),3,5)
        self.assertEqual(type(planesurface1),p2r.obj.PlaneSurface)
        
    def testCreatePolyCurve(self):
        ln1 = p2r.obj.Line.create((0,0,0), (10,0,0))
        ln2 = p2r.obj.Line.create((10,0,0), (20,20,0))
        polycurve1 = p2r.obj.PolyCurve.create((ln1,ln2))
        self.assertEqual(type(polycurve1),p2r.obj.PolyCurve)
        
    def testCreatePolyline(self):
        polyline1 = p2r.obj.Polyline.create(((0,0,0),(10,0,0)))
        self.assertEqual(type(polyline1),p2r.obj.Polyline)
        
    def testCreatePolylineByCrv(self):
        arc1 = p2r.obj.Arc.create((0,0,0), 5, 45)
        polyline1 = p2r.obj.Polyline.create_by_crv(arc1)
        self.assertEqual(type(polyline1),p2r.obj.Polyline)
        
    def testCreatePolylineByMeshBorder(self):
        polyline1 = p2r.obj.Polyline.create(((0,0,0),(10,0,0),(10,10,0),(0,10,0),(0,0,0)))
        mesh1 = p2r.obj.Mesh.create_by_polyline(polyline1)
        nurbscurve1 = p2r.obj.Polyline.create_by_mesh_border(mesh1)
        self.assertEqual(type(nurbscurve1),p2r.obj.NurbsCurve)
        
    def testCreatePolylineByMeshPull(self):
        polyline1 = p2r.obj.Polyline.create(((0,0,0),(10,0,0),(10,10,0),(0,10,0),(0,0,0)))
        mesh1 = p2r.obj.Mesh.create_by_polyline(polyline1)
        nurbscurve1 = p2r.obj.NurbsCurve.create(((0,0,0),(5,0,0),(5,5,0)),(0,0,4,4),2)
        nurbscurve2 = p2r.obj.Polyline.create_by_mesh_pull(nurbscurve1, mesh1)
        self.assertEqual(type(nurbscurve2),p2r.obj.NurbsCurve)
        
    def testCreatePolySurfaceCreateBySrfExtrude(self):
        nurvesurface1  = p2r.obj.NurbsSurface.create_by_corner_pnts(((0,0,0),(5,0,0),(5,5,0),(0,5,0)))
        line1 = p2r.obj.Line.create((5,0,0), (10,0,10))
        polysurface1 = p2r.obj.PolySurface.create_by_srf_extrude(nurvesurface1, line1)        
        self.assertEqual(type(polysurface1),p2r.obj.PolySurface)
        
    def testCreatePolySurfaceCreateBySrfJoin(self):
        plane_surface1 = p2r.obj.PlaneSurface.create(((0,0,0),(1,0,0),(0,1,0)),5,3)
        plane_surface2 = p2r.obj.PlaneSurface.create(((0,0,0),(1,0,0),(0,-1,0)),5,3)
        polysurface1 = p2r.obj.PolySurface.create_by_srf_join((plane_surface1,plane_surface2))        
        self.assertEqual(type(polysurface1),p2r.obj.PolySurface)
        
    def testCreateSphere(self):
        sphere1 = p2r.obj.Sphere.create((0,0,0), 3)
        self.assertEqual(type(sphere1),p2r.obj.Sphere)
        
    def testCreateSphereByPlane(self):
        sphere1 = p2r.obj.Sphere.create_by_plane((0,0,0), 3)
        self.assertEqual(type(sphere1),p2r.obj.Sphere)
        
    def testCreateTorus(self):
        torus1 = p2r.obj.Torus.create((0,0,0), 5, 3)
        self.assertEqual(type(torus1),p2r.obj.Torus)    
        
    def testCreateTorusByPlane(self):
        torus1 = p2r.obj.Torus.create((0,0,0), 5, 3)
        self.assertEqual(type(torus1),p2r.obj.Torus)
        

if __name__ == '__main__':

    unittest.main()

    print "done"
