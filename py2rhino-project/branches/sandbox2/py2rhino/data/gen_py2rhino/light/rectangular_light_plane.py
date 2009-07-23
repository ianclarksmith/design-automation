rectangular_light_plane = {
    "input_folder_name": "Light_Methods",
    "input_file_name": "RectangularLightPlane",
    "output_package_name": "light",
    "output_module_name": "rectangular_light_plane",

    "doc_html": """
        Returns the plane of a rectangular light object.
    """,

    "syntax_html": {
        0: ("strObject"),
    },

    "params_html": {
        0: {
            "name": "strObject",
            "opt_or_req": "Required",
            "type": "String",
            "name_prefix": "str",
            "name_main": "Object",
            "doc": """
        The light object's identifier.
            """
        },
    },

    "returns_html": {
        0: {
            "type": "array",
            "doc": "The plane if successful.  The elements of a plane array are as follows:"
        },
        1: {
            "type": "array",
            "doc": "The plane's origin (3-D point)."
        },
        2: {
            "type": "array",
            "doc": "The plane's X axis direction (3-D vector)."
        },
        3: {
            "type": "array",
            "doc": "The plane's Y axis direction (3-D vector)."
        },
        4: {
            "type": "array",
            "doc": "The plane's Z axis direction (3-D vector)."
        },
        5: {
            "type": "null",
            "doc": "If not successful, or on error."
        },
    },

    "id_com": 776,

    "params_com": {
        0: {
            "name": "vaLight",
            "opt_or_req": "Required",
            "type": "tagVARIANT",
        },
    },

    "returns_com": "tagVARIANT",

}

