# Auto-generated wrapper for Rhino4 RhinoScript functions

import exceptions
import _utils
from _rhinoscript import IRhinoScript

class Document(IRhinoScript):



    def create_preview_image(self, file, view, size, flags, wireframe):
        """

        Creates a bitmap preview image of the current model.

        Parameters

        File : Required, String, str, String
        View : Optional, String, str, String
        Size : Optional, Array, arrdbl, Array of ?
        Flags : Optional, Integer, int, Integer
        Wireframe : Optional, Boolean, bln, Boolean

        Returns

        Boolean : True or False indicating success or failure.

        """

        return self._ApplyTypes_(388, 1, (12, 0), ((8, 0), (8, 0), (8197, 0), (2, 0), (11, 0),), u'CreatePreviewImage', None, file, view, _utils.flatten(size), flags, wireframe)

    def document_modified(self, modified):
        """

        Note, setting the document modified flag to false will prevent the "Do you want to save this file..." from displaying when you close Rhino.

        Parameters

        Modified : Optional, Boolean, bln, Boolean

        Returns

        Boolean : If no modified state is specified, the current modified state if successful.
        Boolean : If a modified state is specified, the previous modified state if successful.

        """

        return self._ApplyTypes_(323, 1, (12, 0), ((11, 0),), u'DocumentModified', None, modified)

    def document_name(self):
        """

        Returns the name of the currently loaded Rhino document (3DM file).

        No parameters

        Returns

        String : The current document name if successful.
        Null : If not successful, or on error.

        """

        return self._ApplyTypes_(113, 1, (12, 0), (,), u'DocumentName', None, )

    def document_path(self):
        """

        Returns the path of the currently loaded Rhino document (3DM file).

        No parameters

        Returns

        String : The current document path if successful.
        Null : If not successful, or on error.

        """

        return self._ApplyTypes_(301, 1, (12, 0), (,), u'DocumentPath', None, )

    def document_u_r_l(self, u_r_l):
        """

        Returns or sets the uniform resource locator (URL) of the currently loaded Rhino document (3DM file).

        Parameters

        URL : Optional, String, str, String

        Returns

        String : If no URL is specified, the current URL if successful.
        String : If a URL is specified, the previous URL if successful.
        Null : If not successful, or on error.

        """

        return self._ApplyTypes_(275, 1, (12, 0), ((8, 0),), u'DocumentURL', None, u_r_l)

    def enable_redraw(self, select):
        """

        Enables or disables screen redrawing.

        Parameters

        Select : Optional, Boolean, bln, Boolean

        Returns

        Boolean : The previous screen redrawing state.

        """

        return self._ApplyTypes_(317, 1, (12, 0), ((11, 0),), u'EnableRedraw', None, select)

    def extract_preview_image(self, file_name, model_name):
        """

        Extracts the bitmap preview image from the specified model (.3dm).

        Parameters

        FileName : Required, String, str, String
        ModelName : Optional, String, str, String

        Returns

        Boolean : True or False indicating success or failure.

        """

        return self._ApplyTypes_(389, 1, (12, 0), ((8, 0), (8, 0),), u'ExtractPreviewImage', None, file_name, model_name)

    def is_document_modified(self):
        """

        Verifies that the current document has been modified in some way.

        No parameters

        Returns

        Boolean : True or False indicating either modified or not modified.

        """

        return self._ApplyTypes_(273, 1, (12, 0), (,), u'IsDocumentModified', None, )

    def notes(self, notes):
        """

        Returns or sets the document's notes.  Notes are generally created by using Rhino's Notes command.

        Parameters

        Notes : Optional, String, str, String

        Returns

        String : If strNotes is not specified, the current notes if successful.
        String : If strNotes is specified, the previous notes if successful.
        Null : If not successful, or on error.

        """

        return self._ApplyTypes_(274, 1, (12, 0), ((8, 0),), u'Notes', None, notes)

    def read_file_version(self):
        """

        Returns the file version of the current document.  Use this function to determine which version of Rhino last saved the document. Note, this function will not return values from referenced or merged files.

        No parameters

        Returns

        Number : The file version of the document if successful.  Note, values less than zero indicate that the current document has not been read (from disk).
        Null : If not successful, or on error.

        """

        return self._ApplyTypes_(737, 1, (12, 0), (,), u'ReadFileVersion', None, )

    def redraw(self):
        """

        Redraws all views.

        No parameters

        No returns


        """

        return self._ApplyTypes_(114, 1, (12, 0), (,), u'Redraw', None, )

    def render_antialias(self, style):
        """

        pixel.  Increasing the antialiasing level can add considerable time to the overall rendering.  See Rhino's DocumentProperties command (Rhino Render window) for details.

        Parameters

        Style : Optional, Number, int, Integer

        Returns

        Number : If intStyle is not specified, the current render antialiasing style if successful.
        Number : If intStyle  is not specified, the previous render antialiasing style if successful.
        Number : Is not successful, or on error.

        """

        return self._ApplyTypes_(333, 1, (12, 0), ((2, 0),), u'RenderAntialias', None, style)

    def render_color(self, item, color):
        """

        Returns or sets the render ambient light or background color. Render colors are represented as RGB colors. An RGB color specifies the relative intensity of red, green, and blue to cause a specific color to be displayed. See Rhino's DocumentProperties command (Rhino Render window) for details.

        Parameters

        Item : Required, Number, int, Integer
        Color : Optional, Number, lng, Integer

        Returns

        Number : If lngColor is not specified, the current intItem color if successful.
        Number : If lngColor is specified, the previous intItem color if successful.
        Null : If not successful, or on error.

        """

        return self._ApplyTypes_(331, 1, (12, 0), ((2, 0), (3, 0),), u'RenderColor', None, item, color)

    def render_mesh_density(self, density):
        """

        For more information on render meshes, see the Document Properties: Mesh topic in the Rhino help file.

        Parameters

        Density : Optional, Number, dbl, Double

        Returns

        Number : If dblDensity is not specified, the current render mesh density if successful.
        Number : If dblDensity is specified, the previous render mesh density if successful.
        Null : If not successful, or on error.

        """

        return self._ApplyTypes_(844, 1, (12, 0), ((5, 0),), u'RenderMeshDensity', None, density)

    def render_mesh_max_angle(self, angle):
        """

        For more information on render meshes, see the Document Properties: Mesh topic in the Rhino help file.

        Parameters

        Angle : Optional, Number, dbl, Double

        Returns

        Number : If dblAngle is not specified, the current render maximum angle if successful.
        Number : If dblAngle is specified, the previous render mesh maximum angle if successful.
        Null : If not successful, or on error.

        """

        return self._ApplyTypes_(845, 1, (12, 0), ((5, 0),), u'RenderMeshMaxAngle', None, angle)

    def render_mesh_max_aspect_ratio(self, ratio):
        """

        For more information on render meshes, see the Document Properties: Mesh topic in the Rhino help file.

        Parameters

        Ratio : Optional, Number, dbl, Double

        Returns

        Number : If dblRatio is not specified, the current render mesh maximum aspect ratio if successful.
        Number : If dblRatio is specified, the previous render mesh maximum aspect ratio if successful.
        Null : If not successful, or on error.

        """

        return self._ApplyTypes_(846, 1, (12, 0), ((5, 0),), u'RenderMeshMaxAspectRatio', None, ratio)

    def render_mesh_max_dist_edge_to_srf(self, distance):
        """

        For more information on render meshes, see the Document Properties: Mesh topic in the Rhino help file.

        Parameters

        Distance : Optional, Number, dbl, Double

        Returns

        Number : If dblDistance is not specified, the current render mesh maximum distance, edge to surface if successful.
        Number : If dblDistance is specified, the previous render mesh maximum distance, edge to surface if successful.
        Null : If not successful, or on error.

        """

        return self._ApplyTypes_(849, 1, (12, 0), ((5, 0),), u'RenderMeshMaxDistEdgeToSrf', None, distance)

    def render_mesh_max_edge_length(self, length):
        """

        For more information on render meshes, see the Document Properties: Mesh topic in the Rhino help file.

        Parameters

        Length : Optional, Number, dbl, Double

        Returns

        Number : If dblLength is not specified, the current render mesh maximum edge length if successful.
        Number : If dblLength is specified, the previous render mesh maximum edge length if successful.
        Null : If not successful, or on error.

        """

        return self._ApplyTypes_(848, 1, (12, 0), ((5, 0),), u'RenderMeshMaxEdgeLength', None, length)

    def render_mesh_min_edge_length(self, length):
        """

        For more information on render meshes, see the Document Properties: Mesh topic in the Rhino help file.

        Parameters

        Length : Optional, Number, dbl, Double

        Returns

        Number : If dblLength is not specified, the current render mesh minimum edge length if successful.
        Number : If dblLength is specified, the previous render mesh minimum edge length if successful.
        Null : If not successful, or on error.

        """

        return self._ApplyTypes_(847, 1, (12, 0), ((5, 0),), u'RenderMeshMinEdgeLength', None, length)

    def render_mesh_min_initial_grid_quads(self, quads):
        """

        For more information on render meshes, see the Document Properties: Mesh topic in the Rhino help file.

        Parameters

        Quads : Optional, Number, int, Integer

        Returns

        Number : If intQuads is not specified, the current render mesh minimum initial grid quads if successful.
        Number : If intQuads is specified, the previous render mesh minimum initial grid quads if successful.
        Null : If not successful, or on error.

        """

        return self._ApplyTypes_(850, 1, (12, 0), ((2, 0),), u'RenderMeshMinInitialGridQuads', None, quads)

    def render_mesh_quality(self, quality):
        """

        For more information on render meshes, see the Document Properties: Mesh topic in the Rhino help file.

        Parameters

        Quality : Optional, Number, int, Integer

        Returns

        Number : If intQuality is not specified, the current render mesh quality if successful.
        Number : If intQuality is specified, the previous render mesh quality if successful.
        Null : If not successful, or on error.

        """

        return self._ApplyTypes_(843, 1, (12, 0), ((2, 0),), u'RenderMeshQuality', None, quality)

    def render_mesh_settings(self, settings):
        """

        For more information on render meshes, see the Document Properties: Mesh topic in the Rhino help file.

        Parameters

        Settings : Optional, Number, int, Integer

        Returns

        Number : If intSettings is not specified, the current render mesh settings if successful.
        Number : If intSettings is specified, the previous render mesh settings if successful.
        Null : If not successful, or on error.

        """

        return self._ApplyTypes_(851, 1, (12, 0), ((2, 0),), u'RenderMeshSettings', None, settings)

    def render_resolution(self, resolution):
        """

        Returns or sets the render resolution. Resolution is measured in pixels. See Rhino's DocumentProperties command (Rhino Render window) for details. Note, if the render resolution is set to "viewport", then the size of the active viewt is returned.

        Parameters

        Resolution : Required, Array, arrdbl, Array of ?

        Returns

        Array : If arrResolution is not specified, an array containing two numbers identifying the current resolution width and height in pixels if successful.
        Array : If arrResolution is specified, an array containing two numbers identifying the previous resolution width and height in pixels if successful.
        Null : If not successful, or on error.

        """

        return self._ApplyTypes_(332, 1, (12, 0), ((8197, 0),), u'RenderResolution', None, _utils.flatten(resolution))

    def render_settings(self, settings):
        """

        Returns or sets render settings.  See Rhino's DocumentProperties command (Rhino Render window) for details.

        Parameters

        Settings : Optional, Number, int, Integer

        Returns

        Number : If intSettings is not specified, the current render settings if successful.
        Number : If intSettings is not specified, the previous render settings if successful.
        Number : Is not successful, or on error.

        """

        return self._ApplyTypes_(334, 1, (12, 0), ((2, 0),), u'RenderSettings', None, settings)

    def unit_absolute_tolerance(self, abs_tol):
        """

        Returns or sets the document's absolute tolerance parameter.  Absolute tolerance is measured in drawing units. See Rhino's DocumentProperties command (Units window) for details.

        Parameters

        AbsTol : Optional, Number, dbl, Double

        Returns

        Number : If dblAbsTol is not specified, the current absolute tolerance if successful.
        Number : If dblAbsTol is specified, the previous absolute tolerance if successful.
        Null : If not successful, or on error.

        """

        return self._ApplyTypes_(324, 1, (12, 0), ((5, 0),), u'UnitAbsoluteTolerance', None, abs_tol)

    def unit_angle_tolerance(self, angle_tol):
        """

        Returns or sets the document's angle tolerance parameter.  Angle tolerance is measured degrees.  See Rhino's DocumentProperties command (Units window) for details.

        Parameters

        AngleTol : Optional, Number, dbl, Double

        Returns

        Number : If dblAngleTol is not specified, the current angle tolerance if successful.
        Number : If dblAngleTol is specified, the previous angle tolerance if successful.
        Null : If not successful, or on error.

        """

        return self._ApplyTypes_(325, 1, (12, 0), ((5, 0),), u'UnitAngleTolerance', None, angle_tol)

    def unit_custom_unit_system(self, units, scale, name):
        """

        Sets the document's units system to a user-defined system.  This overrides the units system set using the UnitSystem method.  See Rhino's DocumentProperties command (Units window) for details.

        Parameters

        Units : Required, Number, dbl, Double
        Scale : Optional, Boolean, bln, Boolean
        Name : Optional, String, str, String

        Returns

        Number : The previous units system if successful.  See UnitSystem for details.
        Null : If not successful, or on error.

        """

        return self._ApplyTypes_(326, 1, (12, 0), ((5, 0), (11, 0), (8, 0),), u'UnitCustomUnitSystem', None, units, scale, name)

    def unit_distance_display_mode(self, mode):
        """

        Returns or sets the document's distance display mode parameter.  See Rhino's DocumentProperties command (Units window) for details.

        Parameters

        Mode : Optional, Number, int, Integer

        Returns

        Number : If intMode is not specified, the current distance display mode if successful.
        Number : If intMode is specified, the previous distance display mode if successful.
        Null : If not successful, or on error.

        """

        return self._ApplyTypes_(327, 1, (12, 0), ((2, 0),), u'UnitDistanceDisplayMode', None, mode)

    def unit_distance_display_precision(self, precision):
        """

        Returns or sets the document's distance display precision parameter.  See Rhino's DocumentProperties command (Units window) for details.

        Parameters

        Precision : Optional, Number, int, Integer

        Returns

        Number : If intPrecision is not specified, the current distance display precision if successful.
        Number : If intPrecision is specified, the previous distance display precision if successful.
        Null : If not successful, or on error.

        """

        return self._ApplyTypes_(328, 1, (12, 0), ((2, 0),), u'UnitDistanceDisplayPrecision', None, precision)

    def unit_relative_tolerance(self, rel_tol):
        """

        Returns or sets the document's relative tolerance parameter.  Relative tolerance is measured in percent. See Rhino's DocumentProperties command (Units window) for details.

        Parameters

        RelTol : Optional, Number, dbl, Double

        Returns

        Number : If dblRelTol is not specified, the current relative tolerance if successful.
        Number : If dblRelTol is specified, the previous relative tolerance if successful.
        Null : If not successful, or on error.

        """

        return self._ApplyTypes_(329, 1, (12, 0), ((5, 0),), u'UnitRelativeTolerance', None, rel_tol)

    def unit_scale(self, to_system, from_system):
        """

        Returns the scale factor for changing between unit systems.

        Parameters

        ToSystem : Required, Number, int, Integer
        FromSystem : Optional, Number, int, Integer

        Returns

        Number : The scale factor for changing between unit systems if successful.
        Null : If not successful, or on error.

        """

        return self._ApplyTypes_(868, 1, (12, 0), ((2, 0), (2, 0),), u'UnitScale', None, to_system, from_system)

    def unit_system(self, system, scale):
        """

        Returns or sets the document's units system.  See Rhino's DocumentProperties command (Units window) for details.

        Parameters

        System : Optional, Number, int, Integer
        Scale : Optional, Boolean, bln, Boolean

        Returns

        Number : The previous units system if successful.
        Null : If not successful, or on error.

        """

        return self._ApplyTypes_(330, 1, (12, 0), ((2, 0), (11, 0),), u'UnitSystem', None, system, scale)

    def unit_system_name(self, capitalize, singular, abbreviate):
        """

        Returns the name of the current unit system.

        Parameters

        Capitalize : Optional, Boolean, bln, Boolean
        Singular : Optional, Boolean, bln, Boolean
        Abbreviate : Optional, Boolean, bln, Boolean

        Returns

        String : The name of the current units system if successful.

        """

        return self._ApplyTypes_(492, 1, (12, 0), ((11, 0), (11, 0), (11, 0),), u'UnitSystemName', None, capitalize, singular, abbreviate)

