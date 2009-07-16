# Auto-generated wrapper for Rhino4 RhinoScript functions
import win32com.client.CLSIDToClass, pythoncom
import win32com.client.util
from pywintypes import IID
from win32com.client import Dispatch
from win32com.client import DispatchBaseClass
import exceptions
class Hatch(DispatchBaseClass):



    def add_hatch(self, curve, hatch, scale, rotation):
        """

        Creates a new hatch object from a closed planar curve object.

        Parameters

        Curve : Required, String, str
        Hatch : Optional, String, str
        Scale : Optional, Number, dbl
        Rotation : Optional, Number, dbl

        Returns

        String : The identifier of the newly created hatch object if successful.
        Null : If not successful, or on error.

        """

        return self._ApplyTypes_(835, 1, (12, 0), ((12, 0), (12, 0), (12, 0), (12, 0)), u'AddHatch', None, curve, hatch, scale, rotation)

    def add_hatch_patterns(self, file_name, replace):
        """

        Adds hatch pattens to the document by importing hatch pattern definitions from a pattern file. For more information on hatch pattern files, see the Rhino help file for the Hatch command.

        Parameters

        FileName : Required, String, str
        Replace : Optional, Boolean, bln

        Returns

        Array : The names of the newly added hatch patterns if successful.
        Null : If not successful, or on error.

        """

        return self._ApplyTypes_(826, 1, (12, 0), ((12, 0), (12, 0)), u'AddHatchPatterns', None, file_name, replace)

    def add_hatches(self, curves, hatch, scale, rotation):
        """

        Creates one or more new hatch objects from an array of closed planar curve objects.

        Parameters

        Curves : Required, Array, arr
        Hatch : Optional, String, str
        Scale : Optional, Number, dbl
        Rotation : Optional, Number, dbl

        Returns

        Array : The identifiers of the newly created hatch objects if successful.
        Null : If not successful, or on error.

        """

        return self._ApplyTypes_(836, 1, (12, 0), ((12, 0), (12, 0), (12, 0), (12, 0)), u'AddHatches', None, curves, hatch, scale, rotation)

    def current_hatch_pattern(self, hatch):
        """

        Returns or sets the current hatch pattern file.

        Parameters

        Hatch : Optional, String, str

        Returns

        String : If a hatch pattern name is not specified, the current hatch pattern if successful.
        String : If a hatch pattern name is specified, the previous current hatch pattern if successful.
        Null : On error.

        """

        return self._ApplyTypes_(827, 1, (12, 0), ((12, 0)), u'CurrentHatchPattern', None, hatch)

    def explode_hatch(self, hatch, delete):
        """

        Explodes a hatch object into its component objects. The exploded objects will be added to the document. If the hatch object uses a solid pattern, then planar face Brep objects will be created. Otherwise, line curve objects will be created.

        Parameters

        Hatch : Required, String, str
        Delete : Optional, Boolean, bln

        Returns

        Array : An array of strings identifying the newly created objects if successful.
        Null : On error.

        """

        return self._ApplyTypes_(841, 1, (12, 0), ((12, 0), (12, 0)), u'ExplodeHatch', None, hatch, delete)

    def hatch_pattern(self, object, hatch):
        """

        Returns or changes a hatch object's hatch pattern.

        Parameters

        Object : Required, String, str
        Hatch : Optional, String, str

        Returns

        String : If a hatch pattern name is not specified, the current hatch pattern if successful.
        String : If a hatch pattern name is specified, the previous current hatch pattern if successful.
        Null : On error.

        """

        return self._ApplyTypes_(837, 1, (12, 0), ((12, 0), (12, 0)), u'HatchPattern', None, object, hatch)

    def hatch_pattern_count(self):
        """

        Returns the number of hatch patterns in the document.

        No parameters

        Returns

        Number : The number of hatch patterns in the document.

        """

        return self._ApplyTypes_(828, 1, (12, 0), (), u'HatchPatternCount', None, )

    def hatch_pattern_description(self, hatch):
        """

        Returns the description of a hatch pattern. Note, not all hatch patterns have descriptions for descriptions are optional.

        Parameters

        Hatch : Required, String, str

        Returns

        String : If hatch pattern's description if successful.
        Null : If not successful, or on error.

        """

        return self._ApplyTypes_(829, 1, (12, 0), ((12, 0)), u'HatchPatternDescription', None, hatch)

    def hatch_pattern_fill_type(self, hatch):
        """

        Gradient, uses fill color definition.

        Parameters

        Hatch : Required, String, str

        Returns

        Number : If hatch pattern's fill type if successful.
        Null : If not successful, or on error.

        """

        return self._ApplyTypes_(831, 1, (12, 0), ((12, 0)), u'HatchPatternFillType', None, hatch)

    def hatch_pattern_names(self):
        """

        Returns the names of all of the hatch pattern in the document.

        No parameters

        Returns

        Array : An array of hatch pattern names if successful.
        Null : If not successful, or on error.

        """

        return self._ApplyTypes_(830, 1, (12, 0), (), u'HatchPatternNames', None, )

    def hatch_rotation(self, object, rotation):
        """

        Returns or modifies the rotation applied to the hatch pattern when it is mapped to the hatch's plane.

        Parameters

        Object : Required, String, str
        Rotation : Optional, Number, dbl

        Returns

        Number : If a rotation angle is not specified, the current rotation angle if successful.
        Number : If a rotation angle is specified, the previous rotation angle if successful.
        Null : On error.

        """

        return self._ApplyTypes_(839, 1, (12, 0), ((12, 0), (12, 0)), u'HatchRotation', None, object, rotation)

    def hatch_scale(self, object, scale):
        """

        Returns or modifies the scale applied to the hatch pattern when it is mapped to the hatch's plane.

        Parameters

        Object : Required, String, str
        Scale : Optional, Number, dbl

        Returns

        Number : If a scale factor is not specified, the current scale factor if successful.
        Number : If a scale factor is specified, the previous scale factor if successful.
        Null : On error.

        """

        return self._ApplyTypes_(838, 1, (12, 0), ((12, 0), (12, 0)), u'HatchScale', None, object, scale)

    def is_hatch(self, object):
        """

        Verifies the existence of a hatch object in the document.

        Parameters

        Object : Required, String, str

        Returns

        Null : On error.

        """

        return self._ApplyTypes_(840, 1, (12, 0), ((12, 0)), u'IsHatch', None, object)

    def is_hatch_pattern(self, hatch):
        """

        Verifies the existence of a hatch pattern in the document.

        Parameters

        Hatch : Required, String, str

        Returns

        Null : On error.

        """

        return self._ApplyTypes_(832, 1, (12, 0), ((12, 0)), u'IsHatchPattern', None, hatch)

    def is_hatch_pattern_current(self, hatch):
        """

        Verifies that a hatch pattern is the current hatch pattern.

        Parameters

        Hatch : Required, String, str

        Returns

        Null : On error.

        """

        return self._ApplyTypes_(833, 1, (12, 0), ((12, 0)), u'IsHatchPatternCurrent', None, hatch)

    def is_hatch_pattern_reference(self, hatch):
        """

        Verifies that a hatch pattern is from a reference file.

        Parameters

        Hatch : Required, String, str

        Returns

        Null : On error.

        """

        return self._ApplyTypes_(834, 1, (12, 0), ((12, 0)), u'IsHatchPatternReference', None, hatch)

