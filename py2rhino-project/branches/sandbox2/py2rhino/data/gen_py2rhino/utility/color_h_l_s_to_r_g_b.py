color_h_l_s_to_r_g_b = {
    "input_folder_name": "Utility_Methods",
    "input_file_name": "ColorHLSToRGB",
    "output_package_name": "utility",
    "output_module_name": "color_h_l_s_to_r_g_b",

    "doc_html": """
        Converts colors from hue-luminance-saturation (HLS) to red-green-blue format.
    """,

    "syntax_html": """
        Rhino.ColorHLSToRGB (lngRGB)
    """,

    "params_html": {
        0: {
            "name": "RGB",
            "opt_or_req": "Required",
            "type": "Array",
            "type_string": "lng",
            "doc": """
        The HLS color value.
            """
        },
    },

    "returns_html": {
        0: {
            "type": "number",
            "doc": "The RGB color value if successful."
        },
        1: {
            "type": "null",
            "doc": "If not successful or on error."
        },
    },

    "id_com": 877,

    "params_com": {
        0: {
            "name": "vaUpperBound",
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

