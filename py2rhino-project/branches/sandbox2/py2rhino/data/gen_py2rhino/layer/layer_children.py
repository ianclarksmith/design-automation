layer_children = {
    "module_name": "layer",
    "class_name": "Layer",
    "method_name": "layer_children",

    "doc_html": """
        Returns the immediate child layers of a layer.
    """,

    "syntax_html": """
        Rhino.LayerChildren (strLayer)
    """,

    "params_html": {
        0: {
            "name": "Layer",
            "opt_or_req": "Required",
            "type": "String",
            "type_string": "str",
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

