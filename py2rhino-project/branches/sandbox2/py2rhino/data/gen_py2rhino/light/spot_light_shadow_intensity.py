spot_light_shadow_intensity = {
    "module_name": "light",
    "class_name": "Light",
    "method_name": "spot_light_shadow_intensity",

    "doc_html": """
        Returns or modifies the shadow intensity of a spot light.
    """,

    "syntax_html": """
        Rhino.SpotLightShadowIntensity (strObject [, dblIntensity])
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
            "name": "Intensity",
            "opt_or_req": "Optional",
            "type": "Number",
            "type_string": "dbl",
            "doc": """
        The new shadow intensity.  A spot light's shadow intensity ranges from 0.0 to 1.0.  If set to 0.0, the spot light will cast no shadows.  If set to 1.0, the spot light will cast black shadows.  If omitted, the current shadow intensity is returned.
            """
        },
    },

    "returns_html": {
        0: {
            "type": "number",
            "doc": "If dblIntensity is not specified, then the current shadow intensity if successful."
        },
        1: {
            "type": "number",
            "doc": "If dblIntensity is specified, then the previous shadow intensity if successful."
        },
        2: {
            "type": "null",
            "doc": "If not successful, or on error."
        },
    },

    "id_com": 172,

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

