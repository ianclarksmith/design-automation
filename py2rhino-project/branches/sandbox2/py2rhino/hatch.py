# Auto-generated wrapper for Rhino4 RhinoScript functions

import py2rhino.functions as rf
class Hatch(_OtherType):    # Class constructor
    def __init__(self):
        pass
    def (, hatch=None, scale=None, rotation=None):

        return _rsf.add_hatch(, hatch, scale, rotation)

    def add_hatches(curves, hatch=None, scale=None, rotation=None):

        return _rsf.add_hatches(curves, hatch, scale, rotation)

    def explode_hatch(, delete=None):

        return _rsf.explode_hatch(, delete)

    def hatch_rotation(, rotation=None):

        return _rsf.hatch_rotation(, rotation)

    def hatch_scale(, scale=None):

        return _rsf.hatch_scale(, scale)

