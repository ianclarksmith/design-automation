layer_child_count = {
    "module_name": "layer",
    "class_name": "Layer",
    "method_name": "layer_child_count",

    "doc_html": """
        Returns the number of immediate child layers of a layer.
    """,

    "syntax_html": """
        Rhino.LayerChildCount (strLayer)
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

