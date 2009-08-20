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
        cone1 = p2r.obj.Cone.create_by_plane((0,0,0), 3, 5)
        self.assertEqual(type(cone1),p2r.obj.Cone)
    
    def testCreateCylinder(self):
        cylinder1 = p2r.obj.Cylinder.create((0,0,0),(1,1,1), 5)
        self.assertEqual(type(cylinder1),p2r.obj.Cylinder)
        
    def testCreateCylinderbyPlane(self):
        cylinder1 = p2r.obj.Cylinder.create_by_plane((0,0,0),2, 5)
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
        polyline1 = p2r.obj.Polyline.create(((0,0,0),(10,0,0)))
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
        mesh1 = p2r.obj.Mesh.create(((0,0,0),(5,0,0),(10,0,0),(0,5,0),(5,5,0),(10,5,0),(0,10,0),(5,10,0),(10,10,0)), ((0,1,4,4),(2,4,1,1),(0,4,3,3),(2,5,4,4),(3,4,6,6),(5,8,4,4),(6,4,7,7),(8,7,4,4)))
        nurbscurve1 = p2r.obj.NurbsCurve.create(((5,0,0),(5,2,0),(3.5,3.5,0)),(0,0,4,4),2)
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
        
    def testCreatePolyline(self):
        polyline1 = p2r.obj.Polyline.create(((0,0,0),(10,0,0)))
        self.assertEqual(type(polyline1),p2r.obj.Polyline)
        
    def testCreatePolylineByCrv(self):
        arc1 = p2r.obj.Arc.create((0,0,0), 5, 45)
        polyline1 = p2r.obj.Polyline.create_by_crv(arc1)
        self.assertEqual(type(polyline1),p2r.obj.Polyline)
        
    def testCreatePolylineByMeshBorder(self):
        mesh1 = p2r.obj.Mesh.create(((0,0,0),(5,0,0),(10,0,0),(0,5,0),(5,5,0),(10,5,0),(0,10,0),(5,10,0),(10,10,0)), ((0,1,4,4),(2,4,1,1),(0,4,3,3),(2,5,4,4),(3,4,6,6),(5,8,4,4),(6,4,7,7),(8,7,4,4)))
        nurbscurve1 = p2r.obj.Polyline.create_by_mesh_border(mesh1)
        self.assertEqual(type(nurbscurve1[0]),p2r.obj.NurbsCurve)
        
    def testCreatePolylineByMeshPull(self):
        mesh1 = p2r.obj.Mesh.create(((0,0,0),(5,0,0),(10,0,0),(0,5,0),(5,5,0),(10,5,0),(0,10,0),(5,10,0),(10,10,0)), ((0,1,4,4),(2,4,1,1),(0,4,3,3),(2,5,4,4),(3,4,6,6),(5,8,4,4),(6,4,7,7),(8,7,4,4)))
        nurbscurve1 = p2r.obj.NurbsCurve.create(((5,0,0),(5,2,0),(3.5,3.5,0)),(0,0,4,4),2)
        nurbscurve2 = p2r.obj.Polyline.create_by_mesh_pull(nurbscurve1, mesh1)
        self.assertEqual(type(nurbscurve2),p2r.obj.NurbsCurve)
        
    def testCreatePolySurfaceCreateBySrfExtrude(self):
        nurvesurface1  = p2r.obj.NurbsSurface.create_by_corner_pnts(((0,0,0),(5,0,0),(5,5,0),(0,5,0)))
        line1 = p2r.obj.Line.create((5,0,0), (10,0,10))
        polysurface1 = p2r.obj.PolySurface.create_by_srf_extrude(nurvesurface1, line1)        
        self.assertEqual(type(polysurface1),p2r.obj.PolySurface)
        
    def testCreatePolySurfaceCreateBySrfJoin(self):
        plane_surface1 = p2r.obj.PlaneSurface.create(((0,0,0),(1,0,0),(0,1,0)),5,3)
        plane_surface2 = p2r.obj.PlaneSurface.create(((0,1,0),(1,2,0),(0,1,3)),5,3)
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
        
    def testArcBoxMorph(self):
        arc1 = p2r.obj.Arc.create((0,0,0), 5, 45)
        arc2 = arc1.defm.box_morph(((0,0,0),(0,1,0),(10,0,0),(0,10,0),(0,0,10),(1,0,0),(0,5,5),(5,0,0)))
        self.assertEqual(type(arc2),p2r.obj.Arc)
        
    def testArcShear(self):
        arc1 = p2r.obj.Arc.create((0,0,0), 5, 45)
        arc2 = arc1.defm.shear((0,0,0),(10,10,10),45)
        self.assertEqual(type(arc2),p2r.obj.Arc)
        
    def testArcTrfm(self):
        arc1 = p2r.obj.Arc.create((0,0,0), 5, 45)
        arc2 = arc1.defm.trfm(((0,0,0),(0,1,0),(0,2,0),(0,3,0),(1,0,0),(1,1,1),(1,2,0),(1,3,0),(2,0,0),(2,1,0),(2,2,1),(2,3,0),(3,0,0),(3,1,0),(3,2,0),(3,3,1)))
        self.assertEqual(type(arc2),p2r.obj.Arc)
        
    def testArcCopySub(self):
        arc1 = p2r.obj.Arc.create_by_3pt((0,0,0), (20,0,0), (10,10,0))
        arc2 = arc1.dupl.copy_by_sub((0,0,0),(10,0,0))
        self.assertEqual(type(arc2),p2r.obj.Arc)
        
    def testArcCopyMove(self):
        arc1 = p2r.obj.Arc.create_by_3pt((0,0,0), (20,0,0), (10,10,0))
        arc2 = arc1.dupl.copy_move()
        self.assertEqual(type(arc2),p2r.obj.Arc)
        
    def testArcCopyMoveByVec(self):
        arc1 = p2r.obj.Arc.create_by_3pt((0,0,0), (20,0,0), (10,10,0))
        arc2 = arc1.dupl.copy_move_by_vec()
        self.assertEqual(type(arc2),p2r.obj.Arc)
        
    def testArcCopyByOffset(self):
        arc1 = p2r.obj.Arc.create_by_3pt((0,0,0), (20,0,0), (10,10,0))
        arc2 = arc1.dupl.copy_by_offset((0,0,0),1)
        self.assertEqual(type(arc2),p2r.obj.Arc)
        
    def testArcCopyBySplit(self):
        arc1 = p2r.obj.Arc.create_by_3pt((0,0,0), (20,0,0), (10,10,0))
        arc2 = arc1.dupl.copy_by_split((0,0,0),1)
        self.assertEqual(type(arc2[0]),p2r.obj.Arc)
        
    def testArcCopyByTrim(self):
        arc1 = p2r.obj.Arc.create_by_3pt((0,0,0), (20,0,0), (10,10,0))
        arc2 = arc1.dupl.copy_by_trim((0,1))
        self.assertEqual(type(arc2),p2r.obj.Arc)        
    
    def testArcCurvature(self):
        arc1 = p2r.obj.Arc.create_by_3pt((0,0,0), (20,0,0), (10,10,0))
        arc2 = arc1.eval.curvature(1)
        self.assertEqual(len(arc2),5)      
    
    def testArcEvalDeriv(self):
        arc1 = p2r.obj.Arc.create_by_3pt((0,0,0), (20,0,0), (10,10,0))
        arc2 = arc1.eval.evaluate_derivatives(1,1)
        self.assertEqual(len(arc2),2)   
    
    def testArcFrame(self):
        arc1 = p2r.obj.Arc.create_by_3pt((0,0,0), (20,0,0), (10,10,0))
        arc2 = arc1.eval.frame(1)
        self.assertEqual(len(arc2),4) 
    
    def testArcPerpFrame(self):
        arc1 = p2r.obj.Arc.create_by_3pt((0,0,0), (20,0,0), (10,10,0))
        arc2 = arc1.eval.frame(1)
        self.assertEqual(len(arc2),4) 
    
    def testArcTangent(self):
        arc1 = p2r.obj.Arc.create_by_3pt((0,0,0), (20,0,0), (10,10,0))
        arc2 = arc1.eval.tangent(1)
        self.assertEqual(len(arc2),3) 
    
    def testArcEvaluate(self):
        arc1 = p2r.obj.Arc.create_by_3pt((0,0,0), (20,0,0), (10,10,0))
        arc2 = arc1.eval.evaluate(1)
        self.assertEqual(len(arc2),3) 
    
    def testArcClosed(self):
        arc1 = p2r.obj.Arc.create((0,0,0), 5, 45)
        arc2 = arc1.func.close()
        self.assertEqual(type(arc2),p2r.obj.Arc)
    
    def testArcExtend(self):
        arc1 = p2r.obj.Arc.create_by_3pt((0,0,0), (20,0,0), (10,10,0))
        arc2 = p2r.obj.Arc.create((0,0,0), 5, 45)
        arc3 = arc1.func.extend(1,1,arc2)
        self.assertEqual(type(arc3),p2r.obj.Arc)
    
    def testArcExtendLength(self):
        arc1 = p2r.obj.Arc.create((0,0,0), 5, 45)
        arc2 = arc1.func.extend_length(2,2,3)
        #print arc2
        self.assertEqual(type(arc2),p2r.obj.NurbsCurve) #TODO: to check if it is suppose to return as a nurbscurve
        
    def testArcExtendPnt(self):
        arc1 = p2r.obj.Arc.create((0,0,0), 5, 45)
        arc2 = arc1.func.extend_pnt(1,(1,1,1))
        self.assertEqual(type(arc2),p2r.obj.NurbsCurve) #TODO: to check if it is suppose to return as a nurbscurve
        
    def testArcGroups(self):
        arc1 = p2r.obj.Arc.create((0,0,0), 5, 45)
        arc2 = arc1.grps.groups()
        self.assertEqual(type(arc2),p2r.obj.Arc)
        
    def testArcTopGroup(self):
        arc1 = p2r.obj.Arc.create((0,0,0), 5, 45)
        arc2 = arc1.grps.top_group()
        self.assertEqual(type(arc2),p2r.obj.Arc)  
        
    def testArcIndex(self):
        arc1 = p2r.obj.Arc.create((0,0,0), 5, 45)
        arc2 = arc1.mtrl.index()
        self.assertEqual(type(arc2),int)       
        
    def testArcSource(self):
        arc1 = p2r.obj.Arc.create((0,0,0), 5, 45)
        arc2 = arc1.mtrl.source(0)              #TODO: if 0 is not provided, none is returned.
        self.assertEqual(type(arc2),int)   
        
    def testArcAngle(self):
        arc1 = p2r.obj.Arc.create((0,0,0), 5, 45)
        arc2 = arc1.prop.angle()
        self.assertEqual(type(arc2),float)   
        
    def testArcCenterPnt(self):
        arc1 = p2r.obj.Arc.create((0,0,0), 5, 45)
        arc2 = arc1.prop.center_pnt()
        self.assertEqual(len(arc2),3)   
        
    def testArcMidPnt(self):
        arc1 = p2r.obj.Arc.create((0,0,0), 5, 45)
        arc2 = arc1.prop.mid_pnt()
        self.assertEqual(len(arc2),3)   
        
    def testArcRadius(self):
        arc1 = p2r.obj.Arc.create((0,0,0), 5, 45)
        radius = arc1.prop.radius()
        self.assertEqual(type(radius),float)   
        
    def testArcAddMesh(self):
        arc1 = p2r.obj.Arc.create((0,0,0), 5, 45)
        arc2 = arc1.rndr.add_mesh()
        self.assertEqual(type(arc2),bool)   
        
    def testArcEnable(self):
        arc1 = p2r.obj.Arc.create((0,0,0), 5, 45)
        arc2 = arc1.rndr.enable()
        self.assertEqual(type(arc2),bool)   
        
    def testArcHasMesh(self):
        arc1 = p2r.obj.Arc.create((0,0,0), 5, 45)
        arc2 = arc1.rndr.has_mesh()
        self.assertEqual(type(arc2),bool)   
            
    def testArcHide(self):
        arc1 = p2r.obj.Arc.create((0,0,0), 5, 45)
        arc2 = arc1.stat.hide()
        self.assertEqual(type(arc2),int)  
        
    def testArcLock(self):
        arc1 = p2r.obj.Arc.create((0,0,0), 5, 45)
        arc2 = arc1.stat.lock()
        self.assertEqual(type(arc2),int)  
        
    def testArcMatchObjectAttributes(self):
        arc1 = p2r.obj.Arc.create((0,0,0), 5, 45)
        arc2 = p2r.obj.Arc.create_by_3pt((0,0,0), (20,0,0), (10,10,0))
        match = arc1.stat.match_object_attributes(arc2)
        self.assertEqual(type(match),int)  
        
    def testArcResetObjectAttributes(self):
        arc1 = p2r.obj.Arc.create((0,0,0), 5, 45)
        reset = arc1.stat.reset_object_attributes()
        self.assertEqual(type(reset),int)  
        
    def testArcMoveToLayoutSpace(self):
        arc1 = p2r.obj.Arc.create((0,0,0), 5, 45)
        reset = arc1.stat.move_to_layout_space()
        self.assertEqual(type(reset),str)  
        
    def testArcSelect(self):
        arc1 = p2r.obj.Arc.create((0,0,0), 5, 45)
        sel = arc1.stat.select()
        self.assertEqual(type(sel),int)  
        
    def testArcShow(self):
        arc1 = p2r.obj.Arc.create((0,0,0), 5, 45)
        sel = arc1.stat.show()
        self.assertEqual(type(sel),int)  
        
    def testArcUnlock(self):
        arc1 = p2r.obj.Arc.create((0,0,0), 5, 45)
        arc2 = arc1.stat.unlock()
        self.assertEqual(type(arc2),int) 
        
    def testArcUnselect(self):
        arc1 = p2r.obj.Arc.create((0,0,0), 5, 45)
        sel = arc1.stat.unselect()
        self.assertEqual(type(sel),int) 
        
    def testArcIsClosable(self):
        arc1 = p2r.obj.Arc.create((0,0,0), 5, 45)
        closable = arc1.test.is_closable()
        self.assertEqual(type(closable),bool) 
        
    def testArcIsClosed(self):
        arc1 = p2r.obj.Arc.create((0,0,0), 5, 45)
        closed = arc1.test.is_closed()
        self.assertEqual(type(closed),bool) 
        
    def testArcInPlane(self):
        arc1 = p2r.obj.Arc.create((0,0,0), 5, 45)
        plane = arc1.test.in_plane()
        self.assertEqual(type(plane),bool) 
        
    def testArcIsLinear(self):
        arc1 = p2r.obj.Arc.create((0,0,0), 5, 45)
        linear = arc1.test.is_linear()
        self.assertEqual(type(linear),bool)
        
    def testArcIsPeriodic(self):
        arc1 = p2r.obj.Arc.create((0,0,0), 5, 45)
        periodic = arc1.test.is_periodic()
        self.assertEqual(type(periodic),bool)
        
    def testArcIsPlanar(self):
        arc1 = p2r.obj.Arc.create((0,0,0), 5, 45)
        planar = arc1.test.is_planar()
        self.assertEqual(type(planar),bool)
        
    def testArcIsRational(self):
        arc1 = p2r.obj.Arc.create((0,0,0), 5, 45)
        rational = arc1.test.is_rational()
        self.assertEqual(type(rational),bool)   
        
    def testArcIsPntOnCrv(self):
        arc1 = p2r.obj.Arc.create((0,0,0), 5, 45)
        on_crv = arc1.test.is_pnt_on_crv((0,0,0))
        self.assertEqual(type(on_crv),bool)         
        
    def testArcMirror(self):
        arc1 = p2r.obj.Arc.create((0,0,0), 5, 45)
        arc2 = arc1.trfm.mirror((0,0,0),(1,1,1))
        self.assertEqual(type(arc2),p2r.obj.Arc)  
        
    def testArcMove(self):
        arc1 = p2r.obj.Arc.create((0,0,0), 5, 45)
        arc2 = arc1.trfm.move((0,0,0),(1,1,1))
        self.assertEqual(type(arc2),p2r.obj.Arc)  
        
    def testArcMoveByVec(self):
        arc1 = p2r.obj.Arc.create((0,0,0), 5, 45)
        arc2 = arc1.trfm.move_by_vec(((0,0,0),(1,1,1)))
        self.assertEqual(type(arc2),p2r.obj.Arc)  
        
    def testArcOrient(self):
        arc1 = p2r.obj.Arc.create((0,0,0), 5, 45)
        arc2 = arc1.trfm.orient((0,0,0),(1,1,1))
        self.assertEqual(type(arc2),p2r.obj.Arc)  
        
    def testArcRemap(self):
        arc1 = p2r.obj.Arc.create((0,0,0), 5, 45)
        arc2 = arc1.trfm.remap((0,0,0),(1,1,1))
        self.assertEqual(type(arc2),p2r.obj.Arc)  
        
    def testArcRotate(self):
        arc1 = p2r.obj.Arc.create((0,0,0), 5, 45)
        arc2 = arc1.trfm.rotate((0,0,0),45)
        self.assertEqual(type(arc2),p2r.obj.Arc)  
        
    def testArcScale(self):
        arc1 = p2r.obj.Arc.create((0,0,0), 5, 45)
        arc2 = arc1.trfm.scale((0,0,0),(1,2,3))
        self.assertEqual(type(arc2),p2r.obj.Arc)     
        
    def testArcDescription(self):
        arc1 = p2r.obj.Arc.create((0,0,0), 5, 45)
        arc2 = arc1.util.description()
        self.assertEqual(type(arc2),unicode)   
        
    def testArcDump(self):
        arc1 = p2r.obj.Arc.create((0,0,0), 5, 45)
        arc2 = arc1.util.dump()
        self.assertEqual(type(arc2),unicode) 
        
    def testBoxMorph(self):
        box1 = p2r.obj.Box.create(((0,0,0),(0,0,1),(5,0,0),(10,0,0),(20,0,0),(20,0,1),(8,0,0),(20,10,0)))
        box2 = box1.defm.box_morph(((0,0,0),(0,1,0),(10,0,0),(0,10,0),(0,0,10),(1,0,0),(0,5,5),(5,0,0)))
        self.assertEqual(type(box2),p2r.obj.Box)
        
    def testBoxShear(self):
        box1 = p2r.obj.Box.create(((0,0,0),(0,0,1),(5,0,0),(10,0,0),(20,0,0),(20,0,1),(8,0,0),(20,10,0)))
        box2 = box1.defm.shear((0,0,0),(10,10,10),45)
        self.assertEqual(type(box2),p2r.obj.Box)
        
    def testBoxTrfm(self):
        box1 = p2r.obj.Box.create(((0,0,0),(0,0,1),(5,0,0),(10,0,0),(20,0,0),(20,0,1),(8,0,0),(20,10,0)))
        box2 = box1.defm.trfm(((0,0,0),(0,1,0),(0,2,0),(0,3,0),(1,0,0),(1,1,1),(1,2,0),(1,3,0),(2,0,0),(2,1,0),(2,2,1),(2,3,0),(3,0,0),(3,1,0),(3,2,0),(3,3,1)))
        self.assertEqual(type(box2),p2r.obj.Box)
        
    def testBoxCopyMove(self):
        box1 = p2r.obj.Box.create(((0,0,0),(0,0,1),(5,0,0),(10,0,0),(20,0,0),(20,0,1),(8,0,0),(20,10,0)))
        box2 = box1.dupl.copy_move()
        self.assertEqual(type(box2),p2r.obj.Box)
        
    def testBoxCopyMoveByVec(self):
        box1 = p2r.obj.Box.create(((0,0,0),(0,0,1),(5,0,0),(10,0,0),(20,0,0),(20,0,1),(8,0,0),(20,10,0)))
        box2 = box1.dupl.copy_move_by_vec()
        self.assertEqual(type(box2),p2r.obj.Box)
        
    def testBoxEvaluate(self):
        box1 = p2r.obj.Box.create(((0,0,0),(0,0,1),(5,0,0),(10,0,0),(20,0,0),(20,0,1),(8,0,0),(20,10,0)))
        box2 = box1.eval.evaluate(1)
        self.assertEqual(len(box2),3) 

    def testBoxEvalDeriv(self):
        box1 = p2r.obj.Box.create(((0,0,0),(0,0,1),(5,0,0),(10,0,0),(20,0,0),(20,0,1),(8,0,0),(20,10,0)))
        box2 = box1.eval.evaluate_derivatives(1,1)
        self.assertEqual(type(box2),list)   

    def testBoxEvalFrame(self):
        box1 = p2r.obj.Box.create(((0,0,0),(0,0,1),(5,0,0),(10,0,0),(20,0,0),(20,0,1),(8,0,0),(20,10,0)))
        box2 = box1.eval.evaluate_frame((0,1))
        self.assertEqual(type(box2),list)   
               
    def testBoxGroups(self):
        box1 = p2r.obj.Box.create(((0,0,0),(0,0,1),(5,0,0),(10,0,0),(20,0,0),(20,0,1),(8,0,0),(20,10,0)))
        box2 = box1.grps.groups()
        self.assertEqual(type(box2),p2r.obj.Box)
        
    def testBoxTopGroup(self):
        box1 = p2r.obj.Box.create(((0,0,0),(0,0,1),(5,0,0),(10,0,0),(20,0,0),(20,0,1),(8,0,0),(20,10,0)))
        box2 = box1.grps.top_group()
        self.assertEqual(type(box2),p2r.obj.Box)  

    def testBoxFlip(self):
        box1 = p2r.obj.Box.create(((0,0,0),(0,0,1),(5,0,0),(10,0,0),(20,0,0),(20,0,1),(8,0,0),(20,10,0)))
        box2 = box1.modf.flip()
        self.assertEqual(type(box2),bool)  
        
    def testBoxInsertKnot(self):
        box1 = p2r.obj.Box.create(((0,0,0),(0,0,1),(5,0,0),(10,0,0),(20,0,0),(20,0,1),(8,0,0),(20,10,0)))
        box2 = box1.modf.insert_knot((0,1),0)
        self.assertEqual(type(box2),bool)  

    def testBoxRebuild(self):
        box1 = p2r.obj.Box.create(((0,0,0),(0,0,1),(5,0,0),(10,0,0),(20,0,0),(20,0,1),(8,0,0),(20,10,0)))
        box2 = box1.modf.rebuild()
        self.assertEqual(type(box2),bool)  
        
    def testBoxRemoveKnot(self):
        box1 = p2r.obj.Box.create(((0,0,0),(0,0,1),(5,0,0),(10,0,0),(20,0,0),(20,0,1),(8,0,0),(20,10,0)))
        box2 = box1.modf.remove_knot((0,1),0)
        self.assertEqual(type(box2),bool)  

    def testBoxReverse(self):
        box1 = p2r.obj.Box.create(((0,0,0),(0,0,1),(5,0,0),(10,0,0),(20,0,0),(20,0,1),(8,0,0),(20,10,0)))
        box2 = box1.modf.reverse()
        self.assertEqual(type(box2),bool)  

    def testBoxShrinkTrimmed(self):
        box1 = p2r.obj.Box.create(((0,0,0),(0,0,1),(5,0,0),(10,0,0),(20,0,0),(20,0,1),(8,0,0),(20,10,0)))
        box2 = box1.modf.shrink_trimmed()
        self.assertEqual(type(box2),bool)  

    def testBoxSeam(self):
        box1 = p2r.obj.Box.create(((0,0,0),(0,0,1),(5,0,0),(10,0,0),(20,0,0),(20,0,1),(8,0,0),(20,10,0)))
        box2 = box1.modf.seam(0,1)
        self.assertEqual(type(box2),bool) 

    def testBoxIndex(self):
        box1 = p2r.obj.Box.create(((0,0,0),(0,0,1),(5,0,0),(10,0,0),(20,0,0),(20,0,1),(8,0,0),(20,10,0)))
        box2 = box1.mtrl.index()
        self.assertEqual(type(box2),int) 
        
    def testBoxSource(self):
        box1 = p2r.obj.Box.create(((0,0,0),(0,0,1),(5,0,0),(10,0,0),(20,0,0),(20,0,1),(8,0,0),(20,10,0)))
        box2 = box1.mtrl.source()
        self.assertEqual(type(box2),int)
        
    def testBoxVolume(self):
        box1 = p2r.obj.Box.create(((0,0,0),(0,0,1),(5,0,0),(10,0,0),(20,0,0),(20,0,1),(8,0,0),(20,10,0)))
        box2 = box1.prop.volume()
        self.assertEqual(type(box2),tuple)  
        
    def testBoxVolumeCentroid(self):
        box1 = p2r.obj.Box.create(((0,0,0),(0,0,1),(5,0,0),(10,0,0),(20,0,0),(20,0,1),(8,0,0),(20,10,0)))
        box2 = box1.prop.volume_centroid()
        self.assertEqual(type(box2),tuple) 
        
    def testBoxVolumeMoments(self):
        box1 = p2r.obj.Box.create(((0,0,0),(0,0,1),(5,0,0),(10,0,0),(20,0,0),(20,0,1),(8,0,0),(20,10,0)))
        box2 = box1.prop.volume_moments()
        self.assertEqual(type(box2),tuple) 
        
    def testBoxAddMesh(self):
        box1 = p2r.obj.Box.create(((0,0,0),(0,0,1),(5,0,0),(10,0,0),(20,0,0),(20,0,1),(8,0,0),(20,10,0)))
        box2 = box1.rndr.add_mesh()
        self.assertEqual(type(box2),bool)   
        
    def testBoxEnable(self):
        box1 = p2r.obj.Box.create(((0,0,0),(0,0,1),(5,0,0),(10,0,0),(20,0,0),(20,0,1),(8,0,0),(20,10,0)))
        box2 = box1.rndr.enable()
        self.assertEqual(type(box2),bool)   
        
    def testBoxHasMesh(self):
        box1 = p2r.obj.Box.create(((0,0,0),(0,0,1),(5,0,0),(10,0,0),(20,0,0),(20,0,1),(8,0,0),(20,10,0)))
        box2 = box1.rndr.has_mesh()
        self.assertEqual(type(box2),bool)   
        
    def testBoxHide(self):
        box1 = p2r.obj.Box.create(((0,0,0),(0,0,1),(5,0,0),(10,0,0),(20,0,0),(20,0,1),(8,0,0),(20,10,0)))
        box2 = box1.stat.hide()
        self.assertEqual(type(box2),int)  
        
    def testBoxLock(self):
        box1 = p2r.obj.Box.create(((0,0,0),(0,0,1),(5,0,0),(10,0,0),(20,0,0),(20,0,1),(8,0,0),(20,10,0)))
        box2 = box1.stat.lock()
        self.assertEqual(type(box2),int)  
        
    def testBoxMatchObjectAttributes(self):
        box1 = p2r.obj.Box.create(((0,0,0),(0,0,1),(5,0,0),(10,0,0),(20,0,0),(20,0,1),(8,0,0),(20,10,0)))
        box2 = p2r.obj.Box.create(((0,0,0),(0,0,1),(5,0,0),(10,0,0),(20,0,0),(20,0,1),(8,0,0),(20,10,0)))
        match = box1.stat.match_object_attributes(box2)
        self.assertEqual(type(match),int)  
        
    def testBoxResetObjectAttributes(self):
        box1 = p2r.obj.Box.create(((0,0,0),(0,0,1),(5,0,0),(10,0,0),(20,0,0),(20,0,1),(8,0,0),(20,10,0)))
        reset = box1.stat.reset_object_attributes()
        self.assertEqual(type(reset),int)  
        
    def testBoxMoveToLayoutSpace(self):
        box1 = p2r.obj.Box.create(((0,0,0),(0,0,1),(5,0,0),(10,0,0),(20,0,0),(20,0,1),(8,0,0),(20,10,0)))
        reset = box1.stat.move_to_layout_space()
        self.assertEqual(type(reset),str)  
        
    def testBoxSelect(self):
        box1 = p2r.obj.Box.create(((0,0,0),(0,0,1),(5,0,0),(10,0,0),(20,0,0),(20,0,1),(8,0,0),(20,10,0)))
        sel = box1.stat.select()
        self.assertEqual(type(sel),int)  
        
    def testBoxShow(self):
        box1 = p2r.obj.Box.create(((0,0,0),(0,0,1),(5,0,0),(10,0,0),(20,0,0),(20,0,1),(8,0,0),(20,10,0)))
        sel = box1.stat.show()
        self.assertEqual(type(sel),int)  
        
    def testBoxUnlock(self):
        box1 = p2r.obj.Box.create(((0,0,0),(0,0,1),(5,0,0),(10,0,0),(20,0,0),(20,0,1),(8,0,0),(20,10,0)))
        box2 = box1.stat.unlock()
        self.assertEqual(type(box2),int) 
        
    def testBoxUnselect(self):
        box1 = p2r.obj.Box.create(((0,0,0),(0,0,1),(5,0,0),(10,0,0),(20,0,0),(20,0,1),(8,0,0),(20,10,0)))
        sel = box1.stat.unselect()
        self.assertEqual(type(sel),int) 
        
    def testBoxIsBrep(self):
        box1 = p2r.obj.Box.create(((0,0,0),(0,0,1),(5,0,0),(10,0,0),(20,0,0),(20,0,1),(8,0,0),(20,10,0)))
        box2 = box1.test.is_brep()
        self.assertEqual(type(box2),bool) 
        
    def testBoxIsBrepManifold(self):
        box1 = p2r.obj.Box.create(((0,0,0),(0,0,1),(5,0,0),(10,0,0),(20,0,0),(20,0,1),(8,0,0),(20,10,0)))
        box2 = box1.test.is_brep_manifold()
        self.assertEqual(type(box2),bool) 
        
    def testBoxIsParameterOnSrf(self):
        box1 = p2r.obj.Box.create(((0,0,0),(0,0,1),(5,0,0),(10,0,0),(20,0,0),(20,0,1),(8,0,0),(20,10,0)))
        box2 = box1.test.is_parameter_on_srf((0,0))
        self.assertEqual(type(box2),bool) 
        
    def testBoxIsPointInSrf(self):
        box1 = p2r.obj.Box.create(((0,0,0),(0,0,1),(5,0,0),(10,0,0),(20,0,0),(20,0,1),(8,0,0),(20,10,0)))
        box2 = box1.test.is_pnt_in_srf((0,0,0))
        self.assertEqual(type(box2),bool) 
        
    def testBoxIsPointOnSrf(self):
        box1 = p2r.obj.Box.create(((0,0,0),(0,0,1),(5,0,0),(10,0,0),(20,0,0),(20,0,1),(8,0,0),(20,10,0)))
        box2 = box1.test.is_pnt_on_srf((0,0,0))
        self.assertEqual(type(box2),bool) 
        
    def testBoxIsPolySurfaceClosed(self):
        box1 = p2r.obj.Box.create(((0,0,0),(0,0,1),(5,0,0),(10,0,0),(20,0,0),(20,0,1),(8,0,0),(20,10,0)))
        box2 = box1.test.is_poly_surface_closed()
        self.assertEqual(type(box2),bool) 
        
    def testBoxIsPlaneSurface(self):
        box1 = p2r.obj.Box.create(((0,0,0),(0,0,1),(5,0,0),(10,0,0),(20,0,0),(20,0,1),(8,0,0),(20,10,0)))
        box2 = box1.test.is_plane_surface()
        self.assertEqual(type(box2),bool) 
        
    def testBoxIsPolySrf(self):
        box1 = p2r.obj.Box.create(((0,0,0),(0,0,1),(5,0,0),(10,0,0),(20,0,0),(20,0,1),(8,0,0),(20,10,0)))
        box2 = box1.test.is_poly_srf()
        self.assertEqual(type(box2),bool)     
        
    def testBoxIsPolySrfPlanar(self):
        box1 = p2r.obj.Box.create(((0,0,0),(0,0,1),(5,0,0),(10,0,0),(20,0,0),(20,0,1),(8,0,0),(20,10,0)))
        box2 = box1.test.is_poly_srf_planar()
        self.assertEqual(type(box2),bool)     
        
    def testBoxIsSrfClosed(self):
        box1 = p2r.obj.Box.create(((0,0,0),(0,0,1),(5,0,0),(10,0,0),(20,0,0),(20,0,1),(8,0,0),(20,10,0)))
        box2 = box1.test.is_srf_closed(0)
        self.assertEqual(type(box2),bool)   
        
    def testBoxIsSrfPeriodic(self):
        box1 = p2r.obj.Box.create(((0,0,0),(0,0,1),(5,0,0),(10,0,0),(20,0,0),(20,0,1),(8,0,0),(20,10,0)))
        box2 = box1.test.is_srf_periodic(0)
        self.assertEqual(type(box2),bool) 
        
    def testBoxIsSrfPlanar(self):
        box1 = p2r.obj.Box.create(((0,0,0),(0,0,1),(5,0,0),(10,0,0),(20,0,0),(20,0,1),(8,0,0),(20,10,0)))
        box2 = box1.test.is_srf_planar()
        self.assertEqual(type(box2),bool)  
        
    def testBoxIsSrfRational(self):
        box1 = p2r.obj.Box.create(((0,0,0),(0,0,1),(5,0,0),(10,0,0),(20,0,0),(20,0,1),(8,0,0),(20,10,0)))
        box2 = box1.test.is_srf_rational()
        self.assertEqual(type(box2),bool)  
        
    def testBoxIsSrfSingular(self):
        box1 = p2r.obj.Box.create(((0,0,0),(0,0,1),(5,0,0),(10,0,0),(20,0,0),(20,0,1),(8,0,0),(20,10,0)))
        box2 = box1.test.is_srf_singular(0)
        self.assertEqual(type(box2),bool)  
        
    def testBoxIsSrfTrimmed(self):
        box1 = p2r.obj.Box.create(((0,0,0),(0,0,1),(5,0,0),(10,0,0),(20,0,0),(20,0,1),(8,0,0),(20,10,0)))
        box2 = box1.test.is_srf_trimmed()
        self.assertEqual(type(box2),bool)

    def testBoxMirror(self):
        box1 = p2r.obj.Box.create(((0,0,0),(0,0,1),(5,0,0),(10,0,0),(20,0,0),(20,0,1),(8,0,0),(20,10,0)))
        box2 = box1.trfm.mirror((0,0,0),(1,1,1))
        self.assertEqual(type(box2),p2r.obj.Box)  
        
    def testBoxMove(self):
        box1 = p2r.obj.Box.create(((0,0,0),(0,0,1),(5,0,0),(10,0,0),(20,0,0),(20,0,1),(8,0,0),(20,10,0)))
        box2 = box1.trfm.move((0,0,0),(1,1,1))
        self.assertEqual(type(box2),p2r.obj.Box)  
        
    def testBoxMoveByVec(self):
        box1 = p2r.obj.Box.create(((0,0,0),(0,0,1),(5,0,0),(10,0,0),(20,0,0),(20,0,1),(8,0,0),(20,10,0)))
        box2 = box1.trfm.move_by_vec(((0,0,0),(1,1,1)))
        self.assertEqual(type(box2),p2r.obj.Box)  
        
    def testBoxOrient(self):
        box1 = p2r.obj.Box.create(((0,0,0),(0,0,1),(5,0,0),(10,0,0),(20,0,0),(20,0,1),(8,0,0),(20,10,0)))
        box2 = box1.trfm.orient((0,0,0),(1,1,1))
        self.assertEqual(type(box2),p2r.obj.Box)  
        
    def testBoxRemap(self):
        box1 = p2r.obj.Box.create(((0,0,0),(0,0,1),(5,0,0),(10,0,0),(20,0,0),(20,0,1),(8,0,0),(20,10,0)))
        box2 = box1.trfm.remap((0,0,0),(1,1,1))
        self.assertEqual(type(box2),p2r.obj.Box)  
        
    def testBoxRotate(self):
        box1 = p2r.obj.Box.create(((0,0,0),(0,0,1),(5,0,0),(10,0,0),(20,0,0),(20,0,1),(8,0,0),(20,10,0)))
        box2 = box1.trfm.rotate((0,0,0),45)
        self.assertEqual(type(box2),p2r.obj.Box)  
        
    def testBoxScale(self):
        box1 = p2r.obj.Box.create(((0,0,0),(0,0,1),(5,0,0),(10,0,0),(20,0,0),(20,0,1),(8,0,0),(20,10,0)))
        box2 = box1.trfm.scale((0,0,0),(1,2,3))
        self.assertEqual(type(box2),p2r.obj.Box)     
        
    def testBoxDescription(self):
        box1 = p2r.obj.Box.create(((0,0,0),(0,0,1),(5,0,0),(10,0,0),(20,0,0),(20,0,1),(8,0,0),(20,10,0)))
        box2 = box1.util.description()
        self.assertEqual(type(box2),unicode)   #TODO:double check if unicode is the correct return type
        
    def testBoxDump(self):
        box1 = p2r.obj.Box.create(((0,0,0),(0,0,1),(5,0,0),(10,0,0),(20,0,0),(20,0,1),(8,0,0),(20,10,0)))
        box2 = box1.util.dump()  
        self.assertEqual(type(box2),unicode) #TODO:double check if unicode is the correct return type
        
    def testCirclecBoxMorph(self):
        circle1 = p2r.obj.Circle.create((0,0,0), 45)
        circle2 = circle1.defm.box_morph(((0,0,0),(0,1,0),(10,0,0),(0,10,0),(0,0,10),(1,0,0),(0,5,5),(5,0,0)))
        self.assertEqual(type(circle2),p2r.obj.Circle)
        
    def testCircleShear(self):
        circle1 = p2r.obj.Circle.create((0,0,0), 45)
        circle2 = circle1.defm.shear((0,0,0),(10,10,10),45)
        self.assertEqual(type(circle2),p2r.obj.Circle)
        
    def testCircleTrfm(self):
        circle1 = p2r.obj.Circle.create((0,0,0), 45)
        circle2 = circle1.defm.trfm(((0,0,0),(0,1,0),(0,2,0),(0,3,0),(1,0,0),(1,1,1),(1,2,0),(1,3,0),(2,0,0),(2,1,0),(2,2,1),(2,3,0),(3,0,0),(3,1,0),(3,2,0),(3,3,1)))
        self.assertEqual(type(circle2),p2r.obj.Circle)

    def testCircleCopySub(self):
        circle1 = p2r.obj.Circle.create((0,0,0), 45)
        circle2 = circle1.dupl.copy_by_sub((0,0,0),(10,0,0))
        self.assertEqual(type(circle2),p2r.obj.Circle)
        
    def testCircleCopyMove(self):
        circle1 = p2r.obj.Circle.create((0,0,0), 45)
        circle2 = circle1.dupl.copy_move()
        self.assertEqual(type(circle2),p2r.obj.Circle)
        
    def testCircleCopyMoveByVec(self):
        circle1 = p2r.obj.Circle.create((0,0,0), 45)
        circle2 = circle1.dupl.copy_move_by_vec()
        self.assertEqual(type(circle2),p2r.obj.Circle)
        
    def testCircleCopyByOffset(self):
        circle1 = p2r.obj.Circle.create((0,0,0), 45)
        circle2 = circle1.dupl.copy_by_offset((0,0,0),1)
        self.assertEqual(type(circle2),p2r.obj.Circle)
        
    def testCircleCopyBySplit(self):
        circle1 = p2r.obj.Circle.create((0,0,0), 45)
        circle2 = circle1.dupl.copy_by_split((0,0,0),1)
        self.assertEqual(type(circle2[0]),p2r.obj.Arc) #TODO:double check if arc is the correct return type
        
    def testCircleCopyByTrim(self):
        circle1 = p2r.obj.Circle.create((0,0,0), 45)
        circle2 = circle1.dupl.copy_by_trim((0,1))
        self.assertEqual(type(circle2),p2r.obj.Circle)  

    def testCircleCurvature(self):
        circle1 = p2r.obj.Circle.create((0,0,0), 45)
        circle2 = circle1.eval.curvature(1)
        self.assertEqual(len(circle2),5)      
    
    def testCircleEvalDeriv(self):
        circle1 = p2r.obj.Circle.create((0,0,0), 45)
        circle2 = circle1.eval.evaluate_derivatives(1,1)
        self.assertEqual(len(circle2),2)   
    
    def testCircleFrame(self):
        circle1 = p2r.obj.Circle.create((0,0,0), 45)
        circle2 = circle1.eval.frame(1)
        self.assertEqual(len(circle2),4) 
    
    def testCirclePerpFrame(self):
        circle1 = p2r.obj.Circle.create((0,0,0), 45)
        circle2 = circle1.eval.frame(1)
        self.assertEqual(len(circle2),4) 
    
    def testCircleTangent(self):
        circle1 = p2r.obj.Circle.create((0,0,0), 45)
        circle2 = circle1.eval.tangent(1)
        self.assertEqual(len(circle2),3) 
    
    def testCircleEvaluate(self):
        circle1 = p2r.obj.Circle.create((0,0,0), 45)
        circle2 = circle1.eval.evaluate(1)
        self.assertEqual(len(circle2),3) 
    
    def testCircleArea(self):
        circle1 = p2r.obj.Circle.create((0,0,0), 45)
        circle2 = p2r.obj.Circle.create((0,0,0), 25)
        area = circle1.func.area(circle2)
        self.assertEqual(type(area),tuple) 
    
    def testCircleAreaCentroid(self):
        circle1 = p2r.obj.Circle.create((0,0,0), 45)
        circle2 = p2r.obj.Circle.create((0,0,0), 25)
        areac = circle1.func.area_centroid(circle2)
        self.assertEqual(type(areac),tuple) 
    
    def testCircleBooleanDifference(self):
        circle1 = p2r.obj.Circle.create((0,0,0), 45)
        arc1 = p2r.obj.Arc.create((0,0,0), 5, 45)
        diff = circle1.func.boolean_difference(arc1)
        self.assertEqual(type(diff),list) 
    
    def testCircleBooleanIntersection(self):
        circle1 = p2r.obj.Circle.create((0,0,0), 45)
        arc1 = p2r.obj.Arc.create((0,0,0), 5, 45)
        intersn = circle1.func.boolean_intersection(arc1)
        self.assertEqual(type(intersn),list) 
    
    def testCircleBooleanUnion(self):
        circle1 = p2r.obj.Circle.create((0,0,0), 45)
        arc1 = p2r.obj.Arc.create_by_3pt((0,0,0), (20,0,0), (10,10,0))
        arc2 = p2r.obj.Arc.create((0,0,0), 5, 45)
        union = circle1.func.boolean_union((arc1,arc2))
        self.assertEqual(type(union),bool) 
    
    def testCircleContainment(self):
        circle1 = p2r.obj.Circle.create((0,0,0), 45)
        circle2 = p2r.obj.Circle.create_by_3pt((0,0,0),(0,1,0),(1,0,0))
        cmt = circle1.func.containment(circle2)
        self.assertEqual(type(cmt),int) 
    
    def testCirclePointInside(self):
        circle1 = p2r.obj.Circle.create((0,0,0), 45)
        pnt = circle1.func.pnt_inside((0,0,0))
        self.assertEqual(type(pnt),int) 
            
    def testCircleGroups(self):
        circle1 = p2r.obj.Circle.create((0,0,0), 45)
        circle2 = circle1.grps.groups()
        self.assertEqual(type(circle2),p2r.obj.Circle)
        
    def testCircleTopGroup(self):
        circle1 = p2r.obj.Circle.create((0,0,0), 45)
        circle2 = circle1.grps.top_group()
        self.assertEqual(type(circle2),p2r.obj.Circle) 

    def testCircleInsertKnot(self):
        circle1 = p2r.obj.Circle.create((0,0,0), 45)
        circle2 = circle1.modf.insert_knot((0,1),0)
        self.assertEqual(type(circle2),bool)  

    def testCircleRebuild(self):
        circle1 = p2r.obj.Circle.create((0,0,0), 45)
        circle2 = circle1.modf.rebuild()
        self.assertEqual(type(circle2),bool)  
        
    def testCircleRemoveKnot(self):
        circle1 = p2r.obj.Circle.create((0,0,0), 45)
        circle2 = circle1.modf.remove_knot((0,1),0)
        self.assertEqual(type(circle2),bool)  

    def testCircleReverse(self):
        circle1 = p2r.obj.Circle.create((0,0,0), 45)
        circle2 = circle1.modf.reverse()
        self.assertEqual(type(circle2),bool)  

    def testCircleSeam(self):
        circle1 = p2r.obj.Circle.create((0,0,0), 45)
        circle2 = circle1.modf.seam(0,1)
        self.assertEqual(type(circle2),bool) 

    def testCircleIndex(self):
        circle1 = p2r.obj.Circle.create((0,0,0), 45)
        circle2 = circle1.mtrl.index()
        self.assertEqual(type(circle2),int) 
        
    def testCircleSource(self):
        circle1 = p2r.obj.Circle.create((0,0,0), 45)
        circle2 = circle1.mtrl.source()
        self.assertEqual(type(circle2),int)
        
    def testCircleCenterPoint(self):
        circle1 = p2r.obj.Circle.create((0,0,0), 45)
        circle2 = circle1.prop.center_pnt()
        self.assertEqual(type(circle2),tuple)
        
    def testCircleCircumference(self):
        circle1 = p2r.obj.Circle.create((0,0,0), 45)
        circle2 = circle1.prop.circumference()
        self.assertEqual(type(circle2),float)
        
    def testCircleRadius(self):
        circle1 = p2r.obj.Circle.create((0,0,0), 45)
        circle2 = circle1.prop.radius()
        self.assertEqual(type(circle2),float)
        
    
    def testCircleAddMesh(self):
        circle1 = p2r.obj.Circle.create((0,0,0), 45)
        circle2 = circle1.rndr.add_mesh()
        self.assertEqual(type(circle2),bool)   
        
    def testCircleEnable(self):
        circle1 = p2r.obj.Circle.create((0,0,0), 45)
        circle2 = circle1.rndr.enable()
        self.assertEqual(type(circle2),bool)   
        
    def testCircleHasMesh(self):
        circle1 = p2r.obj.Circle.create((0,0,0), 45)
        circle2 = circle1.rndr.has_mesh()
        self.assertEqual(type(circle2),bool)         
        
    def testCircleHide(self):
        circle1 = p2r.obj.Circle.create((0,0,0), 45)
        circle2 = circle1.stat.hide()
        self.assertEqual(type(circle2),int)  
        
    def testCircleLock(self):
        circle1 = p2r.obj.Circle.create((0,0,0), 45)
        circle2 = circle1.stat.lock()
        self.assertEqual(type(circle2),int)  
        
    def testCircleMatchObjectAttributes(self):
        circle1 = p2r.obj.Circle.create((0,0,0), 45)
        circle2 = p2r.obj.Circle.create_by_3pt((0,0,0), (20,0,0), (10,10,0))
        match = circle1.stat.match_object_attributes(circle2)
        self.assertEqual(type(match),int)  
        
    def testCircleResetObjectAttributes(self):
        circle1 = p2r.obj.Circle.create((0,0,0), 45)
        reset = circle1.stat.reset_object_attributes()
        self.assertEqual(type(reset),int)  
        
    def testCircleMoveToLayoutSpace(self):
        circle1 = p2r.obj.Circle.create((0,0,0), 45)
        reset = circle1.stat.move_to_layout_space()
        self.assertEqual(type(reset),str)  
        
    def testCircleSelect(self):
        circle1 = p2r.obj.Circle.create((0,0,0), 45)
        sel = circle1.stat.select()
        self.assertEqual(type(sel),int)  
        
    def testCircleShow(self):
        circle1 = p2r.obj.Circle.create((0,0,0), 45)
        sel = circle1.stat.show()
        self.assertEqual(type(sel),int)  
        
    def testCircleUnlock(self):
        circle1 = p2r.obj.Circle.create((0,0,0), 45)
        circle2 = circle1.stat.unlock()
        self.assertEqual(type(circle2),int) 
        
    def testCircleUnselect(self):
        circle1 = p2r.obj.Circle.create((0,0,0), 45)
        sel = circle1.stat.unselect()
        self.assertEqual(type(sel),int) 
        
    def testCircleIsClosable(self):
        circle1 = p2r.obj.Circle.create((0,0,0), 45)
        closable = circle1.test.is_closable()
        self.assertEqual(type(closable),bool) 
        
    def testCircleIsClosed(self):
        circle1 = p2r.obj.Circle.create((0,0,0), 45)
        closed = circle1.test.is_closed()
        self.assertEqual(type(closed),bool) 
        
    def testCircleInPlane(self):
        circle1 = p2r.obj.Circle.create((0,0,0), 45)
        plane = circle1.test.in_plane()
        self.assertEqual(type(plane),bool) 
        
    def testCircleIsLinear(self):
        circle1 = p2r.obj.Circle.create((0,0,0), 45)
        linear = circle1.test.is_linear()
        self.assertEqual(type(linear),bool)
        
    def testCircleIsPeriodic(self):
        circle1 = p2r.obj.Circle.create((0,0,0), 45)
        periodic = circle1.test.is_periodic()
        self.assertEqual(type(periodic),bool)
        
    def testCircleIsPlanar(self):
        circle1 = p2r.obj.Circle.create((0,0,0), 45)
        planar = circle1.test.is_planar()
        self.assertEqual(type(planar),bool)
        
    def testCircleIsRational(self):
        circle1 = p2r.obj.Circle.create((0,0,0), 45)
        rational = circle1.test.is_rational()
        self.assertEqual(type(rational),bool)   
        
    def testCircleIsPntOnCrv(self):
        circle1 = p2r.obj.Circle.create((0,0,0), 45)
        on_crv = circle1.test.is_pnt_on_crv()
        self.assertEqual(type(on_crv),bool)         
        
    def testCircleMirror(self):
        circle1 = p2r.obj.Circle.create((0,0,0), 45)
        circle2 = circle1.trfm.mirror((0,0,0),(1,1,1))
        self.assertEqual(type(circle2),p2r.obj.Circle)  
        
    def testCircleMove(self):
        circle1 = p2r.obj.Circle.create((0,0,0), 45)
        circle2 = circle1.trfm.move((0,0,0),(1,1,1))
        self.assertEqual(type(circle2),p2r.obj.Circle)  
        
    def testCircleMoveByVec(self):
        circle1 = p2r.obj.Circle.create((0,0,0), 45)
        circle2 = circle1.trfm.move_by_vec(((0,0,0),(1,1,1)))
        self.assertEqual(type(circle2),p2r.obj.Circle)  
        
    def testCircleOrient(self):
        circle1 = p2r.obj.Circle.create((0,0,0), 45)
        circle2 = circle1.trfm.orient((0,0,0),(1,1,1))
        self.assertEqual(type(circle2),p2r.obj.Circle)  
        
    def testCircleRemap(self):
        circle1 = p2r.obj.Circle.create((0,0,0), 45)
        circle2 = circle1.trfm.remap((0,0,0),(1,1,1))
        self.assertEqual(type(circle2),p2r.obj.Circle)  
        
    def testCircleRotate(self):
        circle1 = p2r.obj.Circle.create((0,0,0), 45)
        circle2 = circle1.trfm.rotate((0,0,0),45)
        self.assertEqual(type(circle2),p2r.obj.Circle)  
        
    def testCircleScale(self):
        circle1 = p2r.obj.Circle.create((0,0,0), 45)
        circle2 = circle1.trfm.scale((0,0,0),(1,2,3))
        self.assertEqual(type(circle2),p2r.obj.Circle)     
        
    def testCircleDescription(self):
        circle1 = p2r.obj.Circle.create((0,0,0), 45)
        circle2 = circle1.util.description()
        self.assertEqual(type(circle2),unicode)   #TODO:double check if unicode is the correct return type
        
    def testCircleDump(self):
        circle1 = p2r.obj.Circle.create((0,0,0), 45)
        circle2 = circle1.util.dump()
        self.assertEqual(type(circle2),unicode) #TODO:double check if unicode is the correct return type
        
    def testConeBoxMorph(self):
        cone1 = p2r.obj.Cone.create((0,0,0), (1,1,1), 5)
        cone2 = cone1.defm.box_morph(((0,0,0),(0,1,0),(10,0,0),(0,10,0),(0,0,10),(1,0,0),(0,5,5),(5,0,0)))
        self.assertEqual(type(cone2),p2r.obj.Cone)
        
    def testConeShear(self):
        cone1 = p2r.obj.Cone.create((0,0,0), (1,1,1), 5)
        cone2 = cone1.defm.shear((0,0,0),(10,10,10),45)
        self.assertEqual(type(cone2),p2r.obj.Cone)
        
    def testConeTrfm(self):
        cone1 = p2r.obj.Cone.create((0,0,0), (1,1,1), 5)
        cone2 = cone1.defm.trfm(((0,0,0),(0,1,0),(0,2,0),(0,3,0),(1,0,0),(1,1,1),(1,2,0),(1,3,0),(2,0,0),(2,1,0),(2,2,1),(2,3,0),(3,0,0),(3,1,0),(3,2,0),(3,3,1)))
        self.assertEqual(type(cone2),p2r.obj.Cone)
        
    def testConeCopyMove(self):
        cone1 = p2r.obj.Cone.create((0,0,0), (1,1,1), 5)
        cone2 = cone1.dupl.copy_move()
        self.assertEqual(type(cone2),p2r.obj.Cone)
        
    def testConeCopyMoveByVec(self):
        cone1 = p2r.obj.Cone.create((0,0,0), (1,1,1), 5)
        cone2 = cone1.dupl.copy_move_by_vec()
        self.assertEqual(type(cone2),p2r.obj.Cone)
        
    def testConeEvaluate(self):
        cone1 = p2r.obj.Cone.create((0,0,0),(1,1,1), 5)
        cone2 = cone1.eval.evaluate(1)
        self.assertEqual(len(cone2),3) 

    def testConeEvalDeriv(self):
        cone1 = p2r.obj.Cone.create((0,0,0),(1,1,1), 5)
        cone2 = cone1.eval.evaluate_derivatives(1,1)
        self.assertEqual(type(cone2),list)   

    def testConeEvalFrame(self):
        cone1 = p2r.obj.Cone.create((0,0,0),(1,1,1), 5)
        cone2 = cone1.eval.evaluate_frame((0,1))
        self.assertEqual(type(cone2),list)  
        
    def testConeGroups(self):
        cone1 = p2r.obj.Cone.create((0,0,0), (1,1,1), 5)
        cone2 = cone1.grps.groups()
        self.assertEqual(type(cone2),p2r.obj.Cone)
        
    def testConeTopGroup(self):
        cone1 = p2r.obj.Cone.create((0,0,0), (1,1,1), 5)
        cone2 = cone1.grps.top_group()
        self.assertEqual(type(cone2),p2r.obj.Cone)  

    def testConeFlip(self):
        cone1 = p2r.obj.Cone.create((0,0,0), (1,1,1), 5)
        cone2 = cone1.modf.flip()
        self.assertEqual(type(cone2),bool)  
        
    def testConeInsertKnot(self):
        cone1 = p2r.obj.Cone.create((0,0,0), (1,1,1), 5)
        cone2 = cone1.modf.insert_knot((0,1),0)
        self.assertEqual(type(cone2),bool)  

    def testConeRebuild(self):
        cone1 = p2r.obj.Cone.create((0,0,0), (1,1,1), 5)
        cone2 = cone1.modf.rebuild()
        self.assertEqual(type(cone2),bool)  
        
    def testConeRemoveKnot(self):
        cone1 = p2r.obj.Cone.create((0,0,0), (1,1,1), 5)
        cone2 = cone1.modf.remove_knot((0,1),0)
        self.assertEqual(type(cone2),bool)  

    def testConeReverse(self):
        cone1 = p2r.obj.Cone.create((0,0,0), (1,1,1), 5)
        cone2 = cone1.modf.reverse()
        self.assertEqual(type(cone2),bool)  

    def testConeShrinkTrimmed(self):
        cone1 = p2r.obj.Cone.create((0,0,0), (1,1,1), 5)
        cone2 = cone1.modf.shrink_trimmed()
        self.assertEqual(type(cone2),bool) 

    def testConeDefinition(self):
        cone1 = p2r.obj.Cone.create((0,0,0), (1,1,1), 5)
        cone2 = cone1.prop.cone_def()
        self.assertEqual(len(cone2),3) 
        
    def testConeAddMesh(self):
        cone1 = p2r.obj.Cone.create((0,0,0), (1,1,1), 5)
        cone2 = cone1.rndr.add_mesh()
        self.assertEqual(type(cone2),bool)   
        
    def testConeEnable(self):
        cone1 = p2r.obj.Cone.create((0,0,0), (1,1,1), 5)
        cone2 = cone1.rndr.enable()
        self.assertEqual(type(cone2),bool)   
        
    def testConeHasMesh(self):
        cone1 = p2r.obj.Cone.create((0,0,0), (1,1,1), 5)
        cone2 = cone1.rndr.has_mesh()
        self.assertEqual(type(cone2),bool)   
                
    def testConeHide(self):
        cone1 = p2r.obj.Cone.create((0,0,0), (1,1,1), 5)
        cone2 = cone1.stat.hide()
        self.assertEqual(type(cone2),int)  
        
    def testConeLock(self):
        cone1 = p2r.obj.Cone.create((0,0,0), (1,1,1), 5)
        cone2 = cone1.stat.lock()
        self.assertEqual(type(cone2),int)  
        
    def testConeMatchObjectAttributes(self):
        cone1 = p2r.obj.Cone.create((0,0,0), (1,1,1), 5)
        cone2 = p2r.obj.Cone.create((0,0,0), (1,1,1), 5)
        match = cone1.stat.match_object_attributes(cone2)
        self.assertEqual(type(match),int)  
        
    def testConeResetObjectAttributes(self):
        cone1 = p2r.obj.Cone.create((0,0,0), (1,1,1), 5)
        reset = cone1.stat.reset_object_attributes()
        self.assertEqual(type(reset),int)  
        
    def testConeMoveToLayoutSpace(self):
        cone1 = p2r.obj.Cone.create((0,0,0), (1,1,1), 5)
        reset = cone1.stat.move_to_layout_space()
        self.assertEqual(type(reset),str)  
        
    def testConeSelect(self):
        cone1 = p2r.obj.Cone.create((0,0,0), (1,1,1), 5)
        sel = cone1.stat.select()
        self.assertEqual(type(sel),int)  
        
    def testConeShow(self):
        cone1 = p2r.obj.Cone.create((0,0,0), (1,1,1), 5)
        sel = cone1.stat.show()
        self.assertEqual(type(sel),int)  
        
    def testConeUnlock(self):
        cone1 = p2r.obj.Cone.create((0,0,0), (1,1,1), 5)
        cone2 = cone1.stat.unlock()
        self.assertEqual(type(cone2),int) 
        
    def testConeUnselect(self):
        cone1 = p2r.obj.Cone.create((0,0,0), (1,1,1), 5)
        sel = cone1.stat.unselect()
        self.assertEqual(type(sel),int) 
        
    def testConeIsBrep(self):
        cone1 = p2r.obj.Cone.create((0,0,0), (1,1,1), 5)
        cone2 = cone1.test.is_brep()
        self.assertEqual(type(cone2),bool) 
        
    def testConeIsBrepManifold(self):
        cone1 = p2r.obj.Cone.create((0,0,0), (1,1,1), 5)
        cone2 = cone1.test.is_brep_manifold()
        self.assertEqual(type(cone2),bool) 
        
    def testConeIsParameterOnSrf(self):
        cone1 = p2r.obj.Cone.create((0,0,0), (1,1,1), 5)
        cone2 = cone1.test.is_parameter_on_srf((0,0))
        self.assertEqual(type(cone2),bool) 
        
    def testConeIsPointInSrf(self):
        cone1 = p2r.obj.Cone.create((0,0,0), (1,1,1), 5)
        cone2 = cone1.test.is_pnt_in_srf((0,0,0))
        self.assertEqual(type(cone2),bool) 
        
    def testConeIsPointOnSrf(self):
        cone1 = p2r.obj.Cone.create((0,0,0), (1,1,1), 5)
        cone2 = cone1.test.is_pnt_on_srf((0,0,0))
        self.assertEqual(type(cone2),bool) 
        
    def testConeIsPolySurfaceClosed(self):
        cone1 = p2r.obj.Cone.create((0,0,0), (1,1,1), 5)
        cone2 = cone1.test.is_poly_surface_closed()
        self.assertEqual(type(cone2),bool) 
        
    def testConeIsPlaneSurface(self):
        cone1 = p2r.obj.Cone.create((0,0,0), (1,1,1), 5)
        cone2 = cone1.test.is_plane_surface()
        self.assertEqual(type(cone2),bool) 
        
    def testConeIsPolySrf(self):
        cone1 = p2r.obj.Cone.create((0,0,0), (1,1,1), 5)
        cone2 = cone1.test.is_poly_srf()
        self.assertEqual(type(cone2),bool)     
        
    def testConeIsPolySrfPlanar(self):
        cone1 = p2r.obj.Cone.create((0,0,0), (1,1,1), 5)
        cone2 = cone1.test.is_poly_srf_planar()
        self.assertEqual(type(cone2),bool)     
        
    def testConeIsSrfClosed(self):
        cone1 = p2r.obj.Cone.create((0,0,0), (1,1,1), 5)
        cone2 = cone1.test.is_srf_closed(0)
        self.assertEqual(type(cone2),bool)   
        
    def testConeIsSrfPeriodic(self):
        cone1 = p2r.obj.Cone.create((0,0,0), (1,1,1), 5)
        cone2 = cone1.test.is_srf_periodic(0)
        self.assertEqual(type(cone2),bool) 
        
    def testConeIsSrfPlanar(self):
        cone1 = p2r.obj.Cone.create((0,0,0), (1,1,1), 5)
        cone2 = cone1.test.is_srf_planar()
        self.assertEqual(type(cone2),bool)  
        
    def testConeIsSrfRational(self):
        cone1 = p2r.obj.Cone.create((0,0,0), (1,1,1), 5)
        cone2 = cone1.test.is_srf_rational()
        self.assertEqual(type(cone2),bool)  
        
    def testConeIsSrfSingular(self):
        cone1 = p2r.obj.Cone.create((0,0,0), (1,1,1), 5)
        cone2 = cone1.test.is_srf_singular(0)
        self.assertEqual(type(cone2),bool)  
        
    def testConeIsSrfTrimmed(self):
        cone1 = p2r.obj.Cone.create((0,0,0), (1,1,1), 5)
        cone2 = cone1.test.is_srf_trimmed()
        self.assertEqual(type(cone2),bool)

    def testConeMirror(self):
        cone1 = p2r.obj.Cone.create((0,0,0), (1,1,1), 5)
        cone2 = cone1.trfm.mirror((0,0,0),(1,1,1))
        self.assertEqual(type(cone2),p2r.obj.Cone)  
        
    def testConeMove(self):
        cone1 = p2r.obj.Cone.create((0,0,0), (1,1,1), 5)
        cone2 = cone1.trfm.move((0,0,0),(1,1,1))
        self.assertEqual(type(cone2),p2r.obj.Cone)  
        
    def testConeMoveByVec(self):
        cone1 = p2r.obj.Cone.create((0,0,0), (1,1,1), 5)
        cone2 = cone1.trfm.move_by_vec(((0,0,0),(1,1,1)))
        self.assertEqual(type(cone2),p2r.obj.Cone)  
        
    def testConeOrient(self):
        cone1 = p2r.obj.Cone.create((0,0,0), (1,1,1), 5)
        cone2 = cone1.trfm.orient((0,0,0),(1,1,1))
        self.assertEqual(type(cone2),p2r.obj.Cone)  
        
    def testConeRemap(self):
        cone1 = p2r.obj.Cone.create((0,0,0), (1,1,1), 5)
        cone2 = cone1.trfm.remap((0,0,0),(1,1,1))
        self.assertEqual(type(cone2),p2r.obj.Cone)  
        
    def testConeRotate(self):
        cone1 = p2r.obj.Cone.create((0,0,0), (1,1,1), 5)
        cone2 = cone1.trfm.rotate((0,0,0),45)
        self.assertEqual(type(cone2),p2r.obj.Cone)  
        
    def testConeScale(self):
        cone1 = p2r.obj.Cone.create((0,0,0), (1,1,1), 5)
        cone2 = cone1.trfm.scale((0,0,0),(1,2,3))
        self.assertEqual(type(cone2),p2r.obj.Cone)     
        
    def testConeDescription(self):
        cone1 = p2r.obj.Cone.create((0,0,0), (1,1,1), 5)
        cone2 = cone1.util.description()
        self.assertEqual(type(cone2),unicode)   #TODO:double check if unicode is the correct return type
        
    def testConeDump(self):
        cone1 = p2r.obj.Cone.create((0,0,0), (1,1,1), 5)
        cone2 = cone1.util.dump()  
        self.assertEqual(type(cone2),unicode) #TODO:double check if unicode is the correct return type
        
    def testCylinderBoxMorph(self):
        cylinder1 = p2r.obj.Cylinder.create((0,0,0),(1,1,1), 5)
        cylinder2 = cylinder1.defm.box_morph(((0,0,0),(0,1,0),(10,0,0),(0,10,0),(0,0,10),(1,0,0),(0,5,5),(5,0,0)))
        self.assertEqual(type(cylinder2),p2r.obj.Cylinder)
        
    def testCylinderShear(self):
        cylinder1 = p2r.obj.Cylinder.create((0,0,0),(1,1,1), 5)
        cylinder2 = cylinder1.defm.shear((0,0,0),(10,10,10),45)
        self.assertEqual(type(cylinder2),p2r.obj.Cylinder)
        
    def testCylinderTrfm(self):
        cylinder1 = p2r.obj.Cylinder.create((0,0,0),(1,1,1), 5)
        cylinder2 = cylinder1.defm.trfm(((0,0,0),(0,1,0),(0,2,0),(0,3,0),(1,0,0),(1,1,1),(1,2,0),(1,3,0),(2,0,0),(2,1,0),(2,2,1),(2,3,0),(3,0,0),(3,1,0),(3,2,0),(3,3,1)))
        self.assertEqual(type(cylinder2),p2r.obj.Cylinder)    
        
    def testCylinderCopyMove(self):
        cylinder1 = p2r.obj.Cylinder.create((0,0,0),(1,1,1), 5)
        cylinder2 = cylinder1.dupl.copy_move()
        self.assertEqual(type(cylinder2),p2r.obj.Cylinder)
        
    def testCylinderCopyMoveByVec(self):
        cylinder1 = p2r.obj.Cylinder.create((0,0,0),(1,1,1), 5)
        cylinder2 = cylinder1.dupl.copy_move_by_vec()
        self.assertEqual(type(cylinder2),p2r.obj.Cylinder)
        
    def testCylinderEvaluate(self):
        cylinder1 = p2r.obj.Cylinder.create((0,0,0),(1,1,1), 5)
        cylinder2 = cylinder1.eval.evaluate(1)
        self.assertEqual(len(cylinder2),3) 

    def testCylinderEvalDeriv(self):
        cylinder1 = p2r.obj.Cylinder.create((0,0,0),(1,1,1), 5)
        cylinder2 = cylinder1.eval.evaluate_derivatives(1,1)
        self.assertEqual(type(cylinder2),list)   

    def testCylinderEvalFrame(self):
        cylinder1 = p2r.obj.Cylinder.create((0,0,0),(1,1,1), 5)
        cylinder2 = cylinder1.eval.evaluate_frame((0,1))
        self.assertEqual(type(cylinder2),list)      
        
    def testCylinderGroups(self):
        cylinder1 = p2r.obj.Cylinder.create((0,0,0),(1,1,1), 5)
        cylinder2 = cylinder1.grps.groups()
        self.assertEqual(type(cylinder2),p2r.obj.Cylinder)
        
    def testCylinderTopGroup(self):
        cylinder1 = p2r.obj.Cylinder.create((0,0,0),(1,1,1), 5)
        cylinder2 = cylinder1.grps.top_group()
        self.assertEqual(type(cylinder2),p2r.obj.Cylinder)  

    def testCylinderFlip(self):
        cylinder1 = p2r.obj.Cylinder.create((0,0,0),(1,1,1), 5)
        cylinder2 = cylinder1.modf.flip()
        self.assertEqual(type(cylinder2),bool)  
        
    def testCylinderInsertKnot(self):
        cylinder1 = p2r.obj.Cylinder.create((0,0,0),(1,1,1), 5)
        cylinder2 = cylinder1.modf.insert_knot((0,1),0)
        self.assertEqual(type(cylinder2),bool)  

    def testCylinderRebuild(self):
        cylinder1 = p2r.obj.Cylinder.create((0,0,0),(1,1,1), 5)
        cylinder2 = cylinder1.modf.rebuild()
        self.assertEqual(type(cylinder2),bool)  
        
    def testCylinderRemoveKnot(self):
        cylinder1 = p2r.obj.Cylinder.create((0,0,0),(1,1,1), 5)
        cylinder2 = cylinder1.modf.remove_knot((0,1),0)
        self.assertEqual(type(cylinder2),bool)  

    def testCylinderReverse(self):
        cylinder1 = p2r.obj.Cylinder.create((0,0,0),(1,1,1), 5)
        cylinder2 = cylinder1.modf.reverse()
        self.assertEqual(type(cylinder2),bool)  

    def testCylinderShrinkTrimmed(self):
        cylinder1 = p2r.obj.Cylinder.create((0,0,0),(1,1,1), 5)
        cylinder2 = cylinder1.modf.shrink_trimmed()
        self.assertEqual(type(cylinder2),bool) 

    def testCylinderDefinition(self):
        cylinder1 = p2r.obj.Cylinder.create((0,0,0),(1,1,1), 5)
        cylinder2 = cylinder1.prop.cylinder_def()
        self.assertEqual(len(cylinder2),3) 
        
    def testCylinderAddMesh(self):
        cylinder1 = p2r.obj.Cylinder.create((0,0,0),(1,1,1), 5)
        cylinder2 = cylinder1.rndr.add_mesh()
        self.assertEqual(type(cylinder2),bool) 
        
    def testCylinderEnable(self):
        cylinder1 = p2r.obj.Cylinder.create((0,0,0),(1,1,1), 5)
        cylinder2 = cylinder1.rndr.enable()
        self.assertEqual(type(cylinder2),bool)   
        
    def testCylinderHasMesh(self):
        cylinder1 = p2r.obj.Cylinder.create((0,0,0),(1,1,1), 5)
        cylinder2 = cylinder1.rndr.has_mesh()
        self.assertEqual(type(cylinder2),bool)    
    def testCylinderHide(self):
        cylinder1 = p2r.obj.Cylinder.create((0,0,0),(1,1,1), 5)
        cylinder2 = cylinder1.stat.hide()
        self.assertEqual(type(cylinder2),int)  
        
    def testCylinderLock(self):
        cylinder1 = p2r.obj.Cylinder.create((0,0,0),(1,1,1), 5)
        cylinder2 = cylinder1.stat.lock()
        self.assertEqual(type(cylinder2),int)  
        
    def testCylinderMatchObjectAttributes(self):
        cylinder1 = p2r.obj.Cylinder.create((0,0,0),(1,1,1), 5)
        cylinder2 = p2r.obj.Cylinder.create((0,0,0), (1,1,1), 5)
        match = cylinder1.stat.match_object_attributes(cylinder2)
        self.assertEqual(type(match),int)  
        
    def testCylinderResetObjectAttributes(self):
        cylinder1 = p2r.obj.Cylinder.create((0,0,0),(1,1,1), 5)
        reset = cylinder1.stat.reset_object_attributes()
        self.assertEqual(type(reset),int)  
        
    def testCylinderMoveToLayoutSpace(self):
        cylinder1 = p2r.obj.Cylinder.create((0,0,0),(1,1,1), 5)
        reset = cylinder1.stat.move_to_layout_space()
        self.assertEqual(type(reset),str)  
        
    def testCylinderSelect(self):
        cylinder1 = p2r.obj.Cylinder.create((0,0,0),(1,1,1), 5)
        sel = cylinder1.stat.select()
        self.assertEqual(type(sel),int)  
        
    def testCylinderShow(self):
        cylinder1 = p2r.obj.Cylinder.create((0,0,0),(1,1,1), 5)
        sel = cylinder1.stat.show()
        self.assertEqual(type(sel),int)  
        
    def testCylinderUnlock(self):
        cylinder1 = p2r.obj.Cylinder.create((0,0,0),(1,1,1), 5)
        cylinder2 = cylinder1.stat.unlock()
        self.assertEqual(type(cylinder2),int) 
        
    def testCylinderUnselect(self):
        cylinder1 = p2r.obj.Cylinder.create((0,0,0),(1,1,1), 5)
        sel = cylinder1.stat.unselect()
        self.assertEqual(type(sel),int) 
        
    def testCylinderIsBrep(self):
        cylinder1 = p2r.obj.Cylinder.create((0,0,0),(1,1,1), 5)
        cylinder2 = cylinder1.test.is_brep()
        self.assertEqual(type(cylinder2),bool) 
        
    def testCylinderIsBrepManifold(self):
        cylinder1 = p2r.obj.Cylinder.create((0,0,0),(1,1,1), 5)
        cylinder2 = cylinder1.test.is_brep_manifold()
        self.assertEqual(type(cylinder2),bool) 
        
    def testCylinderIsParameterOnSrf(self):
        cylinder1 = p2r.obj.Cylinder.create((0,0,0),(1,1,1), 5)
        cylinder2 = cylinder1.test.is_parameter_on_srf((0,0))
        self.assertEqual(type(cylinder2),bool) 
        
    def testCylinderIsPointInSrf(self):
        cylinder1 = p2r.obj.Cylinder.create((0,0,0),(1,1,1), 5)
        cylinder2 = cylinder1.test.is_pnt_in_srf((0,0,0))
        self.assertEqual(type(cylinder2),bool) 
        
    def testCylinderIsPointOnSrf(self):
        cylinder1 = p2r.obj.Cylinder.create((0,0,0),(1,1,1), 5)
        cylinder2 = cylinder1.test.is_pnt_on_srf((0,0,0))
        self.assertEqual(type(cylinder2),bool) 
        
    def testCylinderIsPolySurfaceClosed(self):
        cylinder1 = p2r.obj.Cylinder.create((0,0,0),(1,1,1), 5)
        cylinder2 = cylinder1.test.is_poly_surface_closed()
        self.assertEqual(type(cylinder2),bool) 
        
    def testCylinderIsPlaneSurface(self):
        cylinder1 = p2r.obj.Cylinder.create((0,0,0),(1,1,1), 5)
        cylinder2 = cylinder1.test.is_plane_surface()
        self.assertEqual(type(cylinder2),bool) 
        
    def testCylinderIsPolySrf(self):
        cylinder1 = p2r.obj.Cylinder.create((0,0,0),(1,1,1), 5)
        cylinder2 = cylinder1.test.is_poly_srf()
        self.assertEqual(type(cylinder2),bool)     
        
    def testCylinderIsPolySrfPlanar(self):
        cylinder1 = p2r.obj.Cylinder.create((0,0,0),(1,1,1), 5)
        cylinder2 = cylinder1.test.is_poly_srf_planar()
        self.assertEqual(type(cylinder2),bool)     
        
    def testCylinderIsSrfClosed(self):
        cylinder1 = p2r.obj.Cylinder.create((0,0,0),(1,1,1), 5)
        cylinder2 = cylinder1.test.is_srf_closed(0)
        self.assertEqual(type(cylinder2),bool)   
        
    def testCylinderIsSrfPeriodic(self):
        cylinder1 = p2r.obj.Cylinder.create((0,0,0),(1,1,1), 5)
        cylinder2 = cylinder1.test.is_srf_periodic(0)
        self.assertEqual(type(cylinder2),bool) 
        
    def testCylinderIsSrfPlanar(self):
        cylinder1 = p2r.obj.Cylinder.create((0,0,0),(1,1,1), 5)
        cylinder2 = cylinder1.test.is_srf_planar()
        self.assertEqual(type(cylinder2),bool)  
        
    def testCylinderIsSrfRational(self):
        cylinder1 = p2r.obj.Cylinder.create((0,0,0),(1,1,1), 5)
        cylinder2 = cylinder1.test.is_srf_rational()
        self.assertEqual(type(cylinder2),bool)  
        
    def testCylinderIsSrfSingular(self):
        cylinder1 = p2r.obj.Cylinder.create((0,0,0),(1,1,1), 5)
        cylinder2 = cylinder1.test.is_srf_singular(0)
        self.assertEqual(type(cylinder2),bool)  
        
    def testCylinderIsSrfTrimmed(self):
        cylinder1 = p2r.obj.Cylinder.create((0,0,0),(1,1,1), 5)
        cylinder2 = cylinder1.test.is_srf_trimmed()
        self.assertEqual(type(cylinder2),bool)

    def testCylinderMirror(self):
        cylinder1 = p2r.obj.Cylinder.create((0,0,0),(1,1,1), 5)
        cylinder2 = cylinder1.trfm.mirror((0,0,0),(1,1,1))
        self.assertEqual(type(cylinder2),p2r.obj.Cylinder)  
        
    def testCylinderMove(self):
        cylinder1 = p2r.obj.Cylinder.create((0,0,0),(1,1,1), 5)
        cylinder2 = cylinder1.trfm.move((0,0,0),(1,1,1))
        self.assertEqual(type(cylinder2),p2r.obj.Cylinder)  
        
    def testCylinderMoveByVec(self):
        cylinder1 = p2r.obj.Cylinder.create((0,0,0),(1,1,1), 5)
        cylinder2 = cylinder1.trfm.move_by_vec(((0,0,0),(1,1,1)))
        self.assertEqual(type(cylinder2),p2r.obj.Cylinder)  
        
    def testCylinderOrient(self):
        cylinder1 = p2r.obj.Cylinder.create((0,0,0),(1,1,1), 5)
        cylinder2 = cylinder1.trfm.orient((0,0,0),(1,1,1))
        self.assertEqual(type(cylinder2),p2r.obj.Cylinder)  
        
    def testCylinderRemap(self):
        cylinder1 = p2r.obj.Cylinder.create((0,0,0),(1,1,1), 5)
        cylinder2 = cylinder1.trfm.remap((0,0,0),(1,1,1))
        self.assertEqual(type(cylinder2),p2r.obj.Cylinder)  
        
    def testCylinderRotate(self):
        cylinder1 = p2r.obj.Cylinder.create((0,0,0),(1,1,1), 5)
        cylinder2 = cylinder1.trfm.rotate((0,0,0),45)
        self.assertEqual(type(cylinder2),p2r.obj.Cylinder)  
        
    def testCylinderScale(self):
        cylinder1 = p2r.obj.Cylinder.create((0,0,0),(1,1,1), 5)
        cylinder2 = cylinder1.trfm.scale((0,0,0),(1,2,3))
        self.assertEqual(type(cylinder2),p2r.obj.Cylinder)     
        
    def testCylinderDescription(self):
        cylinder1 = p2r.obj.Cylinder.create((0,0,0),(1,1,1), 5)
        cylinder2 = cylinder1.util.description()
        self.assertEqual(type(cylinder2),unicode)   #TODO:double check if unicode is the correct return type
        
    def testCylinderDump(self):
        cylinder1 = p2r.obj.Cylinder.create((0,0,0),(1,1,1), 5)
        cylinder2 = cylinder1.util.dump()  
        self.assertEqual(type(cylinder2),unicode) #TODO:double check if unicode is the correct return type
             
    def testEllipseBoxMorph(self):
        ellipse1 = p2r.obj.Ellipse.create(((0,0,0),(0,1,0),(1,0,0)), 5, 10)
        ellipse2 = ellipse1.defm.box_morph(((0,0,0),(0,1,0),(10,0,0),(0,10,0),(0,0,10),(1,0,0),(0,5,5),(5,0,0)))
        self.assertEqual(type(ellipse2),p2r.obj.Ellipse)
        
    def testEllipseShear(self):
        ellipse1 = p2r.obj.Ellipse.create(((0,0,0),(0,1,0),(1,0,0)), 5, 10)
        ellipse2 = ellipse1.defm.shear((0,0,0),(10,10,10),45)
        self.assertEqual(type(ellipse2),p2r.obj.Ellipse)
        
    def testEllipseTrfm(self):
        ellipse1 = p2r.obj.Ellipse.create(((0,0,0),(0,1,0),(1,0,0)), 5, 10)
        ellipse2 = ellipse1.defm.trfm(((0,0,0),(0,1,0),(0,2,0),(0,3,0),(1,0,0),(1,1,1),(1,2,0),(1,3,0),(2,0,0),(2,1,0),(2,2,1),(2,3,0),(3,0,0),(3,1,0),(3,2,0),(3,3,1)))
        self.assertEqual(type(ellipse2),p2r.obj.Ellipse)   
        
    def testEllipseCopySub(self):
        ellipse1 = p2r.obj.Ellipse.create(((0,0,0),(0,1,0),(1,0,0)), 5, 10)
        ellipse2 = ellipse1.dupl.copy_by_sub((0,0,0),(10,0,0))
        self.assertEqual(type(ellipse2),p2r.obj.Ellipse)
        
    def testEllipseCopyMove(self):
        ellipse1 = p2r.obj.Ellipse.create(((0,0,0),(0,1,0),(1,0,0)), 5, 10)
        ellipse2 = ellipse1.dupl.copy_move()
        self.assertEqual(type(ellipse2),p2r.obj.Ellipse)
        
    def testEllipseCopyMoveByVec(self):
        ellipse1 = p2r.obj.Ellipse.create(((0,0,0),(0,1,0),(1,0,0)), 5, 10)
        ellipse2 = ellipse1.dupl.copy_move_by_vec()
        self.assertEqual(type(ellipse2),p2r.obj.Ellipse)
        
    def testEllipseCopyByOffset(self):
        ellipse1 = p2r.obj.Ellipse.create(((0,0,0),(0,1,0),(1,0,0)), 5, 10)
        ellipse2 = ellipse1.dupl.copy_by_offset((0,0,0),1)
        self.assertEqual(type(ellipse2),p2r.obj.Ellipse)
        
    def testEllipseCopyBySplit(self):
        ellipse1 = p2r.obj.Ellipse.create(((0,0,0),(0,1,0),(1,0,0)), 5, 10)
        ellipse2 = ellipse1.dupl.copy_by_split((0,0,0),1)
        self.assertEqual(type(ellipse2[0]),p2r.obj.EllipticalArc) 
        
    def testEllipseCopyByTrim(self):
        ellipse1 = p2r.obj.Ellipse.create(((0,0,0),(0,1,0),(1,0,0)), 5, 10)
        ellipse2 = ellipse1.dupl.copy_by_trim((0,1))
        self.assertEqual(type(ellipse2),p2r.obj.EllipticalArc)  
        
    def testEllipseCurvature(self):
        ellipse1 = p2r.obj.Ellipse.create(((0,0,0),(0,1,0),(1,0,0)), 5, 10)
        ellipse2 = ellipse1.eval.curvature(1)
        self.assertEqual(len(ellipse2),5)      
    
    def testEllipseEvalDeriv(self):
        ellipse1 = p2r.obj.Ellipse.create(((0,0,0),(0,1,0),(1,0,0)), 5, 10)
        ellipse2 = ellipse1.eval.evaluate_derivatives(1,1)
        self.assertEqual(len(ellipse2),2)   
    
    def testEllipseFrame(self):
        ellipse1 = p2r.obj.Ellipse.create(((0,0,0),(0,1,0),(1,0,0)), 5, 10)
        ellipse2 = ellipse1.eval.frame(1)
        self.assertEqual(len(ellipse2),4) 
    
    def testEllipsePerpFrame(self):
        ellipse1 = p2r.obj.Ellipse.create(((0,0,0),(0,1,0),(1,0,0)), 5, 10)
        ellipse2 = ellipse1.eval.frame(1)
        self.assertEqual(len(ellipse2),4) 
    
    def testEllipseTangent(self):
        ellipse1 = p2r.obj.Ellipse.create(((0,0,0),(0,1,0),(1,0,0)), 5, 10)
        ellipse2 = ellipse1.eval.tangent(1)
        self.assertEqual(len(ellipse2),3) 
    
    def testEllipseEvaluate(self):
        ellipse1 = p2r.obj.Ellipse.create(((0,0,0),(0,1,0),(1,0,0)), 5, 10)
        ellipse2 = ellipse1.eval.evaluate(1)
        self.assertEqual(len(ellipse2),3) 

    def testEllipseArea(self):
        ellipse1 = p2r.obj.Ellipse.create(((0,0,0),(0,1,0),(1,0,0)), 5, 10)
        circle1 = p2r.obj.Circle.create((0,0,0), 25)
        area = ellipse1.func.area(ellipse2)
        self.assertEqual(type(area),tuple) 
    
    def testEllipseAreaCentroid(self):
        ellipse1 = p2r.obj.Ellipse.create(((0,0,0),(0,1,0),(1,0,0)), 5, 10)
        circle1 = p2r.obj.Circle.create((0,0,0), 25)
        areac = ellipse1.func.area_centroid(circle1)
        self.assertEqual(type(areac),tuple) 
    
    def testEllipseBooleanDifference(self):
        ellipse1 = p2r.obj.Ellipse.create(((0,0,0),(0,1,0),(1,0,0)), 5, 10)
        circle1 = p2r.obj.Circle.create((0,0,0), 25)
        diff = ellipse1.func.boolean_difference(circle1)
        self.assertEqual(type(diff),list) 
    
    def testEllipseBooleanIntersection(self):
        ellipse1 = p2r.obj.Ellipse.create(((0,0,0),(0,1,0),(1,0,0)), 5, 10)
        circle1 = p2r.obj.Circle.create((0,0,0), 25)
        intersn = ellipse1.func.boolean_intersection(circle1)
        self.assertEqual(type(intersn),list) 
    
    def testEllipseBooleanUnion(self):
        ellipse1 = p2r.obj.Ellipse.create(((0,0,0),(0,1,0),(1,0,0)), 5, 10)
        ellipse2 = p2r.obj.Ellipse.create(((0,0,0),(0,1,0),(1,0,0)), 5, 10)
        circle1 = p2r.obj.Circle.create((0,0,0), 25)
        union = circle1.func.boolean_union((ellipse1,ellipse2))
        self.assertEqual(type(union),bool) 
    
    def testEllipseContainment(self):
        ellipse1 = p2r.obj.Ellipse.create(((0,0,0),(0,1,0),(1,0,0)), 5, 10)
        ellipse2 = p2r.obj.Ellipse.create_by_3pt((0,0,0),(0,1,0),(1,0,0))
        cmt = ellipse1.func.containment(ellipse2)
        self.assertEqual(type(cmt),int) 
    
    def testEllipsePointInside(self):
        ellipse1 = p2r.obj.Ellipse.create(((0,0,0),(0,1,0),(1,0,0)), 5, 10)
        pnt = ellipse1.func.pnt_inside((0,0,0))
        self.assertEqual(type(pnt),int) 

    def testEllipseGroups(self):
        ellipse1 = p2r.obj.Ellipse.create(((0,0,0),(0,1,0),(1,0,0)), 5, 10)
        ellipse2 = ellipse1.grps.groups()
        self.assertEqual(type(ellipse2),p2r.obj.Ellipse)
        
    def testEllipseTopGroup(self):
        ellipse1 = p2r.obj.Ellipse.create(((0,0,0),(0,1,0),(1,0,0)), 5, 10)
        ellipse2 = ellipse1.grps.top_group()
        self.assertEqual(type(ellipse2),p2r.obj.Ellipse)         
        
    def testEllipseInsertKnot(self):
        ellipse1 = p2r.obj.Ellipse.create(((0,0,0),(0,1,0),(1,0,0)), 5, 10)
        ellipse2 = ellipse1.modf.insert_knot((0,1),0)
        self.assertEqual(type(ellipse2),bool)  

    def testEllipseRebuild(self):
        ellipse1 = p2r.obj.Ellipse.create(((0,0,0),(0,1,0),(1,0,0)), 5, 10)
        ellipse2 = ellipse1.modf.rebuild()
        self.assertEqual(type(ellipse2),bool)  
        
    def testEllipseRemoveKnot(self):
        ellipse1 = p2r.obj.Ellipse.create(((0,0,0),(0,1,0),(1,0,0)), 5, 10)
        ellipse2 = ellipse1.modf.remove_knot((0,1),0)
        self.assertEqual(type(ellipse2),bool)  

    def testEllipseReverse(self):
        ellipse1 = p2r.obj.Ellipse.create(((0,0,0),(0,1,0),(1,0,0)), 5, 10)
        ellipse2 = ellipse1.modf.reverse()
        self.assertEqual(type(ellipse2),bool)  

    def testEllipseSeam(self):
        ellipse1 = p2r.obj.Ellipse.create(((0,0,0),(0,1,0),(1,0,0)), 5, 10)
        ellipse2 = ellipse1.modf.seam(0,1)
        self.assertEqual(type(ellipse2),bool) 

    def testEllipseIndex(self):
        ellipse1 = p2r.obj.Ellipse.create(((0,0,0),(0,1,0),(1,0,0)), 5, 10)
        ellipse2 = ellipse1.mtrl.index()
        self.assertEqual(type(ellipse2),int) 
        
    def testEllipseSource(self):
        ellipse1 = p2r.obj.Ellipse.create(((0,0,0),(0,1,0),(1,0,0)), 5, 10)
        ellipse2 = ellipse1.mtrl.source()
        self.assertEqual(type(ellipse2),int)

    def testEllipseCenterPoint(self):
        ellipse1 = p2r.obj.Ellipse.create(((0,0,0),(0,1,0),(1,0,0)), 5, 10)
        ellipse2 = ellipse1.prop.center_pnt()
        self.assertEqual(type(ellipse2),p2r.obj.Ellipse)

    def testEllipseQuadPoints(self):
        ellipse1 = p2r.obj.Ellipse.create(((0,0,0),(0,1,0),(1,0,0)), 5, 10)
        ellipse2 = ellipse1.prop.quad_pnts()
        self.assertEqual(type(ellipse2),p2r.obj.Ellipse)
        
    def testEllipseAddMesh(self):
        ellipse1 = p2r.obj.Ellipse.create(((0,0,0),(0,1,0),(1,0,0)), 5, 10)
        ellipse2 = ellipse1.rndr.add_mesh()
        self.assertEqual(type(ellipse2),bool)   
        
    def testEllipseEnable(self):
        ellipse1 = p2r.obj.Ellipse.create(((0,0,0),(0,1,0),(1,0,0)), 5, 10)
        ellipse2 = ellipse1.rndr.enable()
        self.assertEqual(type(ellipse2),bool)   
        
    def testEllipseHasMesh(self):
        ellipse1 = p2r.obj.Ellipse.create(((0,0,0),(0,1,0),(1,0,0)), 5, 10)
        ellipse2 = ellipse1.rndr.has_mesh()
        self.assertEqual(type(ellipse2),bool)   
            
    def testEllipseHide(self):
        ellipse1 = p2r.obj.Ellipse.create(((0,0,0),(0,1,0),(1,0,0)), 5, 10)
        ellipse2 = ellipse1.stat.hide()
        self.assertEqual(type(ellipse2),int)  
        
    def testEllipseLock(self):
        ellipse1 = p2r.obj.Ellipse.create(((0,0,0),(0,1,0),(1,0,0)), 5, 10)
        ellipse2 = ellipse1.stat.lock()
        self.assertEqual(type(ellipse2),int)  
        
    def testEllipseMatchObjectAttributes(self):
        ellipse1 = p2r.obj.Ellipse.create(((0,0,0),(0,1,0),(1,0,0)), 5, 10)
        ellipse2 = p2r.obj.Ellipse.create_by_3pt((0,0,0), (20,0,0), (10,10,0))
        match = ellipse1.stat.match_object_attributes(ellipse2)
        self.assertEqual(type(match),int)  
        
    def testEllipseResetObjectAttributes(self):
        ellipse1 = p2r.obj.Ellipse.create(((0,0,0),(0,1,0),(1,0,0)), 5, 10)
        reset = ellipse1.stat.reset_object_attributes()
        self.assertEqual(type(reset),int)  
        
    def testEllipseMoveToLayoutSpace(self):
        ellipse1 = p2r.obj.Ellipse.create(((0,0,0),(0,1,0),(1,0,0)), 5, 10)
        reset = ellipse1.stat.move_to_layout_space()
        self.assertEqual(type(reset),str)  
        
    def testEllipseSelect(self):
        ellipse1 = p2r.obj.Ellipse.create(((0,0,0),(0,1,0),(1,0,0)), 5, 10)
        sel = ellipse1.stat.select()
        self.assertEqual(type(sel),int)  
        
    def testEllipseShow(self):
        ellipse1 = p2r.obj.Ellipse.create(((0,0,0),(0,1,0),(1,0,0)), 5, 10)
        sel = ellipse1.stat.show()
        self.assertEqual(type(sel),int)  
        
    def testEllipseUnlock(self):
        ellipse1 = p2r.obj.Ellipse.create(((0,0,0),(0,1,0),(1,0,0)), 5, 10)
        ellipse2 = ellipse1.stat.unlock()
        self.assertEqual(type(ellipse2),int) 
        
    def testEllipseUnselect(self):
        ellipse1 = p2r.obj.Ellipse.create(((0,0,0),(0,1,0),(1,0,0)), 5, 10)
        sel = ellipse1.stat.unselect()
        self.assertEqual(type(sel),int) 
        
    def testEllipseIsClosable(self):
        ellipse1 = p2r.obj.Ellipse.create(((0,0,0),(0,1,0),(1,0,0)), 5, 10)
        closable = ellipse1.test.is_closable()
        self.assertEqual(type(closable),bool) 
        
    def testEllipseIsClosed(self):
        ellipse1 = p2r.obj.Ellipse.create(((0,0,0),(0,1,0),(1,0,0)), 5, 10)
        closed = ellipse1.test.is_closed()
        self.assertEqual(type(closed),bool) 
        
    def testEllipseInPlane(self):
        ellipse1 = p2r.obj.Ellipse.create(((0,0,0),(0,1,0),(1,0,0)), 5, 10)
        plane = ellipse1.test.in_plane()
        self.assertEqual(type(plane),bool) 
        
    def testEllipseIsLinear(self):
        ellipse1 = p2r.obj.Ellipse.create(((0,0,0),(0,1,0),(1,0,0)), 5, 10)
        linear = ellipse1.test.is_linear()
        self.assertEqual(type(linear),bool)
        
    def testEllipseIsPeriodic(self):
        ellipse1 = p2r.obj.Ellipse.create(((0,0,0),(0,1,0),(1,0,0)), 5, 10)
        periodic = ellipse1.test.is_periodic()
        self.assertEqual(type(periodic),bool)
        
    def testEllipseIsPlanar(self):
        ellipse1 = p2r.obj.Ellipse.create(((0,0,0),(0,1,0),(1,0,0)), 5, 10)
        planar = ellipse1.test.is_planar()
        self.assertEqual(type(planar),bool)
        
    def testEllipseIsRational(self):
        ellipse1 = p2r.obj.Ellipse.create(((0,0,0),(0,1,0),(1,0,0)), 5, 10)
        rational = ellipse1.test.is_rational()
        self.assertEqual(type(rational),bool)   
        
    def testEllipseIsPntOnCrv(self):
        ellipse1 = p2r.obj.Ellipse.create(((0,0,0),(0,1,0),(1,0,0)), 5, 10)
        on_crv = ellipse1.test.is_pnt_on_crv((0,0,0))
        self.assertEqual(type(on_crv),bool)         
        
    def testEllipseMirror(self):
        ellipse1 = p2r.obj.Ellipse.create(((0,0,0),(0,1,0),(1,0,0)), 5, 10)
        ellipse2 = ellipse1.trfm.mirror((0,0,0),(1,1,1))
        self.assertEqual(type(ellipse2),p2r.obj.Ellipse)  
        
    def testEllipseMove(self):
        ellipse1 = p2r.obj.Ellipse.create(((0,0,0),(0,1,0),(1,0,0)), 5, 10)
        ellipse2 = ellipse1.trfm.move((0,0,0),(1,1,1))
        self.assertEqual(type(ellipse2),p2r.obj.Ellipse)  
        
    def testEllipseMoveByVec(self):
        ellipse1 = p2r.obj.Ellipse.create(((0,0,0),(0,1,0),(1,0,0)), 5, 10)
        ellipse2 = ellipse1.trfm.move_by_vec(((0,0,0),(1,1,1)))
        self.assertEqual(type(ellipse2),p2r.obj.Ellipse)  
        
    def testEllipseOrient(self):
        ellipse1 = p2r.obj.Ellipse.create(((0,0,0),(0,1,0),(1,0,0)), 5, 10)
        ellipse2 = ellipse1.trfm.orient((0,0,0),(1,1,1))
        self.assertEqual(type(ellipse2),p2r.obj.Ellipse)  
        
    def testEllipseRemap(self):
        ellipse1 = p2r.obj.Ellipse.create(((0,0,0),(0,1,0),(1,0,0)), 5, 10)
        ellipse2 = ellipse1.trfm.remap((0,0,0),(1,1,1))
        self.assertEqual(type(ellipse2),p2r.obj.Ellipse)  
        
    def testEllipseRotate(self):
        ellipse1 = p2r.obj.Ellipse.create(((0,0,0),(0,1,0),(1,0,0)), 5, 10)
        ellipse2 = ellipse1.trfm.rotate((0,0,0),45)
        self.assertEqual(type(ellipse2),p2r.obj.Ellipse)  
        
    def testEllipseScale(self):
        ellipse1 = p2r.obj.Ellipse.create(((0,0,0),(0,1,0),(1,0,0)), 5, 10)
        ellipse2 = ellipse1.trfm.scale((0,0,0),(1,2,3))
        self.assertEqual(type(ellipse2),p2r.obj.Ellipse)     
        
    def testEllipseDescription(self):
        ellipse1 = p2r.obj.Ellipse.create(((0,0,0),(0,1,0),(1,0,0)), 5, 10)
        ellipse2 = ellipse1.util.description()
        self.assertEqual(type(ellipse2),unicode)   
        
    def testEllipseDump(self):
        ellipse1 = p2r.obj.Ellipse.create(((0,0,0),(0,1,0),(1,0,0)), 5, 10)
        ellipse2 = ellipse1.util.dump()
        self.assertEqual(type(ellipse2),unicode) 
        
    def testLineBoxMorph(self):
        line1 = p2r.obj.Line.create((5,0,0), (10,0,10))
        line2 = line1.defm.box_morph(((0,0,0),(0,1,0),(10,0,0),(0,10,0),(0,0,10),(1,0,0),(0,5,5),(5,0,0)))
        self.assertEqual(type(line2),p2r.obj.Line)
        
    def testLineShear(self):
        line1 = p2r.obj.Line.create((5,0,0), (10,0,10))
        line2 = line1.defm.shear((0,0,0),(10,10,10),45)
        self.assertEqual(type(line2),p2r.obj.Line)
        
    def testLineTrfm(self):
        line1 = p2r.obj.Line.create((5,0,0), (10,0,10))
        line2 = line1.defm.trfm(((0,0,0),(0,1,0),(0,2,0),(0,3,0),(1,0,0),(1,1,1),(1,2,0),(1,3,0),(2,0,0),(2,1,0),(2,2,1),(2,3,0),(3,0,0),(3,1,0),(3,2,0),(3,3,1)))
        self.assertEqual(type(line2),p2r.obj.Line) 
    
    def testLineCurvature(self):
        line1 = p2r.obj.Line.create_by_3pt((0,0,0), (20,0,0), (10,10,0))
        line2 = line1.eval.curvature(1)
        self.assertEqual(len(line2),5)      
    
    def testLineEvalDeriv(self):
        line1 = p2r.obj.Line.create_by_3pt((0,0,0), (20,0,0), (10,10,0))
        line2 = line1.eval.evaluate_derivatives(1,1)
        self.assertEqual(len(line2),2)   
    
    def testLineFrame(self):
        line1 = p2r.obj.Line.create_by_3pt((0,0,0), (20,0,0), (10,10,0))
        line2 = line1.eval.frame(1)
        self.assertEqual(len(line2),4) 
    
    def testLinePerpFrame(self):
        line1 = p2r.obj.Line.create_by_3pt((0,0,0), (20,0,0), (10,10,0))
        line2 = line1.eval.frame(1)
        self.assertEqual(len(line2),4) 
    
    def testLineTangent(self):
        line1 = p2r.obj.Line.create_by_3pt((0,0,0), (20,0,0), (10,10,0))
        line2 = line1.eval.tangent(1)
        self.assertEqual(len(line2),3) 
    
    def testLineEvaluate(self):
        line1 = p2r.obj.Line.create_by_3pt((0,0,0), (20,0,0), (10,10,0))
        line2 = line1.eval.evaluate(1)
        self.assertEqual(len(line2),3) 
    
    def testLineClosed(self):
        line1 = p2r.obj.Line.create((5,0,0), (10,0,10))
        line2 = line1.func.close()
        self.assertEqual(type(line2),p2r.obj.Line)
    
    def testLineExtend(self):
        line1 = p2r.obj.Line.create_by_3pt((0,0,0), (20,0,0), (10,10,0))
        line2 = p2r.obj.Line.create((0,0,0), 5, 45)
        line3 = line1.func.extend(1,1,line2)
        self.assertEqual(type(line3),p2r.obj.Line)
    
    def testLineExtendLength(self):
        line1 = p2r.obj.Line.create((5,0,0), (10,0,10))
        line2 = line1.func.extend_length(2,2,3)
        #print line2
        self.assertEqual(type(line2),p2r.obj.NurbsCurve) #TODO: to check if it is suppose to return as a nurbscurve
        
    def testLineExtendPnt(self):
        line1 = p2r.obj.Line.create((5,0,0), (10,0,10))
        line2 = line1.func.extend_pnt(1,(1,1,1))
        self.assertEqual(type(line2),p2r.obj.NurbsCurve) #TODO: to check if it is suppose to return as a nurbscurve
        
    def testLineGroups(self):
        line1 = p2r.obj.Line.create((5,0,0), (10,0,10))
        line2 = line1.grps.groups()
        self.assertEqual(type(line2),p2r.obj.Line)
        
    def testLineTopGroup(self):
        line1 = p2r.obj.Line.create((5,0,0), (10,0,10))
        line2 = line1.grps.top_group()
        self.assertEqual(type(line2),p2r.obj.Line)  
        
    def testLineIndex(self):
        line1 = p2r.obj.Line.create((5,0,0), (10,0,10))
        line2 = line1.mtrl.index()
        self.assertEqual(type(line2),int)       
        
    def testLineSource(self):
        line1 = p2r.obj.Line.create((5,0,0), (10,0,10))
        line2 = line1.mtrl.source(0)              #TODO: if 0 is not provided, none is returned.
        self.assertEqual(type(line2),int)   
 
    
        
    def testLineAddMesh(self):
        line1 = p2r.obj.Line.create((5,0,0), (10,0,10))
        line2 = line1.rndr.add_mesh()
        self.assertEqual(type(line2),bool)   
        
    def testLineEnable(self):
        line1 = p2r.obj.Line.create((5,0,0), (10,0,10))
        line2 = line1.rndr.enable()
        self.assertEqual(type(line2),bool)   
        
    def testLineHasMesh(self):
        line1 = p2r.obj.Line.create((5,0,0), (10,0,10))
        line2 = line1.rndr.has_mesh()
        self.assertEqual(type(line2),bool)   
            
    def testLineHide(self):
        line1 = p2r.obj.Line.create((5,0,0), (10,0,10))
        line2 = line1.stat.hide()
        self.assertEqual(type(line2),int)  
        
    def testLineLock(self):
        line1 = p2r.obj.Line.create((5,0,0), (10,0,10))
        line2 = line1.stat.lock()
        self.assertEqual(type(line2),int)  
        
    def testLineMatchObjectAttributes(self):
        line1 = p2r.obj.Line.create((5,0,0), (10,0,10))
        line2 = p2r.obj.Line.create_by_3pt((0,0,0), (20,0,0), (10,10,0))
        match = line1.stat.match_object_attributes(line2)
        self.assertEqual(type(match),int)  
        
    def testLineResetObjectAttributes(self):
        line1 = p2r.obj.Line.create((5,0,0), (10,0,10))
        reset = line1.stat.reset_object_attributes()
        self.assertEqual(type(reset),int)  
        
    def testLineMoveToLayoutSpace(self):
        line1 = p2r.obj.Line.create((5,0,0), (10,0,10))
        reset = line1.stat.move_to_layout_space()
        self.assertEqual(type(reset),str)  
        
    def testLineSelect(self):
        line1 = p2r.obj.Line.create((5,0,0), (10,0,10))
        sel = line1.stat.select()
        self.assertEqual(type(sel),int)  
        
    def testLineShow(self):
        line1 = p2r.obj.Line.create((5,0,0), (10,0,10))
        sel = line1.stat.show()
        self.assertEqual(type(sel),int)  
        
    def testLineUnlock(self):
        line1 = p2r.obj.Line.create((5,0,0), (10,0,10))
        line2 = line1.stat.unlock()
        self.assertEqual(type(line2),int) 
        
    def testLineUnselect(self):
        line1 = p2r.obj.Line.create((5,0,0), (10,0,10))
        sel = line1.stat.unselect()
        self.assertEqual(type(sel),int) 
        
    def testLineIsClosable(self):
        line1 = p2r.obj.Line.create((5,0,0), (10,0,10))
        closable = line1.test.is_closable()
        self.assertEqual(type(closable),bool) 
        
    def testLineIsClosed(self):
        line1 = p2r.obj.Line.create((5,0,0), (10,0,10))
        closed = line1.test.is_closed()
        self.assertEqual(type(closed),bool) 
        
    def testLineInPlane(self):
        line1 = p2r.obj.Line.create((5,0,0), (10,0,10))
        plane = line1.test.in_plane()
        self.assertEqual(type(plane),bool) 
        
    def testLineIsLinear(self):
        line1 = p2r.obj.Line.create((5,0,0), (10,0,10))
        linear = line1.test.is_linear()
        self.assertEqual(type(linear),bool)
        
    def testLineIsPeriodic(self):
        line1 = p2r.obj.Line.create((5,0,0), (10,0,10))
        periodic = line1.test.is_periodic()
        self.assertEqual(type(periodic),bool)
        
    def testLineIsPlanar(self):
        line1 = p2r.obj.Line.create((5,0,0), (10,0,10))
        planar = line1.test.is_planar()
        self.assertEqual(type(planar),bool)
        
    def testLineIsRational(self):
        line1 = p2r.obj.Line.create((5,0,0), (10,0,10))
        rational = line1.test.is_rational()
        self.assertEqual(type(rational),bool)   
        
    def testLineIsPntOnCrv(self):
        line1 = p2r.obj.Line.create((5,0,0), (10,0,10))
        on_crv = line1.test.is_pnt_on_crv((0,0,0))
        self.assertEqual(type(on_crv),bool)         
        
    def testLineMirror(self):
        line1 = p2r.obj.Line.create((5,0,0), (10,0,10))
        line2 = line1.trfm.mirror((0,0,0),(1,1,1))
        self.assertEqual(type(line2),p2r.obj.Line)  
        
    def testLineMove(self):
        line1 = p2r.obj.Line.create((5,0,0), (10,0,10))
        line2 = line1.trfm.move((0,0,0),(1,1,1))
        self.assertEqual(type(line2),p2r.obj.Line)  
        
    def testLineMoveByVec(self):
        line1 = p2r.obj.Line.create((5,0,0), (10,0,10))
        line2 = line1.trfm.move_by_vec(((0,0,0),(1,1,1)))
        self.assertEqual(type(line2),p2r.obj.Line)  
        
    def testLineOrient(self):
        line1 = p2r.obj.Line.create((5,0,0), (10,0,10))
        line2 = line1.trfm.orient((0,0,0),(1,1,1))
        self.assertEqual(type(line2),p2r.obj.Line)  
        
    def testLineRemap(self):
        line1 = p2r.obj.Line.create((5,0,0), (10,0,10))
        line2 = line1.trfm.remap((0,0,0),(1,1,1))
        self.assertEqual(type(line2),p2r.obj.Line)  
        
    def testLineRotate(self):
        line1 = p2r.obj.Line.create((5,0,0), (10,0,10))
        line2 = line1.trfm.rotate((0,0,0),45)
        self.assertEqual(type(line2),p2r.obj.Line)  
        
    def testLineScale(self):
        line1 = p2r.obj.Line.create((5,0,0), (10,0,10))
        line2 = line1.trfm.scale((0,0,0),(1,2,3))
        self.assertEqual(type(line2),p2r.obj.Line)     
        
    def testLineDescription(self):
        line1 = p2r.obj.Line.create((5,0,0), (10,0,10))
        line2 = line1.util.description()
        self.assertEqual(type(line2),unicode)   
        
    def testLineDump(self):
        line1 = p2r.obj.Line.create((5,0,0), (10,0,10))
        line2 = line1.util.dump()
        self.assertEqual(type(line2),unicode) 
if __name__ == '__main__':
    unittest.main()
