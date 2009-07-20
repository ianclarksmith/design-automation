add_clipping_plane = {
    "input_folder_name": "Geometry_Methods",
    "input_file_name": "AddClippingPlane",
    "output_package_name": "geometry",
    "output_module_name": "add_clipping_plane",

    "doc_html": """
        Creates a clipping plane. A clipping plane is a plane for visibly clipping away geometry in a specific view. Note, clipping planes are infinite.
    """,

    "syntax_html": """
        Rhino.AddClippingPlane (arrPlane, dblDU, dblDV, [strView])
    """,

    "params_html": {
        0: {
            "name": "Plane",
            "opt_or_req": "Required",
            "type": "Array",
            "type_string": "arr",
            "doc": """
        The plane.
            """
        },
        1: {
            "name": "DU",
            "opt_or_req": "Required",
            "type": "Number",
            "type_string": "dbl",
            "doc": """
        The magnitude in the U direction.
            """
        },
        2: {
            "name": "DV",
            "opt_or_req": "Required",
            "type": "Number",
            "type_string": "dbl",
            "doc": """
        The magnitude in the V direction.
            """
        },
        3: {
            "name": "View",
            "opt_or_req": "Optional",
            "type": "String",
            "type_string": "str",
            "doc": """
        The title of the view to clip.  If omitted, the current active view is used.
            """
        },
        4: {
            "name": "Views",
            "opt_or_req": "Optional",
            "type": "Array",
            "type_string": "arr",
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

