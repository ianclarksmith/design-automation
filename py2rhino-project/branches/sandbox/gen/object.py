# Auto-generated wrapper for Rhino4 RhinoScript functions
import win32com.client.CLSIDToClass, pythoncom
import win32com.client.util
from pywintypes import IID
from win32com.client import Dispatch
from win32com.client import DispatchBaseClass
class Object(DispatchBaseClass):



	def ObjectGroups(self, strObject):
		"""

		Returns all of the group names that an object is assigned.

		Parameters

		strObject : Required,   String,   The identifier of the object

		Returns

		Array : An array of all group names for the object if successful.
		Null : If not successful, or on error.

		"""

		pass

	def RotateObjects(self, arrObjects, arrPoint, dblAngle, arrAxis, blnCopy):
		"""

		Rotates one or more objects. Rotation is based on the active construction plane.

		Parameters

		arrObjects : Required,  Array,  An array of strings identifying the objects to rotate
		arrPoint : Required,  Array,  The 3-D center point of the rotation
		dblAngle : Required,  Number,  The rotation angle in degrees
		arrAxis : Optional,  Array,  A 3-D vector that identifies the axis of rotation
		blnCopy : Optional,  Boolean,  Copy the object

		Returns

		String : An array of strings identifying the rotated objects if successful.
		Null : If not successful, or on error.

		"""

		pass

	def ObjectPrintColor(self, strObject, arrObjects, lngColor):
		"""

		Returns or modifies the print color of an object.  Object print colors are represented as RGB colors.  An RGB color specifies the relative intensity of red, green, and blue to cause a specific color to be displayed.

		Parameters

		strObject : Required,   String,   The identifier of the object
		arrObjects : Required,   Array,   An array of strings identifying the objects to modify
		lngColor : Optional,   Number,   The new print color value

		Returns

		Number : If a print color value is not specified,  the current print color value if successful.
		Number : If a print color value is specified, the previous print color value if successful.
		Number : If arrObjects is specified, then the number of objects modified if successful.
		Null : If not successful, or on error.

		"""

		pass

	def MirrorObject(self, strObject, arrStartPt, arrEndPt, blnCopy):
		"""

		Mirrors a single object.

		Parameters

		strObject : Required,  String,  The identifier of the object to mirror
		arrStartPt : Required,  Array,  The start of the mirror plane
		arrEndPt : Required,  Array,  The end of the mirror plane
		blnCopy : Optional,  Boolean,  Copy the object

		Returns

		String : The identifier of the mirrored object if successful.
		Null : If not successful, or on error.

		"""

		pass

	def ObjectMaterialIndex(self, strObject):
		"""

		If the return value of ObjectMaterialSource is "material by object", then the return value of this function is the index of the object's rendering material.  A material index of -1 indicates no material has been assigned, and that Rhino's internal default material has been assigned to the object.

		Parameters

		strObject : Required,   String,   The identifier of the object

		Returns

		Number : The rendering material index if successful.
		Null : If not successful, or on error.

		"""

		pass

	def OrientObject(self, strObject, arrReference, arrTarget, intFlags):
		"""

		Orients a single object based on input points.

		Parameters

		strObject : Required,   String,   The identifier of the object to orient
		arrReference : Required,   Array,   An array of 3-D reference points
		arrTarget : Required,   Array,   An array of 3-D target points
		intFlags : Optional,   Number,   The orient flags

		Returns

		String : The identifier of the oriented object if successful.
		Null : If not successful, or on error.

		"""

		pass

	def IsVisibleInView(self, strObject, strView):
		"""

		Verifies that an object is visible in a view.

		Parameters

		strObject : Required,   String,   The identifier of an object
		strView : Optional,   String,   The title of the view

		Returns

		Null : On error.

		"""

		pass

	def UnlockObjects(self, arrObjects):
		"""

		Unlocks one or more objects.  Locked object are visible, and they can be snapped to.  But, they cannot be selected.

		Parameters

		arrObjects : Required,   Array,   An array of strings identifying the objects to unlock

		Returns

		Number : The number of objects unlocked if successful.
		Null : If not successful, or on error.

		"""

		pass

	def ObjectMeshQuality(self, strObject, intQuality):
		"""

		Returns or sets the render mesh quality of an object's custom render mesh parameters.

		Parameters

		strObject : Required,   Object,   The identifier of an object that has custom render mesh parameters
		intQuality : Optional,   Number,   The render mesh quality, either:

		Returns

		Boolean : If intQuality is not specified, the current render mesh quality if successful.
		Boolean : If intQuality is specified, the previous render mesh quality if successful.
		Null : If the object does not have custom render mesh parameters, or on error.

		"""

		pass

	def MoveObjects(self, arrObjects, arrStart, arrEnd, arrTranslation):
		"""

		Copies one or more objects.

		Parameters

		arrObjects : Required,   Array,   An array of strings identifying the objects to move
		arrStart : Required,   Array,   The 3-D starting, or base, point of the move operation
		arrEnd : Required,   Array,   The 3-D ending point of the move operation
		arrTranslation : Required,   Array,   The 3-D translation vector

		Returns

		Number : An array of strings identifying the moved objects if successful.
		Null : If not successful, or on error.

		"""

		pass

	def ObjectMeshDensity(self, strObject, dblDensity):
		"""

		For more information on render meshes, see the Document Properties: Mesh topic in the Rhino help file.

		Parameters

		strObject : Required,   Object,   The identifier of an object that has custom render mesh parameters
		dblDensity : Optional,   Number,   The render mesh density, which is a number between 0

		Returns

		Boolean : If dblDensity is not specified, the current render mesh density if successful.
		Boolean : If dblDensity is specified, the previous render mesh density if successful.
		Null : If not successful, or on error.

		"""

		pass

	def LockObjects(self, arrObjects):
		"""

		Locks one or more objects.  Locked object are visible, and they can be snapped to.  But, they cannot be selected.

		Parameters

		arrObjects : Required,   Array,   An array of strings identifying the objects to lock

		Returns

		Number : The number of objects locked if successful.
		Null : If not successful, or on error.

		"""

		pass

	def ShowObjects(self, arrObjects):
		"""

		Shows one or more hidden objects.  Hidden objects are not visible, cannot be snapped to, and cannot be selected.

		Parameters

		arrObjects : Required,   Array,   An array of strings identifying the objects to show

		Returns

		Number : The number of objects shown if successful.
		Null : If not successful, or on error.

		"""

		pass

	def ObjectMeshMaxAspectRatio(self, strObject, dblRatio):
		"""

		For more information on render meshes, see the Document Properties: Mesh topic in the Rhino help file.

		Parameters

		strObject : Required,   Object,   The identifier of an object that has custom render mesh parameters
		dblRatio : Optional,   Number,   The render mesh maximum aspect ratio

		Returns

		Boolean : If dblRatio is not specified, the current render mesh maximum aspect ratio if successful.
		Boolean : If dblRatio is specified, the previous render mesh maximum aspect ratio if successful.
		Null : If not successful, or on error.

		"""

		pass

	def FlashObject(self, strObject, arrObjects, blnStyle):
		"""

		Causes the selection state of one or more objects to change momentarily so the object appears to flash on the screen.

		Parameters

		strObject : Required,   String,   The identifier of the object to flash
		arrObjects : Required,   Array,   The identifiers of the objects to flash
		blnStyle : Optional,   Boolean,   The flash style

		No returns


		"""

		pass

	def ObjectDescription(self, strObject):
		"""

		Returns a short text description of an object.

		Parameters

		strObject : Required,   String,   The identifier of the object

		Returns

		String : A short text description of the object is successful.
		Null : If not successful, or on error.

		"""

		pass

	def ObjectLayer(self, strObject, arrObjects, strLayer):
		"""

		Returns or modifies the layer of an object.

		Parameters

		strObject : Required,   String,   The identifier of the object
		arrObjects : Required,   Array,   An array of strings identifying the objects to modify
		strLayer : Optional,   String,   The name of an existing layer

		Returns

		Number : If a layer is not specified,  the object's current layer if successful.
		Number : If a layer is specified, the object's previous layer if successful.
		Number : If arrObjects is specified, then the number of objects modified if successful.
		Null : If not successful, or on error.

		"""

		pass

	def RotateObject(self, strObject, arrPoint, dblAngle, arrAxis, blnCopy):
		"""

		Rotates a single object. Rotation is based on the active construction plane.

		Parameters

		strObject : Required,  String,  The identifier of the object to rotate
		arrPoint : Required,  Array,  The 3-D center point of the rotation
		dblAngle : Required,  Number,  The rotation angle in degrees
		arrAxis : Optional,  Array,  A 3-D vector that identifies the axis of rotation
		blnCopy : Optional,  Boolean,  Copy the object

		Returns

		String : The identifier of the rotated object if successful.
		Null : If not successful, or on error.

		"""

		pass

	def ObjectColor(self, strObject, arrObjects, lngColor):
		"""

		Returns or modifies the color of an object.  Object colors are represented as RGB colors.  An RGB color specifies the relative intensity of red, green, and blue to cause a specific color to be displayed.

		Parameters

		strObject : Required,   String,   The identifier of the object
		arrObjects : Required,   Array,   An array of strings identifying the objects to modify
		lngColor : Optional,   Number,   The new color value

		Returns

		Number : If a color value is not specified,  the current color value if successful.
		Number : If a color value is specified, the previous color value if successful.
		Number : If arrObjects is specified, then the number of objects modified if successful.
		Null : If not successful, or on error.

		"""

		pass

	def CopyObject(self, strObject, arrStart, arrEnd, arrTranslation):
		"""

		Copies a single object from one location to another, or in-place.

		Parameters

		strObject : Required,   String,   The identifier of the object to copy
		arrStart : Optional,   Array,   The 3-D starting, or base, point of the copy operation
		arrEnd : Optional,   Array,   The 3-D ending point of the copy operation
		arrTranslation : Optional,   Array,   The 3-D translation vector

		Returns

		String : The identifier of the copied object if successful.
		Null : If not successful, or on error.

		"""

		pass

	def ObjectMeshMaxAngle(self, strObject, dblAngle):
		"""

		For more information on render meshes, see the Document Properties: Mesh topic in the Rhino help file.

		Parameters

		strObject : Required,   Object,   The identifier of an object that has custom render mesh parameters
		dblAngle : Optional,   Number,   The render mesh maximum angle in degrees

		Returns

		Boolean : If dblAngle is not specified, the current render mesh maximum angle if successful.
		Boolean : If dblAngle is specified, the previous render mesh maximum angle if successful.
		Null : If not successful, or on error.

		"""

		pass

	def ShowObject(self, strObject):
		"""

		Shows a previously hidden object.  Hidden objects are not visible, cannot be snapped to, and cannot be selected.

		Parameters

		strObject : Required,   String,   The identifier of the object to show

		Returns

		Boolean : True or false indicating success or failure.
		Null : On error.

		"""

		pass

	def ObjectMeshMaxEdgeLength(self, strObject, dblLength):
		"""

		For more information on render meshes, see the Document Properties: Mesh topic in the Rhino help file.

		Parameters

		strObject : Required,   Object,   The identifier of an object that has custom render mesh parameters
		dblLength : Optional,   Number,   The render mesh maximum edge length

		Returns

		Boolean : If dblLength is not specified, the current render mesh maximum edge length if successful.
		Boolean : If dblLength is specified, the previous render mesh maximum edge length if successful.
		Null : If not successful, or on error.

		"""

		pass

	def HideObject(self, strObject):
		"""

		Hides a single object.  Hidden objects are not visible, cannot be snapped to, and cannot be selected.

		Parameters

		strObject : Required,   String,   The identifier of the object to hide

		Returns

		Boolean : True or false indicating success or failure.
		Null : On error.

		"""

		pass

	def TransformObjects(self, arrObjects, arrMatrix, blnCopy):
		"""

		1

		Parameters

		arrObjects : Required,   Array,   An array of strings identifying the objects to transform
		arrMatrix : Required,  Array,  The transformation matrix (4x4 array of numbers)
		blnCopy : Optional,  Boolean,  Copy the objects

		Returns

		Array : An array of strings identifying the newly transformed objects if successful.
		Null : If not successful, or on error.

		"""

		pass

	def ObjectHasMesh(self, strObject):
		"""

		Verifies that an object has custom render mesh parameters.

		Parameters

		strObject : Required,   Object,   The identifier of a meshable object

		Returns

		Boolean : True of the object has custom render mesh parameters, False otherwise.
		Null : On error.

		"""

		pass

	def EnableObjectMesh(self, arrObjects, blnEnable):
		"""

		For more information on render meshes, see the Document Properties: Mesh topic in the Rhino help file.

		Parameters

		arrObjects : Required,   Object,   The identifier of a meshable object
		blnEnable : Optional,   Boolean,   Enable the custom render mesh settings

		Returns

		Boolean : If blnEnable is not specified, then the current enabled/disabled state if successful.
		Boolean : If blnEnable is not specified, then the current enabled/disabled state if successful.
		Null : If the object does not have custom render mesh parameters, or on error.

		"""

		pass

	def MoveObject(self, strObject, arrStart, arrEnd, arrTranslation):
		"""

		Moves a single object.

		Parameters

		strObject : Required,   String,   The identifier of the object to move
		arrStart : Required,   Array,   The 3-D starting, or base, point of the move operation
		arrEnd : Required,   Array,   The 3-D ending point of the move operation
		arrTranslation : Required,   Array,   The 3-D translation vector

		Returns

		Boolean : The identifier of the moved object if successful.
		Null : If not successful, or on error.

		"""

		pass

	def ObjectTopGroup(self, strObject):
		"""

		Returns the top most group name that an object is assigned.  This function primarily applies to objects that are members of nested groups.

		Parameters

		strObject : Required,   String,   The identifier of the object

		Returns

		String : The top most group name of the object if successful
		Null : If not successful, or on error.

		"""

		pass

	def DeleteObjects(self, arrObjects):
		"""

		Deletes one or more objects from the document.

		Parameters

		arrObjects : Required,   Array,   An array of strings identifying the objects to delete

		Returns

		Number : The number of objects deleted if successful.
		Null : If not successful, or on error.

		"""

		pass

	def ObjectDump(self, strObject, intType):
		"""

		Returns a detailed description of an object.

		Parameters

		strObject : Required,   String,   The identifier of the object
		intType : Optional,   The type of dump,   The acceptable values are as follows:

		Returns

		String : A detailed description of the object is successful.
		Null : If not successful, or on error.

		"""

		pass

	def IsObjectInGroup(self, strObject, strGroup):
		"""

		Verifies that an object is a member of a specified group.

		Parameters

		strObject : Required,   String,   The identifier of an object
		strGroup : Optional,   String,   The name of a group

		Returns

		Null : On error.

		"""

		pass

	def UnlockObject(self, strObject):
		"""

		Unlocks a previously locked object.  Locked object are visible, and they can be snapped to.  But, they cannot be selected.

		Parameters

		strObject : Required,   String,   The identifier of the object to unlock

		Returns

		Boolean : True or false indicating success or failure.
		Null : On error.

		"""

		pass

	def ObjectMaterialSource(self, strObject, arrObjects, intSource):
		"""

		The default rendering material source for new objects is "material by layer."

		Parameters

		strObject : Required,   String,   The identifier of the object
		arrObjects : Required,   Array,   An array of strings identifying the objects to modify
		intSource : Optional,   Number,   The new rendering material source

		Returns

		Number : If a rendering material source is not specified,  the current rendering material source if successful.
		Number : If a rendering material source is specified, the previous rendering material source if successful.
		Number : If arrObjects is specified, then the number of objects modified if successful.
		Null : If not successful, or on error.

		"""

		pass

	def SelectObjects(self, arrObjects):
		"""

		Selects one or more objects.

		Parameters

		arrObjects : Required,   Array,   An array of strings identifying the objects to select

		Returns

		Number : The number of objects selected if successful.
		Null : If not successful, or on error.

		"""

		pass

	def CopyObjects(self, arrObjects, arrStart, arrEnd, arrTranslation):
		"""

		Copies one or more objects from one location to another, or in-place.

		Parameters

		arrObjects : Required,   Array,   An array of strings identifying the objects to copy
		arrStart : Optional,   Array,   The 3-D starting, or base, point of the copy operation
		arrEnd : Optional,   Array,   The 3-D ending point of the copy operation
		arrTranslation : Optional,   Array,   The 3-D translation vector

		Returns

		Array : An array of strings identifying the copied objects if successful.
		Null : If not successful, or on error.

		"""

		pass

	def ObjectNames(self, arrObjects, arrNames):
		"""

		Returns or modifies the user-definable name of one or more objects.

		Parameters

		arrObjects : Required,   Array,   An array of strings identifying the objects
		arrNames : Optional,   Array,    An array of strings identifying the new user-definable names

		Returns

		Array : If arrNames is not specified,  the current object names if successful. Note, if an object does not have a user-definable name, it's corresponding element will be Null.
		Array : If arrNames is specified,  the previous object names if successful.  Note, if an object does not have a user-definable name, it's corresponding element will be Null.
		Null : If not successful, or on error.

		"""

		pass

	def ObjectMeshMaxDistEdgeToSrf(self, strObject, dblDistance):
		"""

		For more information on render meshes, see the Document Properties: Mesh topic in the Rhino help file.

		Parameters

		strObject : Required,   Object,   The identifier of an object that has custom render mesh parameters
		dblDistance : Optional,   Number,   The render mesh maximum distance, edge to surface

		Returns

		Boolean : If dblDistance is not specified, the current render mesh maximum distance, edge to surface if successful.
		Boolean : If dblDistance is specified, the previous render mesh maximum distance, edge to surface if successful.
		Null : If not successful, or on error.

		"""

		pass

	def HideObjects(self, arrObjects):
		"""

		Hides one or more objects.  Hidden objects are not visible, cannot be snapped to, and cannot be selected.

		Parameters

		arrObjects : Required,   Array,   An array of strings identifying the objects to hide

		Returns

		Number : The number of objects hidden if successful.
		Null : If not successful, or on error.

		"""

		pass

	def ShearObjects(self, arrObjects, arrOrigin, arrRefPt, arrScale, blnCopy):
		"""

		Performs a shear transformation on one or more objects. Transformation is based on the active construction plane.

		Parameters

		arrObjects : Required,  Array,  An array of strings identifying the objects to shear
		arrOrigin : Required,  Array,  The origin of the shear transformation
		arrRefPt : Required,  Array,  The reference point of the shear transformation
		arrScale : Required,  Number,  An angle in degrees of the shear transformation, where -90
		blnCopy : Optional,  Boolean,  Copy the objects

		Returns

		Array : An array of strings identifying the scaled objects if successful.
		Null : If not successful, or on error.

		"""

		pass

	def IsObjectInBox(self, strObject, arrBox, blnMode):
		"""

		Verifies an object's bounding box is inside of another bounding box.

		Parameters

		strObject : Required,   String,   The identifier of an object
		arrBox : Required,   Array,   The bounding box to test against
		blnMode : Optional,   Boolean,   The test mode

		Returns

		Null : On error.

		"""

		pass

	def IsObjectSolid(self, strObject):
		"""

		Verifies that an object is a closed, solid object.

		Parameters

		strObject : Required,   String,   The identifier of an object

		Returns

		Null : On error.

		"""

		pass

	def UnselectObject(self, strObject):
		"""

		Unselects a single selected object.

		Parameters

		strObject : Required,   String,   The identifier of the object to unselect

		Returns

		Boolean : True or false indicating success or failure.
		Null : On error.

		"""

		pass

	def ScaleObjects(self, arrObjects, arrOrigin, arrScale, blnCopy):
		"""

		Scales one or more objects. This function can be used to perform uniform or non-uniform scale transformations. Scaling is based on the active construction plane.

		Parameters

		arrObjects : Required,  Array,  An array of strings identifying the objects to scale
		arrOrigin : Required,  Array,  The origin of the scale transformation
		arrScale : Required,  Array,  An array of three numbers that identify the X axis, Y axis, and Z axis scale factors to apply
		blnCopy : Optional,  Boolean,  Copy the objects

		Returns

		Array : An array of strings identifying the scaled objects if successful.
		Null : If not successful, or on error.

		"""

		pass

	def ObjectMeshMinEdgeLength(self, strObject, dblLength):
		"""

		For more information on render meshes, see the Document Properties: Mesh topic in the Rhino help file.

		Parameters

		strObject : Required,   Object,   The identifier of an object that has custom render mesh parameters
		dblLength : Optional,   Number,   The render mesh minimum edge length

		Returns

		Boolean : If dblLength is not specified, the current render mesh minimum edge length if successful.
		Boolean : If dblLength is specified, the previous render mesh minimum edge length if successful.
		Null : If not successful, or on error.

		"""

		pass

	def MatchObjectAttributes(self, strTarget, arrTargets, strSource):
		"""

		Matches, or copies, the attributes of a source object to a target object or an array of target objects. If the source object is not specified, the attributes of the target object(s) will be reset to Rhino's default object attributes.

		Parameters

		strTarget : Required,   String,   The identifier of the target object
		arrTargets : Required,   Array,    An array of strings identifying the target objects
		strSource : Optional,   String,   The identifier of the source object

		Returns

		Number : The number of objects whose attributes were modified if successful.
		Null : If not successful, or on error.

		"""

		pass

	def ObjectPrintColorSource(self, strObject, arrObjects, intSource):
		"""

		4. Print color from parent.  For objects with parents, like objects in block instances, use parent's print color.  If no parent, treats as print color from layer.

		Parameters

		strObject : Required,   String,   The identifier of the object
		arrObjects : Required,   Array,   An array of strings identifying the objects to modify
		intSource : Optional,   Number,   The new print color source

		Returns

		Number : If a print color source is not specified,  the current color source if successful.
		Number : If a print color source is specified, the previous color source if successful.
		Number : If arrObjects is specified, then the number of objects modified if successful.
		Null : If not successful, or on error.

		"""

		pass

	def ObjectLinetypeSource(self, strObject, arrObjects, intSource):
		"""

		3. Linetype from parent.  For objects with parents, like objects in block instances, use parent's linetype. If no parent, treats as linetype from layer.

		Parameters

		strObject : Required,   String,   The identifier of the object
		arrObjects : Required,   Array,   An array of strings identifying the objects to modify
		intSource : Optional,   Number,   The new linetype source

		Returns

		Number : If a linetype source is not specified,  the current linetype source if successful.
		Number : If a linetype source is specified, the previous linetype source if successful.
		Number : If arrObjects is specified, then the number of objects modified if successful.
		Null : If not successful, or on error.

		"""

		pass

	def RemapObject(self, strObject, arrSrcPlane, arrDstPlane, blnCopy):
		"""

		Remqps a single object from one plane, or coordinate system, to another.

		Parameters

		strObject : Required,  String,  The identifier of the object to remap
		arrSrcPlane : Required,  Array,  The source plane to transform from
		arrDstPlane : Required,  Array,  The destination plane to transform to
		blnCopy : Optional,  Boolean,  Copy the object

		Returns

		String : The identifier of the remapped object if successful.
		Null : If not successful, or on error.

		"""

		pass

	def IsObjectNormal(self, strObject):
		"""

		Verifies that an object is normal.  Normal objects are visible, can be snapped to, and can be selected.

		Parameters

		strObject : Required,   String,   The identifier of an object

		Returns

		Null : On error.

		"""

		pass

	def ObjectMeshSettings(self, strObject, intSettings):
		"""

		Returns or sets the render mesh settings of an object's custom render mesh parameters.

		Parameters

		strObject : Required,   Object,   The identifier of an object that has custom render mesh parameters
		intSettings : Optional,   Number,   The render mesh settings, which is a bit-coded number that allows or disallows certain features

		Returns

		Boolean : If intSettings is not specified, the current render mesh settings if successful.
		Boolean : If intSettings is specified, the previous render mesh settings if successful.
		Null : If the object does not have custom render mesh parameters, or on error.

		"""

		pass

	def ObjectColorSource(self, strObject, arrObjects, intSource):
		"""

		4. Color from parent. For objects with parents, like objects in block instances, use parent's color source. If no parent, treats as color from layer.

		Parameters

		strObject : Required,   String,   The identifier of the object
		arrObjects : Required,   Array,   An array of strings identifying the objects to modify
		intSource : Optional,   Number,   The new color source

		Returns

		Number : If a color source is not specified,  the current color source if successful.
		Number : If a color source is specified, the previous color source if successful.
		Number : If arrObjects is specified, then the number of objects modified if successful.
		Null : If not successful, or on error.

		"""

		pass

	def IsObjectHidden(self, strObject):
		"""

		Verifies that an object is hidden.  Hidden objects are not visible, cannot be snapped to, and cannot be selected.

		Parameters

		strObject : Required,   String,   The identifier of an object

		Returns

		Null : On error.

		"""

		pass

	def IsObjectLocked(self, strObject):
		"""

		Verifies that an object is locked.  Locked object are visible, and they can be snapped to.  But, they cannot be selected.

		Parameters

		strObject : Required,   String,   The identifier of an object

		Returns

		Null : On error.

		"""

		pass

	def RemapObjects(self, arrObject, arrSrcPlane, arrDstPlane, blnCopy):
		"""

		Remqps one or more objects from one plane, or coordinate system, to another.

		Parameters

		arrObject : Required,  Array,  The identifiers of the objects to remap
		arrSrcPlane : Required,  Array,  The source plane to transform from
		arrDstPlane : Required,  Array,  The destination plane to transform to
		blnCopy : Optional,  Boolean,  Copy the object

		Returns

		Array : An array of strings identifying the remapped objects if successful.
		Null : If not successful, or on error.

		"""

		pass

	def OrientObjects(self, arrObjects, arrReference, arrTarget, intFlags):
		"""

		Orients one or more objects based on input points.

		Parameters

		arrObjects : Required,   Array,   An array of strings identifying the objects to orient
		arrReference : Required,   Array,   An array of 3-D reference points
		arrTarget : Required,   Array,   An array of 3-D target points
		intFlags : Optional,   Number,   The orient flags

		Returns

		Array : An array of strings identifying the oriented objects if successful.
		Null : If not successful, or on error.

		"""

		pass

	def ShearObject(self, strObject, arrOrigin, arrRefPt, arrScale, blnCopy):
		"""

		Performs a shear transformation on a single object. Transformation is based on the active construction plane.

		Parameters

		strObject : Required,  String,  The identifier of the object to shear
		arrOrigin : Required,  Array,  The origin of the shear transformation
		arrRefPt : Required,  Array,  The reference point of the shear transformation
		arrScale : Required,  Number,  An angle in degrees of the shear transformation, where -90
		blnCopy : Optional,  Boolean,  Copy the object

		Returns

		String : The identifier of the sheared object if successful.
		Null : If not successful, or on error.

		"""

		pass

	def IsObjectValid(self, strObject):
		"""

		Verifies that an object's geometry is valid and without error.

		Parameters

		strObject : Required,   String,   The identifier of an object

		Returns

		Null : On error.

		"""

		pass

	def ObjectName(self, strObject, arrObjects, strName):
		"""

		Returns or modifies the user-definable name of an object.

		Parameters

		strObject : Required,   String,   The identifier of the object
		arrObjects : Required,   Array,   An array of strings identifying the objects to modify
		strName : Optional,   String,   The new object name

		Returns

		String : If an object name is not specified,  the current object name if successful.
		String : If an object name is specified,  the previous object name if successful.
		Number : If arrObjects is specified, then the number of objects modified if successful.
		Null : If not successful, or on error.

		"""

		pass

	def MirrorObjects(self, arrObjects, arrStartPt, arrEndPt, blnCopy):
		"""

		Mirrors one or more objects.

		Parameters

		arrObjects : Required,  Array,  An array of strings identifying the objects to mirror
		arrStartPt : Required,  Array,  The start of the mirror plane
		arrEndPt : Required,  Array,  The end of the mirror plane
		blnCopy : Optional,  Boolean,  Copy the objects

		Returns

		String : An array of strings identifying the mirrored objects if successful.
		Null : If not successful, or on error.

		"""

		pass

	def ObjectLinetype(self, strObject, arrObjects, strLayer):
		"""

		Returns or modifies the linetype of an object.

		Parameters

		strObject : Required,   String,   The identifier of the object
		arrObjects : Required,   Array,   An array of strings identifying the objects to modify
		strLayer : Optional,   String,   The name of an existing linetype

		Returns

		Number : If a linetype is not specified,  the object's current linetype if successful.
		Number : If a linetype is specified, the object's previous linetype if successful.
		Number : If arrObjects is specified, then the number of objects modified if successful.
		Null : If not successful, or on error.

		"""

		pass

	def ScaleObject(self, strObject, arrOrigin, arrScale, blnCopy):
		"""

		Scales a single object. This function can be used to perform uniform or non-uniform scale transformations. Scaling is based on the active construction plane.

		Parameters

		strObject : Required,  String,  The identifier of the object to scale
		arrOrigin : Required,  Array,  The origin of the scale transformation
		arrScale : Required,  Array,  An array of three numbers that identify the X axis, Y axis, and Z axis scale factors to apply
		blnCopy : Optional,  Boolean,  Copy the object

		Returns

		String : The identifier of the scaled object if successful.
		Null : If not successful, or on error.

		"""

		pass

	def ObjectURL(self, strObject, arrObjects, strURL):
		"""

		Returns or modifies the user-definable URL of an object.

		Parameters

		strObject : Required,   String,   The identifier of the object
		arrObjects : Required,   Array,   An array of strings identifying the objects to modify
		strURL : Optional,   String,   The new object URL

		Returns

		String : If an object URL is not specified,  the current object URL if successful.
		String : If an object URL is specified,  the previous object URL if successful.
		Number : If arrObjects is specified, then the number of objects modified if successful.
		Null : If not successful, or on error.

		"""

		pass

	def IsObjectSelected(self, strObject):
		"""

		Verifies that an object is currently selected.

		Parameters

		strObject : Required,   String,   The identifier of an object

		Returns

		Null : On error.

		"""

		pass

	def IsObjectSelectable(self, strObject):
		"""

		Verifies that an object is selectable.  Objects that are locked, hidden, or on locked or hidden layers cannot be selected.

		Parameters

		strObject : Required,   String,   The identifier of an object

		Returns

		Null : On error.

		"""

		pass

	def TransformObject(self, strObject, arrMatrix, blnCopy):
		"""

		1

		Parameters

		strObject : Required,  String,  The identifier of the object
		arrMatrix : Required,  Array,  The transformation matrix (4x4 array of numbers)
		blnCopy : Optional,  Boolean,  Copy the object

		Returns

		Boolean : The identifier of the transformed object if successful.
		Null : If not successful, or on error.

		"""

		pass

	def ObjectType(self, strObject):
		"""

		Returns the object type.

		Parameters

		strObject : Required,   String,   The identifier of the object

		Returns

		Number : The object type if successful.  The valid object types are as follows:
		Null : If not successful, or on error.

		"""

		pass

	def IsLayoutObject(self, strObject):
		"""

		Verifies that an object is in either page layout space or model space.

		Parameters

		strObject : Required,   String,   The identifier of an object

		Returns

		Null : On error.

		"""

		pass

	def AddObjectMesh(self, strObject, intQuality, blnEnable):
		"""

		For more information on render meshes, see the Document Properties: Mesh topic in the Rhino help file.

		Parameters

		strObject : Required,   Object,   The identifier of a meshable object
		intQuality : Optional,   Number,   The initial settings of the new custom render mesh parameters
		blnEnable : Optional,   Boolean,   Enable the custom render mesh parameters

		Returns

		Boolean : If blnEnable is not specified, then the current enabled/disabled state if successful.
		Boolean : If blnEnable is not specified, then the current enabled/disabled state if successful.
		Null : If the object does not have custom render mesh parameters, or on error.

		"""

		pass

	def ObjectLayout(self, strObject, strLayout, blnReturnName):
		"""

		Returns or changes the layout or model space of an object.

		Parameters

		strObject : Required,   String,   The identifier of the object
		strLayout : Optional,   String,   To change, or move, an object from model space to page layout space, or from one page layout to another, then specify the title or identifier of an existing page layout view
		blnReturnName : Optional,   Boolean,   If True (default), then the name, or title, of the page layout view is returned

		Returns

		String : If strLayout is not specified,  the object's current page layout view if successful. Note, if the object is not in page layout space, Null is returned.
		String : If strLayout  is specified, the object's previous page layout view if successful. Note, if the object was not in page layout space, Null is returned.
		Null : If not successful, or on error.

		"""

		pass

	def BoxMorphObject(self, strObject, arrObjects, arrBoxPoints, blnCopy):
		"""

		Morphs an object by mapping its eight bounding box points to eight new points. Note, this function only works on non-planar objects.

		Parameters

		strObject : Required,  String,  The identifier of the object to morph
		arrObjects : Required,   Array,   An array of strings identifying the objects to morph
		arrBoxPoints : Required,  Array,   An array of eight 3-D points that contain the modified bounding box points
		blnCopy : Optional,  Boolean,  Copy the object

		Returns

		String : The identifier of the morphed object if successful.
		Array : An array of strings identifying the morphed objects if successful.
		Null : If not successful, or on error.

		"""

		pass

	def IsObjectReference(self, strObject):
		"""

		Verifies that an object is a reference object.  Reference objects are object that are not part of the current document.

		Parameters

		strObject : Required,   String,   The identifier of an object

		Returns

		Null : On error.

		"""

		pass

	def LockObject(self, strObject):
		"""

		Locks a single object.  Locked object are visible, and they can be snapped to.  But, they cannot be selected.

		Parameters

		strObject : Required,   String,   The identifier of the object to lock

		Returns

		Boolean : True or false indicating success or failure.
		Null : On error.

		"""

		pass

	def SelectObject(self, strObject):
		"""

		Selects a single object.

		Parameters

		strObject : Required,   String,   The identifier of the object to select

		Returns

		Boolean : True or false indicating success or failure.
		Null : On error.

		"""

		pass

	def UnselectObjects(self, arrObjects):
		"""

		Unselects one or more selected objects.

		Parameters

		arrObjects : Required,   Array,   An array of strings identifying the objects to unselect

		Returns

		Number : The number of objects unselected if successful.
		Null : If not successful, or on error.

		"""

		pass

	def ObjectMeshMinInitialGridQuads(self, strObject, intQuads):
		"""

		For more information on render meshes, see the Document Properties: Mesh topic in the Rhino help file.

		Parameters

		strObject : Required,   Object,   The identifier of an object that has custom render mesh parameters
		intQuads : Optional,   Number,   The render mesh minimum initial grid quads

		Returns

		Boolean : If intQuads is not specified, the current render mesh minimum initial grid quads if successful.
		Boolean : If intQuads is specified, the previous render mesh minimum initial grid quads if successful.
		Null : If not successful, or on error.

		"""

		pass

	def DeleteObject(self, strObject):
		"""

		Deletes a single object from the document.

		Parameters

		strObject : Required,   String,   The identifier of the object to delete

		Returns

		Boolean : True or false indicating success or failure.
		Null : On error.

		"""

		pass

	def IsObject(self, strObject):
		"""

		Verifies the existence of an object.

		Parameters

		strObject : Required,   String,   The identifier of an object

		No returns


		"""

		pass

	def ObjectPrintWidth(self, strObject, arrObjects, dblWidth):
		"""

		Returns or modifies the print width of an object.  Object print widths are measured in millimeters (mm).

		Parameters

		strObject : Required,   String,   The identifier of the object
		arrObjects : Required,   Array,   An array of strings identifying the objects to modify
		dblWidth : Optional,   Number,   The new print width value in millimeters, where dblWidth = 0

		Returns

		Number : If a print width value is not specified,  the current print width value if successful.
		Number : If a print width value is specified, the previous print width value if successful.
		Number : If arrObjects is specified, then the number of objects modified if successful.
		Null : If not successful, or on error.

		"""

		pass

	def ObjectPrintWidthSource(self, strObject, arrObjects, intSource):
		"""

		3. Print width from parent.  For objects with parents, like objects in block instances, use parent's print width.  If no parent, treats as print width from layer.

		Parameters

		strObject : Required,   String,   The identifier of the object
		arrObjects : Required,   Array,   An array of strings identifying the objects to modify
		intSource : Optional,   Number,   The new print width source

		Returns

		Number : If a print width source is not specified,  the current width source if successful.
		Number : If a print width source is specified, the previous width source if successful.
		Number : If arrObjects is specified, then the number of objects modified if successful.
		Null : If not successful, or on error.

		"""

		pass

