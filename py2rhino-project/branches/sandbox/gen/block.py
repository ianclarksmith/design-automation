# Auto-generated wrapper for Rhino4 RhinoScript functions
import win32com.client.CLSIDToClass, pythoncom
import win32com.client.util
from pywintypes import IID
from win32com.client import Dispatch
from win32com.client import DispatchBaseClass
class Block(DispatchBaseClass):



	def blockcontainercount(self, strblock):
		"""

		Returns the number of block definitions that contain a specified block definition.

		Parameters

		strBlock : Required,   String,   The name of an existing block definition

		Returns

		Number : The number of block definitions that contain the specified block definition if successful.
		Null : If not successful, or on error.

		"""

		return self._ApplyTypes_(id, 1, (returns), (params), u'BlockContainerCount', None, strBlock)

	def blockcontainers(self, strblock):
		"""

		Returns the names of the block definitions that contain a specified block definition.

		Parameters

		strBlock : Required,   String,   The name of an existing block definition

		Returns

		Array : An array of block definition names if successful.
		Null : If not successful, or on error.

		"""

		return self._ApplyTypes_(id, 1, (returns), (params), u'BlockContainers', None, strBlock)

	def blockcount(self, ):
		"""

		Returns the number of block definitions in the document.

		No parameters

		Returns

		Number : The number of block definitions in the document.
		Null : On error.

		"""

		return self._ApplyTypes_(id, 1, (returns), (params), u'BlockCount', None, )

	def blockdescription(self, strblock, strtext):
		"""

		Returns or sets the description of a block definition.

		Parameters

		strBlock : Required,   String,   The name of an existing block definition
		strText : Optional,   String,   The new description

		Returns

		String : If a description is not specified,  the current description if successful.
		String : If a description is specified, the previous description if successful.
		Null : If not successful, or on error.

		"""

		return self._ApplyTypes_(id, 1, (returns), (params), u'BlockDescription', None, strBlock, strText)

	def blockinstancecount(self, strblock):
		"""

		Counts the number of instances of the block in the document.  Nested instances are not included in the count.

		Parameters

		strBlock : Required,   String,   The name of an existing block definition

		Returns

		Number : The number of instances of the block in the document if successful.
		Null : If not successful, or on error.

		"""

		return self._ApplyTypes_(id, 1, (returns), (params), u'BlockInstanceCount', None, strBlock)

	def blockinstanceinsertpoint(self, strobject):
		"""

		Returns the insertion point of a block instance.

		Parameters

		strObject : Required,   String,   The identifier of an existing block insertion object

		Returns

		Array : A 3-D point if successful.
		Null : If not successful, or on error.

		"""

		return self._ApplyTypes_(id, 1, (returns), (params), u'BlockInstanceInsertPoint', None, strObject)

	def blockinstancename(self, strobject):
		"""

		Returns the block name of a block instance.

		Parameters

		strObject : Required,   String,   The identifier of an existing block insertion object

		Returns

		String : The block name if successful.
		Null : If not successful, or on error.

		"""

		return self._ApplyTypes_(id, 1, (returns), (params), u'BlockInstanceName', None, strObject)

	def blockinstancexform(self, strobject):
		"""

		Returns the location of a block instance relative to the world coordinate system origin (0,0,0).  The position is returned as a 4x4 transformation matrix

		Parameters

		strObject : Required,   String,   The identifier of an existing block insertion object

		Returns

		Array : A transformation matrix (4x4 array of numbers) if successful.
		Null : If not successful, or on error.

		"""

		return self._ApplyTypes_(id, 1, (returns), (params), u'BlockInstanceXform', None, strObject)

	def blockinstances(self, strblock):
		"""

		Returns the identifiers of the inserted instances of a block.

		Parameters

		strBlock : Required,   String,   The name of an existing block definition

		Returns

		Array : An array of strings identifying the instances of a block if successful.
		Null : If not successful, or on error.

		"""

		return self._ApplyTypes_(id, 1, (returns), (params), u'BlockInstances', None, strBlock)

	def blocknames(self, blnsort):
		"""

		Returns the names of all block definitions in the document.

		Parameters

		blnSort : Optional,   Boolean,   Return a sorted array of block definition names

		Returns

		Array : An array of block definition names if successful.
		Null : If not successful, or on error.

		"""

		return self._ApplyTypes_(id, 1, (returns), (params), u'BlockNames', None, blnSort)

	def blockobjectcount(self, strblock):
		"""

		Returns the number of objects that make up a block definition.

		Parameters

		strBlock : Required,   String,   The name of an existing block definition

		Returns

		Number : The number of objects that make up the block definition if successful.
		Null : If not successful, or on error.

		"""

		return self._ApplyTypes_(id, 1, (returns), (params), u'BlockObjectCount', None, strBlock)

	def blockobjects(self, strblock):
		"""

		Returns the identifiers of the objects that make up a block definition.

		Parameters

		strBlock : Required,   String,   The name of an existing block definition

		Returns

		Array : An array of strings identifying the objects that make up a block definition if successful.
		Null : If not successful, or on error.

		"""

		return self._ApplyTypes_(id, 1, (returns), (params), u'BlockObjects', None, strBlock)

	def blockpath(self, strblock):
		"""

		Returns the path to the source of a linked or embedded block definition.  A linked or embedded block definition is a block definition that was inserted from an external file.

		Parameters

		strBlock : Required,   String,   The name of an existing block definition

		Returns

		String : The path to the linked block file is successful.
		Null : If not successful, or on error.

		"""

		return self._ApplyTypes_(id, 1, (returns), (params), u'BlockPath', None, strBlock)

	def blockurl(self, strblock, strurl):
		"""

		Returns or sets the URL of a block definition.

		Parameters

		strBlock : Required,   String,   The name of an existing block definition
		strURL : Optional,   String,   The new URL

		Returns

		String : If a URL is not specified,  the current URL if successful.
		String : If a URL is specified, the previous URL if successful.
		Null : If not successful, or on error.

		"""

		return self._ApplyTypes_(id, 1, (returns), (params), u'BlockURL', None, strBlock, strURL)

	def blockurltag(self, strblock, strurl):
		"""

		Returns or sets the URL tag, or description, of a block definition.

		Parameters

		strBlock : Required,   String,   The name of an existing block definition
		strURL : Optional,   String,   The new URL tag

		Returns

		String : If a URL tag is not specified,  the current URL tag if successful.
		String : If a URL tag is specified, the previous URL tag if successful.
		Null : If not successful, or on error.

		"""

		return self._ApplyTypes_(id, 1, (returns), (params), u'BlockURLTag', None, strBlock, strURL)

	def deleteblock(self, strblock):
		"""

		Deletes a block definition and all of it's inserted instances.

		Parameters

		strBlock : Required,   String,   The name of an existing block definition

		Returns

		Boolean : True or false indicating success or failure.
		Null : On error.

		"""

		return self._ApplyTypes_(id, 1, (returns), (params), u'DeleteBlock', None, strBlock)

	def explodeblockinstance(self, strobject):
		"""

		Explodes a block instance into it's geometric components.  The exploded objects are added to the document.

		Parameters

		strObject : Required,   String,   The identifier of an existing block definition

		Returns

		Array : An array of strings identifying the newly exploded objects if successful.
		Null : If not successful, or on error.

		"""

		return self._ApplyTypes_(id, 1, (returns), (params), u'ExplodeBlockInstance', None, strObject)

	def insertblock(self, strname, arrpoint, arrscale, dblangle, arrnormal, arrxform):
		"""

		Inserts a block whose definition already exists in the document.

		Parameters

		strName : Required,  String,  The name of the block definition to insert
		arrPoint : Required,  Array,  The 3-D insertion point of the block
		arrScale : Optional,  Array,  An array of three numbers that identify the x,y,z scale factors
		dblAngle : Optional,  Number,  The rotation angle in degrees
		arrNormal : Optional,  Array,  A 3-D vector identifying the axis of rotation
		arrXform : Required,  Array,  4x4 transformation matrix to apply

		Returns

		String : The identifier of the newly inserted block instance, if successful.
		Null : If not successful, or on error.

		"""

		return self._ApplyTypes_(id, 1, (returns), (params), u'InsertBlock', None, strName, arrPoint, arrScale, dblAngle, arrNormal, arrXform)

	def isblock(self, strblock):
		"""

		Verifies the existence of a block definition in the document.

		Parameters

		strBlock : Required,   String,   The name of an existing block definition

		Returns

		Boolean : True or false indicating success or failure.
		Null : On error.

		"""

		return self._ApplyTypes_(id, 1, (returns), (params), u'IsBlock', None, strBlock)

	def isblockembedded(self, strblock):
		"""

		Verifies that a block definition is embedded, or linked, from an external file.

		Parameters

		strBlock : Required,   String,   The name of an existing block definition

		Returns

		Boolean : True or false indicating success or failure.
		Null : On error.

		"""

		return self._ApplyTypes_(id, 1, (returns), (params), u'IsBlockEmbedded', None, strBlock)

	def isblockinuse(self, strblock, intwhere):
		"""

		Verifies that a block definition is being used by an inserted instance.

		Parameters

		strBlock : Required,   String,   The name of an existing block definition
		intWhere : Optional,   Number,   Where to look, where:

		Returns

		Boolean : True or false indicating success or failure.
		Null : On error.

		"""

		return self._ApplyTypes_(id, 1, (returns), (params), u'IsBlockInUse', None, strBlock, intWhere)

	def isblockinstance(self, strobject):
		"""

		Verifies an object is a block instance.

		Parameters

		strObject : Required,   String,   The identifier of an existing block definition

		Returns

		Boolean : True or false indicating success or failure.
		Null : On error.

		"""

		return self._ApplyTypes_(id, 1, (returns), (params), u'IsBlockInstance', None, strObject)

	def isblockreference(self, strblock):
		"""

		Verifies that a block definition is from a reference file.

		Parameters

		strBlock : Required,   String,   The name of an existing block definition

		Returns

		Boolean : True or false indicating success or failure.
		Null : On error.

		"""

		return self._ApplyTypes_(id, 1, (returns), (params), u'IsBlockReference', None, strBlock)

	def renameblock(self, stroldblock, strnewblock):
		"""

		Renames an existing block definition.

		Parameters

		strOldBlock : Required,   String,   The name of an existing block definition
		strNewBlock : Required,   String,   The new block definition name

		Returns

		String : The new block definition name if successful.
		Null : If not successful, or on error.

		"""

		return self._ApplyTypes_(id, 1, (returns), (params), u'RenameBlock', None, strOldBlock, strNewBlock)

