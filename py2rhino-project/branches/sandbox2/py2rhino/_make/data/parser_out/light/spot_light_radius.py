spot_light_radius = {
    "input_folder_name": "Light_Methods",
    "input_file_name": "SpotLightRadius",
    "output_package_name": "light",
    "output_module_name": "spot_light_radius",

    "doc_html": """
        Returns or changes the radius of a spot light.
    """,

    "syntax_html": {
        0: ("strObject", "dblRadius"),
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
            "name": "dblRadius",
            "py_name": "radius",
            "opt_or_req": "Optional",
            "type": "Number",
            "name_prefix": "dbl",
            "name_main": "Radius",
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

