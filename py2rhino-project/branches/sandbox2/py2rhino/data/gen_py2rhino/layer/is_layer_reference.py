is_layer_reference = {
    "input_folder_name": "Layer_Methods",
    "input_file_name": "IsLayerReference",
    "output_package_name": "layer",
    "output_module_name": "is_layer_reference",

    "doc_html": """
        Verifies that an existing layer is from a reference file.
    """,

    "syntax_html": """
        Rhino.IsLayerReference (strLayer)
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

    "id_com": 10,

    "params_com": {
        0: {
            "name": "vaName",
            "opt_or_req": "Required",
            "type": "tagVARIANT",
        },
    },

    "returns_com": "tagVARIANT",

}
