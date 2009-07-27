layer_children = {
    "input_folder_name": "Layer_Methods",
    "input_file_name": "LayerChildren",
    "output_package_name": "layer",
    "output_module_name": "layer_children",

    "doc_html": """
        Returns the immediate child layers of a layer.
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
            "type": "array",
            "doc": "An array of strings identifying the layer's children if successful"
        },
        1: {
            "type": "null",
            "doc": "If the layer has no children, or on error."
        },
    },

    "id_com": 691,

    "params_com": {
        0: {
            "name": "vaName",
            "opt_or_req": "Required",
            "type": "tagVARIANT",
        },
    },

    "returns_com": "tagVARIANT",

}

