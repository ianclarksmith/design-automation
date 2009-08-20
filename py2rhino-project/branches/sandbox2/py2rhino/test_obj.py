import unittest
import py2rhino as p2r

class obj_test(unittest.TestCase):
    #def testSingleWord(self):
        #self.assertEqual('justoneword', 'justoneword')
        
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
        cone1 = p2r.obj.Cone.create((0,0,0), 8, 5)
        self.assertEqual(type(cone1),p2r.obj.Cone)
        
    def testCreateConeByPlane(self):
        cone1 = p2r.obj.Cone.create_by_plane((0,0,0), 8, 5)
        self.assertEqual(type(cone1),p2r.obj.Cone)
    
    def testCreateCylinder(self):
        cylinder1 = p2r.obj.Cylinder.create((0,0,0),2, 5)
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
        nurvesurface1  = p2r.obj.NurbsSurface.create_by_corner_pts(((0,0,0),(5,0,0),(5,5,0),(0,5,0)))
        nurbscurve1 = p2r.obj.NurbsCurve.create_interp_crv_on_srf(nurvesurface1,((0,0,0),(5,0,0)))
        self.assertEqual(type(nurbscurve1),p2r.obj.NurbsCurve)
        
    def testCreateInterpCrvOnSrfUV(self):        
        nurvesurface1  = p2r.obj.NurbsSurface.create_by_corner_pts(((0,0,0),(5,0,0),(5,5,0),(0,5,0)))
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
        nurvesurface1  = p2r.obj.NurbsSurface.create_by_corner_pts(((0,0,0),(5,0,0),(5,5,0),(0,5,0)))
        nurbscurve1 = p2r.obj.NurbsCurve.create_by_srf_contour(nurvesurface1, (0,0,0), (5,0,0))
        self.assertEqual(type(nurbscurve1[0]),p2r.obj.NurbsCurve)
        
    def testCreateNurbsCurveBySurfaceContourCutPlane(self):
        nurvesurface1  = p2r.obj.NurbsSurface.create_by_corner_pts(((0,0,0),(5,0,0),(5,5,0),(0,5,0)))
        nurbscurve1 = p2r.obj.NurbsCurve.create_by_srf_contour_cut_plane(nurvesurface1, ((0,0,0),(1,0,0),(5,0,0)))
        self.assertEqual(type(nurbscurve1),p2r.obj.NurbsCurve)
        
    def testCreateNurbsCurveBySurfaceSection(self):
        nurvesurface1  = p2r.obj.NurbsSurface.create_by_corner_pts(((0,0,0),(5,0,0),(5,5,0),(0,5,0)))
        nurbscurve1 = p2r.obj.NurbsCurve.create_by_srf_section(nurvesurface1, ((0,0,0),(1,0,0),(-0.7,0,0.7),(0.7,0,0.7)))
        self.assertEqual(type(nurbscurve1[0]),p2r.obj.NurbsCurve)
        
    def testCreateNurbsCurveBySurfaceEdge(self):
        nurvesurface1  = p2r.obj.NurbsSurface.create_by_corner_pts(((0,0,0),(5,0,0),(5,5,0),(0,5,0)))
        nurbscurve1 = p2r.obj.NurbsCurve.create_by_srf_edge(nurvesurface1)
        self.assertEqual(type(nurbscurve1[0]),p2r.obj.NurbsCurve)
        
    def testCreateNurbsCurveByMeshBorder(self):
        mesh1 = p2r.obj.Mesh.create(((0,0,0),(5,0,0),(10,0,0),(0,5,0),(5,5,0),(10,5,0),(0,10,0),(5,10,0),(10,10,0)), ((0,1,4,4),(2,4,1,1),(0,4,3,3),(2,5,4,4),(3,4,6,6),(5,8,4,4),(6,4,7,7),(8,7,4,4)))
        nurbscurve1 = p2r.obj.NurbsCurve.create_by_mesh_border(mesh1)
        self.assertEqual(type(nurbscurve1[0]),p2r.obj.NurbsCurve)
        
    def testCreateNurbsCurveBySurfaceBorder(self):
        nurvesurface1  = p2r.obj.NurbsSurface.create_by_corner_pts(((0,0,0),(5,0,0),(5,5,0),(0,5,0)))
        nurbscurve1 = p2r.obj.NurbsCurve.create_by_srf_border(nurvesurface1)
        self.assertEqual(type(nurbscurve1[0]),p2r.obj.NurbsCurve)
        
    def testCreateNurbsCurveBySurfaceISOCurve(self):
        nurvesurface1  = p2r.obj.NurbsSurface.create_by_corner_pts(((0,0,0),(5,0,0),(5,5,0),(0,5,0)))
        nurbscurve1 = p2r.obj.NurbsCurve.create_by_srf_iso_curve(nurvesurface1,2,0)
        self.assertEqual(type(nurbscurve1),p2r.obj.NurbsCurve)
        
    def testCreateNurbsCurveByFit(self):
        nurvesurface1  = p2r.obj.NurbsSurface.create_by_corner_pts(((0,0,0),(5,0,0),(5,5,0),(0,5,0)))
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
        
    def testCreateNurbsCurveByMeshPull(self):
        mesh1 = p2r.obj.Mesh.create(((0,0,0),(5,0,0),(10,0,0),(0,5,0),(5,5,0),(10,5,0),(0,10,0),(5,10,0),(10,10,0)), ((0,1,4,4),(2,4,1,1),(0,4,3,3),(2,5,4,4),(3,4,6,6),(5,8,4,4),(6,4,7,7),(8,7,4,4)))
        nurbscurve1 = p2r.obj.NurbsCurve.create(((5,0,0),(5,2,0),(3.5,3.5,0)),(0,0,4,4),2)
        nurbscurve2 = p2r.obj.NurbsCurve.create_by_mesh_pull(nurbscurve1, mesh1)
        self.assertEqual(type(nurbscurve2),p2r.obj.NurbsCurve)
        
    def testCreateNurbsCurveByShortPath(self):
        planesurface1 = p2r.obj.PlaneSurface.create(((0,0,0),(0,1,0),(1,0,0)),3,5)
        nurbscurve1 = p2r.obj.NurbsCurve.create_by_srf_short_path(planesurface1, (0,0,0) (5,5,5))
        self.assertEqual(type(nurbscurve1),p2r.obj.NurbsCurve)
        
    def testCreateNurbsCurveBySurfacePrincipalCurvature(self):
        nurvesurface1  = p2r.obj.NurbsSurface.create_by_corner_pts(((0,0,0),(5,0,0),(5,5,0),(0,5,0)))
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
        
    def testCreatePolySurfaceCreateBySrfExtrude(self):
        nurvesurface1  = p2r.obj.NurbsSurface.create_by_corner_pts(((0,0,0),(5,0,0),(5,5,0),(0,5,0)))
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
        
    def testArcCopySubCrv(self):
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
    
    def testArcOpenCrvClosed(self):
        arc1 = p2r.obj.Arc.create((0,0,0), 5, 45)
        arc2 = arc1.func.open_crv_close()
        self.assertEqual(type(arc2),p2r.obj.Arc)
    
    def testArcOpenCrvExtend(self):
        arc1 = p2r.obj.Arc.create_by_3pt((0,0,0), (20,0,0), (10,10,0))
        arc2 = p2r.obj.Arc.create((0,0,0), 5, 45)
        arc3 = arc1.func.open_crv_extend(1,1,arc2)
        self.assertEqual(type(arc3),p2r.obj.Arc)
    
    def testArcOpenCrvExtendLength(self):
        arc1 = p2r.obj.Arc.create((0,0,0), 5, 45)
        arc2 = arc1.func.open_crv_extend_length(2,2,3)
        #print arc2
        self.assertEqual(type(arc2),p2r.obj.Arc) 
        
    def testArcOpenCrvExtendPnt(self):
        arc1 = p2r.obj.Arc.create((0,0,0), 5, 45)
        arc2 = arc1.func.open_crv_extend_pnt(1,(1,1,1))
        self.assertEqual(type(arc2),p2r.obj.Arc)
        
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
        
    def testArcDensity(self):
        arc1 = p2r.obj.Arc.create((0,0,0), 5, 45)
        arc2 = arc1.rndr.density()
        self.assertEqual(type(arc2),bool)   
        
    def testArcMaxAngle(self):
        arc1 = p2r.obj.Arc.create((0,0,0), 5, 45)
        arc2 = arc1.rndr.max_angle()
        self.assertEqual(type(arc2),bool)  
        
    def testArcAspectRatio(self):
        arc1 = p2r.obj.Arc.create((0,0,0), 5, 45)
        arc2 = arc1.rndr.max_aspect_ratio()
        self.assertEqual(type(arc2),bool)  
        
    def testArcMaxDistEdgeToSrf(self):
        arc1 = p2r.obj.Arc.create((0,0,0), 5, 45)
        arc2 = arc1.rndr.max_dist_edge_to_srf()
        self.assertEqual(type(arc2),bool)  
        
    def testArcMaxEdgeLength(self):
        arc1 = p2r.obj.Arc.create((0,0,0), 5, 45)
        arc2 = arc1.rndr.max_edge_length()
        self.assertEqual(type(arc2),bool)  
        
    def testArcMinEdgeLength(self):
        arc1 = p2r.obj.Arc.create((0,0,0), 5, 45)
        arc2 = arc1.rndr.min_edge_length()
        self.assertEqual(type(arc2),bool)  
        
    def testArcMinInitialGridQuads(self):
        arc1 = p2r.obj.Arc.create((0,0,0), 5, 45)
        arc2 = arc1.rndr.min_initial_grid_quads()
        self.assertEqual(type(arc2),bool)  
        
    def testArcQuality(self):
        arc1 = p2r.obj.Arc.create((0,0,0), 5, 45)
        arc2 = arc1.rndr.quality()
        self.assertEqual(type(arc2),bool)  
        
    def testArcSettings(self):
        arc1 = p2r.obj.Arc.create((0,0,0), 5, 45)
        arc2 = arc1.rndr.settings()
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
        
    def testArcIsOnCrv(self):
        arc1 = p2r.obj.Arc.create((0,0,0), 5, 45)
        on_crv = arc1.test.is_on_crv()
        self.assertEqual(type(on_crv),bool)            
        
    def testArcMirror(self):
        arc1 = p2r.obj.Arc.create((0,0,0), 5, 45)
        arc2 = arc1.trfm.mirror((0,0,0),(1,1,1))
        self.assertEqual(type(arc2),p2r.obj.Arc) 
        
    def testArcMove(self):
        arc1 = p2r.obj.Arc.create((0,0,0), 5, 45)
        arc2 = arc1.test.move((0,0,0),(1,1,1))
        self.assertEqual(type(arc2),bool)  
        
    def testArcMoveByVec(self):
        arc1 = p2r.obj.Arc.create((0,0,0), 5, 45)
        arc2 = arc1.test.move_by_vec((0,0,0),(1,1,1))
        self.assertEqual(type(arc2),bool)  
        
    def testArcOrient(self):
        arc1 = p2r.obj.Arc.create((0,0,0), 5, 45)
        arc2 = arc1.test.orient((0,0,0),(1,1,1))
        self.assertEqual(type(arc2),p2r.obj.Arc)  
        
    def testArcRemap(self):
        arc1 = p2r.obj.Arc.create((0,0,0), 5, 45)
        arc2 = arc1.test.remap((0,0,0),(1,1,1))
        self.assertEqual(type(arc2),p2r.obj.Arc)  
    
        
if __name__ == '__main__':
    unittest.main()
