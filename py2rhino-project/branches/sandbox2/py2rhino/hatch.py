# Auto-generated wrapper for Rhino4 RhinoScript functions

import exceptions
from py2rhino._util import *
from py2rhino._rhinoscript import IRhinoScript

class Hatch(IRhinoScript):



    def add_hatch(self, curve, hatch=None, scale=None, rotation=None):
        """        
        Creates a new hatch object from a closed planar curve object.
    
        Parameters
        ==========

        curve, String, Required        
        The identifier of the closed planar curve that defines the boundary of the hatch object.
            
        hatch, String, Optional        
        The name of the hatch pattern to be used by the hatch object.  If omitted, the current hatch pattern will be used.
            
        scale, Double, Optional        
        The hatch pattern scale factor.  If omitted, a scale factor of 1.0 will be used.
            
        rotation, Double, Optional        
        The hatch pattern rotation angle in degrees.  If omitted, a rotation angle of 0.0 degrees will be used.
            
        Returns
        =======

        string
        The identifier of the newly created hatch object if successful.

        null
        If not successful, or on error.

        """

        params = [curve, hatch, scale, rotation]
        params_opt_or_req = [Required, Optional, Optional, Optional]
        params_magic_numbers = [(VT_BSTR, 1), (VT_BSTR, 1), (VT_R8, 1), (VT_R8, 1)]
        params_flattened = [curve, hatch, scale, rotation]

        for i in range(len(params)):
            if (params[i] == None) and (params_opt_or_req[i] = "Optional"):
                params_magic_numbers.pop(i)
                params_flattened.pop(i)

        return self._ApplyTypes_(835, 1, (VT_VARIANT, 0), params_magic_numbers, u"AddHatch", None, *params_flattened)

    def add_hatch_patterns(self, file_name, replace=None):
        """        
        Adds hatch pattens to the document by importing hatch pattern definitions from a pattern file. For more information on hatch pattern files, see the Rhino help file for the Hatch command.
    
        Parameters
        ==========

        file_name, String, Required        
        The name of the hatch pattern file to import.
            
        replace, Boolean, Optional        
        If hatch pattern names already in the document match hatch pattern names in the pattern definition file, then the existing hatch patterns will be redefined.  If omitted, existing hatch patterns will not be redefined (False).
            
        Returns
        =======

        array
        The names of the newly added hatch patterns if successful.

        null
        If not successful, or on error.

        """

        params = [file_name, replace]
        params_opt_or_req = [Required, Optional]
        params_magic_numbers = [(VT_BSTR, 1), (VT_BOOL, 1)]
        params_flattened = [file_name, replace]

        for i in range(len(params)):
            if (params[i] == None) and (params_opt_or_req[i] = "Optional"):
                params_magic_numbers.pop(i)
                params_flattened.pop(i)

        return self._ApplyTypes_(826, 1, (VT_VARIANT, 0), params_magic_numbers, u"AddHatchPatterns", None, *params_flattened)

    def add_hatches(self, curves, hatch=None, scale=None, rotation=None):
        """        
        Creates one or more new hatch objects from an array of closed planar curve objects.
    
        Parameters
        ==========

        curves, Array of ????, Required        
        An array of strings that identify one or more closed planar curves that defines the boundaries of the hatch objects.
            
        hatch, String, Optional        
        The name of the hatch pattern to be used by the hatch object.  If omitted, the current hatch pattern will be used.
            
        scale, Double, Optional        
        The hatch pattern scale factor.  If omitted, a scale factor of 1.0 will be used.
            
        rotation, Double, Optional        
        The hatch pattern rotation angle in degrees.  If omitted, a rotation angle of 0.0 degrees will be used.
            
        Returns
        =======

        array
        The identifiers of the newly created hatch objects if successful.

        null
        If not successful, or on error.

        """

        params = [curves, hatch, scale, rotation]
        params_opt_or_req = [Required, Optional, Optional, Optional]
        params_magic_numbers = [(VT_VARIANT, 1), (VT_BSTR, 1), (VT_R8, 1), (VT_R8, 1)]
        params_flattened = [flatten(curves), hatch, scale, rotation]

        for i in range(len(params)):
            if (params[i] == None) and (params_opt_or_req[i] = "Optional"):
                params_magic_numbers.pop(i)
                params_flattened.pop(i)

        return self._ApplyTypes_(836, 1, (VT_VARIANT, 0), params_magic_numbers, u"AddHatches", None, *params_flattened)

    def current_hatch_pattern(self, hatch=None):
        """        
        Returns or sets the current hatch pattern file.
    
        Parameters
        ==========

        hatch, String, Optional        
        The name of an existing hatch pattern to make current.
            
        Returns
        =======

        string
        If a hatch pattern name is not specified, the current hatch pattern if successful.

        string
        If a hatch pattern name is specified, the previous current hatch pattern if successful.

        null
        On error.

        """

        params = [hatch]
        params_opt_or_req = [Optional]
        params_magic_numbers = [(VT_BSTR, 1),]
        params_flattened = [hatch]

        for i in range(len(params)):
            if (params[i] == None) and (params_opt_or_req[i] = "Optional"):
                params_magic_numbers.pop(i)
                params_flattened.pop(i)

        return self._ApplyTypes_(827, 1, (VT_VARIANT, 0), params_magic_numbers, u"CurrentHatchPattern", None, *params_flattened)

    def explode_hatch(self, hatch, delete=None):
        """        
        Explodes a hatch object into its component objects. The exploded objects will be added to the document. If the hatch object uses a solid pattern, then planar face Brep objects will be created. Otherwise, line curve objects will be created.
    
        Parameters
        ==========

        hatch, String, Required        
        The identifier of an object.
            
        delete, Boolean, Optional        
        Delete the hatch object. The default is to not delete the hatch object (False).
            
        Returns
        =======

        array
        An array of strings identifying the newly created objects if successful.

        null
        On error.

        """

        params = [hatch, delete]
        params_opt_or_req = [Required, Optional]
        params_magic_numbers = [(VT_BSTR, 1), (VT_BOOL, 1)]
        params_flattened = [hatch, delete]

        for i in range(len(params)):
            if (params[i] == None) and (params_opt_or_req[i] = "Optional"):
                params_magic_numbers.pop(i)
                params_flattened.pop(i)

        return self._ApplyTypes_(841, 1, (VT_VARIANT, 0), params_magic_numbers, u"ExplodeHatch", None, *params_flattened)

    def hatch_pattern(self, object, hatch=None):
        """        
        Returns or changes a hatch object's hatch pattern.
    
        Parameters
        ==========

        object, String, Required        
        The identifier of a hatch object.
            
        hatch, String, Optional        
        The name of an existing hatch pattern to replace the current hatch pattern.
            
        Returns
        =======

        string
        If a hatch pattern name is not specified, the current hatch pattern if successful.

        string
        If a hatch pattern name is specified, the previous current hatch pattern if successful.

        null
        On error.

        """

        params = [object, hatch]
        params_opt_or_req = [Required, Optional]
        params_magic_numbers = [(VT_BSTR, 1), (VT_BSTR, 1)]
        params_flattened = [object, hatch]

        for i in range(len(params)):
            if (params[i] == None) and (params_opt_or_req[i] = "Optional"):
                params_magic_numbers.pop(i)
                params_flattened.pop(i)

        return self._ApplyTypes_(837, 1, (VT_VARIANT, 0), params_magic_numbers, u"HatchPattern", None, *params_flattened)

    def hatch_pattern_count):
        """        
        Returns the number of hatch patterns in the document.
    
        No parameters

        Returns
        =======

        number
        The number of hatch patterns in the document.

        """

        params = []
        params_opt_or_req = []
        params_magic_numbers = []
        params_flattened = []

        for i in range(len(params)):
            if (params[i] == None) and (params_opt_or_req[i] = "Optional"):
                params_magic_numbers.pop(i)
                params_flattened.pop(i)

        return self._ApplyTypes_(828, 1, (VT_VARIANT, 0), params_magic_numbers, u"HatchPatternCount", None, *params_flattened)

    def hatch_pattern_description(self, hatch):
        """        
        Returns the description of a hatch pattern. Note, not all hatch patterns have descriptions for descriptions are optional.
    
        Parameters
        ==========

        hatch, String, Required        
        The name of an existing hatch pattern.
            
        Returns
        =======

        string
        If hatch pattern's description if successful.

        null
        If not successful, or on error.

        """

        params = [hatch]
        params_opt_or_req = [Required]
        params_magic_numbers = [(VT_BSTR, 1),]
        params_flattened = [hatch]

        for i in range(len(params)):
            if (params[i] == None) and (params_opt_or_req[i] = "Optional"):
                params_magic_numbers.pop(i)
                params_flattened.pop(i)

        return self._ApplyTypes_(829, 1, (VT_VARIANT, 0), params_magic_numbers, u"HatchPatternDescription", None, *params_flattened)

    def hatch_pattern_fill_type(self, hatch):
        """        
        Returns the fill type of a hatch pattern. Hatch patterns have one of the following fill types:
		Value
		Description
		0
		Solid, uses object color.
		1
		Lines, uses pattern file definition.
		2
		Gradient, uses fill color definition.
    
        Parameters
        ==========

        hatch, String, Required        
        The name of an existing hatch pattern.
            
        Returns
        =======

        number
        If hatch pattern's fill type if successful.

        null
        If not successful, or on error.

        """

        params = [hatch]
        params_opt_or_req = [Required]
        params_magic_numbers = [(VT_BSTR, 1),]
        params_flattened = [hatch]

        for i in range(len(params)):
            if (params[i] == None) and (params_opt_or_req[i] = "Optional"):
                params_magic_numbers.pop(i)
                params_flattened.pop(i)

        return self._ApplyTypes_(831, 1, (VT_VARIANT, 0), params_magic_numbers, u"HatchPatternFillType", None, *params_flattened)

    def hatch_pattern_names):
        """        
        Returns the names of all of the hatch pattern in the document.
    
        No parameters

        Returns
        =======

        array
        An array of hatch pattern names if successful.

        null
        If not successful, or on error.

        """

        params = []
        params_opt_or_req = []
        params_magic_numbers = []
        params_flattened = []

        for i in range(len(params)):
            if (params[i] == None) and (params_opt_or_req[i] = "Optional"):
                params_magic_numbers.pop(i)
                params_flattened.pop(i)

        return self._ApplyTypes_(830, 1, (VT_VARIANT, 0), params_magic_numbers, u"HatchPatternNames", None, *params_flattened)

    def hatch_rotation(self, object, rotation=None):
        """        
        Returns or modifies the rotation applied to the hatch pattern when it is mapped to the hatch's plane.
    
        Parameters
        ==========

        object, String, Required        
        The identifier of a hatch object.
            
        rotation, Double, Optional        
        The rotation angle in degrees.
            
        Returns
        =======

        number
        If a rotation angle is not specified, the current rotation angle if successful.

        number
        If a rotation angle is specified, the previous rotation angle if successful.

        null
        On error.

        """

        params = [object, rotation]
        params_opt_or_req = [Required, Optional]
        params_magic_numbers = [(VT_BSTR, 1), (VT_R8, 1)]
        params_flattened = [object, rotation]

        for i in range(len(params)):
            if (params[i] == None) and (params_opt_or_req[i] = "Optional"):
                params_magic_numbers.pop(i)
                params_flattened.pop(i)

        return self._ApplyTypes_(839, 1, (VT_VARIANT, 0), params_magic_numbers, u"HatchRotation", None, *params_flattened)

    def hatch_scale(self, object, scale=None):
        """        
        Returns or modifies the scale applied to the hatch pattern when it is mapped to the hatch's plane.
    
        Parameters
        ==========

        object, String, Required        
        The identifier of a hatch object.
            
        scale, Double, Optional        
        The scale factor.
            
        Returns
        =======

        number
        If a scale factor is not specified, the current scale factor if successful.

        number
        If a scale factor is specified, the previous scale factor if successful.

        null
        On error.

        """

        params = [object, scale]
        params_opt_or_req = [Required, Optional]
        params_magic_numbers = [(VT_BSTR, 1), (VT_R8, 1)]
        params_flattened = [object, scale]

        for i in range(len(params)):
            if (params[i] == None) and (params_opt_or_req[i] = "Optional"):
                params_magic_numbers.pop(i)
                params_flattened.pop(i)

        return self._ApplyTypes_(838, 1, (VT_VARIANT, 0), params_magic_numbers, u"HatchScale", None, *params_flattened)

    def is_hatch(self, object):
        """        
        Verifies the existence of a hatch object in the document.
    
        Parameters
        ==========

        object, String, Required        
        The identifier of an object.
            
        Returns
        =======

        null
        On error.

        """

        params = [object]
        params_opt_or_req = [Required]
        params_magic_numbers = [(VT_BSTR, 1),]
        params_flattened = [object]

        for i in range(len(params)):
            if (params[i] == None) and (params_opt_or_req[i] = "Optional"):
                params_magic_numbers.pop(i)
                params_flattened.pop(i)

        return self._ApplyTypes_(840, 1, (VT_VARIANT, 0), params_magic_numbers, u"IsHatch", None, *params_flattened)

    def is_hatch_pattern(self, hatch):
        """        
        Verifies the existence of a hatch pattern in the document.
    
        Parameters
        ==========

        hatch, String, Required        
        The name of a hatch pattern.
            
        Returns
        =======

        null
        On error.

        """

        params = [hatch]
        params_opt_or_req = [Required]
        params_magic_numbers = [(VT_BSTR, 1),]
        params_flattened = [hatch]

        for i in range(len(params)):
            if (params[i] == None) and (params_opt_or_req[i] = "Optional"):
                params_magic_numbers.pop(i)
                params_flattened.pop(i)

        return self._ApplyTypes_(832, 1, (VT_VARIANT, 0), params_magic_numbers, u"IsHatchPattern", None, *params_flattened)

    def is_hatch_pattern_current(self, hatch):
        """        
        Verifies that a hatch pattern is the current hatch pattern.
    
        Parameters
        ==========

        hatch, String, Required        
        The name of an existing hatch pattern.
            
        Returns
        =======

        null
        On error.

        """

        params = [hatch]
        params_opt_or_req = [Required]
        params_magic_numbers = [(VT_BSTR, 1),]
        params_flattened = [hatch]

        for i in range(len(params)):
            if (params[i] == None) and (params_opt_or_req[i] = "Optional"):
                params_magic_numbers.pop(i)
                params_flattened.pop(i)

        return self._ApplyTypes_(833, 1, (VT_VARIANT, 0), params_magic_numbers, u"IsHatchPatternCurrent", None, *params_flattened)

    def is_hatch_pattern_reference(self, hatch):
        """        
        Verifies that a hatch pattern is from a reference file.
    
        Parameters
        ==========

        hatch, String, Required        
        The name of an existing hatch pattern.
            
        Returns
        =======

        null
        On error.

        """

        params = [hatch]
        params_opt_or_req = [Required]
        params_magic_numbers = [(VT_BSTR, 1),]
        params_flattened = [hatch]

        for i in range(len(params)):
            if (params[i] == None) and (params_opt_or_req[i] = "Optional"):
                params_magic_numbers.pop(i)
                params_flattened.pop(i)

        return self._ApplyTypes_(834, 1, (VT_VARIANT, 0), params_magic_numbers, u"IsHatchPatternReference", None, *params_flattened)

