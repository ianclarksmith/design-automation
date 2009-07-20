layer_visible = {
    "module_name": "layer",
    "class_name": "Layer",
    "method_name": "layer_visible",

    "doc_html": """
        Returns or changes the visibility property of a layer. This method should be use instead of LayerMode.
    """,

    "syntax_html": """
        Rhino.LayerVisible (strLayer [, blnVisible])
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
        1: {
            "name": "Visible",
            "opt_or_req": "Optional",
            "type": "Boolean",
            "type_string": "bln",
            "doc": """
        The new layer visibility.  True = Visible, False = Hidden.
            """
        },
    },

    "returns_html": {
        0: {
            "type": "boolean",
            "doc": "If a layer mode is not specified,  the current layer visibility if successful."
        },
        1: {
            "type": "boolean",
            "doc": "If a layer mode is specified, the previous layer visibility if successful."
        },
        2: {
            "type": "null",
            "doc": "If not successful, or on error."
        },
    },

    "id_com": 600,

    "params_com": {
        0: {
            "name": "vaLayer",
            "opt_or_req": "Required",
            "type": "tagVARIANT",
        },
        1: {
            "name": "vaVisible",
            "opt_or_req": "Optional",
            "type": "tagVARIANT",
        },
    },

    "returns_com": "tagVARIANT",

}

