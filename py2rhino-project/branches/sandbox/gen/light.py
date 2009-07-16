# Auto-generated wrapper for Rhino4 RhinoScript functions
import win32com.client.CLSIDToClass, pythoncom
import win32com.client.util
from pywintypes import IID
from win32com.client import Dispatch
from win32com.client import DispatchBaseClass
import exceptions
class Light(DispatchBaseClass):



    def add_directional_light(self, start_point, end_point):
        """

        Adds a new directional light object  to the document.

        Parameters

        StartPoint : Required, Array, arr
        EndPoint : Required, Array, arr

        Returns

        String : The identifier of the new object if successful.
        Null : If not successful, or on error.

        """

        return self._ApplyTypes_(153, 1, (12, 0), ((12, 0), (12, 0)), u'AddDirectionalLight', None, start_point, end_point)

    def add_linear_light(self, start_point, end_point, width):
        """

        Adds a new linear light object  to the document.

        Parameters

        StartPoint : Required, Array, arr
        EndPoint : Required, Array, arr
        Width : Optional, Number, dbl

        Returns

        String : The identifier of the new object if successful.
        Null : If not successful, or on error.

        """

        return self._ApplyTypes_(154, 1, (12, 0), ((12, 0), (12, 0), (12, 0)), u'AddLinearLight', None, start_point, end_point, width)

    def add_point_light(self, point):
        """

        Adds a new point light object  to the document.

        Parameters

        Point : Required, Array, arr

        Returns

        String : The identifier of the new object if successful.
        Null : If not successful, or on error.

        """

        return self._ApplyTypes_(155, 1, (12, 0), ((12, 0)), u'AddPointLight', None, point)

    def add_rectangular_light(self, origin, width, height):
        """

        Adds a new rectangular light object  to the document.

        Parameters

        Origin : Required, Array, arr
        Width : Required, Array, arr
        Height : Required, Array, arr

        Returns

        String : The identifier of the new object if successful.
        Null : If not successful, or on error.

        """

        return self._ApplyTypes_(156, 1, (12, 0), ((12, 0), (12, 0), (12, 0)), u'AddRectangularLight', None, origin, width, height)

    def add_spot_light(self, origin, radius, apex):
        """

        Adds a new spot light object  to the document.

        Parameters

        Origin : Required, Array, arr
        Radius : Required, Number, dbl
        Apex : Required, Array, arr

        Returns

        String : The identifier of the new object if successful.
        Null : If not successful, or on error.

        """

        return self._ApplyTypes_(157, 1, (12, 0), ((12, 0), (12, 0), (12, 0)), u'AddSpotLight', None, origin, radius, apex)

    def enable_light(self, object, enable):
        """

        Enables or disables a light object.

        Parameters

        Object : Required, String, str
        Enable : Optional, Boolean, bln

        Returns

        Boolean : If blnEnable is not specified, then the current enabled status if successful.
        Boolean : If blnEnable is specified, then the previous enabled status if successful.
        Null : If not successful, or on error.

        """

        return self._ApplyTypes_(158, 1, (12, 0), ((12, 0), (12, 0)), u'EnableLight', None, object, enable)

    def is_directional_light(self, object):
        """

        Verifies a light object is a directional light.

        Parameters

        Object : Required, String, str

        Returns

        Boolean : True if successful, otherwise False.
        Null : On error.

        """

        return self._ApplyTypes_(159, 1, (12, 0), ((12, 0)), u'IsDirectionalLight', None, object)

    def is_light(self, object):
        """

        Verifies an object is a light object.

        Parameters

        Object : Required, String, str

        Returns

        Boolean : True if successful, otherwise False.
        Null : On error.

        """

        return self._ApplyTypes_(160, 1, (12, 0), ((12, 0)), u'IsLight', None, object)

    def is_light_enabled(self, object):
        """

        Verifies a light object is enabled.

        Parameters

        Object : Required, String, str

        Returns

        Boolean : True if successful, otherwise False.
        Null : On error.

        """

        return self._ApplyTypes_(161, 1, (12, 0), ((12, 0)), u'IsLightEnabled', None, object)

    def is_light_reference(self, object):
        """

        Verifies a light object is referenced from another file.

        Parameters

        Object : Required, String, str

        Returns

        Boolean : True if successful, otherwise False.
        Null : On error.

        """

        return self._ApplyTypes_(162, 1, (12, 0), ((12, 0)), u'IsLightReference', None, object)

    def is_linear_light(self, object):
        """

        Verifies a light object is a linear light.

        Parameters

        Object : Required, String, str

        Returns

        Boolean : True if successful, otherwise False.
        Null : On error.

        """

        return self._ApplyTypes_(163, 1, (12, 0), ((12, 0)), u'IsLinearLight', None, object)

    def is_point_light(self, object):
        """

        Verifies a light object is a point light.

        Parameters

        Object : Required, String, str

        Returns

        Boolean : True if successful, otherwise False.
        Null : On error.

        """

        return self._ApplyTypes_(164, 1, (12, 0), ((12, 0)), u'IsPointLight', None, object)

    def is_rectangular_light(self, object):
        """

        Verifies a light object is a rectangular light.

        Parameters

        Object : Required, String, str

        Returns

        Boolean : True if successful, otherwise False.
        Null : On error.

        """

        return self._ApplyTypes_(165, 1, (12, 0), ((12, 0)), u'IsRectangularLight', None, object)

    def is_spot_light(self, object):
        """

        Verifies a light object is a spot light.

        Parameters

        Object : Required, String, str

        Returns

        Boolean : True if successful, otherwise False.
        Null : On error.

        """

        return self._ApplyTypes_(166, 1, (12, 0), ((12, 0)), u'IsSpotLight', None, object)

    def light_color(self, object, color):
        """

        Returns or changes the color of a light.  Light colors are represented as RGB colors.   An RGB color specifies the relative intensity of red, green, and blue to cause a specific color to be displayed.

        Parameters

        Object : Required, String, str
        Color : Optional, Number, lng

        Returns

        Number : If a color value  is not specified,  the current light value if successful.
        Number : If a color value is specified, the previous light value if successful.
        Null : If not successful, or on error.

        """

        return self._ApplyTypes_(167, 1, (12, 0), ((12, 0), (12, 0)), u'LightColor', None, object, color)

    def light_count(self):
        """

        Returns the number of light objects in the document.

        No parameters

        Returns

        Number : The number of lights in the document.

        """

        return self._ApplyTypes_(168, 1, (12, 0), (), u'LightCount', None, )

    def light_direction(self, object, direction):
        """

        Returns or changes the direction of a light object. This function can be used to return or modify the target of spotlights.

        Parameters

        Object : Required, String, str
        Direction : Optional, Array, arr

        Returns

        Array : If a direction point is not specified,  the current direction if successful.
        Array : If a direction point is specified, the previous direction point if successful.
        Null : If not successful, or on error.

        """

        return self._ApplyTypes_(491, 1, (12, 0), ((12, 0), (12, 0)), u'LightDirection', None, object, direction)

    def light_location(self, object, location):
        """

        Returns or changes the location of a light object.

        Parameters

        Object : Required, String, str
        location : Optional, Array, arr

        Returns

        Array : If a location point is not specified,  the current location if successful.
        Array : If a location point is specified, the previous location point if successful.
        Null : If not successful, or on error.

        """

        return self._ApplyTypes_(490, 1, (12, 0), ((12, 0), (12, 0)), u'LightLocation', None, object, location)

    def light_name(self, object, name):
        """

        Returns or modifies the user-definable name of a light object.

        Parameters

        Object : Required, String, str
        Name : Optional, String, str

        Returns

        String : If strName is not specified,  the current light name if successful.
        String : If strName is specified,  the previous light name if successful.
        Null : If not successful, or on error.

        """

        return self._ApplyTypes_(169, 1, (12, 0), ((12, 0), (12, 0)), u'LightName', None, object, name)

    def light_objects(self):
        """

        Returns the identifier of light objects in the document.

        No parameters

        Returns

        Array : The identifiers of all lights in the document if successful
        Null : If not successful, or on error.

        """

        return self._ApplyTypes_(170, 1, (12, 0), (), u'LightObjects', None, )

    def rectangular_light_plane(self, object):
        """

        Returns the plane of a rectangular light object.

        Parameters

        Object : Required, String, str

        Returns

        Array : The plane if successful.  The elements of a plane array are as follows:
        Array : The plane's origin (3-D point).
        Array : The plane's X axis direction (3-D vector).
        Array : The plane's Y axis direction (3-D vector).
        Array : The plane's Z axis direction (3-D vector).
        Null : If not successful, or on error.

        """

        return self._ApplyTypes_(776, 1, (12, 0), ((12, 0)), u'RectangularLightPlane', None, object)

    def spot_light_hardness(self, object, hardness):
        """

        Returns or changes the hardness of a spot light.  Spotlight hardness controls the fully illuminated region.

        Parameters

        Object : Required, String, str
        Hardness : Optional, Number, dbl

        Returns

        Number : If dblHardness is not specified, then  the current hardness value if successful.
        Number : If dblHardness is specified, then the previous hardness value if successful.
        Null : If not successful, or on error.

        """

        return self._ApplyTypes_(171, 1, (12, 0), ((12, 0), (12, 0)), u'SpotLightHardness', None, object, hardness)

    def spot_light_radius(self, object, radius):
        """

        Returns or changes the radius of a spot light.

        Parameters

        Object : Required, String, str
        Radius : Optional, Number, dbl

        Returns

        Number : If dblRadius is not specified, then the current radius value if successful.
        Number : If dblRadius is specified, then the previous radius value if successful.
        Null : If not successful, or on error.

        """

        return self._ApplyTypes_(584, 1, (12, 0), ((12, 0), (12, 0)), u'SpotLightRadius', None, object, radius)

    def spot_light_shadow_intensity(self, object, intensity):
        """

        Returns or modifies the shadow intensity of a spot light.

        Parameters

        Object : Required, String, str
        Intensity : Optional, Number, dbl

        Returns

        Number : If dblIntensity is not specified, then the current shadow intensity if successful.
        Number : If dblIntensity is specified, then the previous shadow intensity if successful.
        Null : If not successful, or on error.

        """

        return self._ApplyTypes_(172, 1, (12, 0), ((12, 0), (12, 0)), u'SpotLightShadowIntensity', None, object, intensity)

