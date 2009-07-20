add_loft_srf = {
    "module_name": "surface_and_polysurface",
    "class_name": "SurfaceAndPolysurface",
    "method_name": "add_loft_srf",

    "doc_html": """
        Adds a surface created by lofting curves to the document.
		* This function will not perform any curve sorting. You must pass in curves in the order you want them lofted.
		* This function will not adjust the directions of open curves. Use CurveDirectionsMatch and ReverseCurve to adjust the directions of open curves.
		* This function will not adjust the seams of closed curves. Use CurveSeam to adjust the seam of closed curves.
    """,

    "syntax_html": """
        Rhino.AddLoftSrf (arrObjects [, arrStartPt [, arrEndPt [, intType [, intStyle [, nValue [, blnClosed]]]]]])
    """,

    "params_html": {
        0: {
            "name": "Objects",
            "opt_or_req": "Required",
            "type": "Array",
            "type_string": "arr",
            "doc": """
        An ordered array of strings identifying the curve objects to loft.
            """
        },
        1: {
            "name": "StartPt",
            "opt_or_req": "Optional",
            "type": "Array",
            "type_string": "arr",
            "doc": """
        The starting point of the loft.
            """
        },
        2: {
            "name": "EndPt",
            "opt_or_req": "Optional",
            "type": "Array",
            "type_string": "arr",
            "doc": """
        The ending point of the loft.
            """
        },
        3: {
            "name": "Type",
            "opt_or_req": "Optional",
            "type": "Number",
            "type_string": "int",
            "doc": """
        The type of loft. The default loft type is Normal (0). The possible loft types are as follows:
		Value
		Description
		0
		Normal. Uses chord-length parameterization in the loft direction.
		1
		Loose. The surface is allowed to move away from the original curves to make a smoother surface. The surface control points are created at the same locations as the control points of the loft input curves.
		2
		Straight. The sections between the curves are straight. This is also known as a ruled surface.
		3
		Tight. The surface sticks closely to the original curves. Uses square root of chord-length parameterization in the loft direction.
		4
            """
        },
        4: {
            "name": "Style",
            "opt_or_req": "Optional",
            "type": "Number",
            "type_string": "int",
            "doc": """
        The simplify method of the loft. The default value is None (0). The possible loft simplify methods are as follows:
		Value
		Description
		0
		None. Does not simplify.
		1
		Rebuild. Rebuilds the shape curves before lofting.
		2
            """
        },
        5: {
            "name": "Value",
            "opt_or_req": "Optional",
            "type": "Number",
            "type_string": "int",
            "doc": """
        A value based on the specified intStyle. If intStyle=1 (Rebuild), then nValue is the number of control point used to rebuild. If intstyle=1 is specified and this argument is omitted, then curves will be rebuilt using 10 control points. If intStyle=2 (Refit), then nValue is the tolerance used to rebuild. If intstyle=2 is specified and this argument is omitted, then the document's absolute tolerance us used for refitting.
            """
        },
        6: {
            "name": "Closed",
            "opt_or_req": "Optional",
            "type": "Boolean",
            "type_string": "bln",
            "doc": """
        Creates a closed surface, continuing the surface past the last curve around to the first curve. Available when you have selected three shape curves. The default value is not to create a closed surface (False).
            """
        },
    },

    "returns_html": {
        0: {
            "type": "array",
            "doc": "An array containing the identifiers of the new surface objects if successful."
        },
        1: {
            "type": "null",
            "doc": "If not successful, or on error."
        },
    },

    "id_com": 567,

    "params_com": {
        0: {
            "name": "vaObjects",
            "opt_or_req": "Required",
            "type": "tagVARIANT",
        },
        1: {
            "name": "vaStartPt",
            "opt_or_req": "Optional",
            "type": "tagVARIANT",
        },
        2: {
            "name": "vaEndPt",
            "opt_or_req": "Optional",
            "type": "tagVARIANT",
        },
        3: {
            "name": "vaType",
            "opt_or_req": "Optional",
            "type": "tagVARIANT",
        },
        4: {
            "name": "vaSimplify",
            "opt_or_req": "Optional",
            "type": "tagVARIANT",
        },
        5: {
            "name": "vaVal",
            "opt_or_req": "Optional",
            "type": "tagVARIANT",
        },
        6: {
            "name": "vaClosed",
            "opt_or_req": "Optional",
            "type": "tagVARIANT",
        },
    },

    "returns_com": "tagVARIANT",

}

