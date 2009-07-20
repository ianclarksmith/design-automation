surface_area = {
    "module_name": "surface_and_polysurface",
    "class_name": "SurfaceAndPolysurface",
    "method_name": "surface_area",

    "doc_html": """
        Calculates the area of a surface or polysurface object. The results are based on the current drawing units.
    """,

    "syntax_html": """
        Rhino.SurfaceArea (strObject)
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
            "type": "array",
            "doc": "An array of area information if successful.  The array will contain the following information:"
        },
        1: {
            "type": "number",
            "doc": "The area."
        },
        2: {
            "type": "number",
            "doc": "The absolute (+/-) error bound for the area."
        },
        3: {
            "type": "null",
            "doc": "If not successful, or on error."
        },
    },

    "id_com": 382,

    "params_com": {
        0: {
            "name": "vaObject",
            "opt_or_req": "Required",
            "type": "tagVARIANT",
        },
    },

    "returns_com": "tagVARIANT",

}

