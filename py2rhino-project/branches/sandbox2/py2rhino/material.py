# Auto-generated wrapper for Rhino4 RhinoScript functions

import exceptions
import pythoncom
import py2rhino
from py2rhino._util import *
from py2rhino._rhinoscript import IRhinoScript

class Material(IRhinoScript):

    # Class constructor
    def __init__(self):
        if py2rhino._rso is None:
            raise exceptions.Exception
        # initialisation code coped from win32com.client.DispatchBaseClass
        oobj = py2rhino._rso
        oobj = oobj._oleobj_.QueryInterface(self.CLSID, pythoncom.IID_IDispatch)
        self.__dict__["_oleobj_"] = oobj

    def add_material_to_layer(self, object):
        """        
        Adds a material to a layer and returns the new material's index.  If the layer already has a material, then the layer's current material index is returned.
    
        Parameters
        ==========

        object, String, Required        
        The name of an existing layer.
            
        Returns
        =======

        number
        The zero-based material index of the layer if successful.

        null
        If not successful, or on error.

        """

        params = [object]
        required = [True]
        magic = [(VT_BSTR, 1),]
        flattened = [object]

        magic, flattened = select_params(params, required, magic, flattened)

        return self._ApplyTypes_(173, 1, (VT_VARIANT, 0), magic, u"AddMaterialToLayer", None, *flattened)

    def add_material_to_object(self, object):
        """        
        Adds a material to an object and returns the new material's index.  Note, adding a material to an object modifies the object's material source from "By Layer" to "By Object."  See ObjectMaterialSource for details.  If the object already has a material, then the object's current material index is returned.
    
        Parameters
        ==========

        object, String, Required        
        The identifier of the object.
            
        Returns
        =======

        number
        The zero-based material index of the object if successful.

        null
        If not successful, or on error.

        """

        params = [object]
        required = [True]
        magic = [(VT_BSTR, 1),]
        flattened = [object]

        magic, flattened = select_params(params, required, magic, flattened)

        return self._ApplyTypes_(174, 1, (VT_VARIANT, 0), magic, u"AddMaterialToObject", None, *flattened)

    def copy_material(self, src_index, dst_index):
        """        
        Copies the definition of a source material to a destination material.
    
        Parameters
        ==========

        src_index, Integer, Required        
        The index of the source material.
            
        dst_index, Integer, Required        
        The index of the destination material.
            
        Returns
        =======

        boolean
        True or false indicating success or failure.

        null
        On error.

        """

        params = [src_index, dst_index]
        required = [True, True]
        magic = [(VT_I2, 1), (VT_I2, 1)]
        flattened = [src_index, dst_index]

        magic, flattened = select_params(params, required, magic, flattened)

        return self._ApplyTypes_(812, 1, (VT_VARIANT, 0), magic, u"CopyMaterial", None, *flattened)

    def is_material_default(self, material_index):
        """        
        Verifies that a material is a copy of Rhino's built-in "default" material.  The default material is used by objects and layers that have not been assigned a material.
    
        Parameters
        ==========

        material_index, Integer, Required        
        The zero-based material index.
            
        Returns
        =======

        null
        On error.

        """

        params = [material_index]
        required = [True]
        magic = [(VT_I2, 1),]
        flattened = [material_index]

        magic, flattened = select_params(params, required, magic, flattened)

        return self._ApplyTypes_(175, 1, (VT_VARIANT, 0), magic, u"IsMaterialDefault", None, *flattened)

    def is_material_reference(self, material_index):
        """        
        Verifies a material is referenced from another file.
    
        Parameters
        ==========

        material_index, Integer, Required        
        The zero-based material index.
            
        Returns
        =======

        boolean
        True if successful, otherwise False.

        null
        On error.

        """

        params = [material_index]
        required = [True]
        magic = [(VT_I2, 1),]
        flattened = [material_index]

        magic, flattened = select_params(params, required, magic, flattened)

        return self._ApplyTypes_(176, 1, (VT_VARIANT, 0), magic, u"IsMaterialReference", None, *flattened)

    def match_material(self, src_material_index):
        """        
        Copies the material definition from one material to one or more objects.
    
        Parameters
        ==========

        src_material_index, Integer, Required        
        The zero-based source material index.
            
        Returns
        =======

        number
        The number of object that were modified if successful.

        null
        It not successful, or on error.

        """

        params = [src_material_index]
        required = [True]
        magic = [(VT_I2, 1),]
        flattened = [src_material_index]

        magic, flattened = select_params(params, required, magic, flattened)

        return self._ApplyTypes_(322, 1, (VT_VARIANT, 0), magic, u"MatchMaterial", None, *flattened)

    def match_material_2(self, src_object, dest_objects):
        """        
        Copies the material definition from one material to one or more objects.
    
        Parameters
        ==========

        src_object, String, Required        
        The identifier of the source object.  The object must have a material assigned.
            
        dest_objects, Array of Strings, Required        
        An array of destination object identifiers.  If the objects' material sources are set to "By Layer", they will be changed to "By Object."
            
        Returns
        =======

        number
        The number of object that were modified if successful.

        null
        It not successful, or on error.

        """

        params = [src_object, dest_objects]
        required = [True, True]
        magic = [(VT_BSTR, 1), (VT_VARIANT, 1)]
        flattened = [src_object, flatten_params(dest_objects)]

        magic, flattened = select_params(params, required, magic, flattened)

        return self._ApplyTypes_(322, 1, (VT_VARIANT, 0), magic, u"MatchMaterial", None, *flattened)

    def material_bump(self, material_index, file_name=None):
        """        
        Returns or modifies a material's bump bitmap filename.
    
        Parameters
        ==========

        material_index, Integer, Required        
        The zero-based source material index.
            
        file_name, String, Optional        
        The bump bitmap filename.
            
        Returns
        =======

        string
        If strFileName is not specified, the current bump bitmap filename if successful.

        string
        If strFileName is specified, the previous bump bitmap filename if successful.

        null
        It not successful, or on error.

        """

        params = [material_index, file_name]
        required = [True, False]
        magic = [(VT_I2, 1), (VT_BSTR, 1)]
        flattened = [material_index, file_name]

        magic, flattened = select_params(params, required, magic, flattened)

        return self._ApplyTypes_(177, 1, (VT_VARIANT, 0), magic, u"MaterialBump", None, *flattened)

    def material_color(self, material_index, color=None):
        """        
        Returns or modifies a material's diffuse color.  Material colors are represented as RGB colors.  An RGB color specifies the relative intensity of red, green, and blue to cause a specific color to be displayed.
    
        Parameters
        ==========

        material_index, Integer, Required        
        The zero-based source material index.
            
        color, Integer, Optional        
        The new color value.  If omitted, the current material color is returned.
            
        Returns
        =======

        number
        If lngColor is not specified, the current material color if successful.

        number
        If lngColor is specified, the previous material color if successful.

        null
        It not successful, or on error.

        """

        params = [material_index, color]
        required = [True, False]
        magic = [(VT_I2, 1), (VT_I4, 1)]
        flattened = [material_index, color]

        magic, flattened = select_params(params, required, magic, flattened)

        return self._ApplyTypes_(178, 1, (VT_VARIANT, 0), magic, u"MaterialColor", None, *flattened)

    def material_environment_map(self, material_index, file_name=None):
        """        
        Returns or modifies a material's environment bitmap filename.
    
        Parameters
        ==========

        material_index, Integer, Required        
        The zero-based source material index.
            
        file_name, String, Optional        
        The environment bitmap filename.
            
        Returns
        =======

        string
        If strFileName is not specified, the current environment bitmap filename if successful.

        string
        If strFileName is specified, the previous environment bitmap filename if successful.

        null
        It not successful, or on error.

        """

        params = [material_index, file_name]
        required = [True, False]
        magic = [(VT_I2, 1), (VT_BSTR, 1)]
        flattened = [material_index, file_name]

        magic, flattened = select_params(params, required, magic, flattened)

        return self._ApplyTypes_(754, 1, (VT_VARIANT, 0), magic, u"MaterialEnvironmentMap", None, *flattened)

    def material_name(self, material_index, name=None):
        """        
        Returns or modifies a material's user-definable name.
    
        Parameters
        ==========

        material_index, Integer, Required        
        The zero-based source material index.
            
        name, String, Optional        
        The new name.  If omitted, the current name is returned.
            
        Returns
        =======

        string
        If strName is not specified, the current material name if successful.

        string
        If strName is specified, the previous material name if successful.

        null
        It not successful, or on error.

        """

        params = [material_index, name]
        required = [True, False]
        magic = [(VT_I2, 1), (VT_BSTR, 1)]
        flattened = [material_index, name]

        magic, flattened = select_params(params, required, magic, flattened)

        return self._ApplyTypes_(179, 1, (VT_VARIANT, 0), magic, u"MaterialName", None, *flattened)

    def material_reflective_color(self, material_index, color=None):
        """        
        Returns or modifies a material's reflective color.  Reflective colors are represented as RGB colors.  An RGB color specifies the relative intensity of red, green, and blue to cause a specific color to be displayed.
    
        Parameters
        ==========

        material_index, Integer, Required        
        The zero-based source material index.
            
        color, Integer, Optional        
        The new color value.  If omitted, the current reflective color is returned.
            
        Returns
        =======

        number
        If lngColor is not specified, the current reflective color if successful.

        number
        If lngColor is specified, the previous reflective color if successful.

        null
        It not successful, or on error.

        """

        params = [material_index, color]
        required = [True, False]
        magic = [(VT_I2, 1), (VT_I4, 1)]
        flattened = [material_index, color]

        magic, flattened = select_params(params, required, magic, flattened)

        return self._ApplyTypes_(180, 1, (VT_VARIANT, 0), magic, u"MaterialReflectiveColor", None, *flattened)

    def material_shine(self, material_index, shine=None):
        """        
        Returns or modifies a material's shine value.
    
        Parameters
        ==========

        material_index, Integer, Required        
        The zero-based source material index.
            
        shine, Double, Optional        
        The new shine value.  A material's shine value ranges from 0.0 to 255.0, with 0.0 being matte and 255.0 being glossy.  If omitted, the current shine value is returned.
            
        Returns
        =======

        number
        If dblShine is not specified, the current shine value if successful.

        number
        If dblShine is specified, the previous shine value if successful.

        null
        It not successful, or on error.

        """

        params = [material_index, shine]
        required = [True, False]
        magic = [(VT_I2, 1), (VT_R8, 1)]
        flattened = [material_index, shine]

        magic, flattened = select_params(params, required, magic, flattened)

        return self._ApplyTypes_(181, 1, (VT_VARIANT, 0), magic, u"MaterialShine", None, *flattened)

    def material_texture(self, material_index, file_name=None):
        """        
        Returns or modifies a material's texture bitmap filename.
    
        Parameters
        ==========

        material_index, Integer, Required        
        The zero-based source material index.
            
        file_name, String, Optional        
        The texture bitmap filename.
            
        Returns
        =======

        string
        If strFileName is not specified, the current texture bitmap filename if successful.

        string
        If strFileName is specified, the previous texture bitmap filename if successful.

        null
        It not successful, or on error.

        """

        params = [material_index, file_name]
        required = [True, False]
        magic = [(VT_I2, 1), (VT_BSTR, 1)]
        flattened = [material_index, file_name]

        magic, flattened = select_params(params, required, magic, flattened)

        return self._ApplyTypes_(182, 1, (VT_VARIANT, 0), magic, u"MaterialTexture", None, *flattened)

    def material_transparency(self, material_index, transparency=None):
        """        
        Returns or modifies a material's transparency value.
    
        Parameters
        ==========

        material_index, Integer, Required        
        The zero-based source material index.
            
        transparency, Double, Optional        
        The new transparency value.  A material's transparency value ranges from 0.0 to 1.0, with 0.0 being opaque and 1.0 being transparent.  If omitted, the current transparency value is returned.
            
        Returns
        =======

        number
        If dblTransparency is not specified, the current transparency value if successful.

        number
        If dblTransparency is specified, the previous transparency value if successful.

        null
        It not successful, or on error.

        """

        params = [material_index, transparency]
        required = [True, False]
        magic = [(VT_I2, 1), (VT_R8, 1)]
        flattened = [material_index, transparency]

        magic, flattened = select_params(params, required, magic, flattened)

        return self._ApplyTypes_(183, 1, (VT_VARIANT, 0), magic, u"MaterialTransparency", None, *flattened)

    def material_transparency_map(self, material_index, file_name=None):
        """        
        Returns or modifies a material's transparency bitmap filename.
    
        Parameters
        ==========

        material_index, Integer, Required        
        The zero-based source material index.
            
        file_name, String, Optional        
        The transparency bitmap filename.
            
        Returns
        =======

        string
        If strFileName is not specified, the current transparency bitmap filename if successful.

        string
        If strFileName is specified, the previous transparency bitmap filename if successful.

        null
        It not successful, or on error.

        """

        params = [material_index, file_name]
        required = [True, False]
        magic = [(VT_I2, 1), (VT_BSTR, 1)]
        flattened = [material_index, file_name]

        magic, flattened = select_params(params, required, magic, flattened)

        return self._ApplyTypes_(753, 1, (VT_VARIANT, 0), magic, u"MaterialTransparencyMap", None, *flattened)

