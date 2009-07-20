light_location = {
    "module_name": "light",
    "class_name": "Light",
    "method_name": "light_location",

    "doc_html": """
        Returns or changes the location of a light object.
    """,

    "syntax_html": """
        Rhino.LightLocation (strObject [, arrlocation])
    """,

    "params_html": {
        0: {
            "name": "Object",
            "opt_or_req": "Required",
            "type": "String",
            "type_string": "str",
            "doc": """
        The light object's identifier.
            """
        },
        1: {
            "name": "location",
            "opt_or_req": "Optional",
            "type": "Array",
            "type_string": "arr",
            "doc": """
        The new start point, or location.  If omitted, the location point is returned.
            """
        },
    },

    "returns_html": {
        0: {
            "type": "array",
            "doc": "If a location point is not specified,  the current location if successful."
        },
        1: {
            "type": "array",
            "doc": "If a location point is specified, the previous location point if successful."
        },
        2: {
            "type": "null",
            "doc": "If not successful, or on error."
        },
    },

    "id_com": 490,

    "params_com": {
        0: {
            "name": "vaLight",
            "opt_or_req": "Required",
            "type": "tagVARIANT",
        },
        1: {
            "name": "vaPoint",
            "opt_or_req": "Optional",
            "type": "tagVARIANT",
        },
    },

    "returns_com": "tagVARIANT",

}

