current_layer = {
    "input_folder_name": "Layer_Methods",
    "input_file_name": "CurrentLayer",
    "output_package_name": "layer",
    "output_module_name": "current_layer",

    "doc_html": """
        Returns or changes the current layer.
    """,

    "syntax_html": """
        Rhino.CurrentLayer ([strLayer])
    """,

    "params_html": {
        0: {
            "name": "Layer",
            "opt_or_req": "Optional",
            "type": "String",
            "type_string": "str",
            "doc": """
        The name of an existing layer to make current.
            """
        },
    },

    "returns_html": {
        0: {
            "type": "string",
            "doc": "If a layer name is not specified, the name of the current layer if successful."
        },
        1: {
            "type": "string",
            "doc": "If a layer name is specified, the name of the previous current layer if successful."
        },
        2: {
            "type": "null",
            "doc": "If not successful, or on error."
        },
    },

    "id_com": 5,

    "params_com": {
        0: {
            "name": "vaName",
            "opt_or_req": "Optional",
            "type": "tagVARIANT",
        },
    },

    "returns_com": "tagVARIANT",

}

