is_layer_expanded = {
    "input_folder_name": "Layer_Methods",
    "input_file_name": "IsLayerExpanded",
    "output_package_name": "layer",
    "output_module_name": "is_layer_expanded",

    "doc_html": """
        Verifies that a layer is expanded. Expanded layers can be viewed in Rhino's Layer dialog.
    """,

    "syntax_html": """
        Rhino.IsLayerExpanded (strLayer)
    """,

    "params_html": {
        0: {
            "name": "Layer",
            "opt_or_req": "Required",
            "type": "String",
            "type_string": "str",
            "doc": """
        The name of the layer to test.
            """
        },
    },

    "returns_html": {
        0: {
            "type": "boolean",
            "doc": "True if expanded, False if collapsed."
        },
        1: {
            "type": "null",
            "doc": "On error."
        },
    },

    "id_com": 689,

    "params_com": {
        0: {
            "name": "vaName",
            "opt_or_req": "Required",
            "type": "tagVARIANT",
        },
    },

    "returns_com": "tagVARIANT",

}

