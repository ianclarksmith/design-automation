angle = {
    "input_folder_name": "Math_Methods",
    "input_file_name": "Angle",
    "output_package_name": "math",
    "output_module_name": "angle",

    "doc_html": """
        Measures the angle between two points.
    """,

    "syntax_html": {
        0: ("arrPoint1", "arrPoint2", "blnWorld"),
    },

    "params_html": {
        0: {
            "name": "arrPoint1",
            "py_name": "point_1",
            "opt_or_req": "Required",
            "type": "Array",
            "name_prefix": "arr_of_dbl",
            "name_main": "Point1",
            "doc": """
        The first 3-D point.
            """
        },
        1: {
            "name": "arrPoint2",
            "py_name": "point_2",
            "opt_or_req": "Required",
            "type": "Array",
            "name_prefix": "arr_of_dbl",
            "name_main": "Point2",
            "doc": """
        The second 3-D point.
            """
        },
        2: {
            "name": "blnWorld",
            "py_name": "world",
            "opt_or_req": "Optional",
            "type": "Boolean",
            "name_prefix": "bln",
            "name_main": "World",
            "doc": """
        If True, the angle calculation is based on the world coordinate system.  If False, the angle calculation is based on the active construction plane.  The default value is True.
            """
        },
    },

    "returns_html": {
        0: {
            "type": "array",
            "doc": "An array containing the following elements if successful."
        },
        1: {
            "type": "null",
            "doc": "If not successful, or on error."
        },
    },

    "id_com": 115,

    "params_com": {
        0: {
            "name": "vaFrom",
            "opt_or_req": "Required",
            "type": "tagVARIANT",
        },
        1: {
            "name": "vaTo",
            "opt_or_req": "Required",
            "type": "tagVARIANT",
        },
        2: {
            "name": "vaWorld",
            "opt_or_req": "Optional",
            "type": "tagVARIANT",
        },
    },

    "returns_com": "tagVARIANT",

}

