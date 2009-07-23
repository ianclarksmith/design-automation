extrude_surface = {
    "input_folder_name": "Surface_and_Polysurface_Methods",
    "input_file_name": "ExtrudeSurface",
    "output_package_name": "surface_and_polysurface",
    "output_module_name": "extrude_surface",

    "doc_html": """
        Creates a surface or solid by extruding a straight along a path curve.
    """,

    "syntax_html": {
        0: ("strSurface", "strCurve", "blnCap"),
    },

    "params_html": {
        0: {
            "name": "strSurface",
            "opt_or_req": "Required",
            "type": "String",
            "name_prefix": "str",
            "name_main": "Surface",
            "doc": """
        The identifier of the surface object to extrude.
            """
        },
        1: {
            "name": "strCurve",
            "opt_or_req": "Required",
            "type": "String",
            "name_prefix": "str",
            "name_main": "Curve",
            "doc": """
        The identifier of the path curve.
            """
        },
        2: {
            "name": "blnCap",
            "opt_or_req": "Optional",
            "type": "Boolean",
            "name_prefix": "bln",
            "name_main": "Cap",
            "doc": """
        Extrusion is capped at both ends to make a closed polysurface. The default value is True.
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

    "id_com": 541,

    "params_com": {
        0: {
            "name": "vaSurface",
            "opt_or_req": "Required",
            "type": "tagVARIANT",
        },
        1: {
            "name": "vaCurve",
            "opt_or_req": "Required",
            "type": "tagVARIANT",
        },
        2: {
            "name": "vaCap",
            "opt_or_req": "Optional",
            "type": "tagVARIANT",
        },
    },

    "returns_com": "tagVARIANT",

}

