surface_domain = {
    "input_folder_name": "Surface_and_Polysurface_Methods",
    "input_file_name": "SurfaceDomain",
    "output_package_name": "surface_and_polysurface",
    "output_module_name": "surface_domain",

    "doc_html": """
        Returns the domain of a  surface object in the specified direction.
    """,

    "syntax_html": {
        0: ("strObject", "intDirection"),
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
        1: {
            "name": "intDirection",
            "py_name": "direction",
            "opt_or_req": "Required",
            "type": "Number",
            "name_prefix": "int",
            "name_main": "Direction",
            "doc": """
        The direction, either 0 = U, or 1 = V.
            """
        },
    },

    "returns_html": {
        0: {
            "type": "array",
            "doc": "An array containing the domain interval in the specified direction if successful."
        },
        1: {
            "type": "null",
            "doc": "If not successful, or on error."
        },
    },

    "id_com": 217,

    "params_com": {
        0: {
            "name": "vaObject",
            "opt_or_req": "Required",
            "type": "tagVARIANT",
        },
        1: {
            "name": "vaValue",
            "opt_or_req": "Required",
            "type": "tagVARIANT",
        },
    },

    "returns_com": "tagVARIANT",

}

