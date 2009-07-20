layer_print_color = {
    "input_folder_name": "Layer_Methods",
    "input_file_name": "LayerPrintColor",
    "output_package_name": "layer",
    "output_module_name": "layer_print_color",

    "doc_html": """
        Returns or changes the print color of a layer. Layer print colors are represented as RGB colors. An RGB color specifies the relative intensity of red, green, and blue to cause a specific color to be printed.
    """,

    "syntax_html": """
        Rhino.LayerPrintColor (strLayer [, lngColor])
    """,

    "params_html": {
        0: {
            "name": "Layer",
            "opt_or_req": "Required",
            "type": "String",
            "type_string": "str",
            "doc": """
        The name of an existing layer.
            """
        },
        1: {
            "name": "Color",
            "opt_or_req": "Optional",
            "type": "Number",
            "type_string": "lng",
            "doc": """
        The new print color value.  If omitted, the current layer print color is returned.
            """
        },
    },

    "returns_html": {
        0: {
            "type": "number",
            "doc": "If a layer print color is not specified,  the current layer print color if successful."
        },
        1: {
            "type": "number",
            "doc": "If a layer print color is specified, the previous layer print color if successful."
        },
        2: {
            "type": "null",
            "doc": "If not successful, or on error."
        },
    },

    "id_com": 603,

    "params_com": {
        0: {
            "name": "vaLayer",
            "opt_or_req": "Required",
            "type": "tagVARIANT",
        },
        1: {
            "name": "vaPrintColor",
            "opt_or_req": "Optional",
            "type": "tagVARIANT",
        },
    },

    "returns_com": "tagVARIANT",

}

