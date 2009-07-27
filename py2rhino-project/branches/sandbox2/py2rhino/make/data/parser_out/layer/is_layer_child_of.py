is_layer_child_of = {
    "input_folder_name": "Layer_Methods",
    "input_file_name": "IsLayerChildOf",
    "output_package_name": "layer",
    "output_module_name": "is_layer_child_of",

    "doc_html": """
        Verifies that a layer is a child of another layer.
    """,

    "syntax_html": {
        0: ("strLayer", "strTest"),
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
        The name of the layer to test against.
            """
        },
        1: {
            "name": "strTest",
            "py_name": "test",
            "opt_or_req": "Required",
            "type": "String",
            "name_prefix": "str",
            "name_main": "Test",
            "doc": """
        The name of the layer to test
            """
        },
    },

    "returns_html": {
        0: {
            "type": "boolean",
            "doc": "True if strTest is a child of strLayer. False otherwise."
        },
        1: {
            "type": "null",
            "doc": "On error."
        },
    },

    "id_com": 692,

    "params_com": {
        0: {
            "name": "vaName",
            "opt_or_req": "Required",
            "type": "tagVARIANT",
        },
        1: {
            "name": "vaParent",
            "opt_or_req": "Required",
            "type": "tagVARIANT",
        },
    },

    "returns_com": "tagVARIANT",

}

