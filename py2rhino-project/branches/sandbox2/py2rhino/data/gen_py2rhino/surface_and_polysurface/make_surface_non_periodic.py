make_surface_non_periodic = {
    "module_name": "surface_and_polysurface",
    "class_name": "SurfaceAndPolysurface",
    "method_name": "make_surface_non_periodic",

    "doc_html": """
        Makes a periodic surface non-periodic. Non-periodic surfaces can develop kinks when deformed.
    """,

    "syntax_html": """
        Rhino.MakeSurfaceNonPeriodic (strObject, intDirection [, blnDelete])
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
        The direction to make non-periodic, either 0 = U, or 1 = V.
            """
        },
        2: {
            "name": "Delete",
            "opt_or_req": "Optional",
            "type": "Boolean",
            "type_string": "bln",
            "doc": """
        Delete input surface.  If omitted, the input surface will not be deleted (False).
            """
        },
    },

    "returns_html": {
        0: {
            "type": "string",
            "doc": "If blnDelete is False, the identifier of the new object if successful."
        },
        1: {
            "type": "string",
            "doc": "If blnDelete is True, the identifier of the modified object if successful."
        },
        2: {
            "type": "null",
            "doc": "If not successful, or on error."
        },
    },

    "id_com": 926,

    "params_com": {
        0: {
            "name": "vaObject",
            "opt_or_req": "Required",
            "type": "tagVARIANT",
        },
        1: {
            "name": "vaDir",
            "opt_or_req": "Required",
            "type": "tagVARIANT",
        },
        2: {
            "name": "vaDelete",
            "opt_or_req": "Optional",
            "type": "tagVARIANT",
        },
    },

    "returns_com": "tagVARIANT",

}

