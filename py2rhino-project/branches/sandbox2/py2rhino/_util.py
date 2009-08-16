#some utility functions
import py2rhino as p2r
from py2rhino.wrappers import curve
from py2rhino.wrappers import object

def wrap(rhino_id):
    #TODO: implement this function    
    object_type = object.object_type(rhino_id)
    
    """
    0:  Unknown object
    1: Point
    2: Point cloud
    4: Curve
    8: Surface or single-face brep
    16: Polysurface or multiple-face
    32: Mesh
    256: Light
    512: Annotation
    4096:  Instance or block reference
    8192:  Text dot object
    16384: Grip object
    32768: Detail
    65536: Hatch
    131072: Morph control
    134217728: Cage
    268435456: Phantom
    536870912: Clipping plane
    """
    
    if object_type == 4:
        if curve.is_arc(rhino_id): return p2r.Arc(rhino_id)
        elif curve.is_circle(rhino_id): return p2r.Circle(rhino_id)
        elif curve.is_curve(rhino_id): return p2r.NurbsCurve(rhino_id)
        elif curve.is_ellipse(rhino_id): return p2r.Ellipse(rhino_id)
        elif curve.is_line(rhino_id): return p2r.Line(rhino_id)
        elif curve.is_polyline(rhino_id): return p2r.Polyline(rhino_id)

    print "conversion of type not yet implemented"#TODO: add surfaces
    return None 