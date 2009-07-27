curve_brep_intersect = {
    "input_folder_name": "Curve_Methods",
    "input_file_name": "CurveBrepIntersect",
    "output_package_name": "curve",
    "output_module_name": "curve_brep_intersect",

    "doc_html": """
        Intersects a curve object with a brep object. Note, unlike the CurveSurfaceIntersection function, this function works on trimmed surfaces.
    """,

    "syntax_html": {
        0: ("strCurve", "strBrep", "dblTolerance"),
    },

    "params_html": {
        0: {
            "name": "strCurve",
            "py_name": "curve",
            "opt_or_req": "Required",
            "type": "String",
            "name_prefix": "str",
            "name_main": "Curve",
            "doc": """
        The curve object's identifier.
            """
        },
        1: {
            "name": "strBrep",
            "py_name": "brep",
            "opt_or_req": "Required",
            "type": "String",
            "name_prefix": "str",
            "name_main": "Brep",
            "doc": """
        The brep object's identifier.
            """
        },
        2: {
            "name": "dblTolerance",
            "py_name": "tolerance",
            "opt_or_req": "Optional",
            "type": "Number",
            "name_prefix": "dbl",
            "name_main": "Tolerance",
            "doc": """
        The distance tolerance at segment midpoints.  If omitted, the current absolute tolerance is used..
            """
        },
    },

    "returns_html": {
        0: {
            "type": "array",
            "doc": "An array of strings identifying the newly created intersection curve and point objects if successful."
        },
        1: {
            "type": "null",
            "doc": "If not successful, or on error."
        },
    },

    "id_com": 545,

    "params_com": {
        0: {
            "name": "vaCurve",
            "opt_or_req": "Required",
            "type": "tagVARIANT",
        },
        1: {
            "name": "vaBrep",
            "opt_or_req": "Required",
            "type": "tagVARIANT",
        },
        2: {
            "name": "vaTol",
            "opt_or_req": "Optional",
            "type": "tagVARIANT",
        },
    },

    "returns_com": "tagVARIANT",

}

