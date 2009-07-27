color_green_value = {
    "input_folder_name": "Utility_Methods",
    "input_file_name": "ColorGreenValue",
    "output_package_name": "utility",
    "output_module_name": "color_green_value",

    "doc_html": """
        Retrieves an intensity value for the green component of a red-green-blue (RGB) value.
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
            "doc": "The green component if successful."
        },
        1: {
            "type": "null",
            "doc": "If not successful or on error."
        },
    },

    "id_com": 881,

    "params_com": {
        0: {
            "name": "vaRGB",
            "opt_or_req": "Required",
            "type": "tagVARIANT",
        },
    },

    "returns_com": "tagVARIANT",

}

