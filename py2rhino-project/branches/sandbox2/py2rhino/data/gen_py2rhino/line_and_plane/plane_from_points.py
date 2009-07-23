plane_from_points = {
    "input_folder_name": "Line_and_Plane_Methods",
    "input_file_name": "PlaneFromPoints",
    "output_package_name": "line_and_plane",
    "output_module_name": "plane_from_points",

    "doc_html": """
        Creates a plane from three non-colinear points.
    """,

    "syntax_html": {
        0: ("arrOrigin", "arrPointX", "arrPointY"),
    },

    "params_html": {
        0: {
            "name": "arrOrigin",
            "opt_or_req": "Required",
            "type": "Array",
            "name_prefix": "arr_of_dbl",
            "name_main": "Origin",
            "doc": """
        The first point, or origin, of the plane.
            """
        },
        1: {
            "name": "arrPointX",
            "opt_or_req": "Required",
            "type": "Array",
            "name_prefix": "arr_of_dbl",
            "name_main": "PointX",
            "doc": """
        A point on the plane's X axis.
            """
        },
        2: {
            "name": "arrPointY",
            "opt_or_req": "Required",
            "type": "Array",
            "name_prefix": "arr_of_dbl",
            "name_main": "PointY",
            "doc": """
        A point on the plane's Y axis.
            """
        },
    },

    "returns_html": {
        0: {
            "type": "array",
            "doc": "The plane if successful.  The elements of a plane array are as follows:"
        },
        1: {
            "type": "null",
            "doc": "If not successful, or on error."
        },
    },

    "id_com": 649,

    "params_com": {
        0: {
            "name": "vaOrigin",
            "opt_or_req": "Required",
            "type": "tagVARIANT",
        },
        1: {
            "name": "vaX",
            "opt_or_req": "Required",
            "type": "tagVARIANT",
        },
        2: {
            "name": "vaY",
            "opt_or_req": "Required",
            "type": "tagVARIANT",
        },
    },

    "returns_com": "tagVARIANT",

}

