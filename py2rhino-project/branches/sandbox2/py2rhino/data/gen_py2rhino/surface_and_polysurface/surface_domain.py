surface_domain = {
    "module_name": "surface_and_polysurface",
    "class_name": "SurfaceAndPolysurface",
    "method_name": "surface_domain",

    "doc_html": """
        Returns the domain of a  surface object in the specified direction.
    """,

    "syntax_html": """
        Rhino.SurfaceDomain (strObject, intDirection)
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
            "name": "Direction",
            "opt_or_req": "Required",
            "type": "Number",
            "type_string": "int",
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

