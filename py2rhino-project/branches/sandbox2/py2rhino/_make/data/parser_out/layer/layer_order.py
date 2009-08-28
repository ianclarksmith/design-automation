layer_order = {
    "input_folder_name": "Layer_Methods",
    "input_file_name": "LayerOrder",
    "output_package_name": "layer",
    "output_module_name": "layer_order",

    "doc_html": """
        Returns the current display order index of a layer as displayed in Rhino's Layer dialog box.  A display order index of -1 indicates that the current Layer dialog filter does not allow the layer to appear in the layer list.
    """,

    "syntax_html": {
        0: ("strLayer"),
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
    },

    "returns_html": {
        0: {
            "type": "number",
            "doc": "A zero-based display order index if successful."
        },
        1: {
            "type": "null",
            "doc": "If not successful, or on error."
        },
    },

    "id_com": 17,

    "params_com": {
        0: {
            "name": "vaName",
            "opt_or_req": "Required",
            "type": "tagVARIANT",
        },
    },

    "returns_com": "tagVARIANT",

}

