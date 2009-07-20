layer_linetype = {
    "module_name": "layer",
    "class_name": "Layer",
    "method_name": "layer_linetype",

    "doc_html": """
        Returns or changes the linetype of a layer.
    """,

    "syntax_html": """
        Rhino.LayerLinetype (strLayer [, strLinetype])
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
            "name": "Linetype",
            "opt_or_req": "Optional",
            "type": "String",
            "type_string": "str",
            "doc": """
        The name of the new linetype.
            """
        },
    },

    "returns_html": {
        0: {
            "type": "string",
            "doc": "If a linetype is not specified,  the name of the current linetype if successful."
        },
        1: {
            "type": "string",
            "doc": "If a linetype is specified, the name of the previous linetype if successful."
        },
        2: {
            "type": "null",
            "doc": "If not successful, or on error."
        },
    },

    "id_com": 602,

    "params_com": {
        0: {
            "name": "vaLayer",
            "opt_or_req": "Required",
            "type": "tagVARIANT",
        },
        1: {
            "name": "vaLinetype",
            "opt_or_req": "Optional",
            "type": "tagVARIANT",
        },
    },

    "returns_com": "tagVARIANT",

}

