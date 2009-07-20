add_nurbs_surface = {
    "module_name": "surface_and_polysurface",
    "class_name": "SurfaceAndPolysurface",
    "method_name": "add_nurbs_surface",

    "doc_html": """
        Adds a NURBS surface object to the document.
    """,

    "syntax_html": """
        Rhino.AddNurbsSurface (arrPointCount, arrPoints, arrKnotU, arrKnotV, arrDegree [, arrWeights])
    """,

    "params_html": {
        0: {
            "name": "PointCount",
            "opt_or_req": "Required",
            "type": "Array",
            "type_string": "arr",
            "doc": """
        The number of control points in the U and V directions.
            """
        },
        1: {
            "name": "Points",
            "opt_or_req": "Required",
            "type": "Array",
            "type_string": "arr",
            "doc": """
        An array of 3-D control points.
            """
        },
        2: {
            "name": "KnotsU",
            "opt_or_req": "Required",
            "type": "Array",
            "type_string": "arr",
            "doc": """
        The knot values for the surface in the U direction.  The array must contain arrPointCount(0) + arrDegree(0) - 1 elements.
            """
        },
        3: {
            "name": "KnotsU",
            "opt_or_req": "Required",
            "type": "Array",
            "type_string": "arr",
            "doc": """
        The knot values for the surface in the U direction.  The array must contain arrPointCount(1) + arrDegree(1) - 1 elements.
            """
        },
        4: {
            "name": "Degree",
            "opt_or_req": "Required",
            "type": "Array",
            "type_string": "arr",
            "doc": """
        The degree of the surface in the U and V directions.  The degree in each direction must be greater than or equal to one (1).
            """
        },
        5: {
            "name": "Weights",
            "opt_or_req": "Required",
            "type": "Array",
            "type_string": "arr",
            "doc": """
        The weight values for the surface.  The number of elements in arrWeights equal the number of elements in arrPoints.  Weight values must be greater than zero (0).
            """
        },
    },

    "returns_html": {
        0: {
            "type": "string",
            "doc": "The identifier of the new object if successful."
        },
        1: {
            "type": "null",
            "doc": "If not successful, or on error."
        },
    },

    "id_com": 435,

    "params_com": {
        0: {
            "name": "vaPointCount",
            "opt_or_req": "Required",
            "type": "tagVARIANT",
        },
        1: {
            "name": "vaPoints",
            "opt_or_req": "Required",
            "type": "tagVARIANT",
        },
        2: {
            "name": "vaKnotsU",
            "opt_or_req": "Required",
            "type": "tagVARIANT",
        },
        3: {
            "name": "vaKnotsV",
            "opt_or_req": "Required",
            "type": "tagVARIANT",
        },
        4: {
            "name": "vaDegree",
            "opt_or_req": "Required",
            "type": "tagVARIANT",
        },
        5: {
            "name": "vaWeights",
            "opt_or_req": "Optional",
            "type": "tagVARIANT",
        },
    },

    "returns_com": "tagVARIANT",

}

