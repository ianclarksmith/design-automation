import py2rhino._base as p2r_f
from py2rhino._base._util import *

tf = p2r_f.transformation.xform_translation((0,20,0))
print tf
obj1 = p2r_f.curve.add_circle((0,0,0), 10)


magic = ((VT_BSTR, 1), (VT_VARIANT, 1), (VT_BOOL, 1))
flattened = (obj1, tf, True)
obj2 = p2r_f._rsf._ApplyTypes_(272, 1, (VT_VARIANT, 0), magic, u"TransformObject", None, *flattened)
print obj2



magic = ((VT_BSTR, 1), (VT_ARRAY + VT_R8, 1), (VT_BOOL, 1))
flattened = (obj2, flatten_params(tf), True)
print p2r_f._rsf._ApplyTypes_(272, 1, (VT_VARIANT, 0), magic, u"TransformObject", None, *flattened)