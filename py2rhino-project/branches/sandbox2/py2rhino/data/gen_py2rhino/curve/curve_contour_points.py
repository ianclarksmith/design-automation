curve_contour_points = {
    "input_folder_name": "Curve_Methods",
    "input_file_name": "CurveContourPoints",
    "output_package_name": "curve",
    "output_module_name": "curve_contour_points",

    "doc_html": """
        Returns the 3-D point locations calculated by contouring a curve object.
    """,

    "syntax_html": """
        Rhino.CurveContourPoints (strObject, arrStartPoint, arrEndPoint [, dblInterval])
    """,

    "params_html": {
        0: {
            "name": "Object",
            "opt_or_req": "Required",
            "type": "String",
            "type_string": "str",
            "doc": """
        The identifier of a curve object.
            """
        },
        1: {
            "name": "StartPoint",
            "opt_or_req": "Required",
            "type": "Array",
            "type_string": "arr",
            "doc": """
        The 3-D starting point of a center line.
            """
        },
        2: {
            "name": "EndPoint",
            "opt_or_req": "Required",
            "type": "Array",
            "type_string": "arr",
            "doc": """
        The 3-D ending point of a center line.
            """
        },
        3: {
            "name": "Interval",
            "opt_or_req": "Optional",
            "type": "Number",
            "type_string": "dbl",
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

