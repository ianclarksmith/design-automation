expand_layer = {
    "input_folder_name": "Layer_Methods",
    "input_file_name": "ExpandLayer",
    "output_package_name": "layer",
    "output_module_name": "expand_layer",

    "doc_html": """
        Expands a layer. Expanded layers can be viewed in Rhino's Layer dialog.
    """,

    "syntax_html": """
        Rhino.ExpandLayer (strLayer, blnExpand)
    """,

    "params_html": {
        0: {
            "name": "Layer",
            "opt_or_req": "Required",
            "type": "String",
            "type_string": "str",
            "doc": """
        The name of the layer to expand.
            """
        },
        1: {
            "name": "Expand",
            "opt_or_req": "Required",
            "type": "Boolean",
            "type_string": "bln",
            "doc": """
        True to expand, False to collapse.
            """
        },
    },

    "returns_html": {
        0: {
            "type": "boolean",
            "doc": "True or False indicating success or failure."
        },
        1: {
            "type": "null",
            "doc": "On error."
        },
    },

    "id_com": 690,

    "params_com": {
        0: {
            "name": "vaName",
            "opt_or_req": "Required",
            "type": "tagVARIANT",
        },
        1: {
            "name": "vaExpand",
            "opt_or_req": "Required",
            "type": "tagVARIANT",
        },
    },

    "returns_com": "tagVARIANT",

}

