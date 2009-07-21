# Auto-generated wrapper for Rhino4 RhinoScript functions

import exceptions
from py2rhino._util import *
from py2rhino._rhinoscript import IRhinoScript

class Document(IRhinoScript):



    def create_preview_image(self, file, view=None, size=None, flags=None, wireframe=None):
        """        
        Creates a bitmap preview image of the current model.
    
        Parameters
        ==========

        file, String, Required        
        The name of the bitmap file to create.  The extension of the filename controls the format of the bitmap file created.
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
            
        view, String, Optional        
        The title of the view.  If omitted, the current active view is used.
            
        size, Array of ????, Optional        
        An array of two integers that specify the width and height of the bitmap in pixels.
            
        flags, Integer, Optional        
        The bitmap creation flags. This parameter can be a combination of the following:
		Value
		Description
		1
		Honor object highlighting.  The default is to ignore highlighting (False).
		2
		Draw construction plane.  The default is not to draw the construction plane (False).
		4
            
        wireframe, Boolean, Optional        
        If specified and True, then a wireframe preview image, instead of a rendered image, will be created. Note, if this option is specified and True, then the ghosted shading flag is ignored.  The default value is False.
            
        Returns
        =======

        boolean
        True or False indicating success or failure.

        """

        params = [file, view, size, flags, wireframe]
        params_required = [True, False, False, False, False]
        params_magic_numbers = [(VT_BSTR, 1), (VT_BSTR, 1), (VT_VARIANT, 1), (VT_I2, 1), (VT_BOOL, 1)]
        params_flattened = [file, view, flatten(size), flags, wireframe]

        for i in range(len(params)):
            if (params[i] == None) and (not params_required[i]):
                params_magic_numbers.pop(i)
                params_flattened.pop(i)

        params_magic_numbers = tuple(params_magic_numbers)
        params_flattened = tuple(params_flattened)

        return self._ApplyTypes_(388, 1, (VT_VARIANT, 0), params_magic_numbers, u"CreatePreviewImage", None, *params_flattened)

    def document_modified(self, modified=None):
        """        
        Returns or sets the document's modified flag. The modified flag indicates whether or not any changes to the current document have been made.
		Note, setting the document modified flag to false will prevent the "Do you want to save this file..." from displaying when you close Rhino.
    
        Parameters
        ==========

        modified, Boolean, Optional        
        The modified state, either True or False.
            
        Returns
        =======

        boolean
        If no modified state is specified, the current modified state if successful.

        boolean
        If a modified state is specified, the previous modified state if successful.

        """

        params = [modified]
        params_required = [False]
        params_magic_numbers = [(VT_BOOL, 1),]
        params_flattened = [modified]

        for i in range(len(params)):
            if (params[i] == None) and (not params_required[i]):
                params_magic_numbers.pop(i)
                params_flattened.pop(i)

        params_magic_numbers = tuple(params_magic_numbers)
        params_flattened = tuple(params_flattened)

        return self._ApplyTypes_(323, 1, (VT_VARIANT, 0), params_magic_numbers, u"DocumentModified", None, *params_flattened)

    def document_name():
        """        
        Returns the name of the currently loaded Rhino document (3DM file).
    
        No parameters

        Returns
        =======

        string
        The current document name if successful.

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

        return self._ApplyTypes_(113, 1, (VT_VARIANT, 0), params_magic_numbers, u"DocumentName", None, *params_flattened)

    def document_path():
        """        
        Returns the path of the currently loaded Rhino document (3DM file).
    
        No parameters

        Returns
        =======

        string
        The current document path if successful.

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

        return self._ApplyTypes_(301, 1, (VT_VARIANT, 0), params_magic_numbers, u"DocumentPath", None, *params_flattened)

    def document_u_r_l(self, u_r_l=None):
        """        
        Returns or sets the uniform resource locator (URL) of the currently loaded Rhino document (3DM file).
    
        Parameters
        ==========

        u_r_l, String, Optional        
        The URL.
            
        Returns
        =======

        string
        If no URL is specified, the current URL if successful.

        string
        If a URL is specified, the previous URL if successful.

        null
        If not successful, or on error.

        """

        params = [u_r_l]
        params_required = [False]
        params_magic_numbers = [(VT_BSTR, 1),]
        params_flattened = [u_r_l]

        for i in range(len(params)):
            if (params[i] == None) and (not params_required[i]):
                params_magic_numbers.pop(i)
                params_flattened.pop(i)

        params_magic_numbers = tuple(params_magic_numbers)
        params_flattened = tuple(params_flattened)

        return self._ApplyTypes_(275, 1, (VT_VARIANT, 0), params_magic_numbers, u"DocumentURL", None, *params_flattened)

    def enable_redraw(self, select=None):
        """        
        Enables or disables screen redrawing.
    
        Parameters
        ==========

        select, Boolean, Optional        
        The screen redrawing state.  If omitted, screen redrawing is enabled (True).
            
        Returns
        =======

        boolean
        The previous screen redrawing state.

        """

        params = [select]
        params_required = [False]
        params_magic_numbers = [(VT_BOOL, 1),]
        params_flattened = [select]

        for i in range(len(params)):
            if (params[i] == None) and (not params_required[i]):
                params_magic_numbers.pop(i)
                params_flattened.pop(i)

        params_magic_numbers = tuple(params_magic_numbers)
        params_flattened = tuple(params_flattened)

        return self._ApplyTypes_(317, 1, (VT_VARIANT, 0), params_magic_numbers, u"EnableRedraw", None, *params_flattened)

    def extract_preview_image(self, file_name, model_name=None):
        """        
        Extracts the bitmap preview image from the specified model (.3dm).
    
        Parameters
        ==========

        file_name, String, Required        
        The name of the bitmap file to create.  The extension of the filename controls the format of the bitmap file created.
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
            
        model_name, String, Optional        
        The model (.3dm) from which to extract the preview image.  If omitted, the currently loaded model is used.
            
        Returns
        =======

        boolean
        True or False indicating success or failure.

        """

        params = [file_name, model_name]
        params_required = [True, False]
        params_magic_numbers = [(VT_BSTR, 1), (VT_BSTR, 1)]
        params_flattened = [file_name, model_name]

        for i in range(len(params)):
            if (params[i] == None) and (not params_required[i]):
                params_magic_numbers.pop(i)
                params_flattened.pop(i)

        params_magic_numbers = tuple(params_magic_numbers)
        params_flattened = tuple(params_flattened)

        return self._ApplyTypes_(389, 1, (VT_VARIANT, 0), params_magic_numbers, u"ExtractPreviewImage", None, *params_flattened)

    def is_document_modified():
        """        
        Verifies that the current document has been modified in some way.
    
        No parameters

        Returns
        =======

        boolean
        True or False indicating either modified or not modified.

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

        return self._ApplyTypes_(273, 1, (VT_VARIANT, 0), params_magic_numbers, u"IsDocumentModified", None, *params_flattened)

    def notes(self, notes=None):
        """        
        Returns or sets the document's notes.  Notes are generally created by using Rhino's Notes command.
    
        Parameters
        ==========

        notes, String, Optional        
        The notes.
            
        Returns
        =======

        string
        If strNotes is not specified, the current notes if successful.

        string
        If strNotes is specified, the previous notes if successful.

        null
        If not successful, or on error.

        """

        params = [notes]
        params_required = [False]
        params_magic_numbers = [(VT_BSTR, 1),]
        params_flattened = [notes]

        for i in range(len(params)):
            if (params[i] == None) and (not params_required[i]):
                params_magic_numbers.pop(i)
                params_flattened.pop(i)

        params_magic_numbers = tuple(params_magic_numbers)
        params_flattened = tuple(params_flattened)

        return self._ApplyTypes_(274, 1, (VT_VARIANT, 0), params_magic_numbers, u"Notes", None, *params_flattened)

    def read_file_version():
        """        
        Returns the file version of the current document.  Use this function to determine which version of Rhino last saved the document. Note, this function will not return values from referenced or merged files.
    
        No parameters

        Returns
        =======

        number
        The file version of the document if successful.  Note, values less than zero indicate that the current document has not been read (from disk).

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

        return self._ApplyTypes_(737, 1, (VT_VARIANT, 0), params_magic_numbers, u"ReadFileVersion", None, *params_flattened)

    def redraw():
        """        
        Redraws all views.
    
        No parameters

        No returns


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

        return self._ApplyTypes_(114, 1, (VT_VARIANT, 0), params_magic_numbers, u"Redraw", None, *params_flattened)

    def render_antialias(self, style=None):
        """        
        Returns or sets render antialiasing style.  Antialiasing is a process where more than one ray is shot per pixel in an attempt to better resolve the value of the
		pixel.  Increasing the antialiasing level can add considerable time to the overall rendering.  See Rhino's DocumentProperties command (Rhino Render window) for details.
    
        Parameters
        ==========

        style, Integer, Optional        
        The render antialiasing style.
		Value
		Description
		0
		None
		1
		Normal and slower
		2
            
        Returns
        =======

        number
        If intStyle is not specified, the current render antialiasing style if successful.

        number
        If intStyle  is not specified, the previous render antialiasing style if successful.

        number
        Is not successful, or on error.

        """

        params = [style]
        params_required = [False]
        params_magic_numbers = [(VT_I2, 1),]
        params_flattened = [style]

        for i in range(len(params)):
            if (params[i] == None) and (not params_required[i]):
                params_magic_numbers.pop(i)
                params_flattened.pop(i)

        params_magic_numbers = tuple(params_magic_numbers)
        params_flattened = tuple(params_flattened)

        return self._ApplyTypes_(333, 1, (VT_VARIANT, 0), params_magic_numbers, u"RenderAntialias", None, *params_flattened)

    def render_color(self, item, color=None):
        """        
        Returns or sets the render ambient light or background color. Render colors are represented as RGB colors. An RGB color specifies the relative intensity of red, green, and blue to cause a specific color to be displayed. See Rhino's DocumentProperties command (Rhino Render window) for details.
    
        Parameters
        ==========

        item, Integer, Required        
        The item you wish to either query or change.
		0
		Ambient light color.
		1
            
        color, Integer, Optional        
        The new color value. If omitted, the curreng intItem color is returned.
            
        Returns
        =======

        number
        If lngColor is not specified, the current intItem color if successful.

        number
        If lngColor is specified, the previous intItem color if successful.

        null
        If not successful, or on error.

        """

        params = [item, color]
        params_required = [True, False]
        params_magic_numbers = [(VT_I2, 1), (VT_I4, 1)]
        params_flattened = [item, color]

        for i in range(len(params)):
            if (params[i] == None) and (not params_required[i]):
                params_magic_numbers.pop(i)
                params_flattened.pop(i)

        params_magic_numbers = tuple(params_magic_numbers)
        params_flattened = tuple(params_flattened)

        return self._ApplyTypes_(331, 1, (VT_VARIANT, 0), params_magic_numbers, u"RenderColor", None, *params_flattened)

    def render_mesh_density(self, density=None):
        """        
        Returns or sets the render mesh density property of the active document.
		For more information on render meshes, see the Document Properties: Mesh topic in the Rhino help file.
    
        Parameters
        ==========

        density, Double, Optional        
        The render mesh density, which is a number between 0.0 and 1.0.
            
        Returns
        =======

        number
        If dblDensity is not specified, the current render mesh density if successful.

        number
        If dblDensity is specified, the previous render mesh density if successful.

        null
        If not successful, or on error.

        """

        params = [density]
        params_required = [False]
        params_magic_numbers = [(VT_R8, 1),]
        params_flattened = [density]

        for i in range(len(params)):
            if (params[i] == None) and (not params_required[i]):
                params_magic_numbers.pop(i)
                params_flattened.pop(i)

        params_magic_numbers = tuple(params_magic_numbers)
        params_flattened = tuple(params_flattened)

        return self._ApplyTypes_(844, 1, (VT_VARIANT, 0), params_magic_numbers, u"RenderMeshDensity", None, *params_flattened)

    def render_mesh_max_angle(self, angle=None):
        """        
        Returns or sets the render mesh maximum angle property of the active document.
		For more information on render meshes, see the Document Properties: Mesh topic in the Rhino help file.
    
        Parameters
        ==========

        angle, Double, Optional        
        The render mesh maximum angle in degrees.
            
        Returns
        =======

        number
        If dblAngle is not specified, the current render maximum angle if successful.

        number
        If dblAngle is specified, the previous render mesh maximum angle if successful.

        null
        If not successful, or on error.

        """

        params = [angle]
        params_required = [False]
        params_magic_numbers = [(VT_R8, 1),]
        params_flattened = [angle]

        for i in range(len(params)):
            if (params[i] == None) and (not params_required[i]):
                params_magic_numbers.pop(i)
                params_flattened.pop(i)

        params_magic_numbers = tuple(params_magic_numbers)
        params_flattened = tuple(params_flattened)

        return self._ApplyTypes_(845, 1, (VT_VARIANT, 0), params_magic_numbers, u"RenderMeshMaxAngle", None, *params_flattened)

    def render_mesh_max_aspect_ratio(self, ratio=None):
        """        
        Returns or sets the render mesh maximum aspect ratio property of the active document.
		For more information on render meshes, see the Document Properties: Mesh topic in the Rhino help file.
    
        Parameters
        ==========

        ratio, Double, Optional        
        The render mesh maximum aspect ratio.  The suggested range, when not zero, is from 1 to 100.
            
        Returns
        =======

        number
        If dblRatio is not specified, the current render mesh maximum aspect ratio if successful.

        number
        If dblRatio is specified, the previous render mesh maximum aspect ratio if successful.

        null
        If not successful, or on error.

        """

        params = [ratio]
        params_required = [False]
        params_magic_numbers = [(VT_R8, 1),]
        params_flattened = [ratio]

        for i in range(len(params)):
            if (params[i] == None) and (not params_required[i]):
                params_magic_numbers.pop(i)
                params_flattened.pop(i)

        params_magic_numbers = tuple(params_magic_numbers)
        params_flattened = tuple(params_flattened)

        return self._ApplyTypes_(846, 1, (VT_VARIANT, 0), params_magic_numbers, u"RenderMeshMaxAspectRatio", None, *params_flattened)

    def render_mesh_max_dist_edge_to_srf(self, distance=None):
        """        
        Returns or sets the render mesh maximum distance, edge to surface parameter of the active document.
		For more information on render meshes, see the Document Properties: Mesh topic in the Rhino help file.
    
        Parameters
        ==========

        distance, Double, Optional        
        The render mesh maximum distance, edge to surface.
            
        Returns
        =======

        number
        If dblDistance is not specified, the current render mesh maximum distance, edge to surface if successful.

        number
        If dblDistance is specified, the previous render mesh maximum distance, edge to surface if successful.

        null
        If not successful, or on error.

        """

        params = [distance]
        params_required = [False]
        params_magic_numbers = [(VT_R8, 1),]
        params_flattened = [distance]

        for i in range(len(params)):
            if (params[i] == None) and (not params_required[i]):
                params_magic_numbers.pop(i)
                params_flattened.pop(i)

        params_magic_numbers = tuple(params_magic_numbers)
        params_flattened = tuple(params_flattened)

        return self._ApplyTypes_(849, 1, (VT_VARIANT, 0), params_magic_numbers, u"RenderMeshMaxDistEdgeToSrf", None, *params_flattened)

    def render_mesh_max_edge_length(self, length=None):
        """        
        Returns or sets the render mesh maximum edge length parameter of the active document.
		For more information on render meshes, see the Document Properties: Mesh topic in the Rhino help file.
    
        Parameters
        ==========

        length, Double, Optional        
        The render mesh maximum edge length.
            
        Returns
        =======

        number
        If dblLength is not specified, the current render mesh maximum edge length if successful.

        number
        If dblLength is specified, the previous render mesh maximum edge length if successful.

        null
        If not successful, or on error.

        """

        params = [length]
        params_required = [False]
        params_magic_numbers = [(VT_R8, 1),]
        params_flattened = [length]

        for i in range(len(params)):
            if (params[i] == None) and (not params_required[i]):
                params_magic_numbers.pop(i)
                params_flattened.pop(i)

        params_magic_numbers = tuple(params_magic_numbers)
        params_flattened = tuple(params_flattened)

        return self._ApplyTypes_(848, 1, (VT_VARIANT, 0), params_magic_numbers, u"RenderMeshMaxEdgeLength", None, *params_flattened)

    def render_mesh_min_edge_length(self, length=None):
        """        
        Returns or sets the render mesh minimum edge length parameter of the active document.
		For more information on render meshes, see the Document Properties: Mesh topic in the Rhino help file.
    
        Parameters
        ==========

        length, Double, Optional        
        The render mesh minimum edge length.
            
        Returns
        =======

        number
        If dblLength is not specified, the current render mesh minimum edge length if successful.

        number
        If dblLength is specified, the previous render mesh minimum edge length if successful.

        null
        If not successful, or on error.

        """

        params = [length]
        params_required = [False]
        params_magic_numbers = [(VT_R8, 1),]
        params_flattened = [length]

        for i in range(len(params)):
            if (params[i] == None) and (not params_required[i]):
                params_magic_numbers.pop(i)
                params_flattened.pop(i)

        params_magic_numbers = tuple(params_magic_numbers)
        params_flattened = tuple(params_flattened)

        return self._ApplyTypes_(847, 1, (VT_VARIANT, 0), params_magic_numbers, u"RenderMeshMinEdgeLength", None, *params_flattened)

    def render_mesh_min_initial_grid_quads(self, quads=None):
        """        
        Returns or sets the render mesh minimum initial grid quads parameter of the active document.
		For more information on render meshes, see the Document Properties: Mesh topic in the Rhino help file.
    
        Parameters
        ==========

        quads, Integer, Optional        
        The render mesh minimum initial grid quads.  The suggested range is from 0 to 10000.
            
        Returns
        =======

        number
        If intQuads is not specified, the current render mesh minimum initial grid quads if successful.

        number
        If intQuads is specified, the previous render mesh minimum initial grid quads if successful.

        null
        If not successful, or on error.

        """

        params = [quads]
        params_required = [False]
        params_magic_numbers = [(VT_I2, 1),]
        params_flattened = [quads]

        for i in range(len(params)):
            if (params[i] == None) and (not params_required[i]):
                params_magic_numbers.pop(i)
                params_flattened.pop(i)

        params_magic_numbers = tuple(params_magic_numbers)
        params_flattened = tuple(params_flattened)

        return self._ApplyTypes_(850, 1, (VT_VARIANT, 0), params_magic_numbers, u"RenderMeshMinInitialGridQuads", None, *params_flattened)

    def render_mesh_quality(self, quality=None):
        """        
        Returns or sets the render mesh quality of the active document.
		For more information on render meshes, see the Document Properties: Mesh topic in the Rhino help file.
    
        Parameters
        ==========

        quality, Integer, Optional        
        The render mesh quality, either:
		Value
		Description
		0
		Jagged and faster.  Objects may look jagged, but they should shade and render relatively quickly.
		1
		Smooth and slower.  Objects should look smooth, but they may take a very long time to shade and render.
		2
            
        Returns
        =======

        number
        If intQuality is not specified, the current render mesh quality if successful.

        number
        If intQuality is specified, the previous render mesh quality if successful.

        null
        If not successful, or on error.

        """

        params = [quality]
        params_required = [False]
        params_magic_numbers = [(VT_I2, 1),]
        params_flattened = [quality]

        for i in range(len(params)):
            if (params[i] == None) and (not params_required[i]):
                params_magic_numbers.pop(i)
                params_flattened.pop(i)

        params_magic_numbers = tuple(params_magic_numbers)
        params_flattened = tuple(params_flattened)

        return self._ApplyTypes_(843, 1, (VT_VARIANT, 0), params_magic_numbers, u"RenderMeshQuality", None, *params_flattened)

    def render_mesh_settings(self, settings=None):
        """        
        Returns or sets the render mesh settings of the active document.
		For more information on render meshes, see the Document Properties: Mesh topic in the Rhino help file.
    
        Parameters
        ==========

        settings, Integer, Optional        
        The render mesh settings, which is a bit-coded number that allows or disallows certain features.  The bits can be added together in any combination to form a value between 0 and 7.  The bit values are as follows:
		Value
		Description
		0
		No settings enabled.
		1
		Refine mesh enabled.
		2
		Jagged seams enabled.
		4
            
        Returns
        =======

        number
        If intSettings is not specified, the current render mesh settings if successful.

        number
        If intSettings is specified, the previous render mesh settings if successful.

        null
        If not successful, or on error.

        """

        params = [settings]
        params_required = [False]
        params_magic_numbers = [(VT_I2, 1),]
        params_flattened = [settings]

        for i in range(len(params)):
            if (params[i] == None) and (not params_required[i]):
                params_magic_numbers.pop(i)
                params_flattened.pop(i)

        params_magic_numbers = tuple(params_magic_numbers)
        params_flattened = tuple(params_flattened)

        return self._ApplyTypes_(851, 1, (VT_VARIANT, 0), params_magic_numbers, u"RenderMeshSettings", None, *params_flattened)

    def render_resolution(self, resolution):
        """        
        Returns or sets the render resolution. Resolution is measured in pixels. See Rhino's DocumentProperties command (Rhino Render window) for details. Note, if the render resolution is set to "viewport", then the size of the active viewt is returned.
    
        Parameters
        ==========

        resolution, Array of ????, Required        
        An array containing two numbers identifying the resolution width and height in pixels.
            
        Returns
        =======

        array
        If arrResolution is not specified, an array containing two numbers identifying the current resolution width and height in pixels if successful.

        array
        If arrResolution is specified, an array containing two numbers identifying the previous resolution width and height in pixels if successful.

        null
        If not successful, or on error.

        """

        params = [resolution]
        params_required = [True]
        params_magic_numbers = [(VT_VARIANT, 1),]
        params_flattened = [flatten(resolution)]

        for i in range(len(params)):
            if (params[i] == None) and (not params_required[i]):
                params_magic_numbers.pop(i)
                params_flattened.pop(i)

        params_magic_numbers = tuple(params_magic_numbers)
        params_flattened = tuple(params_flattened)

        return self._ApplyTypes_(332, 1, (VT_VARIANT, 0), params_magic_numbers, u"RenderResolution", None, *params_flattened)

    def render_settings(self, settings=None):
        """        
        Returns or sets render settings.  See Rhino's DocumentProperties command (Rhino Render window) for details.
    
        Parameters
        ==========

        settings, Integer, Optional        
        The render setting or settings to modify.  Render settings can be any combination of the following flags:
		Value
		Description
		0
		None.
		1
		Create shadows.
		2
		Use lights on layers that are off.
		4
		Render curves and isocurves.
		8
            
        Returns
        =======

        number
        If intSettings is not specified, the current render settings if successful.

        number
        If intSettings is not specified, the previous render settings if successful.

        number
        Is not successful, or on error.

        """

        params = [settings]
        params_required = [False]
        params_magic_numbers = [(VT_I2, 1),]
        params_flattened = [settings]

        for i in range(len(params)):
            if (params[i] == None) and (not params_required[i]):
                params_magic_numbers.pop(i)
                params_flattened.pop(i)

        params_magic_numbers = tuple(params_magic_numbers)
        params_flattened = tuple(params_flattened)

        return self._ApplyTypes_(334, 1, (VT_VARIANT, 0), params_magic_numbers, u"RenderSettings", None, *params_flattened)

    def unit_absolute_tolerance(self, abs_tol=None):
        """        
        Returns or sets the document's absolute tolerance parameter.  Absolute tolerance is measured in drawing units. See Rhino's DocumentProperties command (Units window) for details.
    
        Parameters
        ==========

        abs_tol, Double, Optional        
        The absolute tolerance in drawing units.
            
        Returns
        =======

        number
        If dblAbsTol is not specified, the current absolute tolerance if successful.

        number
        If dblAbsTol is specified, the previous absolute tolerance if successful.

        null
        If not successful, or on error.

        """

        params = [abs_tol]
        params_required = [False]
        params_magic_numbers = [(VT_R8, 1),]
        params_flattened = [abs_tol]

        for i in range(len(params)):
            if (params[i] == None) and (not params_required[i]):
                params_magic_numbers.pop(i)
                params_flattened.pop(i)

        params_magic_numbers = tuple(params_magic_numbers)
        params_flattened = tuple(params_flattened)

        return self._ApplyTypes_(324, 1, (VT_VARIANT, 0), params_magic_numbers, u"UnitAbsoluteTolerance", None, *params_flattened)

    def unit_angle_tolerance(self, angle_tol=None):
        """        
        Returns or sets the document's angle tolerance parameter.  Angle tolerance is measured degrees.  See Rhino's DocumentProperties command (Units window) for details.
    
        Parameters
        ==========

        angle_tol, Double, Optional        
        The angle tolerance in degrees.
            
        Returns
        =======

        number
        If dblAngleTol is not specified, the current angle tolerance if successful.

        number
        If dblAngleTol is specified, the previous angle tolerance if successful.

        null
        If not successful, or on error.

        """

        params = [angle_tol]
        params_required = [False]
        params_magic_numbers = [(VT_R8, 1),]
        params_flattened = [angle_tol]

        for i in range(len(params)):
            if (params[i] == None) and (not params_required[i]):
                params_magic_numbers.pop(i)
                params_flattened.pop(i)

        params_magic_numbers = tuple(params_magic_numbers)
        params_flattened = tuple(params_flattened)

        return self._ApplyTypes_(325, 1, (VT_VARIANT, 0), params_magic_numbers, u"UnitAngleTolerance", None, *params_flattened)

    def unit_custom_unit_system(self, units, scale=None, name=None):
        """        
        Sets the document's units system to a user-defined system.  This overrides the units system set using the UnitSystem method.  See Rhino's DocumentProperties command (Units window) for details.
    
        Parameters
        ==========

        units, Double, Required        
        The number of units per meter.
            
        scale, Boolean, Optional        
        Scale existing geometry based on the new unit system.  If not specified, any existing geometry is not scaled (False).
            
        name, String, Optional        
        The name of the new unit system.  If not specified, the name "Custom" will be assigned.
            
        Returns
        =======

        number
        The previous units system if successful.  See UnitSystem for details.

        null
        If not successful, or on error.

        """

        params = [units, scale, name]
        params_required = [True, False, False]
        params_magic_numbers = [(VT_R8, 1), (VT_BOOL, 1), (VT_BSTR, 1)]
        params_flattened = [units, scale, name]

        for i in range(len(params)):
            if (params[i] == None) and (not params_required[i]):
                params_magic_numbers.pop(i)
                params_flattened.pop(i)

        params_magic_numbers = tuple(params_magic_numbers)
        params_flattened = tuple(params_flattened)

        return self._ApplyTypes_(326, 1, (VT_VARIANT, 0), params_magic_numbers, u"UnitCustomUnitSystem", None, *params_flattened)

    def unit_distance_display_mode(self, mode=None):
        """        
        Returns or sets the document's distance display mode parameter.  See Rhino's DocumentProperties command (Units window) for details.
    
        Parameters
        ==========

        mode, Integer, Optional        
        The distance display mode.  The available distance display modes are as follows:
		Value
		Description
		0
		Decimal
		1
		Fractional
		2
            
        Returns
        =======

        number
        If intMode is not specified, the current distance display mode if successful.

        number
        If intMode is specified, the previous distance display mode if successful.

        null
        If not successful, or on error.

        """

        params = [mode]
        params_required = [False]
        params_magic_numbers = [(VT_I2, 1),]
        params_flattened = [mode]

        for i in range(len(params)):
            if (params[i] == None) and (not params_required[i]):
                params_magic_numbers.pop(i)
                params_flattened.pop(i)

        params_magic_numbers = tuple(params_magic_numbers)
        params_flattened = tuple(params_flattened)

        return self._ApplyTypes_(327, 1, (VT_VARIANT, 0), params_magic_numbers, u"UnitDistanceDisplayMode", None, *params_flattened)

    def unit_distance_display_precision(self, precision=None):
        """        
        Returns or sets the document's distance display precision parameter.  See Rhino's DocumentProperties command (Units window) for details.
    
        Parameters
        ==========

        precision, Integer, Optional        
        The distance display precision.  If the current distance display mode is Decimal, then intPrecision is the number of decimal places.  If the current distance display mode is Fractional (including Feet and Inches), then the denominator = (1/2)^intPrecision.  Use UnitDistanceDisplayMode to get the current distance display mode.
            
        Returns
        =======

        number
        If intPrecision is not specified, the current distance display precision if successful.

        number
        If intPrecision is specified, the previous distance display precision if successful.

        null
        If not successful, or on error.

        """

        params = [precision]
        params_required = [False]
        params_magic_numbers = [(VT_I2, 1),]
        params_flattened = [precision]

        for i in range(len(params)):
            if (params[i] == None) and (not params_required[i]):
                params_magic_numbers.pop(i)
                params_flattened.pop(i)

        params_magic_numbers = tuple(params_magic_numbers)
        params_flattened = tuple(params_flattened)

        return self._ApplyTypes_(328, 1, (VT_VARIANT, 0), params_magic_numbers, u"UnitDistanceDisplayPrecision", None, *params_flattened)

    def unit_relative_tolerance(self, rel_tol=None):
        """        
        Returns or sets the document's relative tolerance parameter.  Relative tolerance is measured in percent. See Rhino's DocumentProperties command (Units window) for details.
    
        Parameters
        ==========

        rel_tol, Double, Optional        
        The relative tolerance in percent.
            
        Returns
        =======

        number
        If dblRelTol is not specified, the current relative tolerance if successful.

        number
        If dblRelTol is specified, the previous relative tolerance if successful.

        null
        If not successful, or on error.

        """

        params = [rel_tol]
        params_required = [False]
        params_magic_numbers = [(VT_R8, 1),]
        params_flattened = [rel_tol]

        for i in range(len(params)):
            if (params[i] == None) and (not params_required[i]):
                params_magic_numbers.pop(i)
                params_flattened.pop(i)

        params_magic_numbers = tuple(params_magic_numbers)
        params_flattened = tuple(params_flattened)

        return self._ApplyTypes_(329, 1, (VT_VARIANT, 0), params_magic_numbers, u"UnitRelativeTolerance", None, *params_flattened)

    def unit_scale(self, to_system, from_system=None):
        """        
        Returns the scale factor for changing between unit systems.
    
        Parameters
        ==========

        to_system, Integer, Required        
        The units system to convert to.  The possible units systems are as follows:
		Value
		Description
		0
		No unit system
		1
		Microns (1.0e-6 meters)
		2
		Millimeters (1.0e-3 meters)
		3
		Centimeters (1.0e-2 meters)
		4
		Meters
		5
		Kilometers (1.0e+3 meters)
		6
		Microinches (2.54e-8 meters, 1.0e-6 inches)
		7
		Mils (2.54e-5 meters, 0.001 inches)
		8
		Inches (0.0254 meters)
		9
		Feet (0.3408 meters, 12 inches)
		10
		Miles (1609.344 meters, 5280 feet)
		11
		* Reserved for Custom Unit System *
		12
		Angstroms (1.0e-10 meters)
		13
		Nanometers (1.0e-9 meters)
		14
		Decimeters (1.0e-1 meters)
		15
		Dekameters (1.0e+1 meters)
		16
		Hectometers (1.0e+2 meters)
		17
		Megameters (1.0e+6 meters)
		18
		Gigameters (1.0e+9 meters)
		19
		Yards (0.9144  meters, 36 inches)
		20
		Printer point (1/72 inches, computer points)
		21
		Printer pica (1/6 inches, (computer picas)
		22
		Nautical mile (1852 meters)
		23
		Astronomical (1.4959787e+11)
		24
		Lightyears (9.46073e+15 meters)
		25
            
        from_system, Integer, Optional        
        The units system to convert from (see above).  If omitted, the document's current unit system is used
            
        Returns
        =======

        number
        The scale factor for changing between unit systems if successful.

        null
        If not successful, or on error.

        """

        params = [to_system, from_system]
        params_required = [True, False]
        params_magic_numbers = [(VT_I2, 1), (VT_I2, 1)]
        params_flattened = [to_system, from_system]

        for i in range(len(params)):
            if (params[i] == None) and (not params_required[i]):
                params_magic_numbers.pop(i)
                params_flattened.pop(i)

        params_magic_numbers = tuple(params_magic_numbers)
        params_flattened = tuple(params_flattened)

        return self._ApplyTypes_(868, 1, (VT_VARIANT, 0), params_magic_numbers, u"UnitScale", None, *params_flattened)

    def unit_system(self, system=None, scale=None):
        """        
        Returns or sets the document's units system.  See Rhino's DocumentProperties command (Units window) for details.
    
        Parameters
        ==========

        system, Integer, Optional        
        The units system.  The available units systems are as follows:
		Value
		Description
		0
		No unit system
		1
		Microns (1.0e-6 meters)
		2
		Millimeters (1.0e-3 meters)
		3
		Centimeters (1.0e-2 meters)
		4
		Meters
		5
		Kilometers (1.0e+3 meters)
		6
		Microinches (2.54e-8 meters, 1.0e-6 inches)
		7
		Mils (2.54e-5 meters, 0.001 inches)
		8
		Inches (0.0254 meters)
		9
		Feet (0.3408 meters, 12 inches)
		10
		Miles (1609.344 meters, 5280 feet)
		11
		* Reserved for Custom Unit System *
		12
		Angstroms (1.0e-10 meters)
		13
		Nanometers (1.0e-9 meters)
		14
		Decimeters (1.0e-1 meters)
		15
		Dekameters (1.0e+1 meters)
		16
		Hectometers (1.0e+2 meters)
		17
		Megameters (1.0e+6 meters)
		18
		Gigameters (1.0e+9 meters)
		19
		Yards (0.9144  meters, 36 inches)
		20
		Printer point (1/72 inches, computer points)
		21
		Printer pica (1/6 inches, (computer picas)
		22
		Nautical mile (1852 meters)
		23
		Astronomical (1.4959787e+11)
		24
		Lightyears (9.46073e+15 meters)
		25
            
        scale, Boolean, Optional        
        Scale existing geometry based on the new unit system.  If not specified, any existing geometry is not scaled (False).
            
        Returns
        =======

        number
        The previous units system if successful.

        null
        If not successful, or on error.

        """

        params = [system, scale]
        params_required = [False, False]
        params_magic_numbers = [(VT_I2, 1), (VT_BOOL, 1)]
        params_flattened = [system, scale]

        for i in range(len(params)):
            if (params[i] == None) and (not params_required[i]):
                params_magic_numbers.pop(i)
                params_flattened.pop(i)

        params_magic_numbers = tuple(params_magic_numbers)
        params_flattened = tuple(params_flattened)

        return self._ApplyTypes_(330, 1, (VT_VARIANT, 0), params_magic_numbers, u"UnitSystem", None, *params_flattened)

    def unit_system_name(self, capitalize=None, singular=None, abbreviate=None):
        """        
        Returns the name of the current unit system.
    
        Parameters
        ==========

        capitalize, Boolean, Optional        
        Capitalize the first character of the units system name (e.g. return "Millimeter" instead of "millimeter"). The default is not to capitalize the first character (false).
            
        singular, Boolean, Optional        
        Return the singular form of the units system name (e.g. "millimeter" instead of "millimeters"). The default is to return the singular form of the name (true).
            
        abbreviate, Boolean, Optional        
        Abbreviate the name of the units system (e.g. return "mm" instead of "millimeter"). The default is not to abbreviate the name (false).
            
        Returns
        =======

        string
        The name of the current units system if successful.

        """

        params = [capitalize, singular, abbreviate]
        params_required = [False, False, False]
        params_magic_numbers = [(VT_BOOL, 1), (VT_BOOL, 1), (VT_BOOL, 1)]
        params_flattened = [capitalize, singular, abbreviate]

        for i in range(len(params)):
            if (params[i] == None) and (not params_required[i]):
                params_magic_numbers.pop(i)
                params_flattened.pop(i)

        params_magic_numbers = tuple(params_magic_numbers)
        params_flattened = tuple(params_flattened)

        return self._ApplyTypes_(492, 1, (VT_VARIANT, 0), params_magic_numbers, u"UnitSystemName", None, *params_flattened)

