# Auto-generated wrapper for Rhino4 RhinoScript functions

import exceptions
import _utils
from _rhinoscript import IRhinoScript

class Material(IRhinoScript):



    def add_material_to_layer(self, object):
        """

        Adds a material to a layer and returns the new material's index.  If the layer already has a material, then the layer's current material index is returned.

        Parameters

        Object : Required, String, str, String

        Returns

        Number : The zero-based material index of the layer if successful.
        Null : If not successful, or on error.

        """

        return self._ApplyTypes_(173, 1, (12, 0), ((8, 0),), u'AddMaterialToLayer', None, object)

    def add_material_to_object(self, object):
        """

        Adds a material to an object and returns the new material's index.  Note, adding a material to an object modifies the object's material source from "By Layer" to "By Object."  See ObjectMaterialSource for details.  If the object already has a material, then the object's current material index is returned.

        Parameters

        Object : Required, String, str, String

        Returns

        Number : The zero-based material index of the object if successful.
        Null : If not successful, or on error.

        """

        return self._ApplyTypes_(174, 1, (12, 0), ((8, 0),), u'AddMaterialToObject', None, object)

    def copy_material(self, src_index, dst_index):
        """

        Copies the definition of a source material to a destination material.

        Parameters

        SrcIndex : Required, Number, int, Integer
        DstIndex : Required, Number, int, Integer

        Returns

        Boolean : True or false indicating success or failure.
        Null : On error.

        """

        return self._ApplyTypes_(812, 1, (12, 0), ((2, 0), (2, 0),), u'CopyMaterial', None, src_index, dst_index)

    def is_material_default(self, material_index):
        """

        Verifies that a material is a copy of Rhino's built-in "default" material.  The default material is used by objects and layers that have not been assigned a material.

        Parameters

        MaterialIndex : Required, Number, int, Integer

        Returns

        Null : On error.

        """

        return self._ApplyTypes_(175, 1, (12, 0), ((2, 0),), u'IsMaterialDefault', None, material_index)

    def is_material_reference(self, material_index):
        """

        Verifies a material is referenced from another file.

        Parameters

        MaterialIndex : Required, Number, int, Integer

        Returns

        Boolean : True if successful, otherwise False.
        Null : On error.

        """

        return self._ApplyTypes_(176, 1, (12, 0), ((2, 0),), u'IsMaterialReference', None, material_index)

    def match_material(self, src_material_index, src_object, dest_object, dest_objects):
        """


        METHOD NOT IMPLEMENTED DUE TO PARAMETER MISMATCH


        """

        raise exceptions.NotImplementedError

    def material_bump(self, material_index, file_name):
        """

        Returns or modifies a material's bump bitmap filename.

        Parameters

        MaterialIndex : Required, Number, int, Integer
        FileName : Optional, String, str, String

        Returns

        String : If strFileName is not specified, the current bump bitmap filename if successful.
        String : If strFileName is specified, the previous bump bitmap filename if successful.
        Null : It not successful, or on error.

        """

        return self._ApplyTypes_(177, 1, (12, 0), ((2, 0), (8, 0),), u'MaterialBump', None, material_index, file_name)

    def material_color(self, material_index, color):
        """

        Returns or modifies a material's diffuse color.  Material colors are represented as RGB colors.  An RGB color specifies the relative intensity of red, green, and blue to cause a specific color to be displayed.

        Parameters

        MaterialIndex : Required, Number, int, Integer
        Color : Optional, Number, lng, Integer

        Returns

        Number : If lngColor is not specified, the current material color if successful.
        Number : If lngColor is specified, the previous material color if successful.
        Null : It not successful, or on error.

        """

        return self._ApplyTypes_(178, 1, (12, 0), ((2, 0), (3, 0),), u'MaterialColor', None, material_index, color)

    def material_environment_map(self, material_index, file_name):
        """

        Returns or modifies a material's environment bitmap filename.

        Parameters

        MaterialIndex : Required, Number, int, Integer
        FileName : Optional, String, str, String

        Returns

        String : If strFileName is not specified, the current environment bitmap filename if successful.
        String : If strFileName is specified, the previous environment bitmap filename if successful.
        Null : It not successful, or on error.

        """

        return self._ApplyTypes_(754, 1, (12, 0), ((2, 0), (8, 0),), u'MaterialEnvironmentMap', None, material_index, file_name)

    def material_name(self, material_index, name):
        """

        Returns or modifies a material's user-definable name.

        Parameters

        MaterialIndex : Required, Number, int, Integer
        Name : Optional, String, str, String

        Returns

        String : If strName is not specified, the current material name if successful.
        String : If strName is specified, the previous material name if successful.
        Null : It not successful, or on error.

        """

        return self._ApplyTypes_(179, 1, (12, 0), ((2, 0), (8, 0),), u'MaterialName', None, material_index, name)

    def material_reflective_color(self, material_index, color):
        """

        Returns or modifies a material's reflective color.  Reflective colors are represented as RGB colors.  An RGB color specifies the relative intensity of red, green, and blue to cause a specific color to be displayed.

        Parameters

        MaterialIndex : Required, Number, int, Integer
        Color : Optional, Number, lng, Integer

        Returns

        Number : If lngColor is not specified, the current reflective color if successful.
        Number : If lngColor is specified, the previous reflective color if successful.
        Null : It not successful, or on error.

        """

        return self._ApplyTypes_(180, 1, (12, 0), ((2, 0), (3, 0),), u'MaterialReflectiveColor', None, material_index, color)

    def material_shine(self, material_index, shine):
        """

        Returns or modifies a material's shine value.

        Parameters

        MaterialIndex : Required, Number, int, Integer
        Shine : Optional, Number, dbl, Double

        Returns

        Number : If dblShine is not specified, the current shine value if successful.
        Number : If dblShine is specified, the previous shine value if successful.
        Null : It not successful, or on error.

        """

        return self._ApplyTypes_(181, 1, (12, 0), ((2, 0), (5, 0),), u'MaterialShine', None, material_index, shine)

    def material_texture(self, material_index, file_name):
        """

        Returns or modifies a material's texture bitmap filename.

        Parameters

        MaterialIndex : Required, Number, int, Integer
        FileName : Optional, String, str, String

        Returns

        String : If strFileName is not specified, the current texture bitmap filename if successful.
        String : If strFileName is specified, the previous texture bitmap filename if successful.
        Null : It not successful, or on error.

        """

        return self._ApplyTypes_(182, 1, (12, 0), ((2, 0), (8, 0),), u'MaterialTexture', None, material_index, file_name)

    def material_transparency(self, material_index, transparency):
        """

        Returns or modifies a material's transparency value.

        Parameters

        MaterialIndex : Required, Number, int, Integer
        Transparency : Optional, Number, dbl, Double

        Returns

        Number : If dblTransparency is not specified, the current transparency value if successful.
        Number : If dblTransparency is specified, the previous transparency value if successful.
        Null : It not successful, or on error.

        """

        return self._ApplyTypes_(183, 1, (12, 0), ((2, 0), (5, 0),), u'MaterialTransparency', None, material_index, transparency)

    def material_transparency_map(self, material_index, file_name):
        """

        Returns or modifies a material's transparency bitmap filename.

        Parameters

        MaterialIndex : Required, Number, int, Integer
        FileName : Optional, String, str, String

        Returns

        String : If strFileName is not specified, the current transparency bitmap filename if successful.
        String : If strFileName is specified, the previous transparency bitmap filename if successful.
        Null : It not successful, or on error.

        """

        return self._ApplyTypes_(753, 1, (12, 0), ((2, 0), (8, 0),), u'MaterialTransparencyMap', None, material_index, file_name)

