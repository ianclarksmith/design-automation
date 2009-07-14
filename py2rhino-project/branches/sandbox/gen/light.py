# Auto-generated wrapper for Rhino4 RhinoScript functions
import win32com.client.CLSIDToClass, pythoncom
import win32com.client.util
from pywintypes import IID
from win32com.client import Dispatch
from win32com.client import DispatchBaseClass
class Light(DispatchBaseClass):



	def AddDirectionalLight(self, arrStartPoint, arrEndPoint):
		"""

		Adds a new directional light object  to the document.

		Parameters

		arrStartPoint : Required,   Array,  The 3-D starting point of the light
		arrEndPoint : Required,   Array,   The 3-D ending point and direction of the light

		Returns

		String : The identifier of the new object if successful.
		Null : If not successful, or on error.

		"""

		pass

	def AddLinearLight(self, arrStartPoint, arrEndPoint, dblWidth):
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

		pass

	def AddPointLight(self, arrPoint):
		"""

		Adds a new point light object  to the document.

		Parameters

		arrPoint : Required,   Array,   The 3-D location point of the light

		Returns

		String : The identifier of the new object if successful.
		Null : If not successful, or on error.

		"""

		pass

	def AddRectangularLight(self, arrOrigin, arrWidth, arrHeight):
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

		pass

	def AddSpotLight(self, arrOrigin, dblRadius, arrApex):
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

		pass

	def EnableLight(self, strObject, blnEnable):
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

		pass

	def IsDirectionalLight(self, strObject):
		"""

		Verifies a light object is a directional light.

		Parameters

		strObject : Required,   String,   The light object's identifier

		Returns

		Boolean : True if successful, otherwise False.
		Null : On error.

		"""

		pass

	def IsLight(self, strObject):
		"""

		Verifies an object is a light object.

		Parameters

		strObject : Required,   String,   The light object's identifier

		Returns

		Boolean : True if successful, otherwise False.
		Null : On error.

		"""

		pass

	def IsLightEnabled(self, strObject):
		"""

		Verifies a light object is enabled.

		Parameters

		strObject : Required,   String,   The light object's identifier

		Returns

		Boolean : True if successful, otherwise False.
		Null : On error.

		"""

		pass

	def IsLightReference(self, strObject):
		"""

		Verifies a light object is referenced from another file.

		Parameters

		strObject : Required,   String,   The light object's identifier

		Returns

		Boolean : True if successful, otherwise False.
		Null : On error.

		"""

		pass

	def IsLinearLight(self, strObject):
		"""

		Verifies a light object is a linear light.

		Parameters

		strObject : Required,   String,   The light object's identifier

		Returns

		Boolean : True if successful, otherwise False.
		Null : On error.

		"""

		pass

	def IsPointLight(self, strObject):
		"""

		Verifies a light object is a point light.

		Parameters

		strObject : Required,   String,   The light object's identifier

		Returns

		Boolean : True if successful, otherwise False.
		Null : On error.

		"""

		pass

	def IsRectangularLight(self, strObject):
		"""

		Verifies a light object is a rectangular light.

		Parameters

		strObject : Required,   String,   The light object's identifier

		Returns

		Boolean : True if successful, otherwise False.
		Null : On error.

		"""

		pass

	def IsSpotLight(self, strObject):
		"""

		Verifies a light object is a spot light.

		Parameters

		strObject : Required,   String,   The light object's identifier

		Returns

		Boolean : True if successful, otherwise False.
		Null : On error.

		"""

		pass

	def LightColor(self, strObject, lngColor):
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

		pass

	def LightCount(self):
		"""

		Returns the number of light objects in the document.

		No parameters

		Returns

		Number : The number of lights in the document.

		"""

		pass

	def LightDirection(self, strObject, arrDirection):
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

		pass

	def LightLocation(self, strObject, arrlocation):
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

		pass

	def LightName(self, strObject, strName):
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

		pass

	def LightObjects(self):
		"""

		Returns the identifier of light objects in the document.

		No parameters

		Returns

		Array : The identifiers of all lights in the document if successful
		Null : If not successful, or on error.

		"""

		pass

	def RectangularLightPlane(self, strObject):
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

		pass

	def SpotLightHardness(self, strObject, dblHardness):
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

		pass

	def SpotLightRadius(self, strObject, dblRadius):
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

		pass

	def SpotLightShadowIntensity(self, strObject, dblIntensity):
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

		pass

