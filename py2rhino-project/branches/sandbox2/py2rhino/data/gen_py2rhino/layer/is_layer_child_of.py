is_layer_child_of = {
    "module_name": "layer",
    "class_name": "Layer",
    "method_name": "is_layer_child_of",

    "doc_html": """
        Verifies that a layer is a child of another layer.
    """,

    "syntax_html": """
        Rhino.IsLayerChildOf (strLayer, strTest)
    """,

    "params_html": {
        0: {
            "name": "Layer",
            "opt_or_req": "Required",
            "type": "String",
            "type_string": "str",
            "doc": """
        The name of the layer to test against.
            """
        },
        1: {
            "name": "Test",
            "opt_or_req": "Required",
            "type": "String",
            "type_string": "str",
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

