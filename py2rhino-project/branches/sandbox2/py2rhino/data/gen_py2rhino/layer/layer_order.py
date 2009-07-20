layer_order = {
    "module_name": "layer",
    "class_name": "Layer",
    "method_name": "layer_order",

    "doc_html": """
        Returns the current display order index of a layer as displayed in Rhino's Layer dialog box.  A display order index of -1 indicates that the current Layer dialog filter does not allow the layer to appear in the layer list.
    """,

    "syntax_html": """
        Rhino.LayerOrder (strLayer)
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
            "type": "number",
            "doc": "A zero-based display order index if successful."
        },
        1: {
            "type": "null",
            "doc": "If not successful, or on error."
        },
    },

    "id_com": 17,

    "params_com": {
        0: {
            "name": "vaName",
            "opt_or_req": "Required",
            "type": "tagVARIANT",
        },
    },

    "returns_com": "tagVARIANT",

}

