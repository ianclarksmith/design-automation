color_adjust_luma = {
    "input_folder_name": "Utility_Methods",
    "input_file_name": "ColorAdjustLuma",
    "output_package_name": "utility",
    "output_module_name": "color_adjust_luma",

    "doc_html": """
        Changes the luminance of a red-green-blue (RGB) value. Hue and saturation are not affected.
    """,

    "syntax_html": """
        Rhino.ColorAdjustLuma (lngRGB, intLuma [, bScale])
    """,

    "params_html": {
        0: {
            "name": "RGB",
            "opt_or_req": "Required",
            "type": "Number",
            "type_string": "lng",
            "doc": """
        The initial RGB color value.
            """
        },
        1: {
            "name": "Luma",
            "opt_or_req": "Required",
            "type": "Number",
            "type_string": "int",
            "doc": """
        The luminance in units of 0.1 percent of the total range.  For example, a value of intLuma = 50 corresponds to 5 percent of the maximum luminance.
            """
        },
        2: {
            "name": "bScale",
            "opt_or_req": "Optional",
            "type": "Boolean",
            "type_string": "int",
            "doc": """
        If bScale is set to True, intLuma specifies how much to increment or decrement the current luminance.  If bScale is set to FALSE, intLuma specifies the absolute luminance.  The default value is False.
		If bScale is set to TRUE, intLuma can range from -1000 to +1000.
            """
        },
    },

    "returns_html": {
        0: {
            "type": "number",
            "doc": "The modified RGB color value if successful."
        },
        1: {
            "type": "null",
            "doc": "If not successful or on error."
        },
    },

    "id_com": 878,

    "params_com": {
        0: {
            "name": "vaRGB",
            "opt_or_req": "Required",
            "type": "tagVARIANT",
        },
        1: {
            "name": "vaLuma",
            "opt_or_req": "Required",
            "type": "tagVARIANT",
        },
        2: {
            "name": "vaScale",
            "opt_or_req": "Optional",
            "type": "tagVARIANT",
        },
    },

    "returns_com": "tagVARIANT",

}

