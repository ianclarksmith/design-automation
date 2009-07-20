layer_print_width = {
    "module_name": "layer",
    "class_name": "Layer",
    "method_name": "layer_print_width",

    "doc_html": """
        Returns or changes the print width of a layer. Print width is specified in millimeters. A print width of 0.0 denotes the "default" print width.
    """,

    "syntax_html": """
        Rhino.LayerPrintWidth (strLayer [, dblWidth])
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
            "name": "Width",
            "opt_or_req": "Optional",
            "type": "Number",
            "type_string": "dbl",
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

