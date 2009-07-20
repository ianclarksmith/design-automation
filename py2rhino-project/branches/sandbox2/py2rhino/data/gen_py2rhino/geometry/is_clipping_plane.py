is_clipping_plane = {
    "input_folder_name": "Geometry_Methods",
    "input_file_name": "IsClippingPlane",
    "output_package_name": "geometry",
    "output_module_name": "is_clipping_plane",

    "doc_html": """
        Verifies that an object is a clipping plane object.
    """,

    "syntax_html": """
        Rhino.IsClippingPlane (strObject)
    """,

    "params_html": {
        0: {
            "name": "Object",
            "opt_or_req": "Required",
            "type": "String",
            "type_string": "str",
            "doc": """
        The object's identifier.
            """
        },
    },

    "returns_html": {
        0: {
            "type": "boolean",
            "doc": "True if successful, otherwise False."
        },
        1: {
            "type": "null",
            "doc": "On error."
        },
    },

    "id_com": 905,

    "params_com": {
        0: {
            "name": "vaObject",
            "opt_or_req": "Required",
            "type": "tagVARIANT",
        },
    },

    "returns_com": "tagVARIANT",

}

