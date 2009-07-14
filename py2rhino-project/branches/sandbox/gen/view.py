# Auto-generated wrapper for Rhino4 RhinoScript functions
import win32com.client.CLSIDToClass, pythoncom
import win32com.client.util
from pywintypes import IID
from win32com.client import Dispatch
from win32com.client import DispatchBaseClass
class View(DispatchBaseClass):



	def AddNamedCPlane(self):
		"""

		Adds a new named construction plane to the document.

		No parameters

		Returns

		String : The name of the newly created named construction plane if successful.
		Null : If not successful, or on error.

		"""

		pass

	def AddNamedView(self, strName, strView):
		"""

		Adds a new named view to the document.

		Parameters

		strName : Required,   String,   The name of the new named view
		strView : Optional,   String,   The title or identifier of the view to save

		Returns

		String : The name of the newly created named view if successful.
		Null : If not successful, or on error.

		"""

		pass

	def BackgroundBitmap(self, strView, , arrPoint, dblWidth):
		"""

		Returns or sets the background bitmap of the specified view. To remove a wallpaper bitmap, pass an empty string, or "", as the filename to display.

		Parameters

		strView : Optional,   String,   The title or identifier of the view
		 : Optional,   String,   The name of the bitmap file to set as the background bitmap
		arrPoint : Optional,  Array,   A 3-D point the lower left corner of the background bitmap
		dblWidth : Optional,   Number,   The width of the background bitmap

		Returns

		String : If strFileName is not specified,  then the current background bitmap filename if successful.
		String : If strFileName is specified,  then the previous background bitmap filename if successful.
		Null : If not successful, or on error.

		"""

		pass

	def CurrentDetail(self, strLayout, strDetail, blnReturnNames):
		"""

		Returns or changes the current detail view in a page layout view.

		Parameters

		strLayout : Required,   String,   The title or identifier of an existing page layout view
		strDetail : Optional,   String,   The title identifier of the detail view to set current
		blnReturnNames : Optional,   Boolean,   If True (default), then the name, or title, of the detail view is returned

		Returns

		String : If strDetail is not specified, the identifier of the current detail view if successful.
		String : If strDetail is specified, the title or identifier of the previous current detail view is successful.
		Null : If not successful, or on error.

		"""

		pass

	def CurrentView(self, strView, blnReturnName):
		"""

		Returns or sets the currently active view.

		Parameters

		strView : Optional,   String,   The title or identifier of the view to set current
		blnReturnName : Optional,   Boolean,   If True (default), then the name, or title, of the view is returned

		Returns

		String : If the title is not specified, the title or identifier of the current view if successful.
		String : If the title is specified, the title or identifier of the previous current view is successful.
		Null : If not successful, or on error.

		"""

		pass

	def DeleteNamedCPlane(self):
		"""

		Removed a new named construction plane from the document.

		No parameters

		Returns

		Boolean : True or False indicating success or failure.
		Null : On error.

		"""

		pass

	def DeleteNamedView(self):
		"""

		Removed a new named view from  the document.

		No parameters

		Returns

		Boolean : True or False indicating success or failure.
		Null : On error.

		"""

		pass

	def DetailNames(self, strLayout, blnReturnNames):
		"""

		Returns the names, or titles, or identifiers of all detail views in a page layout view.

		Parameters

		strLayout : Required,   String,   The title or identifier of an existing page layout view
		blnReturnNames : Optional,   Boolean,   If True (default), then the names, or titles, of the detail views are returned

		Returns

		Array : A array of strings identifying the detail view names, or titles, or identifiers if successful.
		Null : If not successful, or on error.

		"""

		pass

	def IsBackgroundBitmap(self, strView):
		"""

		Verifies that the specified view contains a background bitmap.

		Parameters

		strView : Required,   String,   The title or identifier of the view

		Returns

		Boolean : True or False indicating success or failure.
		Null : On error.

		"""

		pass

	def IsDetail(self, strLayout, strDetail):
		"""

		Verifies that a detail view exists on a page layout view.

		Parameters

		strLayout : Required,   String,   The title or identifier of an existing page layout view
		strDetail : Required,   String,   The title or identifier of an existing detail view

		Returns

		Null : On error.

		"""

		pass

	def IsLayout(self, strLayout):
		"""

		Verifies that a view is a page layout view.

		Parameters

		strLayout : Required,   String,   The title or identifier of an existing page layout view

		Returns

		Null : On error.

		"""

		pass

	def IsView(self, strView):
		"""

		Verifies that the specified view exists.

		Parameters

		strView : Required,   String,   The title or identifier of the view

		Returns

		Boolean : True or False indicating success or failure.
		Null : On error.

		"""

		pass

	def IsViewCurrent(self, strView):
		"""

		Verifies that the specified view is the current, or active, view.

		Parameters

		strView : Required,   String,   The title or identifier of the view

		Returns

		Boolean : True or False indicating success or failure.
		Null : On error.

		"""

		pass

	def IsViewMaximized(self, strView):
		"""

		Verifies that the specified view is maximized - enlarged so as to fill the entire Rhino window.

		Parameters

		strView : Optional,   String,   The title or identifier of the view

		Returns

		Boolean : True or False indicating success or failure.
		Null : On error.

		"""

		pass

	def IsViewPerspective(self, strView):
		"""

		Verifies that the specified view's projection is set to perspective.

		Parameters

		strView : Optional,   String,   The title or identifier of the view

		Returns

		Boolean : True or False indicating success or failure.
		Null : On error.

		"""

		pass

	def IsViewTitleVisible(self, strView):
		"""

		Verifies that the specified view's title window is visible.

		Parameters

		strView : Optional,   String,   The title or identifier of the view

		Returns

		Boolean : True or False indicating success or failure.
		Null : On error.

		"""

		pass

	def IsWallpaper(self, strView):
		"""

		Verifies that the specified view contains a wallpaper bitmap.

		Parameters

		strView : Required,   String,   The title or identifier of the view

		Returns

		Boolean : True or False indicating success or failure.
		Null : On error.

		"""

		pass

	def MaximizeRestoreView(self, strView):
		"""

		Toggles a view's maximized/restore window state of the specified view.

		Parameters

		strView : Optional,   String,   The title or identifier of the view

		No returns


		"""

		pass

	def NamedCPlane(self, strName):
		"""

		Returns the plane geometry of the specified named construction plane.

		Parameters

		strName : Required,   String,   The name of a named construction plane

		Returns

		Array : An array containing the plane. The elements of a construction plane array are as follows:
		Null : If not successful, or on error.

		"""

		pass

	def NamedCPlanes(self):
		"""

		Returns the names of all named construction planes in the document.

		No parameters

		Returns

		Array : A zero-based, one-dimensional array of strings identifying the named construction planes if successful.
		Null : If not successful, or on error.

		"""

		pass

	def NamedViews(self):
		"""

		Returns the names of all named views in the document.

		No parameters

		Returns

		Array : A zero-based, one-dimensional array of strings identifying the named views if successful.
		Null : If not successful, or on error.

		"""

		pass

	def RenameView(self, strOldTitle, strNewTitle):
		"""

		Renames, or changes the title, of the specified view..

		Parameters

		strOldTitle : Required,   String,   The title or identifier of the view to rename
		strNewTitle : Required,   String,   The new title of the view

		Returns

		String : The view's previous title is successful.
		Null : if not successful, or on error.

		"""

		pass

	def RestoreNamedCPlane(self):
		"""

		Restores a named construction plane to the specified view.

		No parameters

		Returns

		String : The name of the restored named construction plane if successful.
		Null : If not successful, or on error.

		"""

		pass

	def RestoreNamedView(self):
		"""

		Restores a named view to the specified view.

		No parameters

		Returns

		String : The name of the restored named view if successful.
		Null : If not successful, or on error.

		"""

		pass

	def RotateCamera(self, strView, intDirection, dblAngle):
		"""

		Rotates a perspective-projected view's camera. See the RotateCamera command in the Rhino help file for more details.

		Parameters

		strView : Optional,   String,   The title or identifier of the view
		intDirection : Optional,  Number, The direction to rotate the camera where 0 = right, 1 = left, 2 = down, and 3 = up,  The default is 0 = right
		dblAngle : Optional,   Number,   The angle to rotate

		Returns

		Boolean : True or False indicating success or failure.
		Null : On error.

		"""

		pass

	def RotateView(self, strView, intDirection, dblAngle):
		"""

		Rotates a view. See the RotateView command in the Rhino help file for more information.

		Parameters

		strView : Optional,   String,   The title or identifier of the view
		intDirection : Optional,  Number, The direction to rotate the view, where 0 = right, 1 = left, 2 = down, and 3 = up,  The default is 0 = right
		dblAngle : Optional,   Number,   The angle to rotate

		Returns

		Boolean : True or False indicating success or failure.
		Null : On error.

		"""

		pass

	def ShowGrid(self, strView, blnShow):
		"""

		Shows or hides a view's construction plane grid.

		Parameters

		strView : Optional,   String,   The title or identifier of the view to modify
		blnShow : Optional,   Boolean,   The grid display state to set

		Returns

		Boolean : If blnShow is not specified, then the grid display state if successful.
		Boolean : If blnShow is specified, then the previous grid display state if successful.
		Null : On error.

		"""

		pass

	def ShowGridAxes(self, strView, blnShow):
		"""

		Shows or hides a view's construction plane grid axes.

		Parameters

		strView : Optional,   String,   The title or identifier of the view to modify
		blnShow : Optional,   Boolean,   The grid axes display state to set

		Returns

		Boolean : If blnShow is not specified, then the grid axes display state if successful.
		Boolean : If blnShow is specified, then the previous grid axes display state if successful.
		Null : On error.

		"""

		pass

	def ShowViewTitle(self, strView, blnState):
		"""

		Shows or hides the title window of a view.

		Parameters

		strView : Optional,   String,   The title or identifier of the view
		blnState : Optional,   Boolean,   The visible state of the view's title window

		No returns


		"""

		pass

	def ShowWorldAxes(self, strView, blnShow):
		"""

		Shows or hides a view's world axes icon.

		Parameters

		strView : Optional,   String,   The title or identifier of the view to modify
		blnShow : Optional,   Boolean,   The world axes icon display state to set

		Returns

		Boolean : If blnShow is not specified, then the world axes icon display state if successful.
		Boolean : If blnShow is specified, then the previous world axes icon display state if successful.
		Null : On error.

		"""

		pass

	def SynchronizeCPlanes(self):
		"""

		The view synchronization only applies to Rhino's standard-named, parallel-projected views (e.g. Back, Bottom, Front, Left, Right, and Top).  All other views (e.g. Perspective, etc) simply have their construction plane synchronized to that of the specified view's construction plane.

		No parameters

		Returns

		Boolean : True or False indicating success or failure.
		Null : On error.

		"""

		pass

	def TiltView(self, strView, intDirection, dblAngle):
		"""

		Tilts a view by rotating the camera up vector.  See the TiltView command in the Rhino help file for more details.

		Parameters

		strView : Optional,   String,   The title or identifier of the view
		intDirection : Optional,  Number, The direction to rotate the camera where 0 = right and 1 = left, 
		dblAngle : Optional,   Number,   The angle to rotate

		Returns

		Boolean : True or False indicating success or failure.
		Null : On error.

		"""

		pass

	def ViewCPlane(self, strView, arrPlane, 0, 1, 2, 3):
		"""

		Returns or sets the specified view's construction plane.

		Parameters

		strView : Optional,   String,   The title or identifier of the view
		arrPlane : Optional,   Array,  The new construction plane
		0 : Required,   The construction plane's origin (3-D point), 
		1 : Required,   The construction plane's X axis direction (3-D vector), 
		2 : Required,   The construction plane's Y axis direction (3-D vector), 
		3 : Optional,   The construction plane's Z axis direction (3-D vector), 

		Returns

		Array : If a construction plane is not specified, the current construction plane if successful.
		Array : If a construction plane is specified, the previous construction plane if successful.
		Null : If not successful, or on error.

		"""

		pass

	def ViewCamera(self, strView, arrCamera):
		"""

		Returns or sets the camera location of the specified view.

		Parameters

		strView : Optional,   String,   The title or identifier of the view
		arrCamera : Optional,   Array,   A 3-D point identifying the new camera location

		Returns

		Array : If arrCamera is not specified,  then a 3-D point containing the current camera location if successful.
		Array : If arrCamera is specified,  then a 3-D point containing the previous camera location if successful.
		Null : If not successful, or on error.

		"""

		pass

	def ViewCameraLens(self, strView, dblLength):
		"""

		Returns or sets the 35mm camera lens length of the specified perspective projection view.

		Parameters

		strView : Optional,   String,   The title or identifier of the view
		dblLength : Optional,   Number,   The new 35mm camera lens length

		Returns

		Number : If a lens length is not specified, the current lens length if successful.
		Number : If a lens length is specified, the previous lens length is successful.
		Null : If not successful, or on error.

		"""

		pass

	def ViewCameraPlane(self, strView):
		"""

		Returns the orientation of a view's camera.

		Parameters

		strView : Optional,   String,   The title or identifier of the view

		Returns

		Array : The view's camera plane if successful.  The elements of a plane array are as follows:
		Null : If not successful, or on error.

		"""

		pass

	def ViewCameraTarget(self, strView, arrCamera, arrTarget):
		"""

		Returns or sets the camera and target positions of the specified view.

		Parameters

		strView : Optional,   String,   The title or identifier of the view
		arrCamera : Optional,   Array,   A 3-D point identifying the new camera location
		arrTarget : Optional,   Array,   A 3-D point identifying the new target location

		Returns

		Array : If both arrCamera and arrTarget are not specified,  then an array of 3-D point containing the current camera and target locations is returned.
		Array : If either arrCamera or arrTarget are specified,  then an array of 3-D point containing the previous camera and target locations is returned.
		Null : If not successful, or on error.

		"""

		pass

	def ViewCameraUp(self, strView, arrUpVector):
		"""

		Returns or sets the camera up direction of specified view.

		Parameters

		strView : Optional,   String,   The title or identifier of the view
		arrUpVector : Optional,   Array,   A 3-D vector identifying the new camera location

		Returns

		Array : If arrUpVector is not specified,  then a 3-D vector identifying the current camera up direction if successful.
		Array : If arrUpVector is specified,  then a 3-D vector identifying the previous camera up direction if successful.
		Null : If not successful, or on error.

		"""

		pass

	def ViewDisplayMode(self, strView, intMode):
		"""

		Returns or sets a view's display mode.  A view's display mode can be either wireframe, shaded, or render preview.

		Parameters

		strView : Optional,   String,   The title or identifier of the view
		intMode : Optional,   Number,   The display mode

		Returns

		Number : If intMode is not specified, the current display mode for the specified view if successful.
		Number : If intMode is specified, the previous display mode for the specified view if successful.
		Null : If not successful, or on error.

		"""

		pass

	def ViewDisplayModeEx(self, strView, strMode, blnReturnNames):
		"""

		Returns or sets a view's display mode.  Unlike the ViewDisplayMode method, which only allows you to set a view to wireframe, shaded, or render preview, this method allows you to set a view to any display mode including those listed in the Advanced Display Modes section of Rhino's Options dialog box.

		Parameters

		strView : Optional,   String,   The title or identifier of the view
		strMode : Optional,   String,   The name or identifier of the display mode obtained from the ViewDisplayModes method
		blnReturnNames : Optional,   Boolean,   If True (default), then the name the display mode is returned

		Returns

		Number : If strMode is not specified, the current display mode for the specified view if successful.
		Number : If strMode is specified, the previous display mode for the specified view if successful.
		Null : If not successful, or on error.

		"""

		pass

	def ViewDisplayModeName(self, strMode):
		"""

		Returns the name of a display mode given a display mode's identifier.

		Parameters

		strMode : Required,   String,   The identifier of the display mode obtained from the ViewDisplayModes method

		Returns

		String : The name of the display mode if successful.
		Null : If not successful, or on error.

		"""

		pass

	def ViewDisplayModes(self, blnReturnName):
		"""

		Returns a list of view display modes, including those listed in the Advanced Display Modes section of Rhino's Options dialog box.

		Parameters

		blnReturnName : Optional,   Boolean,   If True (default), then the names of the display modes are returned

		Returns

		Array : A array of strings identifying the display mode names or identifiers if successful.
		Null : If not successful, or on error.

		"""

		pass

	def ViewNames(self, blnReturnNames, intType):
		"""

		Returns the names, or titles, or identifiers of all views in the document.

		Parameters

		blnReturnNames : Optional,   Boolean,   If True (default), then the names, or titles, of the views are returned
		intType : Optional,   Number,   The type of view to return, where:

		Returns

		Array : A array of strings identifying the view names, or titles, or identifiers if successful.
		Null : If not successful, or on error.

		"""

		pass

	def ViewNearCorners(self, strView):
		"""

		Returns the 3-D corners points of a view's near clipping plane rectangle. This function can be useful in determining the "real world" size of a parallel-projected view.

		Parameters

		strView : Optional,   String,   The title or identifier of the view

		Returns

		Array : An array of four 3-D points that define the corners of the rectangle if successful.  Points are returned in counter-clockwise order.
		Null : If not successful, or on error.

		"""

		pass

	def ViewProjection(self, strView, intMode):
		"""

		Returns or sets a view's projection mode.  A view's projection mode can be either parallel or perspective.

		Parameters

		strView : Optional,   String,   The title or identifier of the view
		intMode : Optional,   Number,   The projection mode

		Returns

		Number : If intMode is not specified, the current projection mode for the specified view if successful.
		Number : If intMode is specified, the previous projection mode for the specified view if successful.
		Null : If not successful, or on error.

		"""

		pass

	def ViewRadius(self, strView, dblRadius):
		"""

		Returns or sets the radius of the viewing frustum of a parallel-projected view. This function is useful when you need an absolute zoom factor for a parallel-projected view.

		Parameters

		strView : Optional,   String,   The title or identifier of the view
		dblRadius : Optional,   Number,   The view radius

		Returns

		Number : If dblRadius is not specified, the current view radius for the specified view if successful.
		Number : If dblRadius is specified, the previous view radius for the specified view if successful.
		Null : If not successful, or on error.

		"""

		pass

	def ViewSize(self, strView):
		"""

		Returns the width and height in pixels of the specified view.

		Parameters

		strView : Optional,   String,   The title or identifier of the view

		Returns

		Array : A zero-based, one-dimensional array containing two numbers identifying the width and height if successful
		Null : If not successful, or on error.

		"""

		pass

	def ViewTarget(self, strView, arrTarget):
		"""

		Returns or sets the target location of the specified view.

		Parameters

		strView : Optional,   String,   The title or identifier of the view
		arrTarget : Optional,   Array,   A 3-D point identifying the new target location

		Returns

		Array : If arrTarget is not specified,  then a 3-D point containing the current target location if successful.
		Array : If arrTarget is specified,  then a 3-D point containing the previous target location if successful.
		Null : If not successful, or on error.

		"""

		pass

	def ViewTitle(self, strMode):
		"""

		Returns the name, or title, of a view given a view's identifier.

		Parameters

		strMode : Required,   String,   The identifier of the display mode obtained from the ViewNames method

		Returns

		String : The name, or title, of the view if successful.
		Null : If not successful, or on error.

		"""

		pass

	def Wallpaper(self, strView, strFileName):
		"""

		Returns or sets the wallpaper bitmap of the specified view. To remove a wallpaper bitmap, pass an empty string, or "", as the filename to display.

		Parameters

		strView : Optional,   String,   The title or identifier of the view
		strFileName : Optional,   String,   The name of the bitmap file to set as the wallpaper

		Returns

		String : If strFileName is not specified,  then the current wallpaper bitmap filename if successful.
		String : If strFileName is specified,  then the previous wallpaper bitmap filename if successful.
		Null : If not successful, or on error.

		"""

		pass

	def WallpaperGrayScale(self, strView, blnGrayScale):
		"""

		Returns or sets the grayscale display option of the wallpaper bitmap of the specified view.

		Parameters

		strView : Optional,   String,   The title or identifier of the view
		blnGrayScale : Optional,   Boolean,   Display the wallpaper bitmap in grayscale (True) or color (False)

		Returns

		Boolean : If blnGrayScale is not specified,  then the current grayscale display option if successful.
		Boolean : If blnGrayScale is specified,  then the previous grayscale display option if successful.
		Null : If not successful, or on error.

		"""

		pass

	def WallpaperHidden(self, strView, blnHidden):
		"""

		Returns or sets the visibility of the wallpaper bitmap of the specified view.

		Parameters

		strView : Optional,   String,   The title or identifier of the view
		blnHidden : Optional,   Boolean,   Hide the wallpaper bitmap (True) or show the wallpaper bitmap (False)

		Returns

		Boolean : If blnHidden is not specified,  then the current wallpaper visibility if successful.
		Boolean : If blnHidden is specified,  then the previous wallpaper visibility if successful.
		Null : If not successful, or on error.

		"""

		pass

	def ZoomBoundingBox(self, arrCorners, strView, blnAll):
		"""

		Zooms to the extents of a specified bounding box in the specified view, or in the active view.

		Parameters

		arrCorners : Required,   Array,   An array of eight 3-D points that define the corners of the box
		strView : Optional,   String,   The title or identifier of the view
		blnAll : Optional,   Boolean,   Zoom extents in all views

		No returns


		"""

		pass

	def ZoomExtents(self, strView, blnAll):
		"""

		Zooms to the extents of visible objects in the specified view, or in the active view.

		Parameters

		strView : Optional,   String,   The title or identifier of the view
		blnAll : Optional,   Boolean,   Zoom extents in all views

		No returns


		"""

		pass

	def ZoomSelected(self, strView, blnAll):
		"""

		Zooms to the extents of selected objects in the specified view, or in the active view.

		Parameters

		strView : Optional,   String,   The title or identifier of the view
		blnAll : Optional,   Boolean,   Zoom selected in all views

		No returns


		"""

		pass

