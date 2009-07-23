extrude_curve = {
    "input_folder_name": "Surface_and_Polysurface_Methods",
    "input_file_name": "ExtrudeCurve",
    "output_package_name": "surface_and_polysurface",
    "output_module_name": "extrude_curve",

    "doc_html": """
        Creates a surface by extruding a curve along a path curve.
    """,

    "syntax_html": {
        0: ("strCurve", "strPath"),
    },

    "params_html": {
        0: {
            "name": "strCurve",
            "opt_or_req": "Required",
            "type": "String",
            "name_prefix": "str",
            "name_main": "Curve",
            "doc": """
        The identifier of the curve object to extrude.
            """
        },
        1: {
            "name": "strPath",
            "opt_or_req": "Required",
            "type": "String",
            "name_prefix": "str",
            "name_main": "Path",
            "doc": """
        The identifier of the path curve.
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

    "id_com": 538,

    "params_com": {
        0: {
            "name": "vaCurve",
            "opt_or_req": "Required",
            "type": "tagVARIANT",
        },
        1: {
            "name": "vaPath",
            "opt_or_req": "Required",
            "type": "tagVARIANT",
        },
    },

    "returns_com": "tagVARIANT",

}

