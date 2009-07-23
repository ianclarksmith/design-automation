layer_color = {
    "input_folder_name": "Layer_Methods",
    "input_file_name": "LayerColor",
    "output_package_name": "layer",
    "output_module_name": "layer_color",

    "doc_html": """
        Returns or changes the color of a layer.  Layer colors are represented as RGB colors.  An RGB color specifies the relative intensity of red, green, and blue to cause a specific color to be displayed.
    """,

    "syntax_html": {
        0: ("strLayer", "lngColor"),
    },

    "params_html": {
        0: {
            "name": "strLayer",
            "opt_or_req": "Required",
            "type": "String",
            "name_prefix": "str",
            "name_main": "Layer",
            "doc": """
        The name of an existing layer.
            """
        },
        1: {
            "name": "lngColor",
            "opt_or_req": "Optional",
            "type": "Number",
            "name_prefix": "lng",
            "name_main": "Color",
            "doc": """
        The new color value.  If omitted, the current layer color is returned.
            """
        },
    },

    "returns_html": {
        0: {
            "type": "number",
            "doc": "If a color value  is not specified,  the current color value if successful."
        },
        1: {
            "type": "number",
            "doc": "If a color value is specified, the previous color value if successful."
        },
        2: {
            "type": "null",
            "doc": "If not successful, or on error."
        },
    },

    "id_com": 11,

    "params_com": {
        0: {
            "name": "vaName",
            "opt_or_req": "Required",
            "type": "tagVARIANT",
        },
        1: {
            "name": "vaColor",
            "opt_or_req": "Optional",
            "type": "tagVARIANT",
        },
    },

    "returns_com": "tagVARIANT",

}

