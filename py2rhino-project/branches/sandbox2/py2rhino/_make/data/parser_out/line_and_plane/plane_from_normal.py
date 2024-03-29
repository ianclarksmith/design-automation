plane_from_normal = {
    "input_folder_name": "Line_and_Plane_Methods",
    "input_file_name": "PlaneFromNormal",
    "output_package_name": "line_and_plane",
    "output_module_name": "plane_from_normal",

    "doc_html": """
        Creates a plane from an origin point and a normal direction vector.
    """,

    "syntax_html": {
        0: ("arrOrigin", "arrNormal"),
    },

    "params_html": {
        0: {
            "name": "arrOrigin",
            "py_name": "origin",
            "opt_or_req": "Required",
            "type": "Array",
            "name_prefix": "arr_of_dbl",
            "name_main": "Origin",
            "doc": """
        A 3-D point identifying the origin of the plane.
            """
        },
        1: {
            "name": "arrNormal",
            "py_name": "normal",
            "opt_or_req": "Required",
            "type": "Array",
            "name_prefix": "arr_of_dbl",
            "name_main": "Normal",
            "doc": """
        A non-zero 3-D vector identifying the normal direction of the plane.
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

    "id_com": 626,

    "params_com": {
        0: {
            "name": "vaOrigin",
            "opt_or_req": "Required",
            "type": "tagVARIANT",
        },
        1: {
            "name": "vaNormal",
            "opt_or_req": "Required",
            "type": "tagVARIANT",
        },
    },

    "returns_com": "tagVARIANT",

}

