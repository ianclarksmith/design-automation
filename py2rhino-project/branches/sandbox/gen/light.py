# Auto-generated wrapper for Rhino4 RhinoScript functions
import win32com.client.CLSIDToClass, pythoncom
import win32com.client.util
from pywintypes import IID
from win32com.client import Dispatch
from win32com.client import DispatchBaseClass
class Light(DispatchBaseClass):



	def adddirectionallight(self, arrstartpoint, arrendpoint):
		"""

		Adds a new directional light object  to the document.

		Parameters

		arrStartPoint : Required,   Array,  The 3-D starting point of the light
		arrEndPoint : Required,   Array,   The 3-D ending point and direction of the light

		Returns

		String : The identifier of the new object if successful.
		Null : If not successful, or on error.

		"""

		return self._ApplyTypes_(id, 1, (returns), (params), u'AddDirectionalLight', None, arrStartPoint, arrEndPoint)

	def addlinearlight(self, arrstartpoint, arrendpoint, dblwidth):
		"""

		Adds a new linear light object  to the document.

		Parameters

		arrStartPoint : Required,   Array,   The 3-D starting point of the light
		arrEndPoint : Required,   Array,   The 3-D ending point and direction of the light
		dblWidth : Optional,   Number,   The width of the light

		Returns

		String : The identifier of the new object if successful.
		Null : If not successful, or on error.

		"""

		return self._ApplyTypes_(id, 1, (returns), (params), u'AddLinearLight', None, arrStartPoint, arrEndPoint, dblWidth)

	def addpointlight(self, arrpoint):
		"""

		Adds a new point light object  to the document.

		Parameters

		arrPoint : Required,   Array,   The 3-D location point of the light

		Returns

		String : The identifier of the new object if successful.
		Null : If not successful, or on error.

		"""

		return self._ApplyTypes_(id, 1, (returns), (params), u'AddPointLight', None, arrPoint)

	def addrectangularlight(self, arrorigin, arrwidth, arrheight):
		"""

		Adds a new rectangular light object  to the document.

		Parameters

		arrOrigin : Required,   Array,   The 3-D origin point of the light
		arrWidth : Required,   Array,   The 3-D width and direction point of the light
		arrHeight : Required,   Array,   The 3-D height and direction point of the light

		Returns

		String : The identifier of the new object if successful.
		Null : If not successful, or on error.

		"""

		return self._ApplyTypes_(id, 1, (returns), (params), u'AddRectangularLight', None, arrOrigin, arrWidth, arrHeight)

	def addspotlight(self, arrorigin, dblradius, arrapex):
		"""

		Adds a new spot light object  to the document.

		Parameters

		arrOrigin : Required,   Array,   The 3-D origin point of the light
		dblRadius : Required,   Number,   The radius of the cone
		arrApex : Required,   Array,   The 3-D apex point of the light

		Returns

		String : The identifier of the new object if successful.
		Null : If not successful, or on error.

		"""

		return self._ApplyTypes_(id, 1, (returns), (params), u'AddSpotLight', None, arrOrigin, dblRadius, arrApex)

	def enablelight(self, strobject, blnenable):
		"""

		Enables or disables a light object.

		Parameters

		strObject : Required,   String,   The identifier of the light object
		blnEnable : Optional,   Boolean,   The light's enabled status

		Returns

		Boolean : If blnEnable is not specified, then the current enabled status if successful.
		Boolean : If blnEnable is specified, then the previous enabled status if successful.
		Null : If not successful, or on error.

		"""

		return self._ApplyTypes_(id, 1, (returns), (params), u'EnableLight', None, strObject, blnEnable)

	def isdirectionallight(self, strobject):
		"""

		Verifies a light object is a directional light.

		Parameters

		strObject : Required,   String,   The light object's identifier

		Returns

		Boolean : True if successful, otherwise False.
		Null : On error.

		"""

		return self._ApplyTypes_(id, 1, (returns), (params), u'IsDirectionalLight', None, strObject)

	def islight(self, strobject):
		"""

		Verifies an object is a light object.

		Parameters

		strObject : Required,   String,   The light object's identifier

		Returns

		Boolean : True if successful, otherwise False.
		Null : On error.

		"""

		return self._ApplyTypes_(id, 1, (returns), (params), u'IsLight', None, strObject)

	def islightenabled(self, strobject):
		"""

		Verifies a light object is enabled.

		Parameters

		strObject : Required,   String,   The light object's identifier

		Returns

		Boolean : True if successful, otherwise False.
		Null : On error.

		"""

		return self._ApplyTypes_(id, 1, (returns), (params), u'IsLightEnabled', None, strObject)

	def islightreference(self, strobject):
		"""

		Verifies a light object is referenced from another file.

		Parameters

		strObject : Required,   String,   The light object's identifier

		Returns

		Boolean : True if successful, otherwise False.
		Null : On error.

		"""

		return self._ApplyTypes_(id, 1, (returns), (params), u'IsLightReference', None, strObject)

	def islinearlight(self, strobject):
		"""

		Verifies a light object is a linear light.

		Parameters

		strObject : Required,   String,   The light object's identifier

		Returns

		Boolean : True if successful, otherwise False.
		Null : On error.

		"""

		return self._ApplyTypes_(id, 1, (returns), (params), u'IsLinearLight', None, strObject)

	def ispointlight(self, strobject):
		"""

		Verifies a light object is a point light.

		Parameters

		strObject : Required,   String,   The light object's identifier

		Returns

		Boolean : True if successful, otherwise False.
		Null : On error.

		"""

		return self._ApplyTypes_(id, 1, (returns), (params), u'IsPointLight', None, strObject)

	def isrectangularlight(self, strobject):
		"""

		Verifies a light object is a rectangular light.

		Parameters

		strObject : Required,   String,   The light object's identifier

		Returns

		Boolean : True if successful, otherwise False.
		Null : On error.

		"""

		return self._ApplyTypes_(id, 1, (returns), (params), u'IsRectangularLight', None, strObject)

	def isspotlight(self, strobject):
		"""

		Verifies a light object is a spot light.

		Parameters

		strObject : Required,   String,   The light object's identifier

		Returns

		Boolean : True if successful, otherwise False.
		Null : On error.

		"""

		return self._ApplyTypes_(id, 1, (returns), (params), u'IsSpotLight', None, strObject)

	def lightcolor(self, strobject, lngcolor):
		"""

		Returns or changes the color of a light.  Light colors are represented as RGB colors.   An RGB color specifies the relative intensity of red, green, and blue to cause a specific color to be displayed.

		Parameters

		strObject : Required,   String,   The light object's identifier
		lngColor : Optional,   Number,   The new color value

		Returns

		Number : If a color value  is not specified,  the current light value if successful.
		Number : If a color value is specified, the previous light value if successful.
		Null : If not successful, or on error.

		"""

		return self._ApplyTypes_(id, 1, (returns), (params), u'LightColor', None, strObject, lngColor)

	def lightcount(self, ):
		"""

		Returns the number of light objects in the document.

		No parameters

		Returns

		Number : The number of lights in the document.

		"""

		return self._ApplyTypes_(id, 1, (returns), (params), u'LightCount', None, )

	def lightdirection(self, strobject, arrdirection):
		"""

		Returns or changes the direction of a light object. This function can be used to return or modify the target of spotlights.

		Parameters

		strObject : Required,   String,   The light object's identifier
		arrDirection : Optional,   Array,   The new end point, or direction

		Returns

		Array : If a direction point is not specified,  the current direction if successful.
		Array : If a direction point is specified, the previous direction point if successful.
		Null : If not successful, or on error.

		"""

		return self._ApplyTypes_(id, 1, (returns), (params), u'LightDirection', None, strObject, arrDirection)

	def lightlocation(self, strobject, arrlocation):
		"""

		Returns or changes the location of a light object.

		Parameters

		strObject : Required,   String,   The light object's identifier
		arrlocation : Optional,   Array,   The new start point, or location

		Returns

		Array : If a location point is not specified,  the current location if successful.
		Array : If a location point is specified, the previous location point if successful.
		Null : If not successful, or on error.

		"""

		return self._ApplyTypes_(id, 1, (returns), (params), u'LightLocation', None, strObject, arrlocation)

	def lightname(self, strobject, strname):
		"""

		Returns or modifies the user-definable name of a light object.

		Parameters

		strObject : Required,   String,   The identifier of the light object
		strName : Optional,   String,   The new light name

		Returns

		String : If strName is not specified,  the current light name if successful.
		String : If strName is specified,  the previous light name if successful.
		Null : If not successful, or on error.

		"""

		return self._ApplyTypes_(id, 1, (returns), (params), u'LightName', None, strObject, strName)

	def lightobjects(self, ):
		"""

		Returns the identifier of light objects in the document.

		No parameters

		Returns

		Array : The identifiers of all lights in the document if successful
		Null : If not successful, or on error.

		"""

		return self._ApplyTypes_(id, 1, (returns), (params), u'LightObjects', None, )

	def rectangularlightplane(self, strobject):
		"""

		Returns the plane of a rectangular light object.

		Parameters

		strObject : Required,   String,   The light object's identifier

		Returns

		Array : The plane if successful.  The elements of a plane array are as follows:
		Array : The plane's origin (3-D point).
		Array : The plane's X axis direction (3-D vector).
		Array : The plane's Y axis direction (3-D vector).
		Array : The plane's Z axis direction (3-D vector).
		Null : If not successful, or on error.

		"""

		return self._ApplyTypes_(id, 1, (returns), (params), u'RectangularLightPlane', None, strObject)

	def spotlighthardness(self, strobject, dblhardness):
		"""

		Returns or changes the hardness of a spot light.  Spotlight hardness controls the fully illuminated region.

		Parameters

		strObject : Required,   String,   The light object's identifier
		dblHardness : Optional,   Number,   The new hardness value

		Returns

		Number : If dblHardness is not specified, then  the current hardness value if successful.
		Number : If dblHardness is specified, then the previous hardness value if successful.
		Null : If not successful, or on error.

		"""

		return self._ApplyTypes_(id, 1, (returns), (params), u'SpotLightHardness', None, strObject, dblHardness)

	def spotlightradius(self, strobject, dblradius):
		"""

		Returns or changes the radius of a spot light.

		Parameters

		strObject : Required,   String,   The light object's identifier
		dblRadius : Optional,   Number,   The new radius value

		Returns

		Number : If dblRadius is not specified, then the current radius value if successful.
		Number : If dblRadius is specified, then the previous radius value if successful.
		Null : If not successful, or on error.

		"""

		return self._ApplyTypes_(id, 1, (returns), (params), u'SpotLightRadius', None, strObject, dblRadius)

	def spotlightshadowintensity(self, strobject, dblintensity):
		"""

		Returns or modifies the shadow intensity of a spot light.

		Parameters

		strObject : Required,   String,   The light object's identifier
		dblIntensity : Optional,   Number,   The new shadow intensity

		Returns

		Number : If dblIntensity is not specified, then the current shadow intensity if successful.
		Number : If dblIntensity is specified, then the previous shadow intensity if successful.
		Null : If not successful, or on error.

		"""

		return self._ApplyTypes_(id, 1, (returns), (params), u'SpotLightShadowIntensity', None, strObject, dblIntensity)

