
import py2rhino as p2r
cone1 = p2r.obj.Cone.create((0,0,0), (0,0,8), 5)
cone1.trfm.move_by_vec((0,0,50))

cir = p2r.obj.Circle.create((0,0,0), 50)
cir2 = cir.dupl.copy_move_by_vec((0,20,0))

cir.func.boolean_intersection(cir2)



print "done"
