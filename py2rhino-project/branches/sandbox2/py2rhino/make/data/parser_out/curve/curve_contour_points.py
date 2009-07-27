curve_contour_points = {
    "input_folder_name": "Curve_Methods",
    "input_file_name": "CurveContourPoints",
    "output_package_name": "curve",
    "output_module_name": "curve_contour_points",

    "doc_html": """
        Returns the 3-D point locations calculated by contouring a curve object.
    """,

    "syntax_html": {
        0: ("strObject", "arrStartPoint", "arrEndPoint", "dblInterval"),
    },

    "params_html": {
        0: {
            "name": "strObject",
            "py_name": "object",
            "opt_or_req": "Required",
            "type": "String",
            "name_prefix": "str",
            "name_main": "Object",
            "doc": """
        The identifier of a curve object.
            """
        },
        1: {
            "name": "arrStartPoint",
            "py_name": "start_point",
            "opt_or_req": "Required",
            "type": "Array",
            "name_prefix": "arr_of_dbl",
            "name_main": "StartPoint",
            "doc": """
        The 3-D starting point of a center line.
            """
        },
        2: {
            "name": "arrEndPoint",
            "py_name": "end_point",
            "opt_or_req": "Required",
            "type": "Array",
            "name_prefix": "arr_of_dbl",
            "name_main": "EndPoint",
            "doc": """
        The 3-D ending point of a center line.
            """
        },
        3: {
            "name": "dblInterval",
            "py_name": "interval",
            "opt_or_req": "Optional",
            "type": "Number",
            "name_prefix": "dbl",
            "name_main": "Interval",
            "doc": """
        The distance between contour curves.  If omitted, the interval will be equal to the diagonal distance of the object's bounding box divided by 50.
            """
        },
    },

    "returns_html": {
        0: {
            "type": "array",
            "doc": "An array of 3-D points, one for each contour, if successful."
        },
        1: {
            "type": "null",
            "doc": "If not successful, or on error."
        },
    },

    "id_com": 748,

    "params_com": {
        0: {
            "name": "vaObject",
            "opt_or_req": "Required",
            "type": "tagVARIANT",
        },
        1: {
            "name": "vaBase",
            "opt_or_req": "Required",
            "type": "tagVARIANT",
        },
        2: {
            "name": "vaEnd",
            "opt_or_req": "Required",
            "type": "tagVARIANT",
        },
        3: {
            "name": "vaInterval",
            "opt_or_req": "Optional",
            "type": "tagVARIANT",
        },
    },

    "returns_com": "tagVARIANT",

}

