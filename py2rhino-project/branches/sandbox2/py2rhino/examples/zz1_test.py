#from py2rhino.nurbs_curve import NurbsCurve
import py2rhino as p2r

#######u'Type mismatch in parameter. String required.'############
#arc2 = p2r.Arc.create((0,0,0), 5, 45)
#print arc2.rndr.enable()
#density onwards.. all none.
##################################################################

######################u'Type mismatch in parameter. One-dimensional array required.############
#arc2 = p2r.Arc.create((0,0,0), 5, 45)
#arc2.defm.trfm((1,0,0))
###############################################################################################


###############should only ask for 1 curve, not 2#############
#arc1 = p2r.Arc.create_by_3pt((0,0,0), (20,0,0), (10,10,0))
#arc2 = p2r.Arc.create((0,0,0), 5, 45)
#arc2.create_by_fillet(arc1)c 
###############################################################

#####################not used#########################
#_SurfaceRootType is not specified in the surface 
######################################################

#####################Return none in functional and obj####################################
#nurve_surface1  = p2r.NurbsSurface.create_by_corner_pts(((0,0,0),(5,0,0),(5,5,0),(0,5,0)))
#print nurve_surface1.genr.fit()
#sphere1 = p2r.Sphere.create((0,0,0), 10)
#print sphere1.genr.make_non_periodic(1)
#print sphere1.modf.rebuild()
#print nurve_surface1.test.is_poly_srf_planar()
#print nurve_surface1.test.is_poly_surface_closed()

#arc2 = p2r.Arc.create((0,0,0), 5, 45)
#print arc2.defm.box_morph((1,0,0))
#print arc2.grps.top_group()
#print arc2.grps.groups()
#arc2 = p2r.Arc.create((0,0,0), 5, 45)
#print arc2.modf.seam(1)
##########################################################################################



###############return float() argument must be a string or a number, same in func###############
#plane_surface = p2r.PlaneSurface.create(((0,0,0),(1,0,0),(0,1,0)),5,3)
#print plane_surface.modf.insert_knot((0,0,1),1)
#print plane_surface.modf.remove_knot((0,0,1),1)
################################################################################################

################return none, same as func.##################################
#arc1 = p2r.Arc.create_by_3pt((0,0,0), (20,0,0), (10,10,0))
#print arc1.defm.shear((0.0,0.0,0.0), (10.0,0.0,0.0), 20.0, True) 
#############################################################################


'''


#############################same problem in function###############################
#plane_surface1 = p2r.PlaneSurface.create(((0,0,0),(1,0,0),(0,1,0)),5,3)
#plane_surface2 = p2r.PlaneSurface.create(((0,1,0),(1,2,0),(0,1,3)),5,3)
#polysurface1 = p2r.PolySurface.create_by_srf_join((plane_surface1,plane_surface2))
#print polysurface1
#####################################################################################

############the following can't work in both function and objection##################
#in function, we specify: print p2r.curve.line_fit_from_points(((0,0,0),(10,10,10)))
#return 'Type mismatch in parameter. Array required.', None, 0, 0), None)
#arc1 = p2r.Arc.create_by_3pt((0,0,0), (20,0,0), (10,10,0))
#print arc1.func.line_fit_from_pnts()   
####################################################################################


######################PROBLEM:argument 2 to map() must support iteration################################
#nurve_surface6 = p2r.NurbsSurface.create_by_planar_crv(arc1) #fixed this only
#nurve_curve3 = p2r.NurbsCurve.create_by_srf_contour_cut_plane(plane_surface,((0,0,0),(1,0,0),(0,1,0)))
#nurve_curve3 = p2r.NurbsCurve.create_by_srf_iso_curve(plane_surface,((1,0,0),(0,1,0)),2)
#circle1 = p2r.Circle.create(((0,0,0),(1,0,0),(0,1,0)), 5)
#line1 = p2r.Line.create((5,0,0), (10,0,10))

#nurve_curve9 = p2r.NurbsCurve.create_by_projection_to_srf(arc1,plane_surface,(0,0,1))
#nurve_surface7 = p2r.NurbsSurface.create_by_extrude_crv(circle1,line1) #works in functional level
#nurve_surface8 = p2r.NurbsSurface.create_by_extrude_crv(circle1, (0,0,10))#works in functional level

#nurve_surface1  = p2r.NurbsSurface.create_by_corner_pts(((0,0,0),(5,0,0),(5,5,0),(0,5,0)))
#line1 = p2r.Line.create((5,0,0), (10,0,10))
#polysurface1 = p2r.PolySurface.create_by_srf_extrude(nurve_surface1, line1) #works in functional level
#arc1 = p2r.Arc.create((0,0,0), 5, 90)
#arc2 = p2r.Arc.create((10,0,0), 5, 90)
#print arc1.stat.match_object_attributes(arc2)

#circle1 = p2r.Circle.create((0,0,0), 10)
#circle2 = p2r.Circle.create((0,0,0), 10)
#print circle1
#print p2r.NurbsSurface.create_by_sweep_1(circle2, circle1)
###########################################################################################################



#####################Return none in functional and obj####################################
#line1 = p2r.Line.create((5,0,0), (10,0,10))
#nurve_surface11 = p2r.NurbsSurface.create_by_rev(line1,((0,0,0),(0,0,1)))
##########################################################################################

#############PROBLEM:u'Type mismatch in parameter. Array required in both functional and obj.#######################
#cylinder1 = p2r.Cylinder.create((0,0,0),2, 5)
#cylinder2 = p2r.Cylinder.create_by_plane((0,0,0),2, 5)
#print cylinder1
#cone1 = p2r.Cone.create((0,0,0), 8, 5)
#cone2 = p2r.Cone.create_by_plane((0,0,0), 8, 5)
#print cone1
###########################################################################################
'''

print "done"