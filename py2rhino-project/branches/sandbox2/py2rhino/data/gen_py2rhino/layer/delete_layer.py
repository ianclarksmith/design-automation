delete_layer = {
    "module_name": "layer",
    "class_name": "Layer",
    "method_name": "delete_layer",

    "doc_html": """
        Removes an existing layer from the document.  The layer to be removed cannot be the current layer.  Unlike the PurgeLayer method,  the layer must be empty, or contain no objects, before it can be removed. Any layers that are children of the specified layer will also be removed if they are also empty.
    """,

    "syntax_html": """
        Rhino.DeleteLayer (strLayer)
    """,

    "params_html": {
        0: {
            "name": "Layer",
            "opt_or_req": "Required",
            "type": "String",
            "type_string": "str",
            "doc": """
        The name of an empty layer.
            """
        },
    },

    "returns_html": {
        0: {
            "type": "boolean",
            "doc": "True or false indicating success or failure."
        },
        1: {
            "type": "null",
            "doc": "On error."
        },
    },

    "id_com": 4,

    "params_com": {
        0: {
            "name": "vaName",
            "opt_or_req": "Required",
            "type": "tagVARIANT",
        },
    },

    "returns_com": "tagVARIANT",

}

