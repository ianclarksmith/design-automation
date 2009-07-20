is_layer_locked = {
    "input_folder_name": "Layer_Methods",
    "input_file_name": "IsLayerLocked",
    "output_package_name": "layer",
    "output_module_name": "is_layer_locked",

    "doc_html": """
        Verifies that an existing layer is locked.
    """,

    "syntax_html": """
        Rhino.IsLayerLocked (strLayer)
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

    "id_com": 8,

    "params_com": {
        0: {
            "name": "vaName",
            "opt_or_req": "Required",
            "type": "tagVARIANT",
        },
    },

    "returns_com": "tagVARIANT",

}
