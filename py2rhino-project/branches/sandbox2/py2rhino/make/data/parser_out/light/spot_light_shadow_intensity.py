spot_light_shadow_intensity = {
    "input_folder_name": "Light_Methods",
    "input_file_name": "SpotLightShadowIntensity",
    "output_package_name": "light",
    "output_module_name": "spot_light_shadow_intensity",

    "doc_html": """
        Returns or modifies the shadow intensity of a spot light.
    """,

    "syntax_html": {
        0: ("strObject", "dblIntensity"),
    },

    "params_html": {
        0: {
            "name": "strObject",
            "py_name": "object",
            "opt_or_req": "Required",
            "type": "String",
            "name_prefix": "str",
            "name_main": "Object",
            "doc": """
        The light object's identifier.
            """
        },
        1: {
            "name": "dblIntensity",
            "py_name": "intensity",
            "opt_or_req": "Optional",
            "type": "Number",
            "name_prefix": "dbl",
            "name_main": "Intensity",
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

