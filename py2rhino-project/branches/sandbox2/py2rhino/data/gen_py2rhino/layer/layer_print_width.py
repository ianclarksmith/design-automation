layer_print_width = {
    "input_folder_name": "Layer_Methods",
    "input_file_name": "LayerPrintWidth",
    "output_package_name": "layer",
    "output_module_name": "layer_print_width",

    "doc_html": """
        Returns or changes the print width of a layer. Print width is specified in millimeters. A print width of 0.0 denotes the "default" print width.
    """,

    "syntax_html": {
        0: ("strLayer", "dblWidth"),
    },

    "params_html": {
        0: {
            "name": "strLayer",
            "py_name": "layer",
            "opt_or_req": "Required",
            "type": "String",
            "name_prefix": "str",
            "name_main": "Layer",
            "doc": """
        The name of an existing layer.
            """
        },
        1: {
            "name": "dblWidth",
            "py_name": "width",
            "opt_or_req": "Optional",
            "type": "Number",
            "name_prefix": "dbl",
            "name_main": "Width",
            "doc": """
        The new layer print width in millimeters.
            """
        },
    },

    "returns_html": {
        0: {
            "type": "number",
            "doc": "If a layer print width is not specified,  the current layer print width if successful."
        },
        1: {
            "type": "number",
            "doc": "If a layer print width is specified, the previous layer print width if successful."
        },
        2: {
            "type": "null",
            "doc": "If not successful, or on error."
        },
    },

    "id_com": 604,

    "params_com": {
        0: {
            "name": "vaLayer",
            "opt_or_req": "Required",
            "type": "tagVARIANT",
        },
        1: {
            "name": "vaPrintWidth",
            "opt_or_req": "Optional",
            "type": "tagVARIANT",
        },
    },

    "returns_com": "tagVARIANT",

}

