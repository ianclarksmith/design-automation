color_red_value = {
    "input_folder_name": "Utility_Methods",
    "input_file_name": "ColorRedValue",
    "output_package_name": "utility",
    "output_module_name": "color_red_value",

    "doc_html": """
        Retrieves an intensity value for the red component of a red-green-blue (RGB) value.
    """,

    "syntax_html": {
        0: ("lngRGB"),
    },

    "params_html": {
        0: {
            "name": "lngRGB",
            "py_name": "r_g_b",
            "opt_or_req": "Required",
            "type": "Number",
            "name_prefix": "lng",
            "name_main": "RGB",
            "doc": """
        The RGB color value.
            """
        },
    },

    "returns_html": {
        0: {
            "type": "number",
            "doc": "The red component if successful."
        },
        1: {
            "type": "null",
            "doc": "If not successful or on error."
        },
    },

    "id_com": 880,

    "params_com": {
        0: {
            "name": "vaRGB",
            "opt_or_req": "Required",
            "type": "tagVARIANT",
        },
    },

    "returns_com": "tagVARIANT",

}

