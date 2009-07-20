is_surface_planar = {
    "input_folder_name": "Surface_and_Polysurface_Methods",
    "input_file_name": "IsSurfacePlanar",
    "output_package_name": "surface_and_polysurface",
    "output_module_name": "is_surface_planar",

    "doc_html": """
        Verifies a surface object is planar.
    """,

    "syntax_html": """
        Rhino.IsSurfacePlanar (strObject)
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
        1: {
            "name": "Tolerance",
            "opt_or_req": "Optional",
            "type": "Number",
            "type_string": "dbl",
            "doc": """
        A tolerance to use when checking. The default is to use Rhino's current absolute tolerance.
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

    "id_com": 213,

    "params_com": {
        0: {
            "name": "vaObject",
            "opt_or_req": "Required",
            "type": "tagVARIANT",
        },
        1: {
            "name": "vaTol",
            "opt_or_req": "Optional",
            "type": "tagVARIANT",
        },
    },

    "returns_com": "tagVARIANT",

}

