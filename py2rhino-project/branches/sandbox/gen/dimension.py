# Auto-generated wrapper for Rhino4 RhinoScript functions

import exceptions
import _utils
from _rhinoscript import IRhinoScript

class Dimension(IRhinoScript):



    def add_dim_style(self, dim_style):
        """

        Adds a new dimension style to the document.  The new dimension style will be initialized with the current default dimension style properties.

        Parameters

        DimStyle : Optional, String, str, String

        Returns

        String : The name of the new dimension style if successful.
        Null : If not successful, or on error.

        """

        return self._ApplyTypes_(455, 1, (12, 0), ((8, 0),), u'AddDimStyle', None, dim_style)

    def add_leader(self, points, view, text):
        """

        Adds an annotation leader to the document. Leader objects are planar. The array of 3-D points passed to this member should be co-planar.

        Parameters

        Points : Required, Array, arrdbl, Array of ?
        View : Optional, String, str, String
        Text : Optional, String, str, String

        Returns

        String : The identifier of the new object if successful.
        Null : If not successful, or on error.

        """

        return self._ApplyTypes_(321, 1, (12, 0), ((8197, 0), (8, 0), (8, 0),), u'AddLeader', None, _utils.flatten(points), view, text)

    def current_dim_style(self, dim_style):
        """

        Returns or changes the current default dimension style.

        Parameters

        DimStyle : Optional, String, str, String

        Returns

        String : If a dimension style is not specified, the name of the current dimension style if successful.
        String : If a dimension style is specified, the name of the previous current dimension style if successful.
        Null : If not successful, or on error.

        """

        return self._ApplyTypes_(453, 1, (12, 0), ((8, 0),), u'CurrentDimStyle', None, dim_style)

    def delete_dim_style(self, dim_style):
        """

        Removes an existing dimension style from the document.  The dimension style to be removed cannot be the reference by any dimension objects.

        Parameters

        DimStyle : Required, String, str, String

        Returns

        String : The name of the deleted dimension style if successful.
        Null : If not successful, or on error.

        """

        return self._ApplyTypes_(456, 1, (12, 0), ((8, 0),), u'DeleteDimStyle', None, dim_style)

    def dim_scale(self, scale):
        """

        Returns or changes the document's global dimension scale.

        Parameters

        Scale : Optional, Number, dbl, Double

        Returns

        Number : If a dimension scale is not specified, the current dimension scale if successful.
        Number : If a dimension scale is specified, the previous dimension scale if successful.
        Null : If not successful, or on error.

        """

        return self._ApplyTypes_(460, 1, (12, 0), ((5, 0),), u'DimScale', None, scale)

    def dim_style_angle_precision(self, dim_style, precision):
        """

        Returns or changes the angle display precision of a dimension style.

        Parameters

        DimStyle : Required, String, str, String
        Precision : Optional, Number, int, Integer

        Returns

        Number : If a precision is not specified, the current angle precision if successful.
        Number : If a precision is specified, the previous angle precision if successful.
        Null : If not successful, or on error.

        """

        return self._ApplyTypes_(464, 1, (12, 0), ((8, 0), (2, 0),), u'DimStyleAnglePrecision', None, dim_style, precision)

    def dim_style_arrow_size(self, dim_style, size):
        """

        Returns or changes the arrow size of a dimension style.

        Parameters

        DimStyle : Required, String, str, String
        Size : Optional, Number, dbl, Double

        Returns

        Number : If a size value is not specified, the current arrow size if successful.
        Number : If a size value is specified, the previous arrow size if successful.
        Null : If not successful, or on error.

        """

        return self._ApplyTypes_(468, 1, (12, 0), ((8, 0), (5, 0),), u'DimStyleArrowSize', None, dim_style, size)

    def dim_style_count(self):
        """

        Returns the number of dimension styles in the document.

        No parameters

        Returns

        Number : The number of dimension styles in the document.

        """

        return self._ApplyTypes_(451, 1, (12, 0), (,), u'DimStyleCount', None, )

    def dim_style_extension(self, dim_style, extension):
        """

        Returns or changes the extension line extension of a dimension style.

        Parameters

        DimStyle : Required, String, str, String
        Extension : Optional, Number, dbl, Double

        Returns

        Number : If an extension is not specified, the current extension line extension if successful.
        Number : If an extension is specified, the previous extension line extension if successful.
        Null : If not successful, or on error.

        """

        return self._ApplyTypes_(466, 1, (12, 0), ((8, 0), (5, 0),), u'DimStyleExtension', None, dim_style, extension)

    def dim_style_font(self, dim_style, font):
        """

        Returns or changes the font used by a dimension style.

        Parameters

        DimStyle : Required, String, str, String
        Font : Optional, String, str, String

        Returns

        String : If a font is not specified, the current font if successful.
        String : If a font is specified, the previous font if successful.
        Null : If not successful, or on error.

        """

        return self._ApplyTypes_(462, 1, (12, 0), ((8, 0), (8, 0),), u'DimStyleFont', None, dim_style, font)

    def dim_style_leader_arrow_size(self, dim_style, size):
        """

        Returns or changes the leader arrow size of a dimension style.

        Parameters

        DimStyle : Required, String, str, String
        Size : Optional, Number, dbl, Double

        Returns

        Number : If a size value is not specified, the current leader arrow size if successful.
        Number : If a size value is specified, the previous leader arrow size if successful.
        Null : If not successful, or on error.

        """

        return self._ApplyTypes_(704, 1, (12, 0), ((8, 0), (5, 0),), u'DimStyleLeaderArrowSize', None, dim_style, size)

    def dim_style_linear_precision(self, dim_style, precision):
        """

        Returns or changes the linear display precision of a dimension style.

        Parameters

        DimStyle : Required, String, str, String
        Precision : Optional, Number, int, Integer

        Returns

        Number : If a precision is not specified, the current linear precision if successful.
        Number : If ar precision is specified, the previous linear precision if successful.
        Null : If not successful, or on error.

        """

        return self._ApplyTypes_(463, 1, (12, 0), ((8, 0), (2, 0),), u'DimStyleLinearPrecision', None, dim_style, precision)

    def dim_style_names(self, sort):
        """

        Returns the names of all dimension styles in the document.

        Parameters

        Sort : Optional, Boolean, bln, Boolean

        Returns

        Array : An array of dimension style names if successful.
        Null : If not successful, or on error.

        """

        return self._ApplyTypes_(452, 1, (12, 0), ((11, 0),), u'DimStyleNames', None, sort)

    def dim_style_number_format(self, dim_style, format):
        """

        Returns or changes the number display format of a dimension style.

        Parameters

        DimStyle : Required, String, str, String
        Format : Optional, Number, int, Integer

        Returns

        Number : If a format is not specified, the current number display format if successful.
        Number : If a format is specified, the previous number display format if successful.
        Null : If not successful, or on error.

        """

        return self._ApplyTypes_(459, 1, (12, 0), ((8, 0), (2, 0),), u'DimStyleNumberFormat', None, dim_style, format)

    def dim_style_offset(self, dim_style, offset):
        """

        Returns or changes the extension line offset of a dimension style.

        Parameters

        DimStyle : Required, String, str, String
        Offset : Optional, Number, dbl, Double

        Returns

        Number : If an offset is not specified, the current extension line offset if successful.
        Number : If an offset is specified, the previous extension line offset if successful.
        Null : If not successful, or on error.

        """

        return self._ApplyTypes_(467, 1, (12, 0), ((8, 0), (5, 0),), u'DimStyleOffset', None, dim_style, offset)

    def dim_style_text_alignment(self, dim_style, alignment):
        """

        Returns or changes the text alignment mode of a dimension style.

        Parameters

        DimStyle : Required, String, str, String
        Alignment : Optional, Number, int, Integer

        Returns

        Number : If a mode is not specified, the current text alignment mode  if successful.
        Number : If a mode is specified, the previous text alignment mode if successful.
        Null : If not successful, or on error.

        """

        return self._ApplyTypes_(461, 1, (12, 0), ((8, 0), (2, 0),), u'DimStyleTextAlignment', None, dim_style, alignment)

    def dim_style_text_gap(self, dim_style, gap):
        """

        Returns or changes the text gap used by a dimension style.

        Parameters

        DimStyle : Required, String, str, String
        Gap : Optional, Number, dbl, Double

        Returns

        Number : If a gap is not specified, the current text gap if successful.
        Number : If a gap is specified, the previous text gap if successful.
        Null : If not successful, or on error.

        """

        return self._ApplyTypes_(741, 1, (12, 0), ((8, 0), (5, 0),), u'DimStyleTextGap', None, dim_style, gap)

    def dim_style_text_height(self, dim_style, height):
        """

        Returns or changes the text height used by a dimension style.

        Parameters

        DimStyle : Required, String, str, String
        Height : Optional, Number, dbl, Double

        Returns

        Number : If a height is not specified, the current text height if successful.
        Number : If a height is specified, the previous text height if successful.
        Null : If not successful, or on error.

        """

        return self._ApplyTypes_(465, 1, (12, 0), ((8, 0), (5, 0),), u'DimStyleTextHeight', None, dim_style, height)

    def dimension_style(self, object, style):
        """

        Returns or modifies the dimension style of a dimension object.

        Parameters

        Object : Required, String, str, String
        Style : Optional, String, str, String

        Returns

        String : If strStyle is not specified, then the object's current dimension style if successful.
        String : If strStyle is specified, then the object's previous dimension style if successful.
        Null : On error.

        """

        return self._ApplyTypes_(703, 1, (12, 0), ((8, 0), (8, 0),), u'DimensionStyle', None, object, style)

    def dimension_text(self, object):
        """

        Returns the text displayed by a dimension object.

        Parameters

        Object : Required, String, str, String

        Returns

        String : The dimension text if successful.
        Null : On error.

        """

        return self._ApplyTypes_(469, 1, (12, 0), ((8, 0),), u'DimensionText', None, object)

    def dimension_user_text(self, object, user_text):
        """

        Returns or modifies the user text string of a dimension object. The user text is the string that gets printed when the dimension is drawn. If it contains the token "<>", then the token is replaced with the measured value of the dimension, formatted according to the dimension style settings. Note,  "<>" is the default user text string for linear dimensions.

        Parameters

        Object : Required, String, str, String
        UserText : Optional, String, str, String

        Returns

        String : If strUserText is not specified, then the current user text string if successful.
        String : If strUserText is specified, then the previous user text string if successful.
        Null : On error.

        """

        return self._ApplyTypes_(563, 1, (12, 0), ((8, 0), (8, 0),), u'DimensionUserText', None, object, user_text)

    def dimension_value(self, object):
        """

        Returns the value of a dimension object.

        Parameters

        Object : Required, String, str, String

        Returns

        Number : The value of the dimension successful.
        Null : On error.

        """

        return self._ApplyTypes_(568, 1, (12, 0), ((8, 0),), u'DimensionValue', None, object)

    def is_aligned_dimension(self, object):
        """

        Verifies an object is an aligned dimension object.

        Parameters

        Object : Required, String, str, String

        Returns

        Boolean : True if successful, otherwise False.
        Null : On error.

        """

        return self._ApplyTypes_(566, 1, (12, 0), ((8, 0),), u'IsAlignedDimension', None, object)

    def is_angular_dimension(self, object):
        """

        Verifies an object is an angular dimension object.

        Parameters

        Object : Required, String, str, String

        Returns

        Boolean : True if successful, otherwise False.
        Null : On error.

        """

        return self._ApplyTypes_(338, 1, (12, 0), ((8, 0),), u'IsAngularDimension', None, object)

    def is_diameter_dimension(self, object):
        """

        Verifies an object is a diameter dimension object.

        Parameters

        Object : Required, String, str, String

        Returns

        Boolean : True if successful, otherwise False.
        Null : On error.

        """

        return self._ApplyTypes_(565, 1, (12, 0), ((8, 0),), u'IsDiameterDimension', None, object)

    def is_dim_style(self, dim_style):
        """

        Verifies the existence of a dimension style in the document.

        Parameters

        DimStyle : Required, String, str, String

        Returns

        Null : On error.

        """

        return self._ApplyTypes_(454, 1, (12, 0), ((8, 0),), u'IsDimStyle', None, dim_style)

    def is_dim_style_reference(self, dim_style):
        """

        Verifies that an existing dimension style is from a reference file.

        Parameters

        DimStyle : Required, String, str, String

        Returns

        Null : On error.

        """

        return self._ApplyTypes_(457, 1, (12, 0), ((8, 0),), u'IsDimStyleReference', None, dim_style)

    def is_dimension(self, object):
        """

        Verifies an object is a dimension object.

        Parameters

        Object : Required, String, str, String

        Returns

        Boolean : True if successful, otherwise False.
        Null : On error.

        """

        return self._ApplyTypes_(564, 1, (12, 0), ((8, 0),), u'IsDimension', None, object)

    def is_leader(self, object):
        """

        Verifies an object is a dimension leader object.

        Parameters

        Object : Required, String, str, String

        Returns

        Boolean : True if successful, otherwise False.
        Null : On error.

        """

        return self._ApplyTypes_(337, 1, (12, 0), ((8, 0),), u'IsLeader', None, object)

    def is_linear_dimension(self, object):
        """

        Verifies an object is a linear dimension object.

        Parameters

        Object : Required, String, str, String

        Returns

        Boolean : True if successful, otherwise False.
        Null : On error.

        """

        return self._ApplyTypes_(339, 1, (12, 0), ((8, 0),), u'IsLinearDimension', None, object)

    def is_ordinate_dimension(self, object):
        """

        Verifies an object is an ordinate dimension object.

        Parameters

        Object : Required, String, str, String

        Returns

        Boolean : True if successful, otherwise False.
        Null : On error.

        """

        return self._ApplyTypes_(659, 1, (12, 0), ((8, 0),), u'IsOrdinateDimension', None, object)

    def is_radial_dimension(self, object):
        """

        Verifies an object is a radial dimension object.

        Parameters

        Object : Required, String, str, String

        Returns

        Boolean : True if successful, otherwise False.
        Null : On error.

        """

        return self._ApplyTypes_(340, 1, (12, 0), ((8, 0),), u'IsRadialDimension', None, object)

    def leader_text(self, object, text):
        """

        Returns or modifies the text string of a dimension leader object.

        Parameters

        Object : Required, String, str, String
        Text : Optional, String, str, String

        Returns

        String : If strText is not specified, then the current text string if successful.
        String : If strText is specified, then the previous text string if successful.
        Null : On error.

        """

        return self._ApplyTypes_(895, 1, (12, 0), ((8, 0), (8, 0),), u'LeaderText', None, object, text)

    def rename_dim_style(self, old_style, new_style):
        """

        Renames an existing dimension style.

        Parameters

        OldStyle : Required, String, str, String
        NewStyle : Required, String, str, String

        Returns

        String : The new dimension style name if successful.
        Null : If not successful, or on error.

        """

        return self._ApplyTypes_(458, 1, (12, 0), ((8, 0), (8, 0),), u'RenameDimStyle', None, old_style, new_style)

