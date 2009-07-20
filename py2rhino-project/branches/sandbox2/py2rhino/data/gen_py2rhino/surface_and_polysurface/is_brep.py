is_brep = {
    "module_name": "surface_and_polysurface",
    "class_name": "SurfaceAndPolysurface",
    "method_name": "is_brep",

    "doc_html": """
        Verifies an object is a Brep, or a boundary representation model, object.
    """,

    "syntax_html": """
        Rhino.IsBrep (strObject)
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

    "id_com": 206,

    "params_com": {
        0: {
            "name": "vaObject",
            "opt_or_req": "Required",
            "type": "tagVARIANT",
        },
    },

    "returns_com": "tagVARIANT",

}

