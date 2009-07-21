# Auto-generated wrapper for Rhino4 RhinoScript functions

import exceptions
from py2rhino._util import *
from py2rhino._rhinoscript import IRhinoScript

class View(IRhinoScript):



    def add_named_c_plane(self, name, view=None):
        """        
        Adds a new named construction plane to the document.
    
        Parameters
        ==========

        name, String, Required        
        The name of the new named construction plane.
            
        view, String, Optional        
        The title or identifier of the view from which to save the construction plane.  If omitted, the current active view is used.
            
        Returns
        =======

        string
        The name of the newly created named construction plane if successful.

        null
        If not successful, or on error.

        """

        params = [name, view]
        params_required = [True, False]
        params_magic_numbers = [(VT_BSTR, 1), (VT_BSTR, 1)]
        params_flattened = [name, view]

        for i in range(len(params)):
            if (params[i] == None) and (not params_required[i]):
                params_magic_numbers.pop(i)
                params_flattened.pop(i)

        params_magic_numbers = tuple(params_magic_numbers)
        params_flattened = tuple(params_flattened)

        return self._ApplyTypes_(280, 1, (VT_VARIANT, 0), params_magic_numbers, u"AddNamedCPlane", None, *params_flattened)

    def add_named_view(self, name, view=None):
        """        
        Adds a new named view to the document.
    
        Parameters
        ==========

        name, String, Required        
        The name of the new named view.
            
        view, String, Optional        
        The title or identifier of the view to save.  If omitted, the current active view is saved.
            
        Returns
        =======

        string
        The name of the newly created named view if successful.

        null
        If not successful, or on error.

        """

        params = [name, view]
        params_required = [True, False]
        params_magic_numbers = [(VT_BSTR, 1), (VT_BSTR, 1)]
        params_flattened = [name, view]

        for i in range(len(params)):
            if (params[i] == None) and (not params_required[i]):
                params_magic_numbers.pop(i)
                params_flattened.pop(i)

        params_magic_numbers = tuple(params_magic_numbers)
        params_flattened = tuple(params_flattened)

        return self._ApplyTypes_(281, 1, (VT_VARIANT, 0), params_magic_numbers, u"AddNamedView", None, *params_flattened)

    def background_bitmap(self, view=None, file_name=None, point=None, width=None):
        """        
        Returns or sets the background bitmap of the specified view. To remove a wallpaper bitmap, pass an empty string, or "", as the filename to display.
    
        Parameters
        ==========

        view, String, Optional        
        The title or identifier of the view.  If omitted, the current active view is used.
            
        file_name, String, Optional        
        The name of the bitmap file to set as the background bitmap.  The supported bitmap file formats are as follows:
		Type
		Description
		bmp
		Windows Bitmap
		tga
		Truevision Targa
		jpg, jpeg
		JPEG Compliant
		pcx
		Zsoft Paintbrush
		png
		Portable Network Graphics
		tif, tiff
            
        point, Array of ????, Optional        
        A 3-D point the lower left corner of the background bitmap. If omitted, the background bitmap's lower left corner will be located at the world origin, or (0,0,0).
            
        width, Double, Optional        
        The width of the background bitmap. If omitted, the actual width of the bitmap will be used.
            
        Returns
        =======

        string
        If strFileName is not specified,  then the current background bitmap filename if successful.

        string
        If strFileName is specified,  then the previous background bitmap filename if successful.

        null
        If not successful, or on error.

        """

        params = [view, file_name, point, width]
        params_required = [False, False, False, False]
        params_magic_numbers = [(VT_BSTR, 1), (VT_BSTR, 1), (VT_VARIANT, 1), (VT_R8, 1)]
        params_flattened = [view, file_name, flatten(point), width]

        for i in range(len(params)):
            if (params[i] == None) and (not params_required[i]):
                params_magic_numbers.pop(i)
                params_flattened.pop(i)

        params_magic_numbers = tuple(params_magic_numbers)
        params_flattened = tuple(params_flattened)

        return self._ApplyTypes_(780, 1, (VT_VARIANT, 0), params_magic_numbers, u"BackgroundBitmap", None, *params_flattened)

    def current_detail(self, layout, detail=None, return_names=None):
        """        
        Returns or changes the current detail view in a page layout view.
    
        Parameters
        ==========

        layout, String, Required        
        The title or identifier of an existing page layout view.
            
        detail, String, Optional        
        The title identifier of the detail view to set current.  If omitted, identifier of the current detail view is returned.  Note, if no detail views are active, then the title or identifier of the page layout view is returned. Also, to set the page layout view current, simply user strLayout as the value you pass to strDetail.
            
        return_names, Boolean, Optional        
        If True (default), then the name, or title, of the detail view is returned. If False, then the identifier of the detail view is returned.
            
        Returns
        =======

        string
        If strDetail is not specified, the identifier of the current detail view if successful.

        string
        If strDetail is specified, the title or identifier of the previous current detail view is successful.

        null
        If not successful, or on error.

        """

        params = [layout, detail, return_names]
        params_required = [True, False, False]
        params_magic_numbers = [(VT_BSTR, 1), (VT_BSTR, 1), (VT_BOOL, 1)]
        params_flattened = [layout, detail, return_names]

        for i in range(len(params)):
            if (params[i] == None) and (not params_required[i]):
                params_magic_numbers.pop(i)
                params_flattened.pop(i)

        params_magic_numbers = tuple(params_magic_numbers)
        params_flattened = tuple(params_flattened)

        return self._ApplyTypes_(923, 1, (VT_VARIANT, 0), params_magic_numbers, u"CurrentDetail", None, *params_flattened)

    def current_view(self, view=None, return_name=None):
        """        
        Returns or sets the currently active view.
    
        Parameters
        ==========

        view, String, Optional        
        The title or identifier of the view to set current.  If omitted, only the title or identifier of the current view is returned.
            
        return_name, Boolean, Optional        
        If True (default), then the name, or title, of the view is returned. If False, then the identifier of the view is returned.
            
        Returns
        =======

        string
        If the title is not specified, the title or identifier of the current view if successful.

        string
        If the title is specified, the title or identifier of the previous current view is successful.

        null
        If not successful, or on error.

        """

        params = [view, return_name]
        params_required = [False, False]
        params_magic_numbers = [(VT_BSTR, 1), (VT_BOOL, 1)]
        params_flattened = [view, return_name]

        for i in range(len(params)):
            if (params[i] == None) and (not params_required[i]):
                params_magic_numbers.pop(i)
                params_flattened.pop(i)

        params_magic_numbers = tuple(params_magic_numbers)
        params_flattened = tuple(params_flattened)

        return self._ApplyTypes_(251, 1, (VT_VARIANT, 0), params_magic_numbers, u"CurrentView", None, *params_flattened)

    def delete_named_c_plane(self, name):
        """        
        Removed a new named construction plane from the document.
    
        Parameters
        ==========

        name, String, Required        
        The name of the named construction plane to remove.
            
        Returns
        =======

        boolean
        True or False indicating success or failure.

        null
        On error.

        """

        params = [name]
        params_required = [True]
        params_magic_numbers = [(VT_BSTR, 1),]
        params_flattened = [name]

        for i in range(len(params)):
            if (params[i] == None) and (not params_required[i]):
                params_magic_numbers.pop(i)
                params_flattened.pop(i)

        params_magic_numbers = tuple(params_magic_numbers)
        params_flattened = tuple(params_flattened)

        return self._ApplyTypes_(284, 1, (VT_VARIANT, 0), params_magic_numbers, u"DeleteNamedCPlane", None, *params_flattened)

    def delete_named_view(self, name):
        """        
        Removed a new named view from  the document.
    
        Parameters
        ==========

        name, String, Required        
        The name of the named view to remove.
            
        Returns
        =======

        boolean
        True or False indicating success or failure.

        null
        On error.

        """

        params = [name]
        params_required = [True]
        params_magic_numbers = [(VT_BSTR, 1),]
        params_flattened = [name]

        for i in range(len(params)):
            if (params[i] == None) and (not params_required[i]):
                params_magic_numbers.pop(i)
                params_flattened.pop(i)

        params_magic_numbers = tuple(params_magic_numbers)
        params_flattened = tuple(params_flattened)

        return self._ApplyTypes_(285, 1, (VT_VARIANT, 0), params_magic_numbers, u"DeleteNamedView", None, *params_flattened)

    def detail_names(self, layout, return_names=None):
        """        
        Returns the names, or titles, or identifiers of all detail views in a page layout view.
    
        Parameters
        ==========

        layout, String, Required        
        The title or identifier of an existing page layout view.
            
        return_names, Boolean, Optional        
        If True (default), then the names, or titles, of the detail views are returned. If False, then the identifiers of the detail views are returned.
            
        Returns
        =======

        array
        A array of strings identifying the detail view names, or titles, or identifiers if successful.

        null
        If not successful, or on error.

        """

        params = [layout, return_names]
        params_required = [True, False]
        params_magic_numbers = [(VT_BSTR, 1), (VT_BOOL, 1)]
        params_flattened = [layout, return_names]

        for i in range(len(params)):
            if (params[i] == None) and (not params_required[i]):
                params_magic_numbers.pop(i)
                params_flattened.pop(i)

        params_magic_numbers = tuple(params_magic_numbers)
        params_flattened = tuple(params_flattened)

        return self._ApplyTypes_(922, 1, (VT_VARIANT, 0), params_magic_numbers, u"DetailNames", None, *params_flattened)

    def is_background_bitmap(self, view):
        """        
        Verifies that the specified view contains a background bitmap.
    
        Parameters
        ==========

        view, String, Required        
        The title or identifier of the view.
            
        Returns
        =======

        boolean
        True or False indicating success or failure.

        null
        On error.

        """

        params = [view]
        params_required = [True]
        params_magic_numbers = [(VT_BSTR, 1),]
        params_flattened = [view]

        for i in range(len(params)):
            if (params[i] == None) and (not params_required[i]):
                params_magic_numbers.pop(i)
                params_flattened.pop(i)

        params_magic_numbers = tuple(params_magic_numbers)
        params_flattened = tuple(params_flattened)

        return self._ApplyTypes_(779, 1, (VT_VARIANT, 0), params_magic_numbers, u"IsBackgroundBitmap", None, *params_flattened)

    def is_detail(self, layout, detail):
        """        
        Verifies that a detail view exists on a page layout view.
    
        Parameters
        ==========

        layout, String, Required        
        The title or identifier of an existing page layout view.
            
        detail, String, Required        
        The title or identifier of an existing detail view.
            
        Returns
        =======

        null
        On error.

        """

        params = [layout, detail]
        params_required = [True, True]
        params_magic_numbers = [(VT_BSTR, 1), (VT_BSTR, 1)]
        params_flattened = [layout, detail]

        for i in range(len(params)):
            if (params[i] == None) and (not params_required[i]):
                params_magic_numbers.pop(i)
                params_flattened.pop(i)

        params_magic_numbers = tuple(params_magic_numbers)
        params_flattened = tuple(params_flattened)

        return self._ApplyTypes_(921, 1, (VT_VARIANT, 0), params_magic_numbers, u"IsDetail", None, *params_flattened)

    def is_layout(self, layout):
        """        
        Verifies that a view is a page layout view.
    
        Parameters
        ==========

        layout, String, Required        
        The title or identifier of an existing page layout view.
            
        Returns
        =======

        null
        On error.

        """

        params = [layout]
        params_required = [True]
        params_magic_numbers = [(VT_BSTR, 1),]
        params_flattened = [layout]

        for i in range(len(params)):
            if (params[i] == None) and (not params_required[i]):
                params_magic_numbers.pop(i)
                params_flattened.pop(i)

        params_magic_numbers = tuple(params_magic_numbers)
        params_flattened = tuple(params_flattened)

        return self._ApplyTypes_(920, 1, (VT_VARIANT, 0), params_magic_numbers, u"IsLayout", None, *params_flattened)

    def is_view(self, view):
        """        
        Verifies that the specified view exists.
    
        Parameters
        ==========

        view, String, Required        
        The title or identifier of the view.
            
        Returns
        =======

        boolean
        True or False indicating success or failure.

        null
        On error.

        """

        params = [view]
        params_required = [True]
        params_magic_numbers = [(VT_BSTR, 1),]
        params_flattened = [view]

        for i in range(len(params)):
            if (params[i] == None) and (not params_required[i]):
                params_magic_numbers.pop(i)
                params_flattened.pop(i)

        params_magic_numbers = tuple(params_magic_numbers)
        params_flattened = tuple(params_flattened)

        return self._ApplyTypes_(252, 1, (VT_VARIANT, 0), params_magic_numbers, u"IsView", None, *params_flattened)

    def is_view_current(self, view):
        """        
        Verifies that the specified view is the current, or active, view.
    
        Parameters
        ==========

        view, String, Required        
        The title or identifier of the view.
            
        Returns
        =======

        boolean
        True or False indicating success or failure.

        null
        On error.

        """

        params = [view]
        params_required = [True]
        params_magic_numbers = [(VT_BSTR, 1),]
        params_flattened = [view]

        for i in range(len(params)):
            if (params[i] == None) and (not params_required[i]):
                params_magic_numbers.pop(i)
                params_flattened.pop(i)

        params_magic_numbers = tuple(params_magic_numbers)
        params_flattened = tuple(params_flattened)

        return self._ApplyTypes_(253, 1, (VT_VARIANT, 0), params_magic_numbers, u"IsViewCurrent", None, *params_flattened)

    def is_view_maximized(self, view=None):
        """        
        Verifies that the specified view is maximized - enlarged so as to fill the entire Rhino window.
    
        Parameters
        ==========

        view, String, Optional        
        The title or identifier of the view.  If omitted, the current active view is used.
            
        Returns
        =======

        boolean
        True or False indicating success or failure.

        null
        On error.

        """

        params = [view]
        params_required = [False]
        params_magic_numbers = [(VT_BSTR, 1),]
        params_flattened = [view]

        for i in range(len(params)):
            if (params[i] == None) and (not params_required[i]):
                params_magic_numbers.pop(i)
                params_flattened.pop(i)

        params_magic_numbers = tuple(params_magic_numbers)
        params_flattened = tuple(params_flattened)

        return self._ApplyTypes_(254, 1, (VT_VARIANT, 0), params_magic_numbers, u"IsViewMaximized", None, *params_flattened)

    def is_view_perspective(self, view=None):
        """        
        Verifies that the specified view's projection is set to perspective.
    
        Parameters
        ==========

        view, String, Optional        
        The title or identifier of the view.  If omitted, the current active view is used.
            
        Returns
        =======

        boolean
        True or False indicating success or failure.

        null
        On error.

        """

        params = [view]
        params_required = [False]
        params_magic_numbers = [(VT_BSTR, 1),]
        params_flattened = [view]

        for i in range(len(params)):
            if (params[i] == None) and (not params_required[i]):
                params_magic_numbers.pop(i)
                params_flattened.pop(i)

        params_magic_numbers = tuple(params_magic_numbers)
        params_flattened = tuple(params_flattened)

        return self._ApplyTypes_(255, 1, (VT_VARIANT, 0), params_magic_numbers, u"IsViewPerspective", None, *params_flattened)

    def is_view_title_visible(self, view=None):
        """        
        Verifies that the specified view's title window is visible.
    
        Parameters
        ==========

        view, String, Optional        
        The title or identifier of the view.  If omitted, the current active view is omitted.
            
        Returns
        =======

        boolean
        True or False indicating success or failure.

        null
        On error.

        """

        params = [view]
        params_required = [False]
        params_magic_numbers = [(VT_BSTR, 1),]
        params_flattened = [view]

        for i in range(len(params)):
            if (params[i] == None) and (not params_required[i]):
                params_magic_numbers.pop(i)
                params_flattened.pop(i)

        params_magic_numbers = tuple(params_magic_numbers)
        params_flattened = tuple(params_flattened)

        return self._ApplyTypes_(256, 1, (VT_VARIANT, 0), params_magic_numbers, u"IsViewTitleVisible", None, *params_flattened)

    def is_wallpaper(self, view):
        """        
        Verifies that the specified view contains a wallpaper bitmap.
    
        Parameters
        ==========

        view, String, Required        
        The title or identifier of the view.
            
        Returns
        =======

        boolean
        True or False indicating success or failure.

        null
        On error.

        """

        params = [view]
        params_required = [True]
        params_magic_numbers = [(VT_BSTR, 1),]
        params_flattened = [view]

        for i in range(len(params)):
            if (params[i] == None) and (not params_required[i]):
                params_magic_numbers.pop(i)
                params_flattened.pop(i)

        params_magic_numbers = tuple(params_magic_numbers)
        params_flattened = tuple(params_flattened)

        return self._ApplyTypes_(531, 1, (VT_VARIANT, 0), params_magic_numbers, u"IsWallpaper", None, *params_flattened)

    def maximize_restore_view(self, view=None):
        """        
        Toggles a view's maximized/restore window state of the specified view.
    
        Parameters
        ==========

        view, String, Optional        
        The title or identifier of the view.  If omitted, the current active view is used.
            
        No returns


        """

        params = [view]
        params_required = [False]
        params_magic_numbers = [(VT_BSTR, 1),]
        params_flattened = [view]

        for i in range(len(params)):
            if (params[i] == None) and (not params_required[i]):
                params_magic_numbers.pop(i)
                params_flattened.pop(i)

        params_magic_numbers = tuple(params_magic_numbers)
        params_flattened = tuple(params_flattened)

        return self._ApplyTypes_(257, 1, (VT_VARIANT, 0), params_magic_numbers, u"MaximizeRestoreView", None, *params_flattened)

    def named_c_plane(self, name):
        """        
        Returns the plane geometry of the specified named construction plane.
    
        Parameters
        ==========

        name, String, Required        
        The name of a named construction plane.
            
        Returns
        =======

        array
        An array containing the plane. The elements of a construction plane array are as follows:

        null
        If not successful, or on error.

        """

        params = [name]
        params_required = [True]
        params_magic_numbers = [(VT_BSTR, 1),]
        params_flattened = [name]

        for i in range(len(params)):
            if (params[i] == None) and (not params_required[i]):
                params_magic_numbers.pop(i)
                params_flattened.pop(i)

        params_magic_numbers = tuple(params_magic_numbers)
        params_flattened = tuple(params_flattened)

        return self._ApplyTypes_(286, 1, (VT_VARIANT, 0), params_magic_numbers, u"NamedCPlane", None, *params_flattened)

    def named_c_planes():
        """        
        Returns the names of all named construction planes in the document.
    
        No parameters

        Returns
        =======

        array
        A zero-based, one-dimensional array of strings identifying the named construction planes if successful.

        null
        If not successful, or on error.

        """

        params = []
        params_required = []
        params_magic_numbers = []
        params_flattened = []

        for i in range(len(params)):
            if (params[i] == None) and (not params_required[i]):
                params_magic_numbers.pop(i)
                params_flattened.pop(i)

        params_magic_numbers = tuple(params_magic_numbers)
        params_flattened = tuple(params_flattened)

        return self._ApplyTypes_(258, 1, (VT_VARIANT, 0), params_magic_numbers, u"NamedCPlanes", None, *params_flattened)

    def named_views():
        """        
        Returns the names of all named views in the document.
    
        No parameters

        Returns
        =======

        array
        A zero-based, one-dimensional array of strings identifying the named views if successful.

        null
        If not successful, or on error.

        """

        params = []
        params_required = []
        params_magic_numbers = []
        params_flattened = []

        for i in range(len(params)):
            if (params[i] == None) and (not params_required[i]):
                params_magic_numbers.pop(i)
                params_flattened.pop(i)

        params_magic_numbers = tuple(params_magic_numbers)
        params_flattened = tuple(params_flattened)

        return self._ApplyTypes_(259, 1, (VT_VARIANT, 0), params_magic_numbers, u"NamedViews", None, *params_flattened)

    def rename_view(self, old_title, new_title):
        """        
        Renames, or changes the title, of the specified view..
    
        Parameters
        ==========

        old_title, String, Required        
        The title or identifier of the view to rename.
            
        new_title, String, Required        
        The new title of the view.
            
        Returns
        =======

        string
        The view's previous title is successful.

        null
        if not successful, or on error.

        """

        params = [old_title, new_title]
        params_required = [True, True]
        params_magic_numbers = [(VT_BSTR, 1), (VT_BSTR, 1)]
        params_flattened = [old_title, new_title]

        for i in range(len(params)):
            if (params[i] == None) and (not params_required[i]):
                params_magic_numbers.pop(i)
                params_flattened.pop(i)

        params_magic_numbers = tuple(params_magic_numbers)
        params_flattened = tuple(params_flattened)

        return self._ApplyTypes_(260, 1, (VT_VARIANT, 0), params_magic_numbers, u"RenameView", None, *params_flattened)

    def restore_named_c_plane(self, name, view=None):
        """        
        Restores a named construction plane to the specified view.
    
        Parameters
        ==========

        name, String, Required        
        The name of the named construction plane to restore.
            
        view, String, Optional        
        The title or identifier of the view to restore the construction plane.  If omitted, the current active view is used.
            
        Returns
        =======

        string
        The name of the restored named construction plane if successful.

        null
        If not successful, or on error.

        """

        params = [name, view]
        params_required = [True, False]
        params_magic_numbers = [(VT_BSTR, 1), (VT_BSTR, 1)]
        params_flattened = [name, view]

        for i in range(len(params)):
            if (params[i] == None) and (not params_required[i]):
                params_magic_numbers.pop(i)
                params_flattened.pop(i)

        params_magic_numbers = tuple(params_magic_numbers)
        params_flattened = tuple(params_flattened)

        return self._ApplyTypes_(282, 1, (VT_VARIANT, 0), params_magic_numbers, u"RestoreNamedCPlane", None, *params_flattened)

    def restore_named_view(self, name, view=None, restore_bitmap=None):
        """        
        Restores a named view to the specified view.
    
        Parameters
        ==========

        name, String, Required        
        The name of the named view to restore.
            
        view, String, Optional        
        The title or identifier of the view to restore the view.  If omitted, the current active view is used.
            
        restore_bitmap, Boolean, Optional        
        Restore the named view's background bitmap. If omitted, the named view's background bitmap is not restored (false).
            
        Returns
        =======

        string
        The name of the restored named view if successful.

        null
        If not successful, or on error.

        """

        params = [name, view, restore_bitmap]
        params_required = [True, False, False]
        params_magic_numbers = [(VT_BSTR, 1), (VT_BSTR, 1), (VT_BOOL, 1)]
        params_flattened = [name, view, restore_bitmap]

        for i in range(len(params)):
            if (params[i] == None) and (not params_required[i]):
                params_magic_numbers.pop(i)
                params_flattened.pop(i)

        params_magic_numbers = tuple(params_magic_numbers)
        params_flattened = tuple(params_flattened)

        return self._ApplyTypes_(283, 1, (VT_VARIANT, 0), params_magic_numbers, u"RestoreNamedView", None, *params_flattened)

    def rotate_camera(self, view=None, direction=None, angle=None):
        """        
        Rotates a perspective-projected view's camera. See the RotateCamera command in the Rhino help file for more details.
    
        Parameters
        ==========

        view, String, Optional        
        The title or identifier of the view.  If omitted, the current active view is used.
            
        direction, Integer, Optional        
        The default is 0 = right.
            
        angle, Double, Optional        
        The angle to rotate. If omitted, the angle of rotation is specified by the "Increment in divisions of a circle" parameter specified in Options command's View tab.
            
        Returns
        =======

        boolean
        True or False indicating success or failure.

        null
        On error.

        """

        params = [view, direction, angle]
        params_required = [False, False, False]
        params_magic_numbers = [(VT_BSTR, 1), (VT_I2, 1), (VT_R8, 1)]
        params_flattened = [view, direction, angle]

        for i in range(len(params)):
            if (params[i] == None) and (not params_required[i]):
                params_magic_numbers.pop(i)
                params_flattened.pop(i)

        params_magic_numbers = tuple(params_magic_numbers)
        params_flattened = tuple(params_flattened)

        return self._ApplyTypes_(519, 1, (VT_VARIANT, 0), params_magic_numbers, u"RotateCamera", None, *params_flattened)

    def rotate_view(self, view=None, direction=None, angle=None):
        """        
        Rotates a view. See the RotateView command in the Rhino help file for more information.
    
        Parameters
        ==========

        view, String, Optional        
        The title or identifier of the view.  If omitted, the current active view is used.
            
        direction, Integer, Optional        
        The default is 0 = right.
            
        angle, Double, Optional        
        The angle to rotate. If omitted, the angle of rotation is specified by the "Increment in divisions of a circle" parameter specified in Options command's View tab.
            
        Returns
        =======

        boolean
        True or False indicating success or failure.

        null
        On error.

        """

        params = [view, direction, angle]
        params_required = [False, False, False]
        params_magic_numbers = [(VT_BSTR, 1), (VT_I2, 1), (VT_R8, 1)]
        params_flattened = [view, direction, angle]

        for i in range(len(params)):
            if (params[i] == None) and (not params_required[i]):
                params_magic_numbers.pop(i)
                params_flattened.pop(i)

        params_magic_numbers = tuple(params_magic_numbers)
        params_flattened = tuple(params_flattened)

        return self._ApplyTypes_(650, 1, (VT_VARIANT, 0), params_magic_numbers, u"RotateView", None, *params_flattened)

    def show_grid(self, view=None, show=None):
        """        
        Shows or hides a view's construction plane grid.
    
        Parameters
        ==========

        view, String, Optional        
        The title or identifier of the view to modify.  If omitted, the current active view is used.
            
        show, Boolean, Optional        
        The grid display state to set.  If omitted, the current grid display state is returned.
            
        Returns
        =======

        boolean
        If blnShow is not specified, then the grid display state if successful.

        boolean
        If blnShow is specified, then the previous grid display state if successful.

        null
        On error.

        """

        params = [view, show]
        params_required = [False, False]
        params_magic_numbers = [(VT_BSTR, 1), (VT_BOOL, 1)]
        params_flattened = [view, show]

        for i in range(len(params)):
            if (params[i] == None) and (not params_required[i]):
                params_magic_numbers.pop(i)
                params_flattened.pop(i)

        params_magic_numbers = tuple(params_magic_numbers)
        params_flattened = tuple(params_flattened)

        return self._ApplyTypes_(738, 1, (VT_VARIANT, 0), params_magic_numbers, u"ShowGrid", None, *params_flattened)

    def show_grid_axes(self, view=None, show=None):
        """        
        Shows or hides a view's construction plane grid axes.
    
        Parameters
        ==========

        view, String, Optional        
        The title or identifier of the view to modify.  If omitted, the current active view is used.
            
        show, Boolean, Optional        
        The grid axes display state to set.  If omitted, the current grid axes display state is returned.
            
        Returns
        =======

        boolean
        If blnShow is not specified, then the grid axes display state if successful.

        boolean
        If blnShow is specified, then the previous grid axes display state if successful.

        null
        On error.

        """

        params = [view, show]
        params_required = [False, False]
        params_magic_numbers = [(VT_BSTR, 1), (VT_BOOL, 1)]
        params_flattened = [view, show]

        for i in range(len(params)):
            if (params[i] == None) and (not params_required[i]):
                params_magic_numbers.pop(i)
                params_flattened.pop(i)

        params_magic_numbers = tuple(params_magic_numbers)
        params_flattened = tuple(params_flattened)

        return self._ApplyTypes_(739, 1, (VT_VARIANT, 0), params_magic_numbers, u"ShowGridAxes", None, *params_flattened)

    def show_view_title(self, view=None, state=None):
        """        
        Shows or hides the title window of a view.
    
        Parameters
        ==========

        view, String, Optional        
        The title or identifier of the view.  If omitted, the current active view is used.
            
        state, Boolean, Optional        
        The visible state of the view's title window.  If omitted, the title will be shown (True).
            
        No returns


        """

        params = [view, state]
        params_required = [False, False]
        params_magic_numbers = [(VT_BSTR, 1), (VT_BOOL, 1)]
        params_flattened = [view, state]

        for i in range(len(params)):
            if (params[i] == None) and (not params_required[i]):
                params_magic_numbers.pop(i)
                params_flattened.pop(i)

        params_magic_numbers = tuple(params_magic_numbers)
        params_flattened = tuple(params_flattened)

        return self._ApplyTypes_(261, 1, (VT_VARIANT, 0), params_magic_numbers, u"ShowViewTitle", None, *params_flattened)

    def show_world_axes(self, view=None, show=None):
        """        
        Shows or hides a view's world axes icon.
    
        Parameters
        ==========

        view, String, Optional        
        The title or identifier of the view to modify.  If omitted, the current active view is used.
            
        show, Boolean, Optional        
        The world axes icon display state to set.  If omitted, the current world axes icon display state is returned.
            
        Returns
        =======

        boolean
        If blnShow is not specified, then the world axes icon display state if successful.

        boolean
        If blnShow is specified, then the previous world axes icon display state if successful.

        null
        On error.

        """

        params = [view, show]
        params_required = [False, False]
        params_magic_numbers = [(VT_BSTR, 1), (VT_BOOL, 1)]
        params_flattened = [view, show]

        for i in range(len(params)):
            if (params[i] == None) and (not params_required[i]):
                params_magic_numbers.pop(i)
                params_flattened.pop(i)

        params_magic_numbers = tuple(params_magic_numbers)
        params_flattened = tuple(params_flattened)

        return self._ApplyTypes_(740, 1, (VT_VARIANT, 0), params_magic_numbers, u"ShowWorldAxes", None, *params_flattened)

    def synchronize_c_planes(self, view=None):
        """        
        Synchronizes all views and their construction plane to that of a specified view's construction plane.
		Normally, changing a view's construction plane is unique to that view.  This method changes the construction planes and normal views of all views to be of a right-angle orientation based on a specified view's construction plane.  This save the effort of changing all views independently, and maintains a standard right-angle view arrangement.
		The view synchronization only applies to Rhino's standard-named, parallel-projected views (e.g. Back, Bottom, Front, Left, Right, and Top).  All other views (e.g. Perspective, etc) simply have their construction plane synchronized to that of the specified view's construction plane.
    
        Parameters
        ==========

        view, String, Optional        
        The title or identifier of the view from which to synchronize.  If omitted, the current active view is used.
            
        Returns
        =======

        boolean
        True or False indicating success or failure.

        null
        On error.

        """

        params = [view]
        params_required = [False]
        params_magic_numbers = [(VT_BSTR, 1),]
        params_flattened = [view]

        for i in range(len(params)):
            if (params[i] == None) and (not params_required[i]):
                params_magic_numbers.pop(i)
                params_flattened.pop(i)

        params_magic_numbers = tuple(params_magic_numbers)
        params_flattened = tuple(params_flattened)

        return self._ApplyTypes_(289, 1, (VT_VARIANT, 0), params_magic_numbers, u"SynchronizeCPlanes", None, *params_flattened)

    def tilt_view(self, view=None, direction=None, angle=None):
        """        
        Tilts a view by rotating the camera up vector.  See the TiltView command in the Rhino help file for more details.
    
        Parameters
        ==========

        view, String, Optional        
        The title or identifier of the view.  If omitted, the current active view is used.
            
        direction, Integer, Optional        
        
            
        angle, Double, Optional        
        The angle to rotate. If omitted, the angle of rotation is specified by the "Increment in divisions of a circle" parameter specified in Options command's View tab.
            
        Returns
        =======

        boolean
        True or False indicating success or failure.

        null
        On error.

        """

        params = [view, direction, angle]
        params_required = [False, False, False]
        params_magic_numbers = [(VT_BSTR, 1), (VT_I2, 1), (VT_R8, 1)]
        params_flattened = [view, direction, angle]

        for i in range(len(params)):
            if (params[i] == None) and (not params_required[i]):
                params_magic_numbers.pop(i)
                params_flattened.pop(i)

        params_magic_numbers = tuple(params_magic_numbers)
        params_flattened = tuple(params_flattened)

        return self._ApplyTypes_(518, 1, (VT_VARIANT, 0), params_magic_numbers, u"TiltView", None, *params_flattened)

    def view_c_plane(self, view=None, plane=None):
        """        
        Returns or sets the specified view's construction plane.
    
        Parameters
        ==========

        view, String, Optional        
        The title or identifier of the view.  If omitted, the current active view is used.
            
        plane, Array of ????, Optional        
        The new construction plane.  The elements of a plane array are as follows:
		Element
		Description
		0
		Required.  The construction plane's origin (3-D point).
		1
		Required.  The construction plane's X axis direction (3-D vector).
		2
		Required.  The construction plane's Y axis direction (3-D vector).
		3
            
        Returns
        =======

        array
        If a construction plane is not specified, the current construction plane if successful.

        array
        If a construction plane is specified, the previous construction plane if successful.

        null
        If not successful, or on error.

        """

        params = [view, plane]
        params_required = [False, False]
        params_magic_numbers = [(VT_BSTR, 1), (VT_VARIANT, 1)]
        params_flattened = [view, flatten(plane)]

        for i in range(len(params)):
            if (params[i] == None) and (not params_required[i]):
                params_magic_numbers.pop(i)
                params_flattened.pop(i)

        params_magic_numbers = tuple(params_magic_numbers)
        params_flattened = tuple(params_flattened)

        return self._ApplyTypes_(264, 1, (VT_VARIANT, 0), params_magic_numbers, u"ViewCPlane", None, *params_flattened)

    def view_camera(self, view=None, camera=None):
        """        
        Returns or sets the camera location of the specified view.
    
        Parameters
        ==========

        view, String, Optional        
        The title or identifier of the view.  If omitted, the current active view is used.
            
        camera, Array of ????, Optional        
        A 3-D point identifying the new camera location.  If arrCamera is not specified, the current camera location is returned.
            
        Returns
        =======

        array
        If arrCamera is not specified,  then a 3-D point containing the current camera location if successful.

        array
        If arrCamera is specified,  then a 3-D point containing the previous camera location if successful.

        null
        If not successful, or on error.

        """

        params = [view, camera]
        params_required = [False, False]
        params_magic_numbers = [(VT_BSTR, 1), (VT_VARIANT, 1)]
        params_flattened = [view, flatten(camera)]

        for i in range(len(params)):
            if (params[i] == None) and (not params_required[i]):
                params_magic_numbers.pop(i)
                params_flattened.pop(i)

        params_magic_numbers = tuple(params_magic_numbers)
        params_flattened = tuple(params_flattened)

        return self._ApplyTypes_(394, 1, (VT_VARIANT, 0), params_magic_numbers, u"ViewCamera", None, *params_flattened)

    def view_camera_lens(self, view=None, length=None):
        """        
        Returns or sets the 35mm camera lens length of the specified perspective projection view.
    
        Parameters
        ==========

        view, String, Optional        
        The title or identifier of the view.  If omitted, the current active view is used.
            
        length, Double, Optional        
        The new 35mm camera lens length.  If omitted, the previous 35mm camera lens length is returned.
            
        Returns
        =======

        number
        If a lens length is not specified, the current lens length if successful.

        number
        If a lens length is specified, the previous lens length is successful.

        null
        If not successful, or on error.

        """

        params = [view, length]
        params_required = [False, False]
        params_magic_numbers = [(VT_BSTR, 1), (VT_R8, 1)]
        params_flattened = [view, length]

        for i in range(len(params)):
            if (params[i] == None) and (not params_required[i]):
                params_magic_numbers.pop(i)
                params_flattened.pop(i)

        params_magic_numbers = tuple(params_magic_numbers)
        params_flattened = tuple(params_flattened)

        return self._ApplyTypes_(262, 1, (VT_VARIANT, 0), params_magic_numbers, u"ViewCameraLens", None, *params_flattened)

    def view_camera_plane(self, view=None):
        """        
        Returns the orientation of a view's camera.
    
        Parameters
        ==========

        view, String, Optional        
        The title or identifier of the view.  If omitted, the current active view is used.
            
        Returns
        =======

        array
        The view's camera plane if successful.  The elements of a plane array are as follows:

        null
        If not successful, or on error.

        """

        params = [view]
        params_required = [False]
        params_magic_numbers = [(VT_BSTR, 1),]
        params_flattened = [view]

        for i in range(len(params)):
            if (params[i] == None) and (not params_required[i]):
                params_magic_numbers.pop(i)
                params_flattened.pop(i)

        params_magic_numbers = tuple(params_magic_numbers)
        params_flattened = tuple(params_flattened)

        return self._ApplyTypes_(778, 1, (VT_VARIANT, 0), params_magic_numbers, u"ViewCameraPlane", None, *params_flattened)

    def view_camera_target(self, view=None, camera=None, target=None):
        """        
        Returns or sets the camera and target positions of the specified view.
    
        Parameters
        ==========

        view, String, Optional        
        The title or identifier of the view.  If omitted, the current active view is used.
            
        camera, Array of ????, Optional        
        A 3-D point identifying the new camera location.  If both arrCamera and arrTarget are not specified, the current camera and target locations are returned.
            
        target, Array of ????, Optional        
        A 3-D point identifying the new target location.  If both arrCamera and arrTarget are not specified, the current camera and target locations are returned.
            
        Returns
        =======

        array
        If both arrCamera and arrTarget are not specified,  then an array of 3-D point containing the current camera and target locations is returned.

        array
        If either arrCamera or arrTarget are specified,  then an array of 3-D point containing the previous camera and target locations is returned.

        null
        If not successful, or on error.

        """

        params = [view, camera, target]
        params_required = [False, False, False]
        params_magic_numbers = [(VT_BSTR, 1), (VT_VARIANT, 1), (VT_VARIANT, 1)]
        params_flattened = [view, flatten(camera), flatten(target)]

        for i in range(len(params)):
            if (params[i] == None) and (not params_required[i]):
                params_magic_numbers.pop(i)
                params_flattened.pop(i)

        params_magic_numbers = tuple(params_magic_numbers)
        params_flattened = tuple(params_flattened)

        return self._ApplyTypes_(263, 1, (VT_VARIANT, 0), params_magic_numbers, u"ViewCameraTarget", None, *params_flattened)

    def view_camera_up(self, view=None, up_vector=None):
        """        
        Returns or sets the camera up direction of specified view.
    
        Parameters
        ==========

        view, String, Optional        
        The title or identifier of the view.  If omitted, the current active view is used.
            
        up_vector, Array of ????, Optional        
        A 3-D vector identifying the new camera location.
            
        Returns
        =======

        array
        If arrUpVector is not specified,  then a 3-D vector identifying the current camera up direction if successful.

        array
        If arrUpVector is specified,  then a 3-D vector identifying the previous camera up direction if successful.

        null
        If not successful, or on error.

        """

        params = [view, up_vector]
        params_required = [False, False]
        params_magic_numbers = [(VT_BSTR, 1), (VT_VARIANT, 1)]
        params_flattened = [view, flatten(up_vector)]

        for i in range(len(params)):
            if (params[i] == None) and (not params_required[i]):
                params_magic_numbers.pop(i)
                params_flattened.pop(i)

        params_magic_numbers = tuple(params_magic_numbers)
        params_flattened = tuple(params_flattened)

        return self._ApplyTypes_(517, 1, (VT_VARIANT, 0), params_magic_numbers, u"ViewCameraUp", None, *params_flattened)

    def view_display_mode(self, view=None, mode=None):
        """        
        Returns or sets a view's display mode.  A view's display mode can be either wireframe, shaded, or render preview.
    
        Parameters
        ==========

        view, String, Optional        
        The title or identifier of the view.  If omitted, the current active view is used.
            
        mode, Integer, Optional        
        The display mode.  The display modes are as follows:
		Value
		Description
		0
		Wireframe.
		1
		Shaded.
		2
            
        Returns
        =======

        number
        If intMode is not specified, the current display mode for the specified view if successful.

        number
        If intMode is specified, the previous display mode for the specified view if successful.

        null
        If not successful, or on error.

        """

        params = [view, mode]
        params_required = [False, False]
        params_magic_numbers = [(VT_BSTR, 1), (VT_I2, 1)]
        params_flattened = [view, mode]

        for i in range(len(params)):
            if (params[i] == None) and (not params_required[i]):
                params_magic_numbers.pop(i)
                params_flattened.pop(i)

        params_magic_numbers = tuple(params_magic_numbers)
        params_flattened = tuple(params_flattened)

        return self._ApplyTypes_(290, 1, (VT_VARIANT, 0), params_magic_numbers, u"ViewDisplayMode", None, *params_flattened)

    def view_display_mode_ex(self, view=None, mode=None, return_names=None):
        """        
        Returns or sets a view's display mode.  Unlike the ViewDisplayMode method, which only allows you to set a view to wireframe, shaded, or render preview, this method allows you to set a view to any display mode including those listed in the Advanced Display Modes section of Rhino's Options dialog box.
    
        Parameters
        ==========

        view, String, Optional        
        The title or identifier of the view.  If omitted, the current active view is used.
            
        mode, String, Optional        
        The name or identifier of the display mode obtained from the ViewDisplayModes method.
            
        return_names, Boolean, Optional        
        If True (default), then the name the display mode is returned. If False, then the identifier of the display mode is returned.
            
        Returns
        =======

        number
        If strMode is not specified, the current display mode for the specified view if successful.

        number
        If strMode is specified, the previous display mode for the specified view if successful.

        null
        If not successful, or on error.

        """

        params = [view, mode, return_names]
        params_required = [False, False, False]
        params_magic_numbers = [(VT_BSTR, 1), (VT_BSTR, 1), (VT_BOOL, 1)]
        params_flattened = [view, mode, return_names]

        for i in range(len(params)):
            if (params[i] == None) and (not params_required[i]):
                params_magic_numbers.pop(i)
                params_flattened.pop(i)

        params_magic_numbers = tuple(params_magic_numbers)
        params_flattened = tuple(params_flattened)

        return self._ApplyTypes_(910, 1, (VT_VARIANT, 0), params_magic_numbers, u"ViewDisplayModeEx", None, *params_flattened)

    def view_display_mode_name(self, mode):
        """        
        Returns the name of a display mode given a display mode's identifier.
    
        Parameters
        ==========

        mode, String, Required        
        The identifier of the display mode obtained from the ViewDisplayModes method.
            
        Returns
        =======

        string
        The name of the display mode if successful.

        null
        If not successful, or on error.

        """

        params = [mode]
        params_required = [True]
        params_magic_numbers = [(VT_BSTR, 1),]
        params_flattened = [mode]

        for i in range(len(params)):
            if (params[i] == None) and (not params_required[i]):
                params_magic_numbers.pop(i)
                params_flattened.pop(i)

        params_magic_numbers = tuple(params_magic_numbers)
        params_flattened = tuple(params_flattened)

        return self._ApplyTypes_(909, 1, (VT_VARIANT, 0), params_magic_numbers, u"ViewDisplayModeName", None, *params_flattened)

    def view_display_modes(self, return_name=None):
        """        
        Returns a list of view display modes, including those listed in the Advanced Display Modes section of Rhino's Options dialog box.
    
        Parameters
        ==========

        return_name, Boolean, Optional        
        If True (default), then the names of the display modes are returned. If False, then the identifiers of the display modes are returned.
            
        Returns
        =======

        array
        A array of strings identifying the display mode names or identifiers if successful.

        null
        If not successful, or on error.

        """

        params = [return_name]
        params_required = [False]
        params_magic_numbers = [(VT_BOOL, 1),]
        params_flattened = [return_name]

        for i in range(len(params)):
            if (params[i] == None) and (not params_required[i]):
                params_magic_numbers.pop(i)
                params_flattened.pop(i)

        params_magic_numbers = tuple(params_magic_numbers)
        params_flattened = tuple(params_flattened)

        return self._ApplyTypes_(908, 1, (VT_VARIANT, 0), params_magic_numbers, u"ViewDisplayModes", None, *params_flattened)

    def view_names(self, return_names=None, type=None):
        """        
        Returns the names, or titles, or identifiers of all views in the document.
    
        Parameters
        ==========

        return_names, Boolean, Optional        
        If True (default), then the names, or titles, of the views are returned. If False, then the identifiers of the views are returned.
            
        type, Integer, Optional        
        The type of view to return, where:
		Value
		Description
		0
		Standard model views.
		1
		Page layout views.
		2
            
        Returns
        =======

        array
        A array of strings identifying the view names, or titles, or identifiers if successful.

        null
        If not successful, or on error.

        """

        params = [return_names, type]
        params_required = [False, False]
        params_magic_numbers = [(VT_BOOL, 1), (VT_I2, 1)]
        params_flattened = [return_names, type]

        for i in range(len(params)):
            if (params[i] == None) and (not params_required[i]):
                params_magic_numbers.pop(i)
                params_flattened.pop(i)

        params_magic_numbers = tuple(params_magic_numbers)
        params_flattened = tuple(params_flattened)

        return self._ApplyTypes_(265, 1, (VT_VARIANT, 0), params_magic_numbers, u"ViewNames", None, *params_flattened)

    def view_near_corners(self, view=None):
        """        
        Returns the 3-D corners points of a view's near clipping plane rectangle. This function can be useful in determining the "real world" size of a parallel-projected view.
    
        Parameters
        ==========

        view, String, Optional        
        The title or identifier of the view.  If omitted, the current active view is used.
            
        Returns
        =======

        array
        An array of four 3-D points that define the corners of the rectangle if successful.  Points are returned in counter-clockwise order.

        null
        If not successful, or on error.

        """

        params = [view]
        params_required = [False]
        params_magic_numbers = [(VT_BSTR, 1),]
        params_flattened = [view]

        for i in range(len(params)):
            if (params[i] == None) and (not params_required[i]):
                params_magic_numbers.pop(i)
                params_flattened.pop(i)

        params_magic_numbers = tuple(params_magic_numbers)
        params_flattened = tuple(params_flattened)

        return self._ApplyTypes_(823, 1, (VT_VARIANT, 0), params_magic_numbers, u"ViewNearCorners", None, *params_flattened)

    def view_projection(self, view=None, mode=None):
        """        
        Returns or sets a view's projection mode.  A view's projection mode can be either parallel or perspective.
    
        Parameters
        ==========

        view, String, Optional        
        The title or identifier of the view.  If omitted, the current active view is used.
            
        mode, Integer, Optional        
        The projection mode.  The projection modes are as follows:
		Value
		Description
		1
		Parallel
		2
            
        Returns
        =======

        number
        If intMode is not specified, the current projection mode for the specified view if successful.

        number
        If intMode is specified, the previous projection mode for the specified view if successful.

        null
        If not successful, or on error.

        """

        params = [view, mode]
        params_required = [False, False]
        params_magic_numbers = [(VT_BSTR, 1), (VT_I2, 1)]
        params_flattened = [view, mode]

        for i in range(len(params)):
            if (params[i] == None) and (not params_required[i]):
                params_magic_numbers.pop(i)
                params_flattened.pop(i)

        params_magic_numbers = tuple(params_magic_numbers)
        params_flattened = tuple(params_flattened)

        return self._ApplyTypes_(266, 1, (VT_VARIANT, 0), params_magic_numbers, u"ViewProjection", None, *params_flattened)

    def view_radius(self, view=None, radius=None):
        """        
        Returns or sets the radius of the viewing frustum of a parallel-projected view. This function is useful when you need an absolute zoom factor for a parallel-projected view.
    
        Parameters
        ==========

        view, String, Optional        
        The title or identifier of the view.  If omitted, the current active view is used.
            
        radius, Double, Optional        
        The view radius.
            
        Returns
        =======

        number
        If dblRadius is not specified, the current view radius for the specified view if successful.

        number
        If dblRadius is specified, the previous view radius for the specified view if successful.

        null
        If not successful, or on error.

        """

        params = [view, radius]
        params_required = [False, False]
        params_magic_numbers = [(VT_BSTR, 1), (VT_R8, 1)]
        params_flattened = [view, radius]

        for i in range(len(params)):
            if (params[i] == None) and (not params_required[i]):
                params_magic_numbers.pop(i)
                params_flattened.pop(i)

        params_magic_numbers = tuple(params_magic_numbers)
        params_flattened = tuple(params_flattened)

        return self._ApplyTypes_(824, 1, (VT_VARIANT, 0), params_magic_numbers, u"ViewRadius", None, *params_flattened)

    def view_size(self, view=None):
        """        
        Returns the width and height in pixels of the specified view.
    
        Parameters
        ==========

        view, String, Optional        
        The title or identifier of the view.  If omitted, the current active view is used.
            
        Returns
        =======

        array
        A zero-based, one-dimensional array containing two numbers identifying the width and height if successful

        null
        If not successful, or on error.

        """

        params = [view]
        params_required = [False]
        params_magic_numbers = [(VT_BSTR, 1),]
        params_flattened = [view]

        for i in range(len(params)):
            if (params[i] == None) and (not params_required[i]):
                params_magic_numbers.pop(i)
                params_flattened.pop(i)

        params_magic_numbers = tuple(params_magic_numbers)
        params_flattened = tuple(params_flattened)

        return self._ApplyTypes_(267, 1, (VT_VARIANT, 0), params_magic_numbers, u"ViewSize", None, *params_flattened)

    def view_target(self, view=None, target=None):
        """        
        Returns or sets the target location of the specified view.
    
        Parameters
        ==========

        view, String, Optional        
        The title or identifier of the view.  If omitted, the current active view is used.
            
        target, Array of ????, Optional        
        A 3-D point identifying the new target location.  If arrTarget is not specified, the current target location is returned.
            
        Returns
        =======

        array
        If arrTarget is not specified,  then a 3-D point containing the current target location if successful.

        array
        If arrTarget is specified,  then a 3-D point containing the previous target location if successful.

        null
        If not successful, or on error.

        """

        params = [view, target]
        params_required = [False, False]
        params_magic_numbers = [(VT_BSTR, 1), (VT_VARIANT, 1)]
        params_flattened = [view, flatten(target)]

        for i in range(len(params)):
            if (params[i] == None) and (not params_required[i]):
                params_magic_numbers.pop(i)
                params_flattened.pop(i)

        params_magic_numbers = tuple(params_magic_numbers)
        params_flattened = tuple(params_flattened)

        return self._ApplyTypes_(395, 1, (VT_VARIANT, 0), params_magic_numbers, u"ViewTarget", None, *params_flattened)

    def view_title(self, mode):
        """        
        Returns the name, or title, of a view given a view's identifier.
    
        Parameters
        ==========

        mode, String, Required        
        The identifier of the display mode obtained from the ViewNames method.
            
        Returns
        =======

        string
        The name, or title, of the view if successful.

        null
        If not successful, or on error.

        """

        params = [mode]
        params_required = [True]
        params_magic_numbers = [(VT_BSTR, 1),]
        params_flattened = [mode]

        for i in range(len(params)):
            if (params[i] == None) and (not params_required[i]):
                params_magic_numbers.pop(i)
                params_flattened.pop(i)

        params_magic_numbers = tuple(params_magic_numbers)
        params_flattened = tuple(params_flattened)

        return self._ApplyTypes_(907, 1, (VT_VARIANT, 0), params_magic_numbers, u"ViewTitle", None, *params_flattened)

    def wallpaper(self, view=None, file_name=None):
        """        
        Returns or sets the wallpaper bitmap of the specified view. To remove a wallpaper bitmap, pass an empty string, or "", as the filename to display.
    
        Parameters
        ==========

        view, String, Optional        
        The title or identifier of the view.  If omitted, the current active view is used.
            
        file_name, String, Optional        
        The name of the bitmap file to set as the wallpaper.  The supported bitmap file formats are as follows:
		.bmp
		Windows Bitmap
		.tga
		Truevision Targa
		.jpg, .jpeg
		JPEG Compliant
		.pcx
		Zsoft Paintbrush
		.png
		Portable Network Graphics
		.tif, .tiff
            
        Returns
        =======

        string
        If strFileName is not specified,  then the current wallpaper bitmap filename if successful.

        string
        If strFileName is specified,  then the previous wallpaper bitmap filename if successful.

        null
        If not successful, or on error.

        """

        params = [view, file_name]
        params_required = [False, False]
        params_magic_numbers = [(VT_BSTR, 1), (VT_BSTR, 1)]
        params_flattened = [view, file_name]

        for i in range(len(params)):
            if (params[i] == None) and (not params_required[i]):
                params_magic_numbers.pop(i)
                params_flattened.pop(i)

        params_magic_numbers = tuple(params_magic_numbers)
        params_flattened = tuple(params_flattened)

        return self._ApplyTypes_(532, 1, (VT_VARIANT, 0), params_magic_numbers, u"Wallpaper", None, *params_flattened)

    def wallpaper_gray_scale(self, view=None, gray_scale=None):
        """        
        Returns or sets the grayscale display option of the wallpaper bitmap of the specified view.
    
        Parameters
        ==========

        view, String, Optional        
        The title or identifier of the view.  If omitted, the current active view is used.
            
        gray_scale, Boolean, Optional        
        Display the wallpaper bitmap in grayscale (True) or color (False).
            
        Returns
        =======

        boolean
        If blnGrayScale is not specified,  then the current grayscale display option if successful.

        boolean
        If blnGrayScale is specified,  then the previous grayscale display option if successful.

        null
        If not successful, or on error.

        """

        params = [view, gray_scale]
        params_required = [False, False]
        params_magic_numbers = [(VT_BSTR, 1), (VT_BOOL, 1)]
        params_flattened = [view, gray_scale]

        for i in range(len(params)):
            if (params[i] == None) and (not params_required[i]):
                params_magic_numbers.pop(i)
                params_flattened.pop(i)

        params_magic_numbers = tuple(params_magic_numbers)
        params_flattened = tuple(params_flattened)

        return self._ApplyTypes_(534, 1, (VT_VARIANT, 0), params_magic_numbers, u"WallpaperGrayScale", None, *params_flattened)

    def wallpaper_hidden(self, view=None, hidden=None):
        """        
        Returns or sets the visibility of the wallpaper bitmap of the specified view.
    
        Parameters
        ==========

        view, String, Optional        
        The title or identifier of the view.  If omitted, the current active view is used.
            
        hidden, Boolean, Optional        
        Hide the wallpaper bitmap (True) or show the wallpaper bitmap (False).
            
        Returns
        =======

        boolean
        If blnHidden is not specified,  then the current wallpaper visibility if successful.

        boolean
        If blnHidden is specified,  then the previous wallpaper visibility if successful.

        null
        If not successful, or on error.

        """

        params = [view, hidden]
        params_required = [False, False]
        params_magic_numbers = [(VT_BSTR, 1), (VT_BOOL, 1)]
        params_flattened = [view, hidden]

        for i in range(len(params)):
            if (params[i] == None) and (not params_required[i]):
                params_magic_numbers.pop(i)
                params_flattened.pop(i)

        params_magic_numbers = tuple(params_magic_numbers)
        params_flattened = tuple(params_flattened)

        return self._ApplyTypes_(533, 1, (VT_VARIANT, 0), params_magic_numbers, u"WallpaperHidden", None, *params_flattened)

    def zoom_bounding_box(self, corners, view=None, all=None):
        """        
        Zooms to the extents of a specified bounding box in the specified view, or in the active view.
    
        Parameters
        ==========

        corners, Array of ????, Required        
        An array of eight 3-D points that define the corners of the box.  Points need to be  in counter-clockwise order starting with the bottom rectangle of the box.  Use BoundingBox to obtain the bounding box of objects.
            
        view, String, Optional        
        The title or identifier of the view.  If omitted, the current active view is used.
            
        all, Boolean, Optional        
        Zoom extents in all views.  If omitted, only the specified view is zoomed (False).
            
        No returns


        """

        params = [corners, view, all]
        params_required = [True, False, False]
        params_magic_numbers = [(VT_VARIANT, 1), (VT_BSTR, 1), (VT_BOOL, 1)]
        params_flattened = [flatten(corners), view, all]

        for i in range(len(params)):
            if (params[i] == None) and (not params_required[i]):
                params_magic_numbers.pop(i)
                params_flattened.pop(i)

        params_magic_numbers = tuple(params_magic_numbers)
        params_flattened = tuple(params_flattened)

        return self._ApplyTypes_(479, 1, (VT_VARIANT, 0), params_magic_numbers, u"ZoomBoundingBox", None, *params_flattened)

    def zoom_extents(self, view=None, all=None):
        """        
        Zooms to the extents of visible objects in the specified view, or in the active view.
    
        Parameters
        ==========

        view, String, Optional        
        The title or identifier of the view.  If omitted, the current active view is used.
            
        all, Boolean, Optional        
        Zoom extents in all views.  If omitted, only the specified view is zoomed (False).
            
        No returns


        """

        params = [view, all]
        params_required = [False, False]
        params_magic_numbers = [(VT_BSTR, 1), (VT_BOOL, 1)]
        params_flattened = [view, all]

        for i in range(len(params)):
            if (params[i] == None) and (not params_required[i]):
                params_magic_numbers.pop(i)
                params_flattened.pop(i)

        params_magic_numbers = tuple(params_magic_numbers)
        params_flattened = tuple(params_flattened)

        return self._ApplyTypes_(375, 1, (VT_VARIANT, 0), params_magic_numbers, u"ZoomExtents", None, *params_flattened)

    def zoom_selected(self, view=None, all=None):
        """        
        Zooms to the extents of selected objects in the specified view, or in the active view.
    
        Parameters
        ==========

        view, String, Optional        
        The title or identifier of the view.  If omitted, the current active view is used.
            
        all, Boolean, Optional        
        Zoom selected in all views.  If omitted, only the specified view is zoomed (False).
            
        No returns


        """

        params = [view, all]
        params_required = [False, False]
        params_magic_numbers = [(VT_BSTR, 1), (VT_BOOL, 1)]
        params_flattened = [view, all]

        for i in range(len(params)):
            if (params[i] == None) and (not params_required[i]):
                params_magic_numbers.pop(i)
                params_flattened.pop(i)

        params_magic_numbers = tuple(params_magic_numbers)
        params_flattened = tuple(params_flattened)

        return self._ApplyTypes_(376, 1, (VT_VARIANT, 0), params_magic_numbers, u"ZoomSelected", None, *params_flattened)

