surface_volume = {
    "input_folder_name": "Surface_and_Polysurface_Methods",
    "input_file_name": "SurfaceVolume",
    "output_package_name": "surface_and_polysurface",
    "output_module_name": "surface_volume",

    "doc_html": """
        Calculates the volume of closed surface or polysurface objects.
    """,

    "syntax_html": {
        0: ("strObject"),
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
        The object's identifier.
            """
        },
    },

    "returns_html": {
        0: {
            "type": "array",
            "doc": "An array of volume information if successful.  The array will contain the following information:"
        },
        1: {
            "type": "number",
            "doc": "The volume."
        },
        2: {
            "type": "number",
            "doc": "The absolute (+/-) error bound for the volume."
        },
        3: {
            "type": "null",
            "doc": "If not successful, or on error."
        },
    },

    "id_com": 383,

    "params_com": {
        0: {
            "name": "vaObject",
            "opt_or_req": "Required",
            "type": "tagVARIANT",
        },
    },

    "returns_com": "tagVARIANT",

}

