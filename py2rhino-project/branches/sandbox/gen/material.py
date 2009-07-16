# Auto-generated wrapper for Rhino4 RhinoScript functions
import win32com.client.CLSIDToClass, pythoncom
import win32com.client.util
from pywintypes import IID
from win32com.client import Dispatch
from win32com.client import DispatchBaseClass
class Material(DispatchBaseClass):



    def add_material_to_layer(self, str_object):
        """

        Adds a material to a layer and returns the new material's index.  If the layer already has a material, then the layer's current material index is returned.

        Parameters

        strObject : Required, String, The name of an existing layer

        Returns

        Number : The zero-based material index of the layer if successful.
        Null : If not successful, or on error.

        """

        return self._ApplyTypes_(id, 1, (returns), (params), u'AddMaterialToLayer', None, strObject)

    def add_material_to_object(self, str_object):
        """

        Adds a material to an object and returns the new material's index.  Note, adding a material to an object modifies the object's material source from "By Layer" to "By Object."  See ObjectMaterialSource for details.  If the object already has a material, then the object's current material index is returned.

        Parameters

        strObject : Required, String, The identifier of the object

        Returns

        Number : The zero-based material index of the object if successful.
        Null : If not successful, or on error.

        """

        return self._ApplyTypes_(id, 1, (returns), (params), u'AddMaterialToObject', None, strObject)

    def copy_material(self, int_src_index, int_dst_index):
        """

        Copies the definition of a source material to a destination material.

        Parameters

        intSrcIndex : Required, Number, The index of the source material
        intDstIndex : Required, Number, The index of the destination material

        Returns

        Boolean : True or false indicating success or failure.
        Null : On error.

        """

        return self._ApplyTypes_(id, 1, (returns), (params), u'CopyMaterial', None, intSrcIndex, intDstIndex)

    def is_material_default(self, int_material_index):
        """

        Verifies that a material is a copy of Rhino's built-in "default" material.  The default material is used by objects and layers that have not been assigned a material.

        Parameters

        intMaterialIndex : Required, Number, The zero-based material index

        Returns

        Null : On error.

        """

        return self._ApplyTypes_(id, 1, (returns), (params), u'IsMaterialDefault', None, intMaterialIndex)

    def is_material_reference(self, int_material_index):
        """

        Verifies a material is referenced from another file.

        Parameters

        intMaterialIndex : Required, Number, The zero-based material index

        Returns

        Boolean : True if successful, otherwise False.
        Null : On error.

        """

        return self._ApplyTypes_(id, 1, (returns), (params), u'IsMaterialReference', None, intMaterialIndex)

        """


        METHOD NOT IMPLEMENTED DUE TO PARAMETER MISMATCH


        """

        raise exceptions.NotImplementedError

    def material_bump(self, int_material_index, str_file_name):
        """

        Returns or modifies a material's bump bitmap filename.

        Parameters

        intMaterialIndex : Required, Number, The zero-based source material index
        strFileName : Optional, String, The bump bitmap filename

        Returns

        String : If strFileName is not specified, the current bump bitmap filename if successful.
        String : If strFileName is specified, the previous bump bitmap filename if successful.
        Null : It not successful, or on error.

        """

        return self._ApplyTypes_(id, 1, (returns), (params), u'MaterialBump', None, intMaterialIndex, strFileName)

    def material_color(self, int_material_index, lng_color):
        """

        Returns or modifies a material's diffuse color.  Material colors are represented as RGB colors.  An RGB color specifies the relative intensity of red, green, and blue to cause a specific color to be displayed.

        Parameters

        intMaterialIndex : Required, Number, The zero-based source material index
        lngColor : Optional, Number, The new color value

        Returns

        Number : If lngColor is not specified, the current material color if successful.
        Number : If lngColor is specified, the previous material color if successful.
        Null : It not successful, or on error.

        """

        return self._ApplyTypes_(id, 1, (returns), (params), u'MaterialColor', None, intMaterialIndex, lngColor)

    def material_environment_map(self, int_material_index, str_file_name):
        """

        Returns or modifies a material's environment bitmap filename.

        Parameters

        intMaterialIndex : Required, Number, The zero-based source material index
        strFileName : Optional, String, The environment bitmap filename

        Returns

        String : If strFileName is not specified, the current environment bitmap filename if successful.
        String : If strFileName is specified, the previous environment bitmap filename if successful.
        Null : It not successful, or on error.

        """

        return self._ApplyTypes_(id, 1, (returns), (params), u'MaterialEnvironmentMap', None, intMaterialIndex, strFileName)

    def material_name(self, int_material_index, str_name):
        """

        Returns or modifies a material's user-definable name.

        Parameters

        intMaterialIndex : Required, Number, The zero-based source material index
        strName : Optional, String, The new name

        Returns

        String : If strName is not specified, the current material name if successful.
        String : If strName is specified, the previous material name if successful.
        Null : It not successful, or on error.

        """

        return self._ApplyTypes_(id, 1, (returns), (params), u'MaterialName', None, intMaterialIndex, strName)

    def material_reflective_color(self, int_material_index, lng_color):
        """

        Returns or modifies a material's reflective color.  Reflective colors are represented as RGB colors.  An RGB color specifies the relative intensity of red, green, and blue to cause a specific color to be displayed.

        Parameters

        intMaterialIndex : Required, Number, The zero-based source material index
        lngColor : Optional, Number, The new color value

        Returns

        Number : If lngColor is not specified, the current reflective color if successful.
        Number : If lngColor is specified, the previous reflective color if successful.
        Null : It not successful, or on error.

        """

        return self._ApplyTypes_(id, 1, (returns), (params), u'MaterialReflectiveColor', None, intMaterialIndex, lngColor)

    def material_shine(self, int_material_index, dbl_shine):
        """

        Returns or modifies a material's shine value.

        Parameters

        intMaterialIndex : Required, Number, The zero-based source material index
        dblShine : Optional, Number, The new shine value

        Returns

        Number : If dblShine is not specified, the current shine value if successful.
        Number : If dblShine is specified, the previous shine value if successful.
        Null : It not successful, or on error.

        """

        return self._ApplyTypes_(id, 1, (returns), (params), u'MaterialShine', None, intMaterialIndex, dblShine)

    def material_texture(self, int_material_index, str_file_name):
        """

        Returns or modifies a material's texture bitmap filename.

        Parameters

        intMaterialIndex : Required, Number, The zero-based source material index
        strFileName : Optional, String, The texture bitmap filename

        Returns

        String : If strFileName is not specified, the current texture bitmap filename if successful.
        String : If strFileName is specified, the previous texture bitmap filename if successful.
        Null : It not successful, or on error.

        """

        return self._ApplyTypes_(id, 1, (returns), (params), u'MaterialTexture', None, intMaterialIndex, strFileName)

    def material_transparency(self, int_material_index, dbl_transparency):
        """

        Returns or modifies a material's transparency value.

        Parameters

        intMaterialIndex : Required, Number, The zero-based source material index
        dblTransparency : Optional, Number, The new transparency value

        Returns

        Number : If dblTransparency is not specified, the current transparency value if successful.
        Number : If dblTransparency is specified, the previous transparency value if successful.
        Null : It not successful, or on error.

        """

        return self._ApplyTypes_(id, 1, (returns), (params), u'MaterialTransparency', None, intMaterialIndex, dblTransparency)

    def material_transparency_map(self, int_material_index, str_file_name):
        """

        Returns or modifies a material's transparency bitmap filename.

        Parameters

        intMaterialIndex : Required, Number, The zero-based source material index
        strFileName : Optional, String, The transparency bitmap filename

        Returns

        String : If strFileName is not specified, the current transparency bitmap filename if successful.
        String : If strFileName is specified, the previous transparency bitmap filename if successful.
        Null : It not successful, or on error.

        """

        return self._ApplyTypes_(id, 1, (returns), (params), u'MaterialTransparencyMap', None, intMaterialIndex, strFileName)

