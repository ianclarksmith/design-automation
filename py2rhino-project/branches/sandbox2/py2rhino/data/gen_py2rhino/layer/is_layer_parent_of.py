is_layer_parent_of = {
    "module_name": "layer",
    "class_name": "Layer",
    "method_name": "is_layer_parent_of",

    "doc_html": """
        Verifies that a layer is a parent of another layer.
    """,

    "syntax_html": """
        Rhino.IsLayerParentOf (strLayer, strTest)
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
            "doc": "True if strTest is a parent of strLayer. False otherwise."
        },
        1: {
            "type": "null",
            "doc": "On error."
        },
    },

    "id_com": 693,

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

