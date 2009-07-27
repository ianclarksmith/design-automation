color_r_g_b_to_h_l_s = {
    "input_folder_name": "Utility_Methods",
    "input_file_name": "ColorRGBToHLS",
    "output_package_name": "utility",
    "output_module_name": "color_r_g_b_to_h_l_s",

    "doc_html": """
        Converts colors from red-green-blue (RGB) to hue-luminance-saturation (HLS) format.
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
            "type": "array",
            "doc": "An array containing the hue, luminance, and saturation values if successful."
        },
        1: {
            "type": "null",
            "doc": "If not successful or on error."
        },
    },

    "id_com": 876,

    "params_com": {
        0: {
            "name": "vaHLS",
            "opt_or_req": "Required",
            "type": "tagVARIANT",
        },
    },

    "returns_com": "tagVARIANT",

}

