spot_light_radius = {
    "module_name": "light",
    "class_name": "Light",
    "method_name": "spot_light_radius",

    "doc_html": """
        Returns or changes the radius of a spot light.
    """,

    "syntax_html": """
        Rhino.SpotLightRadius (strObject [, dblRadius])
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
            "name": "Radius",
            "opt_or_req": "Optional",
            "type": "Number",
            "type_string": "dbl",
            "doc": """
        The new radius value.  If omitted, the current radius value is returned.
            """
        },
    },

    "returns_html": {
        0: {
            "type": "number",
            "doc": "If dblRadius is not specified, then the current radius value if successful."
        },
        1: {
            "type": "number",
            "doc": "If dblRadius is specified, then the previous radius value if successful."
        },
        2: {
            "type": "null",
            "doc": "If not successful, or on error."
        },
    },

    "id_com": 584,

    "params_com": {
        0: {
            "name": "vaLight",
            "opt_or_req": "Required",
            "type": "tagVARIANT",
        },
        1: {
            "name": "vaRadius",
            "opt_or_req": "Optional",
            "type": "tagVARIANT",
        },
    },

    "returns_com": "tagVARIANT",

}

