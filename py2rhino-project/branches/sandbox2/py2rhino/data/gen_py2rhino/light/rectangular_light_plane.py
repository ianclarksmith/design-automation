rectangular_light_plane = {
    "module_name": "light",
    "class_name": "Light",
    "method_name": "rectangular_light_plane",

    "doc_html": """
        Returns the plane of a rectangular light object.
    """,

    "syntax_html": """
        Rhino.RectangularLightPlane (strObject)
    """,

    "params_html": {
        0: {
            "name": "Object",
            "opt_or_req": "Required",
            "type": "String",
            "type_string": "str",
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

