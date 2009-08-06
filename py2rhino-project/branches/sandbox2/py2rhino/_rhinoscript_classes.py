# Auto-generated wrapper for Rhino4 RhinoScript classes
import pythoncom
from exceptions import Exception
import py2rhino as p2r
_rsf = None


class _CurveRootEval(object):

    # Class constructor
    def __init__(self, _rhino_id, _class):
        if _rhino_id==None:
            raise Exception("_rhino_id is required.")
        self._rhino_id = _rhino_id
        self._class = _class

    def curvature(self, parameter):
        """
        For help, look up the Rhinoscript function: CurveCurvature
        """
        return _rsf.curve_curvature(self._rhino_id, parameter)

    def evaluate_derivatives(self, parameter, derivative):
        """
        For help, look up the Rhinoscript function: CurveEvaluate
        """
        return _rsf.curve_evaluate(self._rhino_id, parameter, derivative)

    def frame(self, parameter):
        """
        For help, look up the Rhinoscript function: CurveFrame
        """
        return _rsf.curve_frame(self._rhino_id, parameter)

    def perp_frame(self, parameter):
        """
        For help, look up the Rhinoscript function: CurvePerpFrame
        """
        return _rsf.curve_perp_frame(self._rhino_id, parameter)

    def tangent(self, parameter):
        """
        For help, look up the Rhinoscript function: CurveTangent
        """
        return _rsf.curve_tangent(self._rhino_id, parameter, pythoncom.Empty)

    def evaluate(self, parameter):
        """
        For help, look up the Rhinoscript function: EvaluateCurve
        """
        return _rsf.evaluate_curve(self._rhino_id, parameter, pythoncom.Empty)


class _CurveRootGenr(object):

    # Class constructor
    def __init__(self, _rhino_id, _class):
        if _rhino_id==None:
            raise Exception("_rhino_id is required.")
        self._rhino_id = _rhino_id
        self._class = _class

    def fit(self, degree=pythoncom.Empty, tolerance=pythoncom.Empty, angle_tolerance=pythoncom.Empty):
        """
        For help, look up the Rhinoscript function: FitCurve
        """
        _rhino_id = _rsf.fit_curve(self._rhino_id, degree, tolerance, angle_tolerance)
        if _rhino_id:
            return p2r.NurbsCurve(_rhino_id)
        else:
            return None

    def make_non_periodic(self):
        """
        For help, look up the Rhinoscript function: MakeCurveNonPeriodic
        """
        _rhino_id = _rsf.make_curve_non_periodic(self._rhino_id, False)
        if _rhino_id:
            return p2r.NurbsCurve(_rhino_id)
        else:
            return None

    def make_periodic(self):
        """
        For help, look up the Rhinoscript function: MakeCurvePeriodic
        """
        _rhino_id = _rsf.make_curve_periodic(self._rhino_id, False)
        if _rhino_id:
            return p2r.NurbsCurve(_rhino_id)
        else:
            return None


class _CurveRootProp(object):

    # Class constructor
    def __init__(self, _rhino_id, _class):
        if _rhino_id==None:
            raise Exception("_rhino_id is required.")
        self._rhino_id = _rhino_id
        self._class = _class

    def arrows(self, style=pythoncom.Empty):
        """
        For help, look up the Rhinoscript function: CurveArrows
        """
        return _rsf.curve_arrows(self._rhino_id, style)

    def degree(self):
        """
        For help, look up the Rhinoscript function: CurveDegree
        """
        return _rsf.curve_degree(self._rhino_id, pythoncom.Empty)

    def dim(self):
        """
        For help, look up the Rhinoscript function: CurveDim
        """
        return _rsf.curve_dim(self._rhino_id, pythoncom.Empty)

    def discontinuity(self, style):
        """
        For help, look up the Rhinoscript function: CurveDiscontinuity
        """
        return _rsf.curve_discontinuity(self._rhino_id, style)

    def domain(self):
        """
        For help, look up the Rhinoscript function: CurveDomain
        """
        return _rsf.curve_domain(self._rhino_id, pythoncom.Empty)

    def edit_pnts(self, return_parameters=pythoncom.Empty):
        """
        For help, look up the Rhinoscript function: CurveEditPoints
        """
        return _rsf.curve_edit_points(self._rhino_id, return_parameters, pythoncom.Empty)

    def end_pnt(self):
        """
        For help, look up the Rhinoscript function: CurveEndPoint
        """
        return _rsf.curve_end_point(self._rhino_id, pythoncom.Empty)

    def knot_count(self):
        """
        For help, look up the Rhinoscript function: CurveKnotCount
        """
        return _rsf.curve_knot_count(self._rhino_id, pythoncom.Empty)

    def knots(self):
        """
        For help, look up the Rhinoscript function: CurveKnots
        """
        return _rsf.curve_knots(self._rhino_id, pythoncom.Empty)

    def length(self, sub_domain=pythoncom.Empty):
        """
        For help, look up the Rhinoscript function: CurveLength
        """
        return _rsf.curve_length(self._rhino_id, pythoncom.Empty, sub_domain)

    def mid_pnt(self):
        """
        For help, look up the Rhinoscript function: CurveMidPoint
        """
        return _rsf.curve_mid_point(self._rhino_id)

    def normal(self):
        """
        For help, look up the Rhinoscript function: CurveNormal
        """
        return _rsf.curve_normal(self._rhino_id)

    def plane(self):
        """
        For help, look up the Rhinoscript function: CurvePlane
        """
        return _rsf.curve_plane(self._rhino_id)

    def control_pnt_count(self):
        """
        For help, look up the Rhinoscript function: CurvePointCount
        """
        return _rsf.curve_point_count(self._rhino_id, pythoncom.Empty)

    def control_pnts(self):
        """
        For help, look up the Rhinoscript function: CurvePoints
        """
        return _rsf.curve_points(self._rhino_id, pythoncom.Empty)

    def start_pnt(self):
        """
        For help, look up the Rhinoscript function: CurveStartPoint
        """
        return _rsf.curve_start_point(self._rhino_id, pythoncom.Empty)

    def weights(self):
        """
        For help, look up the Rhinoscript function: CurveWeights
        """
        return _rsf.curve_weights(self._rhino_id, pythoncom.Empty)


class _ObjectRoot(object):

    # Class constructor
    def __init__(self, _rhino_id, _class):
        if _rhino_id==None:
            raise Exception("_rhino_id is required.")
        self._rhino_id = _rhino_id
        self._class = _class


class _ObjectRootDefm(object):

    # Class constructor
    def __init__(self, _rhino_id, _class):
        if _rhino_id==None:
            raise Exception("_rhino_id is required.")
        self._rhino_id = _rhino_id
        self._class = _class

    def box_morph(self, box_points, copy=pythoncom.Empty):
        """
        For help, look up the Rhinoscript function: BoxMorphObject
        """
        _rhino_id = _rsf.box_morph_object(self._rhino_id, box_points, copy)
        if _rhino_id:
            return p2r._util.wrap(_rhino_id)
        else:
            return None

    def shear(self, origin, ref_pt, scale, copy=pythoncom.Empty):
        """
        For help, look up the Rhinoscript function: ShearObject
        """
        _rhino_id = _rsf.shear_object(self._rhino_id, origin, ref_pt, scale, copy)
        if _rhino_id:
            return p2r._util.wrap(_rhino_id)
        else:
            return None

    def trfm(self, matrix, copy=pythoncom.Empty):
        """
        For help, look up the Rhinoscript function: TransformObject
        """
        _rhino_id = _rsf.transform_object(self._rhino_id, matrix, copy)
        if _rhino_id:
            return p2r._util.wrap(_rhino_id)
        else:
            return None


class _ObjectRootFunc(object):

    # Class constructor
    def __init__(self, _rhino_id, _class):
        if _rhino_id==None:
            raise Exception("_rhino_id is required.")
        self._rhino_id = _rhino_id
        self._class = _class

    def delete(self):
        """
        For help, look up the Rhinoscript function: DeleteObjects
        """
        return _rsf.delete_objects(self._rhino_id)


class _ObjectRootGrps(object):

    # Class constructor
    def __init__(self, _rhino_id, _class):
        if _rhino_id==None:
            raise Exception("_rhino_id is required.")
        self._rhino_id = _rhino_id
        self._class = _class

    def groups(self):
        """
        For help, look up the Rhinoscript function: ObjectGroups
        """
        return _rsf.object_groups(self._rhino_id)

    def top_group(self):
        """
        For help, look up the Rhinoscript function: ObjectTopGroup
        """
        return _rsf.object_top_group(self._rhino_id)


class _ObjectRootMdfy(object):

    # Class constructor
    def __init__(self, _rhino_id, _class):
        if _rhino_id==None:
            raise Exception("_rhino_id is required.")
        self._rhino_id = _rhino_id
        self._class = _class


class _ObjectRootMtrl(object):

    # Class constructor
    def __init__(self, _rhino_id, _class):
        if _rhino_id==None:
            raise Exception("_rhino_id is required.")
        self._rhino_id = _rhino_id
        self._class = _class

    def index(self):
        """
        For help, look up the Rhinoscript function: ObjectMaterialIndex
        """
        return _rsf.object_material_index(self._rhino_id)

    def source(self, source=pythoncom.Empty):
        """
        For help, look up the Rhinoscript function: ObjectMaterialSource
        """
        return _rsf.object_material_source(self._rhino_id, source)


class _ObjectRootProp(object):

    # Class constructor
    def __init__(self, _rhino_id, _class):
        if _rhino_id==None:
            raise Exception("_rhino_id is required.")
        self._rhino_id = _rhino_id
        self._class = _class

    def color(self, color=pythoncom.Empty):
        """
        For help, look up the Rhinoscript function: ObjectColor
        """
        return _rsf.object_color(self._rhino_id, color)

    def color_source(self, source=pythoncom.Empty):
        """
        For help, look up the Rhinoscript function: ObjectColorSource
        """
        return _rsf.object_color_source(self._rhino_id, source)

    def layer(self, layer=pythoncom.Empty):
        """
        For help, look up the Rhinoscript function: ObjectLayer
        """
        return _rsf.object_layer(self._rhino_id, layer._rhino_id)

    def linetype(self, layer=pythoncom.Empty):
        """
        For help, look up the Rhinoscript function: ObjectLinetype
        """
        return _rsf.object_linetype(self._rhino_id, layer._rhino_id)

    def linetype_source(self, source=pythoncom.Empty):
        """
        For help, look up the Rhinoscript function: ObjectLinetypeSource
        """
        return _rsf.object_linetype_source(self._rhino_id, source)

    def name(self, names=pythoncom.Empty):
        """
        For help, look up the Rhinoscript function: ObjectNames
        """
        return _rsf.object_names(self._rhino_id, names)

    def print_color(self, color=pythoncom.Empty):
        """
        For help, look up the Rhinoscript function: ObjectPrintColor
        """
        return _rsf.object_print_color(self._rhino_id, color)

    def print_color_source(self, source=pythoncom.Empty):
        """
        For help, look up the Rhinoscript function: ObjectPrintColorSource
        """
        return _rsf.object_print_color_source(self._rhino_id, source)

    def print_width(self, width=pythoncom.Empty):
        """
        For help, look up the Rhinoscript function: ObjectPrintWidth
        """
        return _rsf.object_print_width(self._rhino_id, width)

    def print_width_source(self, source=pythoncom.Empty):
        """
        For help, look up the Rhinoscript function: ObjectPrintWidthSource
        """
        return _rsf.object_print_width_source(self._rhino_id, source)


class _ObjectRootRndr(object):

    # Class constructor
    def __init__(self, _rhino_id, _class):
        if _rhino_id==None:
            raise Exception("_rhino_id is required.")
        self._rhino_id = _rhino_id
        self._class = _class

    def add_mesh(self, quality=pythoncom.Empty, enable=pythoncom.Empty):
        """
        For help, look up the Rhinoscript function: AddObjectMesh
        """
        return _rsf.add_object_mesh(self._rhino_id, quality, enable)

    def enable(self, enable=pythoncom.Empty):
        """
        For help, look up the Rhinoscript function: EnableObjectMesh
        """
        return _rsf.enable_object_mesh(self._rhino_id, enable)

    def has_mesh(self):
        """
        For help, look up the Rhinoscript function: ObjectHasMesh
        """
        return _rsf.object_has_mesh(self._rhino_id)

    def density(self, density=pythoncom.Empty):
        """
        For help, look up the Rhinoscript function: ObjectMeshDensity
        """
        return _rsf.object_mesh_density(self._rhino_id, density)

    def max_angle(self, angle=pythoncom.Empty):
        """
        For help, look up the Rhinoscript function: ObjectMeshMaxAngle
        """
        return _rsf.object_mesh_max_angle(self._rhino_id, angle)

    def max_aspect_ratio(self, ratio=pythoncom.Empty):
        """
        For help, look up the Rhinoscript function: ObjectMeshMaxAspectRatio
        """
        return _rsf.object_mesh_max_aspect_ratio(self._rhino_id, ratio)

    def max_dist_edge_to_srf(self, distance=pythoncom.Empty):
        """
        For help, look up the Rhinoscript function: ObjectMeshMaxDistEdgeToSrf
        """
        return _rsf.object_mesh_max_dist_edge_to_srf(self._rhino_id, distance)

    def max_edge_length(self, length=pythoncom.Empty):
        """
        For help, look up the Rhinoscript function: ObjectMeshMaxEdgeLength
        """
        return _rsf.object_mesh_max_edge_length(self._rhino_id, length)

    def min_edge_length(self, length=pythoncom.Empty):
        """
        For help, look up the Rhinoscript function: ObjectMeshMinEdgeLength
        """
        return _rsf.object_mesh_min_edge_length(self._rhino_id, length)

    def min_initial_grid_quads(self, quads=pythoncom.Empty):
        """
        For help, look up the Rhinoscript function: ObjectMeshMinInitialGridQuads
        """
        return _rsf.object_mesh_min_initial_grid_quads(self._rhino_id, quads)

    def quality(self, quality=pythoncom.Empty):
        """
        For help, look up the Rhinoscript function: ObjectMeshQuality
        """
        return _rsf.object_mesh_quality(self._rhino_id, quality)

    def settings(self, settings=pythoncom.Empty):
        """
        For help, look up the Rhinoscript function: ObjectMeshSettings
        """
        return _rsf.object_mesh_settings(self._rhino_id, settings)


class _ObjectRootStat(object):

    # Class constructor
    def __init__(self, _rhino_id, _class):
        if _rhino_id==None:
            raise Exception("_rhino_id is required.")
        self._rhino_id = _rhino_id
        self._class = _class

    def flash(self, style=pythoncom.Empty):
        """
        For help, look up the Rhinoscript function: FlashObject
        """
        return _rsf.flash_object()

    def hide(self):
        """
        For help, look up the Rhinoscript function: HideObjects
        """
        return _rsf.hide_objects(self._rhino_id)

    def lock(self):
        """
        For help, look up the Rhinoscript function: LockObjects
        """
        return _rsf.lock_objects(self._rhino_id)

    def match_object_attributes(self, targets):
        """
        For help, look up the Rhinoscript function: MatchObjectAttributes
        """
        return _rsf.match_object_attributes(map(lambda i: i._rhino_id, targets), self._rhino_id)

    def reset_object_attributes(self, source):
        """
        For help, look up the Rhinoscript function: MatchObjectAttributes
        """
        return _rsf.match_object_attributes(self._rhino_id, source._rhino_id)

    def move_to_layout_space(self, layout=pythoncom.Empty, return_name=pythoncom.Empty):
        """
        For help, look up the Rhinoscript function: ObjectLayout
        """
        return _rsf.object_layout(self._rhino_id, layout, return_name)

    def select(self):
        """
        For help, look up the Rhinoscript function: SelectObjects
        """
        return _rsf.select_objects(self._rhino_id)

    def show(self):
        """
        For help, look up the Rhinoscript function: ShowObjects
        """
        return _rsf.show_objects(self._rhino_id)

    def unlock(self):
        """
        For help, look up the Rhinoscript function: UnlockObjects
        """
        return _rsf.unlock_objects(self._rhino_id)

    def unselect(self):
        """
        For help, look up the Rhinoscript function: UnselectObjects
        """
        return _rsf.unselect_objects(self._rhino_id)


class _ObjectRootTest(object):

    # Class constructor
    def __init__(self, _rhino_id, _class):
        if _rhino_id==None:
            raise Exception("_rhino_id is required.")
        self._rhino_id = _rhino_id
        self._class = _class

    def is_in_layout_space(self):
        """
        For help, look up the Rhinoscript function: IsLayoutObject
        """
        return _rsf.is_layout_object(self._rhino_id)

    def is_hidden(self):
        """
        For help, look up the Rhinoscript function: IsObjectHidden
        """
        return _rsf.is_object_hidden(self._rhino_id)

    def is_in_box(self, box, mode=pythoncom.Empty):
        """
        For help, look up the Rhinoscript function: IsObjectInBox
        """
        return _rsf.is_object_in_box(self._rhino_id, box, mode)

    def is_in_group(self, group=pythoncom.Empty):
        """
        For help, look up the Rhinoscript function: IsObjectInGroup
        """
        return _rsf.is_object_in_group(self._rhino_id, group)

    def is_locked(self):
        """
        For help, look up the Rhinoscript function: IsObjectLocked
        """
        return _rsf.is_object_locked(self._rhino_id)

    def is_normal(self):
        """
        For help, look up the Rhinoscript function: IsObjectNormal
        """
        return _rsf.is_object_normal(self._rhino_id)

    def is_reference(self):
        """
        For help, look up the Rhinoscript function: IsObjectReference
        """
        return _rsf.is_object_reference(self._rhino_id)

    def is_selectable(self):
        """
        For help, look up the Rhinoscript function: IsObjectSelectable
        """
        return _rsf.is_object_selectable(self._rhino_id)

    def is_selected(self):
        """
        For help, look up the Rhinoscript function: IsObjectSelected
        """
        return _rsf.is_object_selected(self._rhino_id)

    def is_solid(self):
        """
        For help, look up the Rhinoscript function: IsObjectSolid
        """
        return _rsf.is_object_solid(self._rhino_id)

    def is_valid(self):
        """
        For help, look up the Rhinoscript function: IsObjectValid
        """
        return _rsf.is_object_valid(self._rhino_id)

    def is_visible_in_view(self, view=pythoncom.Empty):
        """
        For help, look up the Rhinoscript function: IsVisibleInView
        """
        return _rsf.is_visible_in_view(self._rhino_id, view)


class _ObjectRootTrfm(object):

    # Class constructor
    def __init__(self, _rhino_id, _class):
        if _rhino_id==None:
            raise Exception("_rhino_id is required.")
        self._rhino_id = _rhino_id
        self._class = _class

    def copy(self, start=pythoncom.Empty, end=pythoncom.Empty):
        """
        For help, look up the Rhinoscript function: CopyObject
        """
        _rhino_id = _rsf.copy_object(self._rhino_id, start, end)
        if _rhino_id:
            return self._class(_rhino_id)
        else:
            return None

    def copy_by_vec(self, translation=pythoncom.Empty):
        """
        For help, look up the Rhinoscript function: CopyObject2
        """
        _rhino_id = _rsf.copy_object_2(self._rhino_id, translation)
        if _rhino_id:
            return self._class(_rhino_id)
        else:
            return None

    def mirror(self, start_pt, end_pt, copy=pythoncom.Empty):
        """
        For help, look up the Rhinoscript function: MirrorObject
        """
        _rhino_id = _rsf.mirror_object(self._rhino_id, start_pt, end_pt, copy)
        if _rhino_id:
            return self._class(_rhino_id)
        else:
            return None

    def move(self, start, end):
        """
        For help, look up the Rhinoscript function: MoveObject
        """
        _rhino_id = _rsf.move_object(self._rhino_id, start, end)
        if _rhino_id:
            return self._class(_rhino_id)
        else:
            return None

    def move_by_vec(self, translation):
        """
        For help, look up the Rhinoscript function: MoveObject2
        """
        _rhino_id = _rsf.move_object_2(self._rhino_id, translation)
        if _rhino_id:
            return self._class(_rhino_id)
        else:
            return None

    def orient(self, reference, target, flags=pythoncom.Empty):
        """
        For help, look up the Rhinoscript function: OrientObject
        """
        _rhino_id = _rsf.orient_object(self._rhino_id, reference, target, flags)
        if _rhino_id:
            return self._class(_rhino_id)
        else:
            return None

    def remap(self, src_plane, dst_plane, copy=pythoncom.Empty):
        """
        For help, look up the Rhinoscript function: RemapObject
        """
        _rhino_id = _rsf.remap_object(self._rhino_id, src_plane, dst_plane, copy)
        if _rhino_id:
            return self._class(_rhino_id)
        else:
            return None

    def rotate(self, point, angle, axis=pythoncom.Empty, copy=pythoncom.Empty):
        """
        For help, look up the Rhinoscript function: RotateObject
        """
        _rhino_id = _rsf.rotate_object(self._rhino_id, point, angle, axis, copy)
        if _rhino_id:
            return self._class(_rhino_id)
        else:
            return None

    def scale(self, origin, scale, copy=pythoncom.Empty):
        """
        For help, look up the Rhinoscript function: ScaleObject
        """
        _rhino_id = _rsf.scale_object(self._rhino_id, origin, scale, copy)
        if _rhino_id:
            return self._class(_rhino_id)
        else:
            return None


class _ObjectRootType(object):

    # Class constructor
    def __init__(self, _rhino_id, _class):
        if _rhino_id==None:
            raise Exception("_rhino_id is required.")
        self._rhino_id = _rhino_id
        self._class = _class

    def object_type(self):
        """
        For help, look up the Rhinoscript function: ObjectType
        """
        return _rsf.object_type(self._rhino_id)


class _ObjectRootUtil(object):

    # Class constructor
    def __init__(self, _rhino_id, _class):
        if _rhino_id==None:
            raise Exception("_rhino_id is required.")
        self._rhino_id = _rhino_id
        self._class = _class

    def description(self):
        """
        For help, look up the Rhinoscript function: ObjectDescription
        """
        return _rsf.object_description(self._rhino_id)

    def dump(self, type=pythoncom.Empty):
        """
        For help, look up the Rhinoscript function: ObjectDump
        """
        return _rsf.object_dump(self._rhino_id, type)


class _SurfaceRootEval(object):

    # Class constructor
    def __init__(self, _rhino_id, _class):
        if _rhino_id==None:
            raise Exception("_rhino_id is required.")
        self._rhino_id = _rhino_id
        self._class = _class

    def evaluate(self, parameter):
        """
        For help, look up the Rhinoscript function: EvaluateSurface
        """
        return _rsf.evaluate_surface(self._rhino_id, parameter)

    def evaluate_derivatives(self, parameter, derivative):
        """
        For help, look up the Rhinoscript function: SurfaceEvaluate
        """
        return _rsf.surface_evaluate(self._rhino_id, parameter, derivative)

    def evaluate_frame(self, parameter):
        """
        For help, look up the Rhinoscript function: SurfaceFrame
        """
        return _rsf.surface_frame(self._rhino_id, parameter)


class _SurfaceRootGenr(object):

    # Class constructor
    def __init__(self, _rhino_id, _class):
        if _rhino_id==None:
            raise Exception("_rhino_id is required.")
        self._rhino_id = _rhino_id
        self._class = _class

    def fit(self, degree=pythoncom.Empty, tolerance=pythoncom.Empty):
        """
        For help, look up the Rhinoscript function: FitSurface
        """
        _rhino_id = _rsf.fit_surface(self._rhino_id, degree, tolerance)
        if _rhino_id:
            return p2r.NurbsSurface(_rhino_id)
        else:
            return None

    def make_non_periodic(self, direction, delete=pythoncom.Empty):
        """
        For help, look up the Rhinoscript function: MakeSurfaceNonPeriodic
        """
        _rhino_id = _rsf.make_surface_non_periodic(self._rhino_id, direction, delete)
        if _rhino_id:
            return p2r.NurbsSurface(_rhino_id)
        else:
            return None

    def make_periodic(self, direction, delete=pythoncom.Empty):
        """
        For help, look up the Rhinoscript function: MakeSurfacePeriodic
        """
        _rhino_id = _rsf.make_surface_periodic(self._rhino_id, direction, delete)
        if _rhino_id:
            return p2r.NurbsSurface(_rhino_id)
        else:
            return None

    def offset(self, distance):
        """
        For help, look up the Rhinoscript function: OffsetSurface
        """
        _rhino_id = _rsf.offset_surface(self._rhino_id, distance)
        if _rhino_id:
            return p2r.NurbsSurface(_rhino_id)
        else:
            return None


class GenericObject(_ObjectRoot):

    # Class constructor
    def __init__(self, _rhino_id):
        if _rhino_id==None:
            raise Exception("Use the create... methods to create instances of this class.")
        self._rhino_id = _rhino_id

        self.defm = _ObjectRootDefm(_rhino_id, GenericObject)
        self.grps = _ObjectRootGrps(_rhino_id, GenericObject)
        self.mtrl = _ObjectRootMtrl(_rhino_id, GenericObject)
        self.prop = _ObjectRootProp(_rhino_id, GenericObject)
        self.rndr = _ObjectRootRndr(_rhino_id, GenericObject)
        self.stat = _ObjectRootStat(_rhino_id, GenericObject)
        self.test = _ObjectRootTest(_rhino_id, GenericObject)
        self.trfm = _ObjectRootTrfm(_rhino_id, GenericObject)
        self.type = _ObjectRootType(_rhino_id, GenericObject)
        self.util = _ObjectRootUtil(_rhino_id, GenericObject)


class _ArcProp(_CurveRootProp):

    # Class constructor
    def __init__(self, _rhino_id, _class):
        if _rhino_id==None:
            raise Exception("_rhino_id is required.")
        self._rhino_id = _rhino_id
        self._class = _class

    def angle(self):
        """
        For help, look up the Rhinoscript function: ArcAngle
        """
        return _rsf.arc_angle(self._rhino_id, pythoncom.Empty)

    def center_pnt(self):
        """
        For help, look up the Rhinoscript function: ArcCenterPoint
        """
        return _rsf.arc_center_point(self._rhino_id, pythoncom.Empty)

    def mid_pnt(self):
        """
        For help, look up the Rhinoscript function: ArcMidPoint
        """
        return _rsf.arc_mid_point(self._rhino_id, pythoncom.Empty)

    def radius(self):
        """
        For help, look up the Rhinoscript function: ArcRadius
        """
        return _rsf.arc_radius(self._rhino_id, pythoncom.Empty)


class _CircleProp(_CurveRootProp):

    # Class constructor
    def __init__(self, _rhino_id, _class):
        if _rhino_id==None:
            raise Exception("_rhino_id is required.")
        self._rhino_id = _rhino_id
        self._class = _class

    def center_pnt(self):
        """
        For help, look up the Rhinoscript function: CircleCenterPoint
        """
        return _rsf.circle_center_point(self._rhino_id, pythoncom.Empty)

    def circumference(self):
        """
        For help, look up the Rhinoscript function: CircleCircumference
        """
        return _rsf.circle_circumference(self._rhino_id, pythoncom.Empty)

    def radius(self):
        """
        For help, look up the Rhinoscript function: CircleRadius
        """
        return _rsf.circle_radius(self._rhino_id, pythoncom.Empty)


class _CurveRoot(_ObjectRoot):

    # Class constructor
    def __init__(self, _rhino_id, _class):
        if _rhino_id==None:
            raise Exception("_rhino_id is required.")
        self._rhino_id = _rhino_id
        self._class = _class


class _CurveRootFunc(_ObjectRootFunc):

    # Class constructor
    def __init__(self, _rhino_id, _class):
        if _rhino_id==None:
            raise Exception("_rhino_id is required.")
        self._rhino_id = _rhino_id
        self._class = _class

    def crv_arc_length_pnt(self, length, from_start=pythoncom.Empty):
        """
        For help, look up the Rhinoscript function: CurveArcLengthPoint
        """
        return _rsf.curve_arc_length_point(self._rhino_id, length, from_start)

    def closest_pnt(self, point):
        """
        For help, look up the Rhinoscript function: CurveClosestPnt
        """
        return _rsf.curve_closest_pnt(self._rhino_id, point, pythoncom.Empty)

    def contour_pnts(self, start_point, end_point, interval=pythoncom.Empty):
        """
        For help, look up the Rhinoscript function: CurveContourPoints
        """
        return _rsf.curve_contour_points(self._rhino_id, start_point, end_point, interval)

    def crv_intersection(self, curve=pythoncom.Empty, tolerance=pythoncom.Empty):
        """
        For help, look up the Rhinoscript function: CurveCurveIntersection
        """
        return _rsf.curve_curve_intersection(self._rhino_id, curve, tolerance)

    def deviation(self, curve_a):
        """
        For help, look up the Rhinoscript function: CurveDeviation
        """
        return _rsf.curve_deviation(self._rhino_id, curve_a)

    def directions_match(self, curve_1):
        """
        For help, look up the Rhinoscript function: CurveDirectionsMatch
        """
        return _rsf.curve_directions_match(self._rhino_id, curve_1)

    def radius(self, point):
        """
        For help, look up the Rhinoscript function: CurveRadius
        """
        return _rsf.curve_radius(self._rhino_id, point, pythoncom.Empty)

    def srf_intersection(self, surface, tolerance=pythoncom.Empty, angle_tolerance=pythoncom.Empty):
        """
        For help, look up the Rhinoscript function: CurveSurfaceIntersection
        """
        return _rsf.curve_surface_intersection(self._rhino_id, surface, tolerance, angle_tolerance)

    def divide_crv(self, segments, create=pythoncom.Empty, points=pythoncom.Empty):
        """
        For help, look up the Rhinoscript function: DivideCurve
        """
        return _rsf.divide_curve(self._rhino_id, segments, create, points)

    def divide_crv_equidistant(self, distance, create=pythoncom.Empty, points=pythoncom.Empty):
        """
        For help, look up the Rhinoscript function: DivideCurveEquidistant
        """
        return _rsf.divide_curve_equidistant(self._rhino_id, distance, create, points)

    def divide_crv_length(self, length, create=pythoncom.Empty, points=pythoncom.Empty):
        """
        For help, look up the Rhinoscript function: DivideCurveLength
        """
        return _rsf.divide_curve_length(self._rhino_id, length, create, points)

    def line_fit_from_pnts(self):
        """
        For help, look up the Rhinoscript function: LineFitFromPoints
        """
        return _rsf.line_fit_from_points(self._rhino_id)

    def planar_crv_collision(self, curve, plane=pythoncom.Empty, tolerance=pythoncom.Empty):
        """
        For help, look up the Rhinoscript function: PlanarCurveCollision
        """
        return _rsf.planar_curve_collision(self._rhino_id, curve, plane, tolerance)


class _CurveRootFuncClsd(_CurveRootFunc):

    # Class constructor
    def __init__(self, _rhino_id, _class):
        if _rhino_id==None:
            raise Exception("_rhino_id is required.")
        self._rhino_id = _rhino_id
        self._class = _class

    def closed_crv_area(self, objects):
        """
        For help, look up the Rhinoscript function: CurveArea
        """
        return _rsf.curve_area(map(lambda i: i._rhino_id, objects))

    def pclosed_crv_area_centroid(self, objects):
        """
        For help, look up the Rhinoscript function: CurveAreaCentroid
        """
        return _rsf.curve_area_centroid(map(lambda i: i._rhino_id, objects))

    def boolean_difference(self, curve):
        """
        For help, look up the Rhinoscript function: CurveBooleanDifference
        """
        _rhino_ids = _rsf.curve_boolean_difference(self._rhino_id, curve)
        return map(lambda i: p2r._util.wrap(i), _rhino_ids)

    def boolean_intersection(self, curve_a):
        """
        For help, look up the Rhinoscript function: CurveBooleanIntersection
        """
        _rhino_ids = _rsf.curve_boolean_intersection(self._rhino_id, curve_a)
        return map(lambda i: p2r._util.wrap(i), _rhino_ids)

    def boolean_union(self, curves):
        """
        For help, look up the Rhinoscript function: CurveBooleanUnion
        """
        _rhino_ids = _rsf.curve_boolean_union(map(lambda i: i._rhino_id, curves))
        return map(lambda i: p2r._util.wrap(i), _rhino_ids)

    def closed_crv_containment(self, curve__1, plane=pythoncom.Empty, tolerance=pythoncom.Empty):
        """
        For help, look up the Rhinoscript function: PlanarClosedCurveContainment
        """
        return _rsf.planar_closed_curve_containment(self._rhino_id, curve__1, plane, tolerance)

    def closed_crv_pnt_inside(self, point, plane=pythoncom.Empty, tolerance=pythoncom.Empty):
        """
        For help, look up the Rhinoscript function: PointInPlanarClosedCurve
        """
        return _rsf.point_in_planar_closed_curve(point, self._rhino_id, plane, tolerance)


class _CurveRootFuncOpen(_CurveRootFunc):

    # Class constructor
    def __init__(self, _rhino_id, _class):
        if _rhino_id==None:
            raise Exception("_rhino_id is required.")
        self._rhino_id = _rhino_id
        self._class = _class

    def open_crv_close(self, tolerance=pythoncom.Empty):
        """
        For help, look up the Rhinoscript function: CloseCurve
        """
        return _rsf.close_curve(self._rhino_id, tolerance)

    def open_crv_extend(self, type, side, objects):
        """
        For help, look up the Rhinoscript function: ExtendCurve
        """
        return _rsf.extend_curve(self._rhino_id, type, side, objects)

    def open_crv_extend_length(self, type, side, length):
        """
        For help, look up the Rhinoscript function: ExtendCurveLength
        """
        return _rsf.extend_curve_length(self._rhino_id, type, side, length)

    def open_crv_extend_pnt(self, side, point):
        """
        For help, look up the Rhinoscript function: ExtendCurvePoint
        """
        return _rsf.extend_curve_point(self._rhino_id, side, point)


class _CurveRootMdfy(_ObjectRootMdfy):

    # Class constructor
    def __init__(self, _rhino_id, _class):
        if _rhino_id==None:
            raise Exception("_rhino_id is required.")
        self._rhino_id = _rhino_id
        self._class = _class

    def seam(self, parameter):
        """
        For help, look up the Rhinoscript function: CurveSeam
        """

        return _rsf.curve_seam(self._rhino_id, parameter)


    def fair(self, tolerance=pythoncom.Empty):
        """
        For help, look up the Rhinoscript function: FairCurve
        """

        return _rsf.fair_curve(self._rhino_id, tolerance)


    def insert_knot(self, parameter, symmetrical=pythoncom.Empty):
        """
        For help, look up the Rhinoscript function: InsertCurveKnot
        """

        return _rsf.insert_curve_knot(self._rhino_id, parameter, symmetrical)


    def rebuild(self, degree=pythoncom.Empty, point_count=pythoncom.Empty):
        """
        For help, look up the Rhinoscript function: RebuildCurve
        """

        return _rsf.rebuild_curve(self._rhino_id, degree, point_count)


    def remove_knot(self, parameter):
        """
        For help, look up the Rhinoscript function: RemoveCurveKnot
        """

        return _rsf.remove_curve_knot(self._rhino_id, parameter)


    def reverse(self):
        """
        For help, look up the Rhinoscript function: ReverseCurve
        """

        return _rsf.reverse_curve(self._rhino_id)


    def simplify(self, flags=pythoncom.Empty):
        """
        For help, look up the Rhinoscript function: SimplifyCurve
        """

        return _rsf.simplify_curve(self._rhino_id, flags)



class _CurveRootTest(_ObjectRootTest):

    # Class constructor
    def __init__(self, _rhino_id, _class):
        if _rhino_id==None:
            raise Exception("_rhino_id is required.")
        self._rhino_id = _rhino_id
        self._class = _class

    def is_closable(self, tolerance=pythoncom.Empty):
        """
        For help, look up the Rhinoscript function: IsCurveClosable
        """
        return _rsf.is_curve_closable(self._rhino_id, tolerance)

    def is_closed(self):
        """
        For help, look up the Rhinoscript function: IsCurveClosed
        """
        return _rsf.is_curve_closed(self._rhino_id, pythoncom.Empty)

    def in_plane(self, plane=pythoncom.Empty):
        """
        For help, look up the Rhinoscript function: IsCurveInPlane
        """
        return _rsf.is_curve_in_plane(self._rhino_id, plane)

    def is_linear(self):
        """
        For help, look up the Rhinoscript function: IsCurveLinear
        """
        return _rsf.is_curve_linear(self._rhino_id, pythoncom.Empty)

    def is_periodic(self):
        """
        For help, look up the Rhinoscript function: IsCurvePeriodic
        """
        return _rsf.is_curve_periodic(self._rhino_id, pythoncom.Empty)

    def is_planar(self):
        """
        For help, look up the Rhinoscript function: IsCurvePlanar
        """
        return _rsf.is_curve_planar(self._rhino_id, pythoncom.Empty)

    def is_rational(self):
        """
        For help, look up the Rhinoscript function: IsCurveRational
        """
        return _rsf.is_curve_rational(self._rhino_id, pythoncom.Empty)

    def is_on_crv(self, point):
        """
        For help, look up the Rhinoscript function: IsPointOnCurve
        """
        return _rsf.is_point_on_curve(self._rhino_id, point, pythoncom.Empty)


class _CurveRootType(_ObjectRootType):

    # Class constructor
    def __init__(self, _rhino_id, _class):
        if _rhino_id==None:
            raise Exception("_rhino_id is required.")
        self._rhino_id = _rhino_id
        self._class = _class

    def is_arc(self):
        """
        For help, look up the Rhinoscript function: IsArc
        """
        return _rsf.is_arc(self._rhino_id, pythoncom.Empty)

    def is_circle(self):
        """
        For help, look up the Rhinoscript function: IsCircle
        """
        return _rsf.is_circle(self._rhino_id, pythoncom.Empty)

    def is_crv(self):
        """
        For help, look up the Rhinoscript function: IsCurve
        """
        return _rsf.is_curve(self._rhino_id, pythoncom.Empty)

    def is_ellipse(self):
        """
        For help, look up the Rhinoscript function: IsEllipse
        """
        return _rsf.is_ellipse(self._rhino_id)

    def is_line(self):
        """
        For help, look up the Rhinoscript function: IsLine
        """
        return _rsf.is_line(self._rhino_id, pythoncom.Empty)

    def is_poly_crv(self):
        """
        For help, look up the Rhinoscript function: IsPolyCurve
        """
        return _rsf.is_poly_curve(self._rhino_id, pythoncom.Empty)

    def is_polyline(self):
        """
        For help, look up the Rhinoscript function: IsPolyline
        """
        return _rsf.is_polyline(self._rhino_id, pythoncom.Empty)


class _EllipseFunc(_CurveRootFuncClsd):

    # Class constructor
    def __init__(self, _rhino_id, _class):
        if _rhino_id==None:
            raise Exception("_rhino_id is required.")
        self._rhino_id = _rhino_id
        self._class = _class

    def sub(self, param_0, param_1):
        """
        For help, look up the Rhinoscript function: AddSubCrv
        """
        _rhino_id = _rsf.add_sub_crv(self._rhino_id, param_0, param_1)
        if _rhino_id:
            return p2r.EllipticalArc(_rhino_id)
        else:
            return None

    def offset(self, direction, distance, normal=pythoncom.Empty, style=pythoncom.Empty):
        """
        For help, look up the Rhinoscript function: OffsetCurve
        """
        _rhino_ids = _rsf.offset_curve(self._rhino_id, direction, distance, normal, style)
        return map(lambda i: p2r.EllipticalArc(i), _rhino_ids)

    def split(self, parameters, delete=pythoncom.Empty):
        """
        For help, look up the Rhinoscript function: SplitCurve
        """
        _rhino_ids = _rsf.split_curve(self._rhino_id, parameters, delete)
        return map(lambda i: p2r.EllipticalArc(i), _rhino_ids)

    def trim(self, interval, delete=pythoncom.Empty):
        """
        For help, look up the Rhinoscript function: TrimCurve
        """
        _rhino_id = _rsf.trim_curve(self._rhino_id, interval, delete)
        if _rhino_id:
            return p2r.EllipticalArc(_rhino_id)
        else:
            return None


class _EllipseProp(_CurveRootProp):

    # Class constructor
    def __init__(self, _rhino_id, _class):
        if _rhino_id==None:
            raise Exception("_rhino_id is required.")
        self._rhino_id = _rhino_id
        self._class = _class

    def center_pnt(self):
        """
        For help, look up the Rhinoscript function: EllipseCenterPoint
        """
        return _rsf.ellipse_center_point(self._rhino_id)

    def quad_pnts(self):
        """
        For help, look up the Rhinoscript function: EllipseQuadPoints
        """
        return _rsf.ellipse_quad_points(self._rhino_id)


class _EllipticalArcFunc(_CurveRootFuncOpen):

    # Class constructor
    def __init__(self, _rhino_id, _class):
        if _rhino_id==None:
            raise Exception("_rhino_id is required.")
        self._rhino_id = _rhino_id
        self._class = _class

    def sub(self, param_0, param_1):
        """
        For help, look up the Rhinoscript function: AddSubCrv
        """
        _rhino_id = _rsf.add_sub_crv(self._rhino_id, param_0, param_1)
        if _rhino_id:
            return p2r.EllipticalArc(_rhino_id)
        else:
            return None

    def offset(self, direction, distance, normal=pythoncom.Empty, style=pythoncom.Empty):
        """
        For help, look up the Rhinoscript function: OffsetCurve
        """
        _rhino_ids = _rsf.offset_curve(self._rhino_id, direction, distance, normal, style)
        return map(lambda i: p2r.EllipticalArc(i), _rhino_ids)

    def split(self, parameters, delete=pythoncom.Empty):
        """
        For help, look up the Rhinoscript function: SplitCurve
        """
        _rhino_ids = _rsf.split_curve(self._rhino_id, parameters, delete)
        return map(lambda i: p2r.EllipticalArc(i), _rhino_ids)

    def trim(self, interval, delete=pythoncom.Empty):
        """
        For help, look up the Rhinoscript function: TrimCurve
        """
        _rhino_id = _rsf.trim_curve(self._rhino_id, interval, delete)
        if _rhino_id:
            return p2r.EllipticalArc(_rhino_id)
        else:
            return None


class _LineFunc(_CurveRootFuncOpen):

    # Class constructor
    def __init__(self, _rhino_id, _class):
        if _rhino_id==None:
            raise Exception("_rhino_id is required.")
        self._rhino_id = _rhino_id
        self._class = _class

    def sub(self, param_0, param_1):
        """
        For help, look up the Rhinoscript function: AddSubCrv
        """
        _rhino_id = _rsf.add_sub_crv(self._rhino_id, param_0, param_1)
        if _rhino_id:
            return p2r._util.wrap(_rhino_id)
        else:
            return None

    def offset(self, direction, distance, normal=pythoncom.Empty, style=pythoncom.Empty):
        """
        For help, look up the Rhinoscript function: OffsetCurve
        """
        _rhino_ids = _rsf.offset_curve(self._rhino_id, direction, distance, normal, style)
        return map(lambda i: p2r._util.wrap(i), _rhino_ids)

    def split(self, parameters, delete=pythoncom.Empty):
        """
        For help, look up the Rhinoscript function: SplitCurve
        """
        _rhino_ids = _rsf.split_curve(self._rhino_id, parameters, delete)
        return map(lambda i: p2r._util.wrap(i), _rhino_ids)

    def trim(self, interval, delete=pythoncom.Empty):
        """
        For help, look up the Rhinoscript function: TrimCurve
        """
        _rhino_id = _rsf.trim_curve(self._rhino_id, interval, delete)
        if _rhino_id:
            return p2r._util.wrap(_rhino_id)
        else:
            return None


class _PolylineProp(_CurveRootProp):

    # Class constructor
    def __init__(self, _rhino_id, _class):
        if _rhino_id==None:
            raise Exception("_rhino_id is required.")
        self._rhino_id = _rhino_id
        self._class = _class

    def vertices(self):
        """
        For help, look up the Rhinoscript function: PolylineVertices
        """
        return _rsf.polyline_vertices(self._rhino_id, pythoncom.Empty)


class _SurfaceRoot(_ObjectRoot):

    # Class constructor
    def __init__(self, _rhino_id, _class):
        if _rhino_id==None:
            raise Exception("_rhino_id is required.")
        self._rhino_id = _rhino_id
        self._class = _class


class _SurfaceRootFunc(_ObjectRootFunc):

    # Class constructor
    def __init__(self, _rhino_id, _class):
        if _rhino_id==None:
            raise Exception("_rhino_id is required.")
        self._rhino_id = _rhino_id
        self._class = _class

    def cap_planar_holes(self):
        """
        For help, look up the Rhinoscript function: CapPlanarHoles
        """
        return _rsf.cap_planar_holes(self._rhino_id)

    def closest_pnt(self, point):
        """
        For help, look up the Rhinoscript function: SurfaceClosestPoint
        """
        return _rsf.surface_closest_point(self._rhino_id, point)


class _SurfaceRootFuncClsd(_SurfaceRootFunc):

    # Class constructor
    def __init__(self, _rhino_id, _class):
        if _rhino_id==None:
            raise Exception("_rhino_id is required.")
        self._rhino_id = _rhino_id
        self._class = _class

    def boolean_difference(self, breps, delete=pythoncom.Empty):
        """
        For help, look up the Rhinoscript function: BooleanDifference
        """
        _rhino_ids = _rsf.boolean_difference(self._rhino_id, map(lambda i: i._rhino_id, breps), delete)
        return map(lambda i: p2r._util.wrap(i), _rhino_ids)

    def boolean_intersection(self, breps, delete=pythoncom.Empty):
        """
        For help, look up the Rhinoscript function: BooleanIntersection
        """
        _rhino_ids = _rsf.boolean_intersection(self._rhino_id, map(lambda i: i._rhino_id, breps), delete)
        return map(lambda i: p2r._util.wrap(i), _rhino_ids)

    def boolean_union(self, breps, delete=pythoncom.Empty):
        """
        For help, look up the Rhinoscript function: BooleanUnion
        """
        _rhino_ids = _rsf.boolean_union(map(lambda i: i._rhino_id, breps), delete)
        return map(lambda i: p2r._util.wrap(i), _rhino_ids)

    def brep_closest_pnt(self, point):
        """
        For help, look up the Rhinoscript function: BrepClosestPoint
        """
        return _rsf.brep_closest_point(self._rhino_id, point)

    def intersect_breps(self, brep_1, tolerance=pythoncom.Empty):
        """
        For help, look up the Rhinoscript function: IntersectBreps
        """
        _rhino_ids = _rsf.intersect_breps(self._rhino_id, brep_1, tolerance)
        return map(lambda i: p2r._util.wrap(i), _rhino_ids)

    def split_brep(self, cutter, delete=pythoncom.Empty):
        """
        For help, look up the Rhinoscript function: SplitBrep
        """
        _rhino_ids = _rsf.split_brep(self._rhino_id, cutter, delete)
        return map(lambda i: p2r._util.wrap(i), _rhino_ids)

    def volume(self):
        """
        For help, look up the Rhinoscript function: SurfaceVolume
        """
        return _rsf.surface_volume(self._rhino_id)

    def volume_centroid(self):
        """
        For help, look up the Rhinoscript function: SurfaceVolumeCentroid
        """
        return _rsf.surface_volume_centroid(self._rhino_id)

    def volume_moments(self):
        """
        For help, look up the Rhinoscript function: SurfaceVolumeMoments
        """
        return _rsf.surface_volume_moments(self._rhino_id)


class _SurfaceRootFuncOpen(_SurfaceRootFunc):

    # Class constructor
    def __init__(self, _rhino_id, _class):
        if _rhino_id==None:
            raise Exception("_rhino_id is required.")
        self._rhino_id = _rhino_id
        self._class = _class


class _SurfaceRootMdfy(_ObjectRootMdfy):

    # Class constructor
    def __init__(self, _rhino_id, _class):
        if _rhino_id==None:
            raise Exception("_rhino_id is required.")
        self._rhino_id = _rhino_id
        self._class = _class

    def flip(self, flip=pythoncom.Empty):
        """
        For help, look up the Rhinoscript function: FlipSurface
        """

        return _rsf.flip_surface(self._rhino_id, flip)


    def insert_knot(self, parameter, direction, symmetrical=pythoncom.Empty):
        """
        For help, look up the Rhinoscript function: InsertSurfaceKnot
        """

        return _rsf.insert_surface_knot(self._rhino_id, parameter, direction, symmetrical)


    def rebuild(self, degree=pythoncom.Empty, point_count=pythoncom.Empty):
        """
        For help, look up the Rhinoscript function: RebuildSurface
        """

        return _rsf.rebuild_surface(self._rhino_id, degree, point_count)


    def remove_knot(self, parameter, direction):
        """
        For help, look up the Rhinoscript function: RemoveSurfaceKnot
        """

        return _rsf.remove_surface_knot(self._rhino_id, parameter, direction)


    def reverse(self, direction):
        """
        For help, look up the Rhinoscript function: ReverseSurface
        """

        return _rsf.reverse_surface(self._rhino_id, direction)


    def shrink_trimmed(self):
        """
        For help, look up the Rhinoscript function: ShrinkTrimmedSurface
        """

        return _rsf.shrink_trimmed_surface(self._rhino_id)


    def seam(self, direction, parameter):
        """
        For help, look up the Rhinoscript function: SurfaceSeam
        """

        return _rsf.surface_seam(self._rhino_id, direction, parameter)



class _SurfaceRootProp(_ObjectRootProp):

    # Class constructor
    def __init__(self, _rhino_id, _class):
        if _rhino_id==None:
            raise Exception("_rhino_id is required.")
        self._rhino_id = _rhino_id
        self._class = _class

    def area(self):
        """
        For help, look up the Rhinoscript function: SurfaceArea
        """
        return _rsf.surface_area(self._rhino_id)

    def area_centroid(self):
        """
        For help, look up the Rhinoscript function: SurfaceAreaCentroid
        """
        return _rsf.surface_area_centroid(self._rhino_id)

    def area_moments(self):
        """
        For help, look up the Rhinoscript function: SurfaceAreaMoments
        """
        return _rsf.surface_area_moments(self._rhino_id)

    def contour_pnts(self, start_point, end_point, interval=pythoncom.Empty, angle=pythoncom.Empty):
        """
        For help, look up the Rhinoscript function: SurfaceContourPoints
        """
        return _rsf.surface_contour_points(self._rhino_id, start_point, end_point, interval, angle)

    def curvature(self, parameter):
        """
        For help, look up the Rhinoscript function: SurfaceCurvature
        """
        return _rsf.surface_curvature(self._rhino_id, parameter)

    def curvature_analysis(self):
        """
        For help, look up the Rhinoscript function: SurfaceCurvatureAnalysis
        """
        return _rsf.surface_curvature_analysis(self._rhino_id)

    def degree(self, direction=pythoncom.Empty):
        """
        For help, look up the Rhinoscript function: SurfaceDegree
        """
        return _rsf.surface_degree(self._rhino_id, direction)

    def domain(self, direction):
        """
        For help, look up the Rhinoscript function: SurfaceDomain
        """
        return _rsf.surface_domain(self._rhino_id, direction)

    def edit_pnts(self, return_parameters=pythoncom.Empty, return_all=pythoncom.Empty):
        """
        For help, look up the Rhinoscript function: SurfaceEditPoints
        """
        return _rsf.surface_edit_points(self._rhino_id, return_parameters, return_all)

    def isocurve_density(self, density=pythoncom.Empty):
        """
        For help, look up the Rhinoscript function: SurfaceIsocurveDensity
        """
        return _rsf.surface_isocurve_density(self._rhino_id, density)

    def knot_count(self):
        """
        For help, look up the Rhinoscript function: SurfaceKnotCount
        """
        return _rsf.surface_knot_count(self._rhino_id)

    def knots(self):
        """
        For help, look up the Rhinoscript function: SurfaceKnots
        """
        return _rsf.surface_knots(self._rhino_id)

    def normal(self, parameter):
        """
        For help, look up the Rhinoscript function: SurfaceNormal
        """
        return _rsf.surface_normal(self._rhino_id, parameter)

    def pnt_count(self):
        """
        For help, look up the Rhinoscript function: SurfacePointCount
        """
        return _rsf.surface_point_count(self._rhino_id)

    def pnts(self, return_all=pythoncom.Empty):
        """
        For help, look up the Rhinoscript function: SurfacePoints
        """
        return _rsf.surface_points(self._rhino_id, return_all)

    def weights(self):
        """
        For help, look up the Rhinoscript function: SurfaceWeights
        """
        return _rsf.surface_weights(self._rhino_id)


class _SurfaceRootTest(_ObjectRootTest):

    # Class constructor
    def __init__(self, _rhino_id, _class):
        if _rhino_id==None:
            raise Exception("_rhino_id is required.")
        self._rhino_id = _rhino_id
        self._class = _class

    def is_brep(self):
        """
        For help, look up the Rhinoscript function: IsBrep
        """
        return _rsf.is_brep(self._rhino_id)

    def is_brep_manifold(self):
        """
        For help, look up the Rhinoscript function: IsBrepManifold
        """
        return _rsf.is_brep_manifold(self._rhino_id)

    def is_parameter_on_srf(self, parameter):
        """
        For help, look up the Rhinoscript function: IsParameterOnSurface
        """
        return _rsf.is_parameter_on_surface(self._rhino_id, parameter)

    def is_plane_surface(self):
        """
        For help, look up the Rhinoscript function: IsPlaneSurface
        """
        return _rsf.is_plane_surface(self._rhino_id)

    def is_pnt_in_srf(self, point):
        """
        For help, look up the Rhinoscript function: IsPointInSurface
        """
        return _rsf.is_point_in_surface(self._rhino_id, point)

    def is_pnt_on_srf(self, point):
        """
        For help, look up the Rhinoscript function: IsPointOnSurface
        """
        return _rsf.is_point_on_surface(self._rhino_id, point)

    def is_poly_srf(self):
        """
        For help, look up the Rhinoscript function: IsPolySurface
        """
        return _rsf.is_poly_surface(self._rhino_id)

    def is_poly_surface_closed(self):
        """
        For help, look up the Rhinoscript function: IsPolySurfaceClosed
        """
        return _rsf.is_poly_surface_closed(self._rhino_id)

    def is_poly_srf_planar(self):
        """
        For help, look up the Rhinoscript function: IsPolySurfacePlanar
        """
        return _rsf.is_poly_surface_planar(self._rhino_id)

    def is_srf_closed(self, direction):
        """
        For help, look up the Rhinoscript function: IsSurfaceClosed
        """
        return _rsf.is_surface_closed(self._rhino_id, direction)

    def is_srf_periodic(self, direction):
        """
        For help, look up the Rhinoscript function: IsSurfacePeriodic
        """
        return _rsf.is_surface_periodic(self._rhino_id, direction)

    def is_srf_planar(self, tolerance=pythoncom.Empty):
        """
        For help, look up the Rhinoscript function: IsSurfacePlanar
        """
        return _rsf.is_surface_planar(self._rhino_id, tolerance)

    def is_srf_rational(self):
        """
        For help, look up the Rhinoscript function: IsSurfaceRational
        """
        return _rsf.is_surface_rational(self._rhino_id)

    def is_srf_singular(self, direction):
        """
        For help, look up the Rhinoscript function: IsSurfaceSingular
        """
        return _rsf.is_surface_singular(self._rhino_id, direction)

    def is_srf_trimmed(self):
        """
        For help, look up the Rhinoscript function: IsSurfaceTrimmed
        """
        return _rsf.is_surface_trimmed(self._rhino_id)


class _SurfaceRootType(_ObjectRootTest):

    # Class constructor
    def __init__(self, _rhino_id, _class):
        if _rhino_id==None:
            raise Exception("_rhino_id is required.")
        self._rhino_id = _rhino_id
        self._class = _class

    def is_cone(self):
        """
        For help, look up the Rhinoscript function: IsCone
        """
        return _rsf.is_cone(self._rhino_id)

    def is_cylinder(self):
        """
        For help, look up the Rhinoscript function: IsCylinder
        """
        return _rsf.is_cylinder(self._rhino_id)

    def is_sphere(self):
        """
        For help, look up the Rhinoscript function: IsSphere
        """
        return _rsf.is_sphere(self._rhino_id)

    def is_surface(self):
        """
        For help, look up the Rhinoscript function: IsSurface
        """
        return _rsf.is_surface(self._rhino_id)

    def is_torus(self):
        """
        For help, look up the Rhinoscript function: IsTorus
        """
        return _rsf.is_torus(self._rhino_id)


class _TorusProp(_SurfaceRootProp):

    # Class constructor
    def __init__(self, _rhino_id, _class):
        if _rhino_id==None:
            raise Exception("_rhino_id is required.")
        self._rhino_id = _rhino_id
        self._class = _class

    def torus_definition(self):
        """
        For help, look up the Rhinoscript function: SurfaceTorus
        """
        return _rsf.surface_torus(self._rhino_id)


class Arc(_CurveRoot):

    # Class constructor
    def __init__(self, _rhino_id):
        if _rhino_id==None:
            raise Exception("Use the create... methods to create instances of this class.")
        self._rhino_id = _rhino_id

        self.defm = _ObjectRootDefm(_rhino_id, Arc)
        self.eval = _CurveRootEval(_rhino_id, Arc)
        self.func = _ArcFunc(_rhino_id, Arc)
        self.grps = _ObjectRootGrps(_rhino_id, Arc)
        self.modf = _CurveRootMdfy(_rhino_id, Arc)
        self.mtrl = _ObjectRootMtrl(_rhino_id, Arc)
        self.prop = _ArcProp(_rhino_id, Arc)
        self.rndr = _ObjectRootRndr(_rhino_id, Arc)
        self.stat = _ObjectRootStat(_rhino_id, Arc)
        self.test = _CurveRootTest(_rhino_id, Arc)
        self.trfm = _ObjectRootTrfm(_rhino_id, Arc)
        self.util = _ObjectRootUtil(_rhino_id, Arc)

    @classmethod
    def create(cls, plane, radius, angle):
        """
        For help, look up the Rhinoscript function: AddArc
        """

        _rhino_id = _rsf.add_arc(plane, radius, angle)

        if _rhino_id:
            return Arc(_rhino_id)
        else:
            return None

    @classmethod
    def create_by_3pt(cls, start, end, point):
        """
        For help, look up the Rhinoscript function: AddArc3Pt
        """

        _rhino_id = _rsf.add_arc_3_pt(start, end, point)

        if _rhino_id:
            return Arc(_rhino_id)
        else:
            return None

    @classmethod
    def create_by_fillet(cls, curve_0, curve_1, radius=pythoncom.Empty, point_0=pythoncom.Empty, point_1=pythoncom.Empty):
        """
        For help, look up the Rhinoscript function: AddFilletCurve
        """

        _rhino_id = _rsf.add_fillet_curve(curve_0._rhino_id, curve_1._rhino_id, radius, point_0, point_1)

        if _rhino_id:
            return Arc(_rhino_id)
        else:
            return None


class Box(_SurfaceRoot):

    # Class constructor
    def __init__(self, _rhino_id):
        if _rhino_id==None:
            raise Exception("Use the create... methods to create instances of this class.")
        self._rhino_id = _rhino_id

        self.defm = _ObjectRootDefm(_rhino_id, Box)
        self.eval = _SurfaceRootEval(_rhino_id, Box)
        self.func = _SurfaceRootFuncOorc(_rhino_id, Box)
        self.genr = _SurfaceRootGenr(_rhino_id, Box)
        self.grps = _ObjectRootGrps(_rhino_id, Box)
        self.modf = _SurfaceRootMdfy(_rhino_id, Box)
        self.mtrl = _ObjectRootMtrl(_rhino_id, Box)
        self.prop = _ObjectRootProp(_rhino_id, Box)
        self.rndr = _ObjectRootRndr(_rhino_id, Box)
        self.stat = _ObjectRootStat(_rhino_id, Box)
        self.test = _SurfaceRootTest(_rhino_id, Box)
        self.trfm = _ObjectRootTrfm(_rhino_id, Box)
        self.util = _ObjectRootUtil(_rhino_id, Box)

    @classmethod
    def create(cls, corners):
        """
        For help, look up the Rhinoscript function: AddBox
        """

        _rhino_id = _rsf.add_box(corners)

        if _rhino_id:
            return Box(_rhino_id)
        else:
            return None


class Circle(_CurveRoot):

    # Class constructor
    def __init__(self, _rhino_id):
        if _rhino_id==None:
            raise Exception("Use the create... methods to create instances of this class.")
        self._rhino_id = _rhino_id

        self.defm = _ObjectRootDefm(_rhino_id, Circle)
        self.eval = _CurveRootEval(_rhino_id, Circle)
        self.func = _CircleFunc(_rhino_id, Circle)
        self.grps = _ObjectRootGrps(_rhino_id, Circle)
        self.modf = _CurveRootMdfy(_rhino_id, Circle)
        self.mtrl = _ObjectRootMtrl(_rhino_id, Circle)
        self.prop = _CircleProp(_rhino_id, Circle)
        self.rndr = _ObjectRootRndr(_rhino_id, Circle)
        self.stat = _ObjectRootStat(_rhino_id, Circle)
        self.test = _CurveRootTest(_rhino_id, Circle)
        self.trfm = _ObjectRootTrfm(_rhino_id, Circle)
        self.util = _ObjectRootUtil(_rhino_id, Circle)

    @classmethod
    def create(cls, plane, radius):
        """
        For help, look up the Rhinoscript function: AddCircle
        """

        _rhino_id = _rsf.add_circle(plane, radius)

        if _rhino_id:
            return Circle(_rhino_id)
        else:
            return None

    @classmethod
    def create_by_3pt(cls, first, second, third):
        """
        For help, look up the Rhinoscript function: AddCircle3Pt
        """

        _rhino_id = _rsf.add_circle_3_pt(first, second, third)

        if _rhino_id:
            return Circle(_rhino_id)
        else:
            return None


class Cone(_SurfaceRoot):

    # Class constructor
    def __init__(self, _rhino_id):
        if _rhino_id==None:
            raise Exception("Use the create... methods to create instances of this class.")
        self._rhino_id = _rhino_id

        self.defm = _ObjectRootDefm(_rhino_id, Cone)
        self.eval = _SurfaceRootEval(_rhino_id, Cone)
        self.func = _SurfaceRootFuncOorc(_rhino_id, Cone)
        self.genr = _SurfaceRootGenr(_rhino_id, Cone)
        self.grps = _ObjectRootGrps(_rhino_id, Cone)
        self.modf = _SurfaceRootMdfy(_rhino_id, Cone)
        self.mtrl = _ObjectRootMtrl(_rhino_id, Cone)
        self.prop = _ConeProp(_rhino_id, Cone)
        self.rndr = _ObjectRootRndr(_rhino_id, Cone)
        self.stat = _ObjectRootStat(_rhino_id, Cone)
        self.test = _SurfaceRootTest(_rhino_id, Cone)
        self.trfm = _ObjectRootTrfm(_rhino_id, Cone)
        self.util = _ObjectRootUtil(_rhino_id, Cone)

    @classmethod
    def create(cls, base, height, radius, cap=pythoncom.Empty):
        """
        For help, look up the Rhinoscript function: AddCone
        """

        _rhino_id = _rsf.add_cone(base, height, radius, cap)

        if _rhino_id:
            return Cone(_rhino_id)
        else:
            return None

    @classmethod
    def create_by_plane(cls, plane, height, radius, cap=pythoncom.Empty):
        """
        For help, look up the Rhinoscript function: AddCone2
        """

        _rhino_id = _rsf.add_cone_2(plane, height, radius, cap)

        if _rhino_id:
            return Cone(_rhino_id)
        else:
            return None


class Cylinder(_SurfaceRoot):

    # Class constructor
    def __init__(self, _rhino_id):
        if _rhino_id==None:
            raise Exception("Use the create... methods to create instances of this class.")
        self._rhino_id = _rhino_id

        self.defm = _ObjectRootDefm(_rhino_id, Cylinder)
        self.eval = _SurfaceRootEval(_rhino_id, Cylinder)
        self.func = _SurfaceRootFuncOorc(_rhino_id, Cylinder)
        self.genr = _SurfaceRootGenr(_rhino_id, Cylinder)
        self.grps = _ObjectRootGrps(_rhino_id, Cylinder)
        self.modf = _SurfaceRootMdfy(_rhino_id, Cylinder)
        self.mtrl = _ObjectRootMtrl(_rhino_id, Cylinder)
        self.prop = _CylinderProp(_rhino_id, Cylinder)
        self.rndr = _ObjectRootRndr(_rhino_id, Cylinder)
        self.stat = _ObjectRootStat(_rhino_id, Cylinder)
        self.test = _SurfaceRootTest(_rhino_id, Cylinder)
        self.trfm = _ObjectRootTrfm(_rhino_id, Cylinder)
        self.util = _ObjectRootUtil(_rhino_id, Cylinder)

    @classmethod
    def create(cls, base, height, radius, cap=pythoncom.Empty):
        """
        For help, look up the Rhinoscript function: AddCylinder
        """

        _rhino_id = _rsf.add_cylinder(base, height, radius, cap)

        if _rhino_id:
            return Cylinder(_rhino_id)
        else:
            return None

    @classmethod
    def create_by_plane(cls, plane, height, radius, cap=pythoncom.Empty):
        """
        For help, look up the Rhinoscript function: AddCylinder2
        """

        _rhino_id = _rsf.add_cylinder_2(plane, height, radius, cap)

        if _rhino_id:
            return Cylinder(_rhino_id)
        else:
            return None


class Ellipse(_CurveRoot):

    # Class constructor
    def __init__(self, _rhino_id):
        if _rhino_id==None:
            raise Exception("Use the create... methods to create instances of this class.")
        self._rhino_id = _rhino_id

        self.defm = _ObjectRootDefm(_rhino_id, Ellipse)
        self.eval = _CurveRootEval(_rhino_id, Ellipse)
        self.func = _EllipseFunc(_rhino_id, Ellipse)
        self.grps = _ObjectRootGrps(_rhino_id, Ellipse)
        self.modf = _CurveRootMdfy(_rhino_id, Ellipse)
        self.mtrl = _ObjectRootMtrl(_rhino_id, Ellipse)
        self.prop = _EllipseProp(_rhino_id, Ellipse)
        self.rndr = _ObjectRootRndr(_rhino_id, Ellipse)
        self.stat = _ObjectRootStat(_rhino_id, Ellipse)
        self.test = _CurveRootTest(_rhino_id, Ellipse)
        self.trfm = _ObjectRootTrfm(_rhino_id, Ellipse)
        self.util = _ObjectRootUtil(_rhino_id, Ellipse)

    @classmethod
    def create(cls, plane, x_radius, y_radius):
        """
        For help, look up the Rhinoscript function: AddEllipse
        """

        _rhino_id = _rsf.add_ellipse(plane, x_radius, y_radius)

        if _rhino_id:
            return Ellipse(_rhino_id)
        else:
            return None

    @classmethod
    def create_by_3pt(cls, center, second, third):
        """
        For help, look up the Rhinoscript function: AddEllipse3Pt
        """

        _rhino_id = _rsf.add_ellipse_3_pt(center, second, third)

        if _rhino_id:
            return Ellipse(_rhino_id)
        else:
            return None


class EllipticalArc(_CurveRoot):

    # Class constructor
    def __init__(self, _rhino_id):
        if _rhino_id==None:
            raise Exception("Use the create... methods to create instances of this class.")
        self._rhino_id = _rhino_id

        self.defm = _ObjectRootDefm(_rhino_id, EllipticalArc)
        self.eval = _CurveRootEval(_rhino_id, EllipticalArc)
        self.func = _EllipticalArcFunc(_rhino_id, EllipticalArc)
        self.grps = _ObjectRootGrps(_rhino_id, EllipticalArc)
        self.modf = _CurveRootMdfy(_rhino_id, EllipticalArc)
        self.mtrl = _ObjectRootMtrl(_rhino_id, EllipticalArc)
        self.prop = _ObjectRootProp(_rhino_id, EllipticalArc)
        self.rndr = _ObjectRootRndr(_rhino_id, EllipticalArc)
        self.stat = _ObjectRootStat(_rhino_id, EllipticalArc)
        self.test = _CurveRootTest(_rhino_id, EllipticalArc)
        self.trfm = _ObjectRootTrfm(_rhino_id, EllipticalArc)
        self.util = _ObjectRootUtil(_rhino_id, EllipticalArc)


class GenericCurve(_CurveRoot):

    # Class constructor
    def __init__(self, _rhino_id):
        if _rhino_id==None:
            raise Exception("Use the create... methods to create instances of this class.")
        self._rhino_id = _rhino_id

        self.defm = _ObjectRootDefm(_rhino_id, GenericCurve)
        self.eval = _CurveRootEval(_rhino_id, GenericCurve)
        self.func = _CurveRootType(_rhino_id, GenericCurve)
        self.grps = _ObjectRootGrps(_rhino_id, GenericCurve)
        self.mdfy = _CurveRootMdfy(_rhino_id, GenericCurve)
        self.mtrl = _ObjectRootMtrl(_rhino_id, GenericCurve)
        self.prop = _ObjectRootProp(_rhino_id, GenericCurve)
        self.rndr = _ObjectRootRndr(_rhino_id, GenericCurve)
        self.stat = _ObjectRootStat(_rhino_id, GenericCurve)
        self.test = _CurveRootTest(_rhino_id, GenericCurve)
        self.trfm = _ObjectRootTrfm(_rhino_id, GenericCurve)
        self.util = _ObjectRootUtil(_rhino_id, GenericCurve)


class Line(_CurveRoot):

    # Class constructor
    def __init__(self, _rhino_id):
        if _rhino_id==None:
            raise Exception("Use the create... methods to create instances of this class.")
        self._rhino_id = _rhino_id

        self.defm = _ObjectRootDefm(_rhino_id, Line)
        self.eval = _CurveRootEval(_rhino_id, Line)
        self.func = _LineFunc(_rhino_id, Line)
        self.grps = _ObjectRootGrps(_rhino_id, Line)
        self.modf = _CurveRootMdfy(_rhino_id, Line)
        self.mtrl = _ObjectRootMtrl(_rhino_id, Line)
        self.prop = _ObjectRootProp(_rhino_id, Line)
        self.rndr = _ObjectRootRndr(_rhino_id, Line)
        self.stat = _ObjectRootStat(_rhino_id, Line)
        self.test = _CurveRootTest(_rhino_id, Line)
        self.trfm = _ObjectRootTrfm(_rhino_id, Line)
        self.util = _ObjectRootUtil(_rhino_id, Line)

    @classmethod
    def create(cls, start, end):
        """
        For help, look up the Rhinoscript function: AddLine
        """

        _rhino_id = _rsf.add_line(start, end)

        if _rhino_id:
            return Line(_rhino_id)
        else:
            return None


class NurbsCurve(_CurveRoot):

    # Class constructor
    def __init__(self, _rhino_id):
        if _rhino_id==None:
            raise Exception("Use the create... methods to create instances of this class.")
        self._rhino_id = _rhino_id

        self.defm = _ObjectRootDefm(_rhino_id, NurbsCurve)
        self.eval = _CurveRootEval(_rhino_id, NurbsCurve)
        self.func = _NurbsCurveFunc(_rhino_id, NurbsCurve)
        self.grps = _ObjectRootGrps(_rhino_id, NurbsCurve)
        self.modf = _CurveRootMdfy(_rhino_id, NurbsCurve)
        self.mtrl = _ObjectRootMtrl(_rhino_id, NurbsCurve)
        self.prop = _ObjectRootProp(_rhino_id, NurbsCurve)
        self.rndr = _ObjectRootRndr(_rhino_id, NurbsCurve)
        self.stat = _ObjectRootStat(_rhino_id, NurbsCurve)
        self.test = _CurveRootTest(_rhino_id, NurbsCurve)
        self.trfm = _ObjectRootTrfm(_rhino_id, NurbsCurve)
        self.util = _ObjectRootUtil(_rhino_id, NurbsCurve)

    @classmethod
    def create_by_pnts(cls, points, degree=pythoncom.Empty):
        """
        For help, look up the Rhinoscript function: AddCurve
        """

        _rhino_id = _rsf.add_curve(points, degree)

        if _rhino_id:
            return NurbsCurve(_rhino_id)
        else:
            return None

    @classmethod
    def create_interp_crv_on_srf(cls, surface, points):
        """
        For help, look up the Rhinoscript function: AddInterpCrvOnSrf
        """

        _rhino_id = _rsf.add_interp_crv_on_srf(surface._rhino_id, points)

        if _rhino_id:
            return NurbsCurve(_rhino_id)
        else:
            return None

    @classmethod
    def create_interp_crv_on_srf_uv(cls, surface, points):
        """
        For help, look up the Rhinoscript function: AddInterpCrvOnSrfUV
        """

        _rhino_id = _rsf.add_interp_crv_on_srf_u_v(surface._rhino_id, points)

        if _rhino_id:
            return NurbsCurve(_rhino_id)
        else:
            return None

    @classmethod
    def create_interp_crv(cls, points, degree=pythoncom.Empty, knot_style=pythoncom.Empty, start_tan=pythoncom.Empty, end_tan=pythoncom.Empty):
        """
        For help, look up the Rhinoscript function: AddInterpCurve
        """

        _rhino_id = _rsf.add_interp_curve(points, degree, knot_style, start_tan, end_tan)

        if _rhino_id:
            return NurbsCurve(_rhino_id)
        else:
            return None

    @classmethod
    def create_interp_crv_ex(cls, points, degree=pythoncom.Empty, knot_style=pythoncom.Empty, sharp=pythoncom.Empty, start_tangent=pythoncom.Empty, end_tangent=pythoncom.Empty):
        """
        For help, look up the Rhinoscript function: AddInterpCurveEx
        """

        _rhino_id = _rsf.add_interp_curve_ex(points, degree, knot_style, sharp, start_tangent, end_tangent)

        if _rhino_id:
            return NurbsCurve(_rhino_id)
        else:
            return None

    @classmethod
    def create(cls, points, knots, degree, weights=pythoncom.Empty):
        """
        For help, look up the Rhinoscript function: AddNurbsCurve
        """

        _rhino_id = _rsf.add_nurbs_curve(points, knots, degree, weights)

        if _rhino_id:
            return NurbsCurve(_rhino_id)
        else:
            return None

    @classmethod
    def create_by_srf_contour(cls, surface, start_point, end_point, interval=pythoncom.Empty):
        """
        For help, look up the Rhinoscript function: AddSrfContourCrvs
        """

        _rhino_id = _rsf.add_srf_contour_crvs(surface._rhino_id, start_point, end_point, interval)


        return map(lambda i: NurbsCurve(i), _rhino_id)


    @classmethod
    def create_by_srf_contour_cut_plane(cls, surface, plane, interval=pythoncom.Empty):
        """
        For help, look up the Rhinoscript function: AddSrfContourCrvs2
        """

        _rhino_id = _rsf.add_srf_contour_crvs_2(surface._rhino_id, plane, interval)


        return map(lambda i: NurbsCurve(i), _rhino_id)


    @classmethod
    def create_by_srf_section(cls, surface, plane):
        """
        For help, look up the Rhinoscript function: AddSrfSectionCrvs
        """

        _rhino_id = _rsf.add_srf_section_crvs(surface._rhino_id, plane)


        return map(lambda i: NurbsCurve(i), _rhino_id)


    @classmethod
    def create_by_srf_edge(cls, surface, select=pythoncom.Empty):
        """
        For help, look up the Rhinoscript function: DuplicateEdgeCurves
        """

        _rhino_id = _rsf.duplicate_edge_curves(surface._rhino_id, select)


        return map(lambda i: NurbsCurve(i), _rhino_id)


    @classmethod
    def create_by_srf_border(cls, surface):
        """
        For help, look up the Rhinoscript function: DuplicateSurfaceBorder
        """

        _rhino_id = _rsf.duplicate_surface_border(surface._rhino_id)


        return map(lambda i: NurbsCurve(i), _rhino_id)


    @classmethod
    def create_by_srf_iso_curve(cls, surface, parameter, dir):
        """
        For help, look up the Rhinoscript function: ExtractIsoCurve
        """

        _rhino_id = _rsf.extract_iso_curve(surface._rhino_id, parameter, dir)


        return map(lambda i: NurbsCurve(i), _rhino_id)


    @classmethod
    def create_by_projection_to_mesh(cls, curves, meshes, direction):
        """
        For help, look up the Rhinoscript function: ProjectCurveToMesh
        """

        _rhino_id = _rsf.project_curve_to_mesh(map(lambda i: i._rhino_id, curves), meshes, direction)


        return map(lambda i: NurbsCurve(i), _rhino_id)


    @classmethod
    def create_by_projection_to_srf(cls, curve, surfaces, direction):
        """
        For help, look up the Rhinoscript function: ProjectCurveToSurface
        """

        _rhino_id = _rsf.project_curve_to_surface(curve._rhino_id, surfaces, direction)


        return map(lambda i: NurbsCurve(i), _rhino_id)


    @classmethod
    def create_by_srf_pull(cls, surface, curve, delete=pythoncom.Empty):
        """
        For help, look up the Rhinoscript function: PullCurve
        """

        _rhino_id = _rsf.pull_curve(surface._rhino_id, curve._rhino_id, delete)


        return map(lambda i: NurbsCurve(i), _rhino_id)


    @classmethod
    def create_by_srf_short_path(cls, surface, start, end):
        """
        For help, look up the Rhinoscript function: ShortPath
        """

        _rhino_id = _rsf.short_path(surface._rhino_id, start, end)

        if _rhino_id:
            return NurbsCurve(_rhino_id)
        else:
            return None

    @classmethod
    def create_by_srf_principal_curvature(cls, surface, point):
        """
        For help, look up the Rhinoscript function: SurfacePrincipalCurvature
        """

        _rhino_id = _rsf.surface_principal_curvature(surface._rhino_id, point)


        return map(lambda i: NurbsCurve(i), _rhino_id)



class NurbsSurface(_SurfaceRoot):

    # Class constructor
    def __init__(self, _rhino_id):
        if _rhino_id==None:
            raise Exception("Use the create... methods to create instances of this class.")
        self._rhino_id = _rhino_id

        self.defm = _ObjectRootDefm(_rhino_id, NurbsSurface)
        self.eval = _SurfaceRootEval(_rhino_id, NurbsSurface)
        self.func = _SurfaceRootFuncOorc(_rhino_id, NurbsSurface)
        self.genr = _SurfaceRootGenr(_rhino_id, NurbsSurface)
        self.grps = _ObjectRootGrps(_rhino_id, NurbsSurface)
        self.modf = _SurfaceRootMdfy(_rhino_id, NurbsSurface)
        self.mtrl = _ObjectRootMtrl(_rhino_id, NurbsSurface)
        self.prop = _ObjectRootProp(_rhino_id, NurbsSurface)
        self.rndr = _ObjectRootRndr(_rhino_id, NurbsSurface)
        self.stat = _ObjectRootStat(_rhino_id, NurbsSurface)
        self.test = _SurfaceRootTest(_rhino_id, NurbsSurface)
        self.trfm = _ObjectRootTrfm(_rhino_id, NurbsSurface)
        self.util = _ObjectRootUtil(_rhino_id, NurbsSurface)

    @classmethod
    def create_by_cut_plane(cls, objects, start_point, end_point, normal=pythoncom.Empty):
        """
        For help, look up the Rhinoscript function: AddCutPlane
        """

        _rhino_id = _rsf.add_cut_plane(map(lambda i: i._rhino_id, objects), start_point, end_point, normal)

        if _rhino_id:
            return NurbsSurface(_rhino_id)
        else:
            return None

    @classmethod
    def create_by_edge(cls, objects):
        """
        For help, look up the Rhinoscript function: AddEdgeSrf
        """

        _rhino_id = _rsf.add_edge_srf(map(lambda i: i._rhino_id, objects))

        if _rhino_id:
            return NurbsSurface(_rhino_id)
        else:
            return None

    @classmethod
    def create_by_loft(cls, objects, start_pt=pythoncom.Empty, end_pt=pythoncom.Empty, type=pythoncom.Empty, style=pythoncom.Empty, value=pythoncom.Empty, closed=pythoncom.Empty):
        """
        For help, look up the Rhinoscript function: AddLoftSrf
        """

        _rhino_id = _rsf.add_loft_srf(map(lambda i: i._rhino_id, objects), start_pt, end_pt, type, style, value, closed)

        if _rhino_id:
            return NurbsSurface(_rhino_id)
        else:
            return None

    @classmethod
    def create(cls, point_count, points, knots_u, knots_v, degree, weights):
        """
        For help, look up the Rhinoscript function: AddNurbsSurface
        """

        _rhino_id = _rsf.add_nurbs_surface(point_count, points, knots_u, knots_v, degree, weights)

        if _rhino_id:
            return NurbsSurface(_rhino_id)
        else:
            return None

    @classmethod
    def create_by_planar_crv(cls, objects):
        """
        For help, look up the Rhinoscript function: AddPlanarSrf
        """

        _rhino_id = _rsf.add_planar_srf(map(lambda i: i._rhino_id, objects))


        return map(lambda i: NurbsSurface(i), _rhino_id)


    @classmethod
    def create_by_rail_rev(cls, profile, rail, axis):
        """
        For help, look up the Rhinoscript function: AddRailRevSrf
        """

        _rhino_id = _rsf.add_rail_rev_srf(profile._rhino_id, rail._rhino_id, axis)

        if _rhino_id:
            return NurbsSurface(_rhino_id)
        else:
            return None

    @classmethod
    def create_by_rev(cls, profile, axis, start_angle=pythoncom.Empty, end_angle=pythoncom.Empty):
        """
        For help, look up the Rhinoscript function: AddRevSrf
        """

        _rhino_id = _rsf.add_rev_srf(profile._rhino_id, axis, start_angle, end_angle)

        if _rhino_id:
            return NurbsSurface(_rhino_id)
        else:
            return None

    @classmethod
    def create_by_control_pt_grid(cls, count, points, degree=pythoncom.Empty):
        """
        For help, look up the Rhinoscript function: AddSrfControlPtGrid
        """

        _rhino_id = _rsf.add_srf_control_pt_grid(count, points, degree)

        if _rhino_id:
            return NurbsSurface(_rhino_id)
        else:
            return None

    @classmethod
    def create_by_corner_pts(cls, points):
        """
        For help, look up the Rhinoscript function: AddSrfPt
        """

        _rhino_id = _rsf.add_srf_pt(points)

        if _rhino_id:
            return NurbsSurface(_rhino_id)
        else:
            return None

    @classmethod
    def create_by_pt_grid(cls, count, points, degree=pythoncom.Empty, closed=pythoncom.Empty):
        """
        For help, look up the Rhinoscript function: AddSrfPtGrid
        """

        _rhino_id = _rsf.add_srf_pt_grid(count, points, degree, closed)

        if _rhino_id:
            return NurbsSurface(_rhino_id)
        else:
            return None

    @classmethod
    def create_by_sweep_1(cls, rail, shapes, start_pt=pythoncom.Empty, end_pt=pythoncom.Empty, closed=pythoncom.Empty, style=pythoncom.Empty, style_arg=pythoncom.Empty, simplify=pythoncom.Empty, simplify_arg=pythoncom.Empty):
        """
        For help, look up the Rhinoscript function: AddSweep1
        """

        _rhino_id = _rsf.add_sweep_1(rail._rhino_id, map(lambda i: i._rhino_id, shapes), start_pt, end_pt, closed, style, style_arg, simplify, simplify_arg)


        return map(lambda i: NurbsSurface(i), _rhino_id)


    @classmethod
    def create_by_sweep_2(cls, rails, shapes, start_pt=pythoncom.Empty, end_pt=pythoncom.Empty, closed=pythoncom.Empty, simple_sweep=pythoncom.Empty, maintain_height=pythoncom.Empty, simplify=pythoncom.Empty, simplify_arg=pythoncom.Empty):
        """
        For help, look up the Rhinoscript function: AddSweep2
        """

        _rhino_id = _rsf.add_sweep_2(map(lambda i: i._rhino_id, rails), map(lambda i: i._rhino_id, shapes), start_pt, end_pt, closed, simple_sweep, maintain_height, simplify, simplify_arg)


        return map(lambda i: NurbsSurface(i), _rhino_id)


    @classmethod
    def create_by_extrude_crv(cls, curve, path):
        """
        For help, look up the Rhinoscript function: ExtrudeCurve
        """

        _rhino_id = _rsf.extrude_curve(curve._rhino_id, path)

        if _rhino_id:
            return NurbsSurface(_rhino_id)
        else:
            return None

    @classmethod
    def create_by_extrude_crv_pnt(cls, curve, point):
        """
        For help, look up the Rhinoscript function: ExtrudeCurvePoint
        """

        _rhino_id = _rsf.extrude_curve_point(curve._rhino_id, point)

        if _rhino_id:
            return NurbsSurface(_rhino_id)
        else:
            return None

    @classmethod
    def create_by_extrude_crv_straight(cls, curve, start_point, end_point):
        """
        For help, look up the Rhinoscript function: ExtrudeCurveStraight
        """

        _rhino_id = _rsf.extrude_curve_straight(curve._rhino_id, start_point, end_point)

        if _rhino_id:
            return NurbsSurface(_rhino_id)
        else:
            return None

    @classmethod
    def create_by_extrude_crv_tapered(cls, curve, distance, direction, base_point, angle, corner_type=pythoncom.Empty):
        """
        For help, look up the Rhinoscript function: ExtrudeCurveTapered
        """

        _rhino_id = _rsf.extrude_curve_tapered(curve._rhino_id, distance, direction, base_point, angle, corner_type)


        return map(lambda i: NurbsSurface(i), _rhino_id)



class PlaneSurface(_SurfaceRoot):

    # Class constructor
    def __init__(self, _rhino_id):
        if _rhino_id==None:
            raise Exception("Use the create... methods to create instances of this class.")
        self._rhino_id = _rhino_id

        self.defm = _ObjectRootDefm(_rhino_id, PlaneSurface)
        self.eval = _SurfaceRootEval(_rhino_id, PlaneSurface)
        self.func = _SurfaceRootFuncOorc(_rhino_id, PlaneSurface)
        self.genr = _SurfaceRootGenr(_rhino_id, PlaneSurface)
        self.grps = _ObjectRootGrps(_rhino_id, PlaneSurface)
        self.modf = _SurfaceRootMdfy(_rhino_id, PlaneSurface)
        self.mtrl = _ObjectRootMtrl(_rhino_id, PlaneSurface)
        self.prop = _ObjectRootProp(_rhino_id, PlaneSurface)
        self.rndr = _ObjectRootRndr(_rhino_id, PlaneSurface)
        self.stat = _ObjectRootStat(_rhino_id, PlaneSurface)
        self.test = _SurfaceRootTest(_rhino_id, PlaneSurface)
        self.trfm = _ObjectRootTrfm(_rhino_id, PlaneSurface)
        self.util = _ObjectRootUtil(_rhino_id, PlaneSurface)

    @classmethod
    def create(cls, plane, d_u, d_v):
        """
        For help, look up the Rhinoscript function: AddPlaneSurface
        """

        _rhino_id = _rsf.add_plane_surface(plane, d_u, d_v)

        if _rhino_id:
            return PlaneSurface(_rhino_id)
        else:
            return None


class PolySurface(_SurfaceRoot):

    # Class constructor
    def __init__(self, _rhino_id):
        if _rhino_id==None:
            raise Exception("Use the create... methods to create instances of this class.")
        self._rhino_id = _rhino_id

        self.defm = _ObjectRootDefm(_rhino_id, PolySurface)
        self.eval = _SurfaceRootEval(_rhino_id, PolySurface)
        self.func = _SurfaceRootFuncOorc(_rhino_id, PolySurface)
        self.grps = _ObjectRootGrps(_rhino_id, PolySurface)
        self.modf = _SurfaceRootMdfy(_rhino_id, PolySurface)
        self.mtrl = _ObjectRootMtrl(_rhino_id, PolySurface)
        self.prop = _PolySurfaceProp(_rhino_id, PolySurface)
        self.rndr = _ObjectRootRndr(_rhino_id, PolySurface)
        self.stat = _ObjectRootStat(_rhino_id, PolySurface)
        self.test = _SurfaceRootTest(_rhino_id, PolySurface)
        self.trfm = _ObjectRootTrfm(_rhino_id, PolySurface)
        self.util = _ObjectRootUtil(_rhino_id, PolySurface)

    @classmethod
    def create_by_srf_extrude(cls, surface, curve, cap=pythoncom.Empty):
        """
        For help, look up the Rhinoscript function: ExtrudeSurface
        """

        _rhino_id = _rsf.extrude_surface(surface._rhino_id, curve, cap)

        if _rhino_id:
            return PolySurface(_rhino_id)
        else:
            return None

    @classmethod
    def create_by_srf_join(cls, surfaces, delete=pythoncom.Empty):
        """
        For help, look up the Rhinoscript function: JoinSurfaces
        """

        _rhino_id = _rsf.join_surfaces(map(lambda i: i._rhino_id, surfaces), delete)

        if _rhino_id:
            return PolySurface(_rhino_id)
        else:
            return None


class Polyline(_CurveRoot):

    # Class constructor
    def __init__(self, _rhino_id):
        if _rhino_id==None:
            raise Exception("Use the create... methods to create instances of this class.")
        self._rhino_id = _rhino_id

        self.defm = _ObjectRootDefm(_rhino_id, Polyline)
        self.eval = _CurveRootEval(_rhino_id, Polyline)
        self.func = _PolylineFunc(_rhino_id, Polyline)
        self.grps = _ObjectRootGrps(_rhino_id, Polyline)
        self.modf = _CurveRootMdfy(_rhino_id, Polyline)
        self.mtrl = _ObjectRootMtrl(_rhino_id, Polyline)
        self.prop = _PolylineProp(_rhino_id, Polyline)
        self.rndr = _ObjectRootRndr(_rhino_id, Polyline)
        self.stat = _ObjectRootStat(_rhino_id, Polyline)
        self.test = _CurveRootTest(_rhino_id, Polyline)
        self.trfm = _ObjectRootTrfm(_rhino_id, Polyline)
        self.util = _ObjectRootUtil(_rhino_id, Polyline)

    @classmethod
    def create(cls, points):
        """
        For help, look up the Rhinoscript function: AddPolyline
        """

        _rhino_id = _rsf.add_polyline(points)

        if _rhino_id:
            return Polyline(_rhino_id)
        else:
            return None

    @classmethod
    def create_by_crv(cls, curve, angle_tolerance=pythoncom.Empty, tolerance=pythoncom.Empty, delete_input=pythoncom.Empty):
        """
        For help, look up the Rhinoscript function: ConvertCurveToPolyline
        """

        _rhino_id = _rsf.convert_curve_to_polyline(curve._rhino_id, angle_tolerance, tolerance, delete_input)

        if _rhino_id:
            return Polyline(_rhino_id)
        else:
            return None


class Sphere(_SurfaceRoot):

    # Class constructor
    def __init__(self, _rhino_id):
        if _rhino_id==None:
            raise Exception("Use the create... methods to create instances of this class.")
        self._rhino_id = _rhino_id

        self.defm = _ObjectRootDefm(_rhino_id, Sphere)
        self.eval = _SurfaceRootEval(_rhino_id, Sphere)
        self.func = _SurfaceRootFuncOorc(_rhino_id, Sphere)
        self.genr = _SurfaceRootGenr(_rhino_id, Sphere)
        self.grps = _ObjectRootGrps(_rhino_id, Sphere)
        self.modf = _SurfaceRootMdfy(_rhino_id, Sphere)
        self.mtrl = _ObjectRootMtrl(_rhino_id, Sphere)
        self.prop = _SphereProp(_rhino_id, Sphere)
        self.rndr = _ObjectRootRndr(_rhino_id, Sphere)
        self.stat = _ObjectRootStat(_rhino_id, Sphere)
        self.test = _SurfaceRootTest(_rhino_id, Sphere)
        self.trfm = _ObjectRootTrfm(_rhino_id, Sphere)
        self.util = _ObjectRootUtil(_rhino_id, Sphere)

    @classmethod
    def create(cls, center, radius):
        """
        For help, look up the Rhinoscript function: AddSphere
        """

        _rhino_id = _rsf.add_sphere(center, radius)

        if _rhino_id:
            return Sphere(_rhino_id)
        else:
            return None

    @classmethod
    def create_by_plane(cls, center, radius):
        """
        For help, look up the Rhinoscript function: AddSphere2
        """

        _rhino_id = _rsf.add_sphere_2(center, radius)

        if _rhino_id:
            return Sphere(_rhino_id)
        else:
            return None


class Torus(_SurfaceRoot):

    # Class constructor
    def __init__(self, _rhino_id):
        if _rhino_id==None:
            raise Exception("Use the create... methods to create instances of this class.")
        self._rhino_id = _rhino_id

        self.defm = _ObjectRootDefm(_rhino_id, Torus)
        self.eval = _SurfaceRootEval(_rhino_id, Torus)
        self.func = _SurfaceRootFuncOorc(_rhino_id, Torus)
        self.genr = _SurfaceRootGenr(_rhino_id, Torus)
        self.grps = _ObjectRootGrps(_rhino_id, Torus)
        self.modf = _SurfaceRootMdfy(_rhino_id, Torus)
        self.mtrl = _ObjectRootMtrl(_rhino_id, Torus)
        self.prop = _TorusProp(_rhino_id, Torus)
        self.rndr = _ObjectRootRndr(_rhino_id, Torus)
        self.stat = _ObjectRootStat(_rhino_id, Torus)
        self.test = _SurfaceRootTest(_rhino_id, Torus)
        self.trfm = _ObjectRootTrfm(_rhino_id, Torus)
        self.util = _ObjectRootUtil(_rhino_id, Torus)

    @classmethod
    def create(cls, base, major_radius, minor_radius, direction=pythoncom.Empty):
        """
        For help, look up the Rhinoscript function: AddTorus
        """

        _rhino_id = _rsf.add_torus(base, major_radius, minor_radius, direction)

        if _rhino_id:
            return Torus(_rhino_id)
        else:
            return None

    @classmethod
    def create_by_plane(cls, plane, major_radius, minor_radius):
        """
        For help, look up the Rhinoscript function: AddTorus2
        """

        _rhino_id = _rsf.add_torus_2(plane, major_radius, minor_radius)

        if _rhino_id:
            return Torus(_rhino_id)
        else:
            return None


class _ArcFunc(_CurveRootFuncOpen):

    # Class constructor
    def __init__(self, _rhino_id, _class):
        if _rhino_id==None:
            raise Exception("_rhino_id is required.")
        self._rhino_id = _rhino_id
        self._class = _class

    def sub(self, param_0, param_1):
        """
        For help, look up the Rhinoscript function: AddSubCrv
        """
        _rhino_id = _rsf.add_sub_crv(self._rhino_id, param_0, param_1)
        if _rhino_id:
            return p2r.Arc(_rhino_id)
        else:
            return None

    def offset(self, direction, distance, normal=pythoncom.Empty, style=pythoncom.Empty):
        """
        For help, look up the Rhinoscript function: OffsetCurve
        """
        _rhino_ids = _rsf.offset_curve(self._rhino_id, direction, distance, normal, style)
        return map(lambda i: p2r.Arc(i), _rhino_ids)

    def split(self, parameters, delete=pythoncom.Empty):
        """
        For help, look up the Rhinoscript function: SplitCurve
        """
        _rhino_ids = _rsf.split_curve(self._rhino_id, parameters, delete)
        return map(lambda i: p2r.Arc(i), _rhino_ids)

    def trim(self, interval, delete=pythoncom.Empty):
        """
        For help, look up the Rhinoscript function: TrimCurve
        """
        _rhino_id = _rsf.trim_curve(self._rhino_id, interval, delete)
        if _rhino_id:
            return p2r.Arc(_rhino_id)
        else:
            return None


class _CircleFunc(_CurveRootFuncClsd):

    # Class constructor
    def __init__(self, _rhino_id, _class):
        if _rhino_id==None:
            raise Exception("_rhino_id is required.")
        self._rhino_id = _rhino_id
        self._class = _class

    def sub(self, param_0, param_1):
        """
        For help, look up the Rhinoscript function: AddSubCrv
        """
        _rhino_id = _rsf.add_sub_crv(self._rhino_id, param_0, param_1)
        if _rhino_id:
            return p2r.Arc(_rhino_id)
        else:
            return None

    def offset(self, direction, distance, normal=pythoncom.Empty, style=pythoncom.Empty):
        """
        For help, look up the Rhinoscript function: OffsetCurve
        """
        _rhino_ids = _rsf.offset_curve(self._rhino_id, direction, distance, normal, style)
        return map(lambda i: p2r.Circle(i), _rhino_ids)

    def split(self, parameters, delete=pythoncom.Empty):
        """
        For help, look up the Rhinoscript function: SplitCurve
        """
        _rhino_ids = _rsf.split_curve(self._rhino_id, parameters, delete)
        return map(lambda i: p2r.Arc(i), _rhino_ids)

    def trim(self, interval, delete=pythoncom.Empty):
        """
        For help, look up the Rhinoscript function: TrimCurve
        """
        _rhino_id = _rsf.trim_curve(self._rhino_id, interval, delete)
        if _rhino_id:
            return p2r.Arc(_rhino_id)
        else:
            return None


class _ConeProp(_SurfaceRootProp):

    # Class constructor
    def __init__(self, _rhino_id, _class):
        if _rhino_id==None:
            raise Exception("_rhino_id is required.")
        self._rhino_id = _rhino_id
        self._class = _class

    def cone_def(self):
        """
        For help, look up the Rhinoscript function: SurfaceCone
        """
        return _rsf.surface_cone(self._rhino_id)


class _CurveRootFuncOorc(_CurveRootFuncOpen,_CurveRootFuncClsd):

    # Class constructor
    def __init__(self, _rhino_id, _class):
        if _rhino_id==None:
            raise Exception("_rhino_id is required.")
        self._rhino_id = _rhino_id
        self._class = _class


class _CylinderProp(_SurfaceRootProp):

    # Class constructor
    def __init__(self, _rhino_id, _class):
        if _rhino_id==None:
            raise Exception("_rhino_id is required.")
        self._rhino_id = _rhino_id
        self._class = _class

    def cylinder_def(self):
        """
        For help, look up the Rhinoscript function: SurfaceCylinder
        """
        return _rsf.surface_cylinder(self._rhino_id)


class _NurbsCurveFunc(_CurveRootFuncOorc):

    # Class constructor
    def __init__(self, _rhino_id, _class):
        if _rhino_id==None:
            raise Exception("_rhino_id is required.")
        self._rhino_id = _rhino_id
        self._class = _class

    def crv_sub(self, param_0, param_1):
        """
        For help, look up the Rhinoscript function: AddSubCrv
        """
        _rhino_id = _rsf.add_sub_crv(self._rhino_id, param_0, param_1)
        if _rhino_id:
            return p2r.NurbsCurve(_rhino_id)
        else:
            return None

    def offset(self, direction, distance, normal=pythoncom.Empty, style=pythoncom.Empty):
        """
        For help, look up the Rhinoscript function: OffsetCurve
        """
        _rhino_ids = _rsf.offset_curve(self._rhino_id, direction, distance, normal, style)
        return map(lambda i: p2r.NurbsCurve(i), _rhino_ids)

    def offset_on_srf(self, surface, distance, parameter):
        """
        For help, look up the Rhinoscript function: OffsetCurveOnSurface
        """
        _rhino_id = _rsf.offset_curve_on_surface(self._rhino_id, surface._rhino_id, distance, parameter)
        if _rhino_id:
            return p2r.NurbsCurve(_rhino_id)
        else:
            return None

    def split(self, parameters, delete=pythoncom.Empty):
        """
        For help, look up the Rhinoscript function: SplitCurve
        """
        _rhino_ids = _rsf.split_curve(self._rhino_id, parameters, delete)
        return map(lambda i: p2r.NurbsCurve(i), _rhino_ids)

    def trim(self, interval, delete=pythoncom.Empty):
        """
        For help, look up the Rhinoscript function: TrimCurve
        """
        _rhino_id = _rsf.trim_curve(self._rhino_id, interval, delete)
        if _rhino_id:
            return p2r.NurbsCurve(_rhino_id)
        else:
            return None


class _PolySurfaceProp(_SurfaceRootProp):

    # Class constructor
    def __init__(self, _rhino_id, _class):
        if _rhino_id==None:
            raise Exception("_rhino_id is required.")
        self._rhino_id = _rhino_id
        self._class = _class

    def explode(self, objects, delete=pythoncom.Empty):
        """
        For help, look up the Rhinoscript function: ExplodePolysurfaces
        """
        _rhino_ids = _rsf.explode_polysurfaces(map(lambda i: i._rhino_id, objects), delete)
        return map(lambda i: p2r.NurbsSurface(i), _rhino_ids)


class _PolylineFunc(_CurveRootFuncOorc):

    # Class constructor
    def __init__(self, _rhino_id, _class):
        if _rhino_id==None:
            raise Exception("_rhino_id is required.")
        self._rhino_id = _rhino_id
        self._class = _class

    def sub(self, param_0, param_1):
        """
        For help, look up the Rhinoscript function: AddSubCrv
        """
        _rhino_id = _rsf.add_sub_crv(self._rhino_id, param_0, param_1)
        if _rhino_id:
            return p2r.Polyline(_rhino_id)
        else:
            return None

    def offset(self, direction, distance, normal=pythoncom.Empty, style=pythoncom.Empty):
        """
        For help, look up the Rhinoscript function: OffsetCurve
        """
        _rhino_ids = _rsf.offset_curve(self._rhino_id, direction, distance, normal, style)
        return map(lambda i: p2r.Polyline(i), _rhino_ids)

    def split(self, parameters, delete=pythoncom.Empty):
        """
        For help, look up the Rhinoscript function: SplitCurve
        """
        _rhino_ids = _rsf.split_curve(self._rhino_id, parameters, delete)
        return map(lambda i: p2r.Polyline(i), _rhino_ids)

    def trim(self, interval, delete=pythoncom.Empty):
        """
        For help, look up the Rhinoscript function: TrimCurve
        """
        _rhino_id = _rsf.trim_curve(self._rhino_id, interval, delete)
        if _rhino_id:
            return p2r.Polyline(_rhino_id)
        else:
            return None


class _SphereProp(_SurfaceRootProp):

    # Class constructor
    def __init__(self, _rhino_id, _class):
        if _rhino_id==None:
            raise Exception("_rhino_id is required.")
        self._rhino_id = _rhino_id
        self._class = _class

    def cylinder_definition(self):
        """
        For help, look up the Rhinoscript function: SurfaceSphere
        """
        return _rsf.surface_sphere(self._rhino_id)


class _SurfaceRootFuncOorc(_SurfaceRootFuncOpen,_SurfaceRootFuncClsd):

    # Class constructor
    def __init__(self, _rhino_id, _class):
        if _rhino_id==None:
            raise Exception("_rhino_id is required.")
        self._rhino_id = _rhino_id
        self._class = _class