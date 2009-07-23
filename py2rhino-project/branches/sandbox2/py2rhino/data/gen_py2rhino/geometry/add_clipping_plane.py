add_clipping_plane = {
    "input_folder_name": "Geometry_Methods",
    "input_file_name": "AddClippingPlane",
    "output_package_name": "geometry",
    "output_module_name": "add_clipping_plane",

    "doc_html": """
        Creates a clipping plane. A clipping plane is a plane for visibly clipping away geometry in a specific view. Note, clipping planes are infinite.
    """,

    "syntax_html": {
        0: ("arrPlane", "dblDU", "dblDV", "strView"),
        1: ("arrPlane", "dblDU", "dblDV", "arrViews"),
    },

    "params_html": {
        0: {
            "name": "arrPlane",
            "py_name": "plane",
            "opt_or_req": "Required",
            "type": "Array",
            "name_prefix": "arr_of_???",
            "name_main": "Plane",
            "doc": """
        The plane.
            """
        },
        1: {
            "name": "dblDU",
            "py_name": "d_u",
            "opt_or_req": "Required",
            "type": "Number",
            "name_prefix": "dbl",
            "name_main": "DU",
            "doc": """
        The magnitude in the U direction.
            """
        },
        2: {
            "name": "dblDV",
            "py_name": "d_v",
            "opt_or_req": "Required",
            "type": "Number",
            "name_prefix": "dbl",
            "name_main": "DV",
            "doc": """
        The magnitude in the V direction.
            """
        },
        3: {
            "name": "arrViews",
            "py_name": "views",
            "opt_or_req": "Optional",
            "type": "Array",
            "name_prefix": "arr_of_???",
            "name_main": "Views",
            "doc": """
        The titles of the views to clip.  If omitted, the current active view is used.
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

    "id_com": 904,

    "params_com": {
        0: {
            "name": "vaPlane",
            "opt_or_req": "Required",
            "type": "tagVARIANT",
        },
        1: {
            "name": "vaDX",
            "opt_or_req": "Required",
            "type": "tagVARIANT",
        },
        2: {
            "name": "vaDY",
            "opt_or_req": "Required",
            "type": "tagVARIANT",
        },
        3: {
            "name": "vaView",
            "opt_or_req": "Optional",
            "type": "tagVARIANT",
        },
    },

    "returns_com": "tagVARIANT",

}

