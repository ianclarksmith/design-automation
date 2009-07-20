extrude_surface = {
    "module_name": "surface_and_polysurface",
    "class_name": "SurfaceAndPolysurface",
    "method_name": "extrude_surface",

    "doc_html": """
        Creates a surface or solid by extruding a straight along a path curve.
    """,

    "syntax_html": """
        Rhino.ExtrudeSurface (strSurface, strCurve [, blnCap])
    """,

    "params_html": {
        0: {
            "name": "Surface",
            "opt_or_req": "Required",
            "type": "String",
            "type_string": "str",
            "doc": """
        The identifier of the surface object to extrude.
            """
        },
        1: {
            "name": "Curve",
            "opt_or_req": "Required",
            "type": "String",
            "type_string": "str",
            "doc": """
        The identifier of the path curve.
            """
        },
        2: {
            "name": "Cap",
            "opt_or_req": "Optional",
            "type": "Boolean",
            "type_string": "bln",
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

