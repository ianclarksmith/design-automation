spot_light_hardness = {
    "module_name": "light",
    "class_name": "Light",
    "method_name": "spot_light_hardness",

    "doc_html": """
        Returns or changes the hardness of a spot light.  Spotlight hardness controls the fully illuminated region.
    """,

    "syntax_html": """
        Rhino.SpotLightHardness (strObject [, dblHardness])
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
            "name": "Hardness",
            "opt_or_req": "Optional",
            "type": "Number",
            "type_string": "dbl",
            "doc": """
        The new hardness value.  A spot light's hardness values ranges from 0.0 to 1.0.  If omitted, the current hardness value is returned.
            """
        },
    },

    "returns_html": {
        0: {
            "type": "number",
            "doc": "If dblHardness is not specified, then  the current hardness value if successful."
        },
        1: {
            "type": "number",
            "doc": "If dblHardness is specified, then the previous hardness value if successful."
        },
        2: {
            "type": "null",
            "doc": "If not successful, or on error."
        },
    },

    "id_com": 171,

    "params_com": {
        0: {
            "name": "vaLight",
            "opt_or_req": "Required",
            "type": "tagVARIANT",
        },
        1: {
            "name": "vaValue",
            "opt_or_req": "Optional",
            "type": "tagVARIANT",
        },
    },

    "returns_com": "tagVARIANT",

}

