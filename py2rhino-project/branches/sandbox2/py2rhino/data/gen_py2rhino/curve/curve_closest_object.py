curve_closest_object = {
    "input_folder_name": "Curve_Methods",
    "input_file_name": "CurveClosestObject",
    "output_package_name": "curve",
    "output_module_name": "curve_closest_object",

    "doc_html": """
        Returns the 3-D point locations on two objects where they are closest to each other.  Note, this function provides similar functionality to that of Rhino's ClosestPt command when used with the Object option.
    """,

    "syntax_html": {
        0: ("strCurve", "strObject"),
        1: ("strCurve", "arrObjects"),
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
        The identifier of the curve object to test.
            """
        },
        1: {
            "name": "arrObjects",
            "py_name": "objects",
            "opt_or_req": "Required",
            "type": "Array",
            "name_prefix": "arr_of_???",
            "name_main": "Objects",
            "doc": """
        The identifiers of one or more point cloud, curve, surface, or polysurface to test against.
            """
        },
    },

    "returns_html": {
        0: {
            "type": "array",
            "doc": "An array containing the results of the closest point calculation if successful.  The elements of the array are as follows:"
        },
        1: {
            "type": "string",
            "doc": "The identifier of the closest object."
        },
        2: {
            "type": "array",
            "doc": "The 3-D point that is closest to the closest object."
        },
        3: {
            "type": "array",
            "doc": "The 3-D point that is closest to the test curve."
        },
        4: {
            "type": "null",
            "doc": "If not successful, or on error."
        },
    },

    "id_com": 870,

    "params_com": {
        0: {
            "name": "vaCurve",
            "opt_or_req": "Required",
            "type": "tagVARIANT",
        },
        1: {
            "name": "vaObjects",
            "opt_or_req": "Required",
            "type": "tagVARIANT",
        },
    },

    "returns_com": "tagVARIANT",

}

