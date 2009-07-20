is_layer = {
    "input_folder_name": "Layer_Methods",
    "input_file_name": "IsLayer",
    "output_package_name": "layer",
    "output_module_name": "is_layer",

    "doc_html": """
        Verifies the existence of a layer in the document.
    """,

    "syntax_html": """
        Rhino.IsLayer (strLayer)
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

    "id_com": 6,

    "params_com": {
        0: {
            "name": "vaName",
            "opt_or_req": "Required",
            "type": "tagVARIANT",
        },
    },

    "returns_com": "tagVARIANT",

}
