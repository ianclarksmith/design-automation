import py2rhino as p2r
import py2rhino.util.vector as v

cv = p2r.obj.NurbsCurve("6a3976f1-81fa-4df8-9e0b-ede66af220a1")
pl =  cv.eval.frame(0.2)

start  = v.add(pl[0], v.scale(v.unitize(pl[2]), 10))
end  = v.add(pl[0], v.scale(v.unitize(v.reverse(pl[2])), 10))
point  = v.add(pl[0], v.scale(v.unitize(pl[3]), 10))
arc = p2r.obj.Arc.create_by_3pt(start, end, point)

print "done"