is_layer_selectable = {
    "input_folder_name": "Layer_Methods",
    "input_file_name": "IsLayerSelectable",
    "output_package_name": "layer",
    "output_module_name": "is_layer_selectable",

    "doc_html": """
        Verifies that an existing layer is selectable (normal and reference).
    """,

    "syntax_html": """
        Rhino.IsLayerSelectable (strLayer)
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
    },

    "returns_html": {
        0: {
            "type": "null",
            "doc": "On error."
        },
    },

    "id_com": 19,

    "params_com": {
        0: {
            "name": "vaName",
            "opt_or_req": "Required",
            "type": "tagVARIANT",
        },
    },

    "returns_com": "tagVARIANT",

}

