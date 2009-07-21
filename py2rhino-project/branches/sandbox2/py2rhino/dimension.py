# Auto-generated wrapper for Rhino4 RhinoScript functions

import exceptions
from py2rhino._util import *
from py2rhino._rhinoscript import IRhinoScript

class Dimension(IRhinoScript):



    def add_dim_style(self, dim_style=None):
        """        
        Adds a new dimension style to the document.  The new dimension style will be initialized with the current default dimension style properties.
    
        Parameters
        ==========

        dim_style, String, Optional        
        The name of the new dimension style.  If omitted, Rhino automatically generates the dimension style name.
            
        Returns
        =======

        string
        The name of the new dimension style if successful.

        null
        If not successful, or on error.

        """

        params = [dim_style]
        params_required = [False]
        params_magic_numbers = [(VT_BSTR, 1),]
        params_flattened = [dim_style]

        for i in range(len(params)):
            if (params[i] == None) and (not params_required[i]):
                params_magic_numbers.pop(i)
                params_flattened.pop(i)

        params_magic_numbers = tuple(params_magic_numbers)
        params_flattened = tuple(params_flattened)

        return self._ApplyTypes_(455, 1, (VT_VARIANT, 0), params_magic_numbers, u"AddDimStyle", None, *params_flattened)

    def add_leader(self, points, view=None, text=None):
        """        
        Adds an annotation leader to the document. Leader objects are planar. The array of 3-D points passed to this member should be co-planar.
    
        Parameters
        ==========

        points, Array of ????, Required        
        An array of 3-D points.  The array must contain at least two points.
            
        view, String, Optional        
        The title of the view.  If a view title is specified,  arrPoints will be constrained to the view's construction plane. If a view title is not specified, arrPoints will be constrained to a plane fit through the array of points.
            
        text, String, Optional        
        The leader's text string.
            
        Returns
        =======

        string
        The identifier of the new object if successful.

        null
        If not successful, or on error.

        """

        params = [points, view, text]
        params_required = [True, False, False]
        params_magic_numbers = [(VT_VARIANT, 1), (VT_BSTR, 1), (VT_BSTR, 1)]
        params_flattened = [flatten(points), view, text]

        for i in range(len(params)):
            if (params[i] == None) and (not params_required[i]):
                params_magic_numbers.pop(i)
                params_flattened.pop(i)

        params_magic_numbers = tuple(params_magic_numbers)
        params_flattened = tuple(params_flattened)

        return self._ApplyTypes_(321, 1, (VT_VARIANT, 0), params_magic_numbers, u"AddLeader", None, *params_flattened)

    def current_dim_style(self, dim_style=None):
        """        
        Returns or changes the current default dimension style.
    
        Parameters
        ==========

        dim_style, String, Optional        
        The name of an existing dimension style to make current.
            
        Returns
        =======

        string
        If a dimension style is not specified, the name of the current dimension style if successful.

        string
        If a dimension style is specified, the name of the previous current dimension style if successful.

        null
        If not successful, or on error.

        """

        params = [dim_style]
        params_required = [False]
        params_magic_numbers = [(VT_BSTR, 1),]
        params_flattened = [dim_style]

        for i in range(len(params)):
            if (params[i] == None) and (not params_required[i]):
                params_magic_numbers.pop(i)
                params_flattened.pop(i)

        params_magic_numbers = tuple(params_magic_numbers)
        params_flattened = tuple(params_flattened)

        return self._ApplyTypes_(453, 1, (VT_VARIANT, 0), params_magic_numbers, u"CurrentDimStyle", None, *params_flattened)

    def delete_dim_style(self, dim_style):
        """        
        Removes an existing dimension style from the document.  The dimension style to be removed cannot be the reference by any dimension objects.
    
        Parameters
        ==========

        dim_style, String, Required        
        The name of an un-referenced dimension style.
            
        Returns
        =======

        string
        The name of the deleted dimension style if successful.

        null
        If not successful, or on error.

        """

        params = [dim_style]
        params_required = [True]
        params_magic_numbers = [(VT_BSTR, 1),]
        params_flattened = [dim_style]

        for i in range(len(params)):
            if (params[i] == None) and (not params_required[i]):
                params_magic_numbers.pop(i)
                params_flattened.pop(i)

        params_magic_numbers = tuple(params_magic_numbers)
        params_flattened = tuple(params_flattened)

        return self._ApplyTypes_(456, 1, (VT_VARIANT, 0), params_magic_numbers, u"DeleteDimStyle", None, *params_flattened)

    def dim_scale(self, scale=None):
        """        
        Returns or changes the document's global dimension scale.
    
        Parameters
        ==========

        scale, Double, Optional        
        The new global dimension scale value.  If omitted, the current dimension scale will be returned.
            
        Returns
        =======

        number
        If a dimension scale is not specified, the current dimension scale if successful.

        number
        If a dimension scale is specified, the previous dimension scale if successful.

        null
        If not successful, or on error.

        """

        params = [scale]
        params_required = [False]
        params_magic_numbers = [(VT_R8, 1),]
        params_flattened = [scale]

        for i in range(len(params)):
            if (params[i] == None) and (not params_required[i]):
                params_magic_numbers.pop(i)
                params_flattened.pop(i)

        params_magic_numbers = tuple(params_magic_numbers)
        params_flattened = tuple(params_flattened)

        return self._ApplyTypes_(460, 1, (VT_VARIANT, 0), params_magic_numbers, u"DimScale", None, *params_flattened)

    def dim_style_angle_precision(self, dim_style, precision=None):
        """        
        Returns or changes the angle display precision of a dimension style.
    
        Parameters
        ==========

        dim_style, String, Required        
        The name of an existing dimension style.
            
        precision, Integer, Optional        
        The new angle precision value.  If omitted, the current angle precision is returned.
            
        Returns
        =======

        number
        If a precision is not specified, the current angle precision if successful.

        number
        If a precision is specified, the previous angle precision if successful.

        null
        If not successful, or on error.

        """

        params = [dim_style, precision]
        params_required = [True, False]
        params_magic_numbers = [(VT_BSTR, 1), (VT_I2, 1)]
        params_flattened = [dim_style, precision]

        for i in range(len(params)):
            if (params[i] == None) and (not params_required[i]):
                params_magic_numbers.pop(i)
                params_flattened.pop(i)

        params_magic_numbers = tuple(params_magic_numbers)
        params_flattened = tuple(params_flattened)

        return self._ApplyTypes_(464, 1, (VT_VARIANT, 0), params_magic_numbers, u"DimStyleAnglePrecision", None, *params_flattened)

    def dim_style_arrow_size(self, dim_style, size=None):
        """        
        Returns or changes the arrow size of a dimension style.
    
        Parameters
        ==========

        dim_style, String, Required        
        The name of an existing dimension style.
            
        size, Double, Optional        
        The new arrow size.  If omitted, the current arrow size is returned.
            
        Returns
        =======

        number
        If a size value is not specified, the current arrow size if successful.

        number
        If a size value is specified, the previous arrow size if successful.

        null
        If not successful, or on error.

        """

        params = [dim_style, size]
        params_required = [True, False]
        params_magic_numbers = [(VT_BSTR, 1), (VT_R8, 1)]
        params_flattened = [dim_style, size]

        for i in range(len(params)):
            if (params[i] == None) and (not params_required[i]):
                params_magic_numbers.pop(i)
                params_flattened.pop(i)

        params_magic_numbers = tuple(params_magic_numbers)
        params_flattened = tuple(params_flattened)

        return self._ApplyTypes_(468, 1, (VT_VARIANT, 0), params_magic_numbers, u"DimStyleArrowSize", None, *params_flattened)

    def dim_style_count():
        """        
        Returns the number of dimension styles in the document.
    
        No parameters

        Returns
        =======

        number
        The number of dimension styles in the document.

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

        return self._ApplyTypes_(451, 1, (VT_VARIANT, 0), params_magic_numbers, u"DimStyleCount", None, *params_flattened)

    def dim_style_extension(self, dim_style, extension=None):
        """        
        Returns or changes the extension line extension of a dimension style.
    
        Parameters
        ==========

        dim_style, String, Required        
        The name of an existing dimension style.
            
        extension, Double, Optional        
        The new extension line extension.  If omitted, the current extension line extension is returned.
            
        Returns
        =======

        number
        If an extension is not specified, the current extension line extension if successful.

        number
        If an extension is specified, the previous extension line extension if successful.

        null
        If not successful, or on error.

        """

        params = [dim_style, extension]
        params_required = [True, False]
        params_magic_numbers = [(VT_BSTR, 1), (VT_R8, 1)]
        params_flattened = [dim_style, extension]

        for i in range(len(params)):
            if (params[i] == None) and (not params_required[i]):
                params_magic_numbers.pop(i)
                params_flattened.pop(i)

        params_magic_numbers = tuple(params_magic_numbers)
        params_flattened = tuple(params_flattened)

        return self._ApplyTypes_(466, 1, (VT_VARIANT, 0), params_magic_numbers, u"DimStyleExtension", None, *params_flattened)

    def dim_style_font(self, dim_style, font=None):
        """        
        Returns or changes the font used by a dimension style.
    
        Parameters
        ==========

        dim_style, String, Required        
        The name of an existing dimension style.
            
        font, String, Optional        
        The new font face name.  If omitted, the current font is returned.
            
        Returns
        =======

        string
        If a font is not specified, the current font if successful.

        string
        If a font is specified, the previous font if successful.

        null
        If not successful, or on error.

        """

        params = [dim_style, font]
        params_required = [True, False]
        params_magic_numbers = [(VT_BSTR, 1), (VT_BSTR, 1)]
        params_flattened = [dim_style, font]

        for i in range(len(params)):
            if (params[i] == None) and (not params_required[i]):
                params_magic_numbers.pop(i)
                params_flattened.pop(i)

        params_magic_numbers = tuple(params_magic_numbers)
        params_flattened = tuple(params_flattened)

        return self._ApplyTypes_(462, 1, (VT_VARIANT, 0), params_magic_numbers, u"DimStyleFont", None, *params_flattened)

    def dim_style_leader_arrow_size(self, dim_style, size=None):
        """        
        Returns or changes the leader arrow size of a dimension style.
    
        Parameters
        ==========

        dim_style, String, Required        
        The name of an existing dimension style.
            
        size, Double, Optional        
        The new leader arrow size.  If omitted, the current leader arrow size is returned.
            
        Returns
        =======

        number
        If a size value is not specified, the current leader arrow size if successful.

        number
        If a size value is specified, the previous leader arrow size if successful.

        null
        If not successful, or on error.

        """

        params = [dim_style, size]
        params_required = [True, False]
        params_magic_numbers = [(VT_BSTR, 1), (VT_R8, 1)]
        params_flattened = [dim_style, size]

        for i in range(len(params)):
            if (params[i] == None) and (not params_required[i]):
                params_magic_numbers.pop(i)
                params_flattened.pop(i)

        params_magic_numbers = tuple(params_magic_numbers)
        params_flattened = tuple(params_flattened)

        return self._ApplyTypes_(704, 1, (VT_VARIANT, 0), params_magic_numbers, u"DimStyleLeaderArrowSize", None, *params_flattened)

    def dim_style_linear_precision(self, dim_style, precision=None):
        """        
        Returns or changes the linear display precision of a dimension style.
    
        Parameters
        ==========

        dim_style, String, Required        
        The name of an existing dimension style.
            
        precision, Integer, Optional        
        The new linear precision value.  If omitted, the current linear precision is returned.
            
        Returns
        =======

        number
        If a precision is not specified, the current linear precision if successful.

        number
        If ar precision is specified, the previous linear precision if successful.

        null
        If not successful, or on error.

        """

        params = [dim_style, precision]
        params_required = [True, False]
        params_magic_numbers = [(VT_BSTR, 1), (VT_I2, 1)]
        params_flattened = [dim_style, precision]

        for i in range(len(params)):
            if (params[i] == None) and (not params_required[i]):
                params_magic_numbers.pop(i)
                params_flattened.pop(i)

        params_magic_numbers = tuple(params_magic_numbers)
        params_flattened = tuple(params_flattened)

        return self._ApplyTypes_(463, 1, (VT_VARIANT, 0), params_magic_numbers, u"DimStyleLinearPrecision", None, *params_flattened)

    def dim_style_names(self, sort=None):
        """        
        Returns the names of all dimension styles in the document.
    
        Parameters
        ==========

        sort, Boolean, Optional        
        Return a sorted list of dimension style names. The default is not to return a sorted list (False).
            
        Returns
        =======

        array
        An array of dimension style names if successful.

        null
        If not successful, or on error.

        """

        params = [sort]
        params_required = [False]
        params_magic_numbers = [(VT_BOOL, 1),]
        params_flattened = [sort]

        for i in range(len(params)):
            if (params[i] == None) and (not params_required[i]):
                params_magic_numbers.pop(i)
                params_flattened.pop(i)

        params_magic_numbers = tuple(params_magic_numbers)
        params_flattened = tuple(params_flattened)

        return self._ApplyTypes_(452, 1, (VT_VARIANT, 0), params_magic_numbers, u"DimStyleNames", None, *params_flattened)

    def dim_style_number_format(self, dim_style, format=None):
        """        
        Returns or changes the number display format of a dimension style.
    
        Parameters
        ==========

        dim_style, String, Required        
        The name of an existing dimension style.
            
        format, Integer, Optional        
        The new number display format.  If omitted, the current number display format is returned.  The format values are as follows:
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
        If a format is not specified, the current number display format if successful.

        number
        If a format is specified, the previous number display format if successful.

        null
        If not successful, or on error.

        """

        params = [dim_style, format]
        params_required = [True, False]
        params_magic_numbers = [(VT_BSTR, 1), (VT_I2, 1)]
        params_flattened = [dim_style, format]

        for i in range(len(params)):
            if (params[i] == None) and (not params_required[i]):
                params_magic_numbers.pop(i)
                params_flattened.pop(i)

        params_magic_numbers = tuple(params_magic_numbers)
        params_flattened = tuple(params_flattened)

        return self._ApplyTypes_(459, 1, (VT_VARIANT, 0), params_magic_numbers, u"DimStyleNumberFormat", None, *params_flattened)

    def dim_style_offset(self, dim_style, offset=None):
        """        
        Returns or changes the extension line offset of a dimension style.
    
        Parameters
        ==========

        dim_style, String, Required        
        The name of an existing dimension style.
            
        offset, Double, Optional        
        The new extension line offset.  If omitted, the current extension line offset is returned.
            
        Returns
        =======

        number
        If an offset is not specified, the current extension line offset if successful.

        number
        If an offset is specified, the previous extension line offset if successful.

        null
        If not successful, or on error.

        """

        params = [dim_style, offset]
        params_required = [True, False]
        params_magic_numbers = [(VT_BSTR, 1), (VT_R8, 1)]
        params_flattened = [dim_style, offset]

        for i in range(len(params)):
            if (params[i] == None) and (not params_required[i]):
                params_magic_numbers.pop(i)
                params_flattened.pop(i)

        params_magic_numbers = tuple(params_magic_numbers)
        params_flattened = tuple(params_flattened)

        return self._ApplyTypes_(467, 1, (VT_VARIANT, 0), params_magic_numbers, u"DimStyleOffset", None, *params_flattened)

    def dim_style_text_alignment(self, dim_style, alignment=None):
        """        
        Returns or changes the text alignment mode of a dimension style.
    
        Parameters
        ==========

        dim_style, String, Required        
        The name of an existing dimension style.
            
        alignment, Integer, Optional        
        The new text alignment.  If omitted, the current text alignment is returned.  The text alignment values are as follows:
		Value
		Description
		0
		Normal (same as 2)
		1
		Horizontal to view
		2
		Above the dimension line
		3
            
        Returns
        =======

        number
        If a mode is not specified, the current text alignment mode  if successful.

        number
        If a mode is specified, the previous text alignment mode if successful.

        null
        If not successful, or on error.

        """

        params = [dim_style, alignment]
        params_required = [True, False]
        params_magic_numbers = [(VT_BSTR, 1), (VT_I2, 1)]
        params_flattened = [dim_style, alignment]

        for i in range(len(params)):
            if (params[i] == None) and (not params_required[i]):
                params_magic_numbers.pop(i)
                params_flattened.pop(i)

        params_magic_numbers = tuple(params_magic_numbers)
        params_flattened = tuple(params_flattened)

        return self._ApplyTypes_(461, 1, (VT_VARIANT, 0), params_magic_numbers, u"DimStyleTextAlignment", None, *params_flattened)

    def dim_style_text_gap(self, dim_style, gap=None):
        """        
        Returns or changes the text gap used by a dimension style.
    
        Parameters
        ==========

        dim_style, String, Required        
        The name of an existing dimension style.
            
        gap, Double, Optional        
        The new text gap.  If omitted, the current text gap is returned.
            
        Returns
        =======

        number
        If a gap is not specified, the current text gap if successful.

        number
        If a gap is specified, the previous text gap if successful.

        null
        If not successful, or on error.

        """

        params = [dim_style, gap]
        params_required = [True, False]
        params_magic_numbers = [(VT_BSTR, 1), (VT_R8, 1)]
        params_flattened = [dim_style, gap]

        for i in range(len(params)):
            if (params[i] == None) and (not params_required[i]):
                params_magic_numbers.pop(i)
                params_flattened.pop(i)

        params_magic_numbers = tuple(params_magic_numbers)
        params_flattened = tuple(params_flattened)

        return self._ApplyTypes_(741, 1, (VT_VARIANT, 0), params_magic_numbers, u"DimStyleTextGap", None, *params_flattened)

    def dim_style_text_height(self, dim_style, height=None):
        """        
        Returns or changes the text height used by a dimension style.
    
        Parameters
        ==========

        dim_style, String, Required        
        The name of an existing dimension style.
            
        height, Double, Optional        
        The new text height.  If omitted, the current text height is returned.
            
        Returns
        =======

        number
        If a height is not specified, the current text height if successful.

        number
        If a height is specified, the previous text height if successful.

        null
        If not successful, or on error.

        """

        params = [dim_style, height]
        params_required = [True, False]
        params_magic_numbers = [(VT_BSTR, 1), (VT_R8, 1)]
        params_flattened = [dim_style, height]

        for i in range(len(params)):
            if (params[i] == None) and (not params_required[i]):
                params_magic_numbers.pop(i)
                params_flattened.pop(i)

        params_magic_numbers = tuple(params_magic_numbers)
        params_flattened = tuple(params_flattened)

        return self._ApplyTypes_(465, 1, (VT_VARIANT, 0), params_magic_numbers, u"DimStyleTextHeight", None, *params_flattened)

    def dimension_style(self, object, style=None):
        """        
        Returns or modifies the dimension style of a dimension object.
    
        Parameters
        ==========

        object, String, Required        
        The object's identifier.
            
        style, String, Optional        
        The name of an existing dimension style.
            
        Returns
        =======

        string
        If strStyle is not specified, then the object's current dimension style if successful.

        string
        If strStyle is specified, then the object's previous dimension style if successful.

        null
        On error.

        """

        params = [object, style]
        params_required = [True, False]
        params_magic_numbers = [(VT_BSTR, 1), (VT_BSTR, 1)]
        params_flattened = [object, style]

        for i in range(len(params)):
            if (params[i] == None) and (not params_required[i]):
                params_magic_numbers.pop(i)
                params_flattened.pop(i)

        params_magic_numbers = tuple(params_magic_numbers)
        params_flattened = tuple(params_flattened)

        return self._ApplyTypes_(703, 1, (VT_VARIANT, 0), params_magic_numbers, u"DimensionStyle", None, *params_flattened)

    def dimension_text(self, object):
        """        
        Returns the text displayed by a dimension object.
    
        Parameters
        ==========

        object, String, Required        
        The object's identifier.
            
        Returns
        =======

        string
        The dimension text if successful.

        null
        On error.

        """

        params = [object]
        params_required = [True]
        params_magic_numbers = [(VT_BSTR, 1),]
        params_flattened = [object]

        for i in range(len(params)):
            if (params[i] == None) and (not params_required[i]):
                params_magic_numbers.pop(i)
                params_flattened.pop(i)

        params_magic_numbers = tuple(params_magic_numbers)
        params_flattened = tuple(params_flattened)

        return self._ApplyTypes_(469, 1, (VT_VARIANT, 0), params_magic_numbers, u"DimensionText", None, *params_flattened)

    def dimension_user_text(self, object, user_text=None):
        """        
        Returns or modifies the user text string of a dimension object. The user text is the string that gets printed when the dimension is drawn. If it contains the token "<>", then the token is replaced with the measured value of the dimension, formatted according to the dimension style settings. Note,  "<>" is the default user text string for linear dimensions.
    
        Parameters
        ==========

        object, String, Required        
        The object's identifier.
            
        user_text, String, Optional        
        The new user text string value. To reset the use text string, use the string "<>".
            
        Returns
        =======

        string
        If strUserText is not specified, then the current user text string if successful.

        string
        If strUserText is specified, then the previous user text string if successful.

        null
        On error.

        """

        params = [object, user_text]
        params_required = [True, False]
        params_magic_numbers = [(VT_BSTR, 1), (VT_BSTR, 1)]
        params_flattened = [object, user_text]

        for i in range(len(params)):
            if (params[i] == None) and (not params_required[i]):
                params_magic_numbers.pop(i)
                params_flattened.pop(i)

        params_magic_numbers = tuple(params_magic_numbers)
        params_flattened = tuple(params_flattened)

        return self._ApplyTypes_(563, 1, (VT_VARIANT, 0), params_magic_numbers, u"DimensionUserText", None, *params_flattened)

    def dimension_value(self, object):
        """        
        Returns the value of a dimension object.
    
        Parameters
        ==========

        object, String, Required        
        The object's identifier.
            
        Returns
        =======

        number
        The value of the dimension successful.

        null
        On error.

        """

        params = [object]
        params_required = [True]
        params_magic_numbers = [(VT_BSTR, 1),]
        params_flattened = [object]

        for i in range(len(params)):
            if (params[i] == None) and (not params_required[i]):
                params_magic_numbers.pop(i)
                params_flattened.pop(i)

        params_magic_numbers = tuple(params_magic_numbers)
        params_flattened = tuple(params_flattened)

        return self._ApplyTypes_(568, 1, (VT_VARIANT, 0), params_magic_numbers, u"DimensionValue", None, *params_flattened)

    def is_aligned_dimension(self, object):
        """        
        Verifies an object is an aligned dimension object.
    
        Parameters
        ==========

        object, String, Required        
        The object's identifier.
            
        Returns
        =======

        boolean
        True if successful, otherwise False.

        null
        On error.

        """

        params = [object]
        params_required = [True]
        params_magic_numbers = [(VT_BSTR, 1),]
        params_flattened = [object]

        for i in range(len(params)):
            if (params[i] == None) and (not params_required[i]):
                params_magic_numbers.pop(i)
                params_flattened.pop(i)

        params_magic_numbers = tuple(params_magic_numbers)
        params_flattened = tuple(params_flattened)

        return self._ApplyTypes_(566, 1, (VT_VARIANT, 0), params_magic_numbers, u"IsAlignedDimension", None, *params_flattened)

    def is_angular_dimension(self, object):
        """        
        Verifies an object is an angular dimension object.
    
        Parameters
        ==========

        object, String, Required        
        The object's identifier.
            
        Returns
        =======

        boolean
        True if successful, otherwise False.

        null
        On error.

        """

        params = [object]
        params_required = [True]
        params_magic_numbers = [(VT_BSTR, 1),]
        params_flattened = [object]

        for i in range(len(params)):
            if (params[i] == None) and (not params_required[i]):
                params_magic_numbers.pop(i)
                params_flattened.pop(i)

        params_magic_numbers = tuple(params_magic_numbers)
        params_flattened = tuple(params_flattened)

        return self._ApplyTypes_(338, 1, (VT_VARIANT, 0), params_magic_numbers, u"IsAngularDimension", None, *params_flattened)

    def is_diameter_dimension(self, object):
        """        
        Verifies an object is a diameter dimension object.
    
        Parameters
        ==========

        object, String, Required        
        The object's identifier.
            
        Returns
        =======

        boolean
        True if successful, otherwise False.

        null
        On error.

        """

        params = [object]
        params_required = [True]
        params_magic_numbers = [(VT_BSTR, 1),]
        params_flattened = [object]

        for i in range(len(params)):
            if (params[i] == None) and (not params_required[i]):
                params_magic_numbers.pop(i)
                params_flattened.pop(i)

        params_magic_numbers = tuple(params_magic_numbers)
        params_flattened = tuple(params_flattened)

        return self._ApplyTypes_(565, 1, (VT_VARIANT, 0), params_magic_numbers, u"IsDiameterDimension", None, *params_flattened)

    def is_dim_style(self, dim_style):
        """        
        Verifies the existence of a dimension style in the document.
    
        Parameters
        ==========

        dim_style, String, Required        
        The name of a dimension style to test.
            
        Returns
        =======

        null
        On error.

        """

        params = [dim_style]
        params_required = [True]
        params_magic_numbers = [(VT_BSTR, 1),]
        params_flattened = [dim_style]

        for i in range(len(params)):
            if (params[i] == None) and (not params_required[i]):
                params_magic_numbers.pop(i)
                params_flattened.pop(i)

        params_magic_numbers = tuple(params_magic_numbers)
        params_flattened = tuple(params_flattened)

        return self._ApplyTypes_(454, 1, (VT_VARIANT, 0), params_magic_numbers, u"IsDimStyle", None, *params_flattened)

    def is_dim_style_reference(self, dim_style):
        """        
        Verifies that an existing dimension style is from a reference file.
    
        Parameters
        ==========

        dim_style, String, Required        
        The name of an existing dimension style.
            
        Returns
        =======

        null
        On error.

        """

        params = [dim_style]
        params_required = [True]
        params_magic_numbers = [(VT_BSTR, 1),]
        params_flattened = [dim_style]

        for i in range(len(params)):
            if (params[i] == None) and (not params_required[i]):
                params_magic_numbers.pop(i)
                params_flattened.pop(i)

        params_magic_numbers = tuple(params_magic_numbers)
        params_flattened = tuple(params_flattened)

        return self._ApplyTypes_(457, 1, (VT_VARIANT, 0), params_magic_numbers, u"IsDimStyleReference", None, *params_flattened)

    def is_dimension(self, object):
        """        
        Verifies an object is a dimension object.
    
        Parameters
        ==========

        object, String, Required        
        The object's identifier.
            
        Returns
        =======

        boolean
        True if successful, otherwise False.

        null
        On error.

        """

        params = [object]
        params_required = [True]
        params_magic_numbers = [(VT_BSTR, 1),]
        params_flattened = [object]

        for i in range(len(params)):
            if (params[i] == None) and (not params_required[i]):
                params_magic_numbers.pop(i)
                params_flattened.pop(i)

        params_magic_numbers = tuple(params_magic_numbers)
        params_flattened = tuple(params_flattened)

        return self._ApplyTypes_(564, 1, (VT_VARIANT, 0), params_magic_numbers, u"IsDimension", None, *params_flattened)

    def is_leader(self, object):
        """        
        Verifies an object is a dimension leader object.
    
        Parameters
        ==========

        object, String, Required        
        The object's identifier.
            
        Returns
        =======

        boolean
        True if successful, otherwise False.

        null
        On error.

        """

        params = [object]
        params_required = [True]
        params_magic_numbers = [(VT_BSTR, 1),]
        params_flattened = [object]

        for i in range(len(params)):
            if (params[i] == None) and (not params_required[i]):
                params_magic_numbers.pop(i)
                params_flattened.pop(i)

        params_magic_numbers = tuple(params_magic_numbers)
        params_flattened = tuple(params_flattened)

        return self._ApplyTypes_(337, 1, (VT_VARIANT, 0), params_magic_numbers, u"IsLeader", None, *params_flattened)

    def is_linear_dimension(self, object):
        """        
        Verifies an object is a linear dimension object.
    
        Parameters
        ==========

        object, String, Required        
        The object's identifier.
            
        Returns
        =======

        boolean
        True if successful, otherwise False.

        null
        On error.

        """

        params = [object]
        params_required = [True]
        params_magic_numbers = [(VT_BSTR, 1),]
        params_flattened = [object]

        for i in range(len(params)):
            if (params[i] == None) and (not params_required[i]):
                params_magic_numbers.pop(i)
                params_flattened.pop(i)

        params_magic_numbers = tuple(params_magic_numbers)
        params_flattened = tuple(params_flattened)

        return self._ApplyTypes_(339, 1, (VT_VARIANT, 0), params_magic_numbers, u"IsLinearDimension", None, *params_flattened)

    def is_ordinate_dimension(self, object):
        """        
        Verifies an object is an ordinate dimension object.
    
        Parameters
        ==========

        object, String, Required        
        The object's identifier.
            
        Returns
        =======

        boolean
        True if successful, otherwise False.

        null
        On error.

        """

        params = [object]
        params_required = [True]
        params_magic_numbers = [(VT_BSTR, 1),]
        params_flattened = [object]

        for i in range(len(params)):
            if (params[i] == None) and (not params_required[i]):
                params_magic_numbers.pop(i)
                params_flattened.pop(i)

        params_magic_numbers = tuple(params_magic_numbers)
        params_flattened = tuple(params_flattened)

        return self._ApplyTypes_(659, 1, (VT_VARIANT, 0), params_magic_numbers, u"IsOrdinateDimension", None, *params_flattened)

    def is_radial_dimension(self, object):
        """        
        Verifies an object is a radial dimension object.
    
        Parameters
        ==========

        object, String, Required        
        The object's identifier.
            
        Returns
        =======

        boolean
        True if successful, otherwise False.

        null
        On error.

        """

        params = [object]
        params_required = [True]
        params_magic_numbers = [(VT_BSTR, 1),]
        params_flattened = [object]

        for i in range(len(params)):
            if (params[i] == None) and (not params_required[i]):
                params_magic_numbers.pop(i)
                params_flattened.pop(i)

        params_magic_numbers = tuple(params_magic_numbers)
        params_flattened = tuple(params_flattened)

        return self._ApplyTypes_(340, 1, (VT_VARIANT, 0), params_magic_numbers, u"IsRadialDimension", None, *params_flattened)

    def leader_text(self, object, text=None):
        """        
        Returns or modifies the text string of a dimension leader object.
    
        Parameters
        ==========

        object, String, Required        
        The object's identifier.
            
        text, String, Optional        
        The new text string value.
            
        Returns
        =======

        string
        If strText is not specified, then the current text string if successful.

        string
        If strText is specified, then the previous text string if successful.

        null
        On error.

        """

        params = [object, text]
        params_required = [True, False]
        params_magic_numbers = [(VT_BSTR, 1), (VT_BSTR, 1)]
        params_flattened = [object, text]

        for i in range(len(params)):
            if (params[i] == None) and (not params_required[i]):
                params_magic_numbers.pop(i)
                params_flattened.pop(i)

        params_magic_numbers = tuple(params_magic_numbers)
        params_flattened = tuple(params_flattened)

        return self._ApplyTypes_(895, 1, (VT_VARIANT, 0), params_magic_numbers, u"LeaderText", None, *params_flattened)

    def rename_dim_style(self, old_style, new_style):
        """        
        Renames an existing dimension style.
    
        Parameters
        ==========

        old_style, String, Required        
        The name of an existing dimension style.
            
        new_style, String, Required        
        The new dimension style name.
            
        Returns
        =======

        string
        The new dimension style name if successful.

        null
        If not successful, or on error.

        """

        params = [old_style, new_style]
        params_required = [True, True]
        params_magic_numbers = [(VT_BSTR, 1), (VT_BSTR, 1)]
        params_flattened = [old_style, new_style]

        for i in range(len(params)):
            if (params[i] == None) and (not params_required[i]):
                params_magic_numbers.pop(i)
                params_flattened.pop(i)

        params_magic_numbers = tuple(params_magic_numbers)
        params_flattened = tuple(params_flattened)

        return self._ApplyTypes_(458, 1, (VT_VARIANT, 0), params_magic_numbers, u"RenameDimStyle", None, *params_flattened)

