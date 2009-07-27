layer_child_count = {
    "input_folder_name": "Layer_Methods",
    "input_file_name": "LayerChildCount",
    "output_package_name": "layer",
    "output_module_name": "layer_child_count",

    "doc_html": """
        Returns the number of immediate child layers of a layer.
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
        The name of the layer.
            """
        },
    },

    "returns_html": {
        0: {
            "type": "number",
            "doc": "The number of immediate child layers if successful"
        },
        1: {
            "type": "null",
            "doc": "On error."
        },
    },

    "id_com": 694,

    "params_com": {
        0: {
            "name": "vaName",
            "opt_or_req": "Required",
            "type": "tagVARIANT",
        },
    },

    "returns_com": "tagVARIANT",

}

