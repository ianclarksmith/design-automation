# Auto-generated wrapper for Rhino4 RhinoScript functions

import exceptions
from py2rhino._util import *
from py2rhino._rhinoscript import IRhinoScript

class Light(IRhinoScript):



    def add_directional_light(self, start_point, end_point):
        """        
        Adds a new directional light object  to the document.
    
        Parameters
        ==========

        start_point, Array of ????, Required        
        The 3-D starting point of the light.
            
        end_point, Array of ????, Required        
        The 3-D ending point and direction of the light.
            
        Returns
        =======

        string
        The identifier of the new object if successful.

        null
        If not successful, or on error.

        """

        params = [start_point, end_point]
        params_opt_or_req = [Required, Required]
        params_magic_numbers = [(VT_VARIANT, 1), (VT_VARIANT, 1)]
        params_flattened = [flatten(start_point), flatten(end_point)]

        for i in range(len(params)):
            if (params[i] == None) and (params_opt_or_req[i] = "Optional"):
                params_magic_numbers.pop(i)
                params_flattened.pop(i)

        return self._ApplyTypes_(153, 1, (VT_VARIANT, 0), params_magic_numbers, u"AddDirectionalLight", None, *params_flattened)

    def add_linear_light(self, start_point, end_point, width=None):
        """        
        Adds a new linear light object  to the document.
    
        Parameters
        ==========

        start_point, Array of ????, Required        
        The 3-D starting point of the light.
            
        end_point, Array of ????, Required        
        The 3-D ending point and direction of the light.
            
        width, Double, Optional        
        The width of the light.
            
        Returns
        =======

        string
        The identifier of the new object if successful.

        null
        If not successful, or on error.

        """

        params = [start_point, end_point, width]
        params_opt_or_req = [Required, Required, Optional]
        params_magic_numbers = [(VT_VARIANT, 1), (VT_VARIANT, 1), (VT_R8, 1)]
        params_flattened = [flatten(start_point), flatten(end_point), width]

        for i in range(len(params)):
            if (params[i] == None) and (params_opt_or_req[i] = "Optional"):
                params_magic_numbers.pop(i)
                params_flattened.pop(i)

        return self._ApplyTypes_(154, 1, (VT_VARIANT, 0), params_magic_numbers, u"AddLinearLight", None, *params_flattened)

    def add_point_light(self, point):
        """        
        Adds a new point light object  to the document.
    
        Parameters
        ==========

        point, Array of ????, Required        
        The 3-D location point of the light.
            
        Returns
        =======

        string
        The identifier of the new object if successful.

        null
        If not successful, or on error.

        """

        params = [point]
        params_opt_or_req = [Required]
        params_magic_numbers = [(VT_VARIANT, 1),]
        params_flattened = [flatten(point)]

        for i in range(len(params)):
            if (params[i] == None) and (params_opt_or_req[i] = "Optional"):
                params_magic_numbers.pop(i)
                params_flattened.pop(i)

        return self._ApplyTypes_(155, 1, (VT_VARIANT, 0), params_magic_numbers, u"AddPointLight", None, *params_flattened)

    def add_rectangular_light(self, origin, width, height):
        """        
        Adds a new rectangular light object  to the document.
    
        Parameters
        ==========

        origin, Array of ????, Required        
        The 3-D origin point of the light.
            
        width, Array of ????, Required        
        The 3-D width and direction point of the light.
            
        height, Array of ????, Required        
        The 3-D height and direction point of the light.
            
        Returns
        =======

        string
        The identifier of the new object if successful.

        null
        If not successful, or on error.

        """

        params = [origin, width, height]
        params_opt_or_req = [Required, Required, Required]
        params_magic_numbers = [(VT_VARIANT, 1), (VT_VARIANT, 1), (VT_VARIANT, 1)]
        params_flattened = [flatten(origin), flatten(width), flatten(height)]

        for i in range(len(params)):
            if (params[i] == None) and (params_opt_or_req[i] = "Optional"):
                params_magic_numbers.pop(i)
                params_flattened.pop(i)

        return self._ApplyTypes_(156, 1, (VT_VARIANT, 0), params_magic_numbers, u"AddRectangularLight", None, *params_flattened)

    def add_spot_light(self, origin, radius, apex):
        """        
        Adds a new spot light object  to the document.
    
        Parameters
        ==========

        origin, Array of ????, Required        
        The 3-D origin point of the light.
            
        radius, Double, Required        
        The radius of the cone.
            
        apex, Array of ????, Required        
        The 3-D apex point of the light.
            
        Returns
        =======

        string
        The identifier of the new object if successful.

        null
        If not successful, or on error.

        """

        params = [origin, radius, apex]
        params_opt_or_req = [Required, Required, Required]
        params_magic_numbers = [(VT_VARIANT, 1), (VT_R8, 1), (VT_VARIANT, 1)]
        params_flattened = [flatten(origin), radius, flatten(apex)]

        for i in range(len(params)):
            if (params[i] == None) and (params_opt_or_req[i] = "Optional"):
                params_magic_numbers.pop(i)
                params_flattened.pop(i)

        return self._ApplyTypes_(157, 1, (VT_VARIANT, 0), params_magic_numbers, u"AddSpotLight", None, *params_flattened)

    def enable_light(self, object, enable=None):
        """        
        Enables or disables a light object.
    
        Parameters
        ==========

        object, String, Required        
        The identifier of the light object
            
        enable, Boolean, Optional        
        The light's enabled status.
            
        Returns
        =======

        boolean
        If blnEnable is not specified, then the current enabled status if successful.

        boolean
        If blnEnable is specified, then the previous enabled status if successful.

        null
        If not successful, or on error.

        """

        params = [object, enable]
        params_opt_or_req = [Required, Optional]
        params_magic_numbers = [(VT_BSTR, 1), (VT_BOOL, 1)]
        params_flattened = [object, enable]

        for i in range(len(params)):
            if (params[i] == None) and (params_opt_or_req[i] = "Optional"):
                params_magic_numbers.pop(i)
                params_flattened.pop(i)

        return self._ApplyTypes_(158, 1, (VT_VARIANT, 0), params_magic_numbers, u"EnableLight", None, *params_flattened)

    def is_directional_light(self, object):
        """        
        Verifies a light object is a directional light.
    
        Parameters
        ==========

        object, String, Required        
        The light object's identifier.
            
        Returns
        =======

        boolean
        True if successful, otherwise False.

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

        return self._ApplyTypes_(159, 1, (VT_VARIANT, 0), params_magic_numbers, u"IsDirectionalLight", None, *params_flattened)

    def is_light(self, object):
        """        
        Verifies an object is a light object.
    
        Parameters
        ==========

        object, String, Required        
        The light object's identifier.
            
        Returns
        =======

        boolean
        True if successful, otherwise False.

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

        return self._ApplyTypes_(160, 1, (VT_VARIANT, 0), params_magic_numbers, u"IsLight", None, *params_flattened)

    def is_light_enabled(self, object):
        """        
        Verifies a light object is enabled.
    
        Parameters
        ==========

        object, String, Required        
        The light object's identifier.
            
        Returns
        =======

        boolean
        True if successful, otherwise False.

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

        return self._ApplyTypes_(161, 1, (VT_VARIANT, 0), params_magic_numbers, u"IsLightEnabled", None, *params_flattened)

    def is_light_reference(self, object):
        """        
        Verifies a light object is referenced from another file.
    
        Parameters
        ==========

        object, String, Required        
        The light object's identifier.
            
        Returns
        =======

        boolean
        True if successful, otherwise False.

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

        return self._ApplyTypes_(162, 1, (VT_VARIANT, 0), params_magic_numbers, u"IsLightReference", None, *params_flattened)

    def is_linear_light(self, object):
        """        
        Verifies a light object is a linear light.
    
        Parameters
        ==========

        object, String, Required        
        The light object's identifier.
            
        Returns
        =======

        boolean
        True if successful, otherwise False.

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

        return self._ApplyTypes_(163, 1, (VT_VARIANT, 0), params_magic_numbers, u"IsLinearLight", None, *params_flattened)

    def is_point_light(self, object):
        """        
        Verifies a light object is a point light.
    
        Parameters
        ==========

        object, String, Required        
        The light object's identifier.
            
        Returns
        =======

        boolean
        True if successful, otherwise False.

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

        return self._ApplyTypes_(164, 1, (VT_VARIANT, 0), params_magic_numbers, u"IsPointLight", None, *params_flattened)

    def is_rectangular_light(self, object):
        """        
        Verifies a light object is a rectangular light.
    
        Parameters
        ==========

        object, String, Required        
        The light object's identifier.
            
        Returns
        =======

        boolean
        True if successful, otherwise False.

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

        return self._ApplyTypes_(165, 1, (VT_VARIANT, 0), params_magic_numbers, u"IsRectangularLight", None, *params_flattened)

    def is_spot_light(self, object):
        """        
        Verifies a light object is a spot light.
    
        Parameters
        ==========

        object, String, Required        
        The light object's identifier.
            
        Returns
        =======

        boolean
        True if successful, otherwise False.

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

        return self._ApplyTypes_(166, 1, (VT_VARIANT, 0), params_magic_numbers, u"IsSpotLight", None, *params_flattened)

    def light_color(self, object, color=None):
        """        
        Returns or changes the color of a light.  Light colors are represented as RGB colors.   An RGB color specifies the relative intensity of red, green, and blue to cause a specific color to be displayed.
    
        Parameters
        ==========

        object, String, Required        
        The light object's identifier.
            
        color, Integer, Optional        
        The new color value.  If omitted, the current light color is returned.
            
        Returns
        =======

        number
        If a color value  is not specified,  the current light value if successful.

        number
        If a color value is specified, the previous light value if successful.

        null
        If not successful, or on error.

        """

        params = [object, color]
        params_opt_or_req = [Required, Optional]
        params_magic_numbers = [(VT_BSTR, 1), (VT_I4, 1)]
        params_flattened = [object, color]

        for i in range(len(params)):
            if (params[i] == None) and (params_opt_or_req[i] = "Optional"):
                params_magic_numbers.pop(i)
                params_flattened.pop(i)

        return self._ApplyTypes_(167, 1, (VT_VARIANT, 0), params_magic_numbers, u"LightColor", None, *params_flattened)

    def light_count):
        """        
        Returns the number of light objects in the document.
    
        No parameters

        Returns
        =======

        number
        The number of lights in the document.

        """

        params = []
        params_opt_or_req = []
        params_magic_numbers = []
        params_flattened = []

        for i in range(len(params)):
            if (params[i] == None) and (params_opt_or_req[i] = "Optional"):
                params_magic_numbers.pop(i)
                params_flattened.pop(i)

        return self._ApplyTypes_(168, 1, (VT_VARIANT, 0), params_magic_numbers, u"LightCount", None, *params_flattened)

    def light_direction(self, object, direction=None):
        """        
        Returns or changes the direction of a light object. This function can be used to return or modify the target of spotlights.
    
        Parameters
        ==========

        object, String, Required        
        The light object's identifier.
            
        direction, Array of ????, Optional        
        The new end point, or direction.  If omitted, the direction point is returned.
            
        Returns
        =======

        array
        If a direction point is not specified,  the current direction if successful.

        array
        If a direction point is specified, the previous direction point if successful.

        null
        If not successful, or on error.

        """

        params = [object, direction]
        params_opt_or_req = [Required, Optional]
        params_magic_numbers = [(VT_BSTR, 1), (VT_VARIANT, 1)]
        params_flattened = [object, flatten(direction)]

        for i in range(len(params)):
            if (params[i] == None) and (params_opt_or_req[i] = "Optional"):
                params_magic_numbers.pop(i)
                params_flattened.pop(i)

        return self._ApplyTypes_(491, 1, (VT_VARIANT, 0), params_magic_numbers, u"LightDirection", None, *params_flattened)

    def light_location(self, object, location=None):
        """        
        Returns or changes the location of a light object.
    
        Parameters
        ==========

        object, String, Required        
        The light object's identifier.
            
        location, Array of ????, Optional        
        The new start point, or location.  If omitted, the location point is returned.
            
        Returns
        =======

        array
        If a location point is not specified,  the current location if successful.

        array
        If a location point is specified, the previous location point if successful.

        null
        If not successful, or on error.

        """

        params = [object, location]
        params_opt_or_req = [Required, Optional]
        params_magic_numbers = [(VT_BSTR, 1), (VT_VARIANT, 1)]
        params_flattened = [object, flatten(location)]

        for i in range(len(params)):
            if (params[i] == None) and (params_opt_or_req[i] = "Optional"):
                params_magic_numbers.pop(i)
                params_flattened.pop(i)

        return self._ApplyTypes_(490, 1, (VT_VARIANT, 0), params_magic_numbers, u"LightLocation", None, *params_flattened)

    def light_name(self, object, name=None):
        """        
        Returns or modifies the user-definable name of a light object.
    
        Parameters
        ==========

        object, String, Required        
        The identifier of the light object.
            
        name, String, Optional        
        The new light name.  If omitted, the current light name is returned.
            
        Returns
        =======

        string
        If strName is not specified,  the current light name if successful.

        string
        If strName is specified,  the previous light name if successful.

        null
        If not successful, or on error.

        """

        params = [object, name]
        params_opt_or_req = [Required, Optional]
        params_magic_numbers = [(VT_BSTR, 1), (VT_BSTR, 1)]
        params_flattened = [object, name]

        for i in range(len(params)):
            if (params[i] == None) and (params_opt_or_req[i] = "Optional"):
                params_magic_numbers.pop(i)
                params_flattened.pop(i)

        return self._ApplyTypes_(169, 1, (VT_VARIANT, 0), params_magic_numbers, u"LightName", None, *params_flattened)

    def light_objects):
        """        
        Returns the identifier of light objects in the document.
    
        No parameters

        Returns
        =======

        array
        The identifiers of all lights in the document if successful

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

        return self._ApplyTypes_(170, 1, (VT_VARIANT, 0), params_magic_numbers, u"LightObjects", None, *params_flattened)

    def rectangular_light_plane(self, object):
        """        
        Returns the plane of a rectangular light object.
    
        Parameters
        ==========

        object, String, Required        
        The light object's identifier.
            
        Returns
        =======

        array
        The plane if successful.  The elements of a plane array are as follows:

        array
        The plane's origin (3-D point).

        array
        The plane's X axis direction (3-D vector).

        array
        The plane's Y axis direction (3-D vector).

        array
        The plane's Z axis direction (3-D vector).

        null
        If not successful, or on error.

        """

        params = [object]
        params_opt_or_req = [Required]
        params_magic_numbers = [(VT_BSTR, 1),]
        params_flattened = [object]

        for i in range(len(params)):
            if (params[i] == None) and (params_opt_or_req[i] = "Optional"):
                params_magic_numbers.pop(i)
                params_flattened.pop(i)

        return self._ApplyTypes_(776, 1, (VT_VARIANT, 0), params_magic_numbers, u"RectangularLightPlane", None, *params_flattened)

    def spot_light_hardness(self, object, hardness=None):
        """        
        Returns or changes the hardness of a spot light.  Spotlight hardness controls the fully illuminated region.
    
        Parameters
        ==========

        object, String, Required        
        The light object's identifier.
            
        hardness, Double, Optional        
        The new hardness value.  A spot light's hardness values ranges from 0.0 to 1.0.  If omitted, the current hardness value is returned.
            
        Returns
        =======

        number
        If dblHardness is not specified, then  the current hardness value if successful.

        number
        If dblHardness is specified, then the previous hardness value if successful.

        null
        If not successful, or on error.

        """

        params = [object, hardness]
        params_opt_or_req = [Required, Optional]
        params_magic_numbers = [(VT_BSTR, 1), (VT_R8, 1)]
        params_flattened = [object, hardness]

        for i in range(len(params)):
            if (params[i] == None) and (params_opt_or_req[i] = "Optional"):
                params_magic_numbers.pop(i)
                params_flattened.pop(i)

        return self._ApplyTypes_(171, 1, (VT_VARIANT, 0), params_magic_numbers, u"SpotLightHardness", None, *params_flattened)

    def spot_light_radius(self, object, radius=None):
        """        
        Returns or changes the radius of a spot light.
    
        Parameters
        ==========

        object, String, Required        
        The light object's identifier.
            
        radius, Double, Optional        
        The new radius value.  If omitted, the current radius value is returned.
            
        Returns
        =======

        number
        If dblRadius is not specified, then the current radius value if successful.

        number
        If dblRadius is specified, then the previous radius value if successful.

        null
        If not successful, or on error.

        """

        params = [object, radius]
        params_opt_or_req = [Required, Optional]
        params_magic_numbers = [(VT_BSTR, 1), (VT_R8, 1)]
        params_flattened = [object, radius]

        for i in range(len(params)):
            if (params[i] == None) and (params_opt_or_req[i] = "Optional"):
                params_magic_numbers.pop(i)
                params_flattened.pop(i)

        return self._ApplyTypes_(584, 1, (VT_VARIANT, 0), params_magic_numbers, u"SpotLightRadius", None, *params_flattened)

    def spot_light_shadow_intensity(self, object, intensity=None):
        """        
        Returns or modifies the shadow intensity of a spot light.
    
        Parameters
        ==========

        object, String, Required        
        The light object's identifier.
            
        intensity, Double, Optional        
        The new shadow intensity.  A spot light's shadow intensity ranges from 0.0 to 1.0.  If set to 0.0, the spot light will cast no shadows.  If set to 1.0, the spot light will cast black shadows.  If omitted, the current shadow intensity is returned.
            
        Returns
        =======

        number
        If dblIntensity is not specified, then the current shadow intensity if successful.

        number
        If dblIntensity is specified, then the previous shadow intensity if successful.

        null
        If not successful, or on error.

        """

        params = [object, intensity]
        params_opt_or_req = [Required, Optional]
        params_magic_numbers = [(VT_BSTR, 1), (VT_R8, 1)]
        params_flattened = [object, intensity]

        for i in range(len(params)):
            if (params[i] == None) and (params_opt_or_req[i] = "Optional"):
                params_magic_numbers.pop(i)
                params_flattened.pop(i)

        return self._ApplyTypes_(172, 1, (VT_VARIANT, 0), params_magic_numbers, u"SpotLightShadowIntensity", None, *params_flattened)

