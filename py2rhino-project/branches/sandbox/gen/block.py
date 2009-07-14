# Auto-generated wrapper for Rhino4 RhinoScript functions
import win32com.client.CLSIDToClass, pythoncom
import win32com.client.util
from pywintypes import IID
from win32com.client import Dispatch
from win32com.client import DispatchBaseClass
class Block(DispatchBaseClass):



	def BlockObjects(self, strBlock):
		"""

		Returns the identifiers of the objects that make up a block definition.

		Parameters

		strBlock : Required,   String,   The name of an existing block definition

		Returns

		Array : An array of strings identifying the objects that make up a block definition if successful.
		Null : If not successful, or on error.

		"""

		pass

	def BlockCount(self):
		"""

		Returns the number of block definitions in the document.

		No parameters

		Returns

		Number : The number of block definitions in the document.
		Null : On error.

		"""

		pass

	def BlockURLTag(self, strBlock, strURL):
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

		pass

	def BlockPath(self, strBlock):
		"""

		Returns the path to the source of a linked or embedded block definition.  A linked or embedded block definition is a block definition that was inserted from an external file.

		Parameters

		strBlock : Required,   String,   The name of an existing block definition

		Returns

		String : The path to the linked block file is successful.
		Null : If not successful, or on error.

		"""

		pass

	def IsBlockInstance(self, strObject):
		"""

		Verifies an object is a block instance.

		Parameters

		strObject : Required,   String,   The identifier of an existing block definition

		Returns

		Boolean : True or false indicating success or failure.
		Null : On error.

		"""

		pass

	def IsBlockInUse(self, strBlock, intWhere):
		"""

		Verifies that a block definition is being used by an inserted instance.

		Parameters

		strBlock : Required,   String,   The name of an existing block definition
		intWhere : Optional,   Number,   Where to look, where:

		Returns

		Boolean : True or false indicating success or failure.
		Null : On error.

		"""

		pass

	def BlockContainers(self, strBlock):
		"""

		Returns the names of the block definitions that contain a specified block definition.

		Parameters

		strBlock : Required,   String,   The name of an existing block definition

		Returns

		Array : An array of block definition names if successful.
		Null : If not successful, or on error.

		"""

		pass

	def BlockInstanceXform(self, strObject):
		"""

		Returns the location of a block instance relative to the world coordinate system origin (0,0,0).  The position is returned as a 4x4 transformation matrix

		Parameters

		strObject : Required,   String,   The identifier of an existing block insertion object

		Returns

		Array : A transformation matrix (4x4 array of numbers) if successful.
		Null : If not successful, or on error.

		"""

		pass

	def IsBlock(self, strBlock):
		"""

		Verifies the existence of a block definition in the document.

		Parameters

		strBlock : Required,   String,   The name of an existing block definition

		Returns

		Boolean : True or false indicating success or failure.
		Null : On error.

		"""

		pass

	def BlockInstanceInsertPoint(self, strObject):
		"""

		Returns the insertion point of a block instance.

		Parameters

		strObject : Required,   String,   The identifier of an existing block insertion object

		Returns

		Array : A 3-D point if successful.
		Null : If not successful, or on error.

		"""

		pass

	def BlockDescription(self, strBlock, strText):
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

		pass

	def BlockInstanceCount(self, strBlock):
		"""

		Counts the number of instances of the block in the document.  Nested instances are not included in the count.

		Parameters

		strBlock : Required,   String,   The name of an existing block definition

		Returns

		Number : The number of instances of the block in the document if successful.
		Null : If not successful, or on error.

		"""

		pass

	def BlockNames(self, blnSort):
		"""

		Returns the names of all block definitions in the document.

		Parameters

		blnSort : Optional,   Boolean,   Return a sorted array of block definition names

		Returns

		Array : An array of block definition names if successful.
		Null : If not successful, or on error.

		"""

		pass

	def BlockContainerCount(self, strBlock):
		"""

		Returns the number of block definitions that contain a specified block definition.

		Parameters

		strBlock : Required,   String,   The name of an existing block definition

		Returns

		Number : The number of block definitions that contain the specified block definition if successful.
		Null : If not successful, or on error.

		"""

		pass

	def BlockInstances(self, strBlock):
		"""

		Returns the identifiers of the inserted instances of a block.

		Parameters

		strBlock : Required,   String,   The name of an existing block definition

		Returns

		Array : An array of strings identifying the instances of a block if successful.
		Null : If not successful, or on error.

		"""

		pass

	def BlockInstanceName(self, strObject):
		"""

		Returns the block name of a block instance.

		Parameters

		strObject : Required,   String,   The identifier of an existing block insertion object

		Returns

		String : The block name if successful.
		Null : If not successful, or on error.

		"""

		pass

	def DeleteBlock(self, strBlock):
		"""

		Deletes a block definition and all of it's inserted instances.

		Parameters

		strBlock : Required,   String,   The name of an existing block definition

		Returns

		Boolean : True or false indicating success or failure.
		Null : On error.

		"""

		pass

	def BlockURL(self, strBlock, strURL):
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

		pass

	def IsBlockEmbedded(self, strBlock):
		"""

		Verifies that a block definition is embedded, or linked, from an external file.

		Parameters

		strBlock : Required,   String,   The name of an existing block definition

		Returns

		Boolean : True or false indicating success or failure.
		Null : On error.

		"""

		pass

	def ExplodeBlockInstance(self, strObject):
		"""

		Explodes a block instance into it's geometric components.  The exploded objects are added to the document.

		Parameters

		strObject : Required,   String,   The identifier of an existing block definition

		Returns

		Array : An array of strings identifying the newly exploded objects if successful.
		Null : If not successful, or on error.

		"""

		pass

	def BlockObjectCount(self, strBlock):
		"""

		Returns the number of objects that make up a block definition.

		Parameters

		strBlock : Required,   String,   The name of an existing block definition

		Returns

		Number : The number of objects that make up the block definition if successful.
		Null : If not successful, or on error.

		"""

		pass

	def IsBlockReference(self, strBlock):
		"""

		Verifies that a block definition is from a reference file.

		Parameters

		strBlock : Required,   String,   The name of an existing block definition

		Returns

		Boolean : True or false indicating success or failure.
		Null : On error.

		"""

		pass

	def RenameBlock(self, strOldBlock, strNewBlock):
		"""

		Renames an existing block definition.

		Parameters

		strOldBlock : Required,   String,   The name of an existing block definition
		strNewBlock : Required,   String,   The new block definition name

		Returns

		String : The new block definition name if successful.
		Null : If not successful, or on error.

		"""

		pass

	def InsertBlock(self, strName, arrPoint, arrScale, dblAngle, arrNormal, arrXform):
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

		pass

