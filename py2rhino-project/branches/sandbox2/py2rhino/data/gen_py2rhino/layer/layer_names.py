layer_names = {
    "module_name": "layer",
    "class_name": "Layer",
    "method_name": "layer_names",

    "doc_html": """
        Returns the names of all layers in the document.
    """,

    "syntax_html": """
        Rhino.LayerNames ([blnSort])
    """,

    "params_html": {
        0: {
            "name": "Sort",
            "opt_or_req": "Optional",
            "type": "Boolean",
            "type_string": "bln",
            "doc": """
        Return a sorted list of layer names. The default is not to return a sorted list (False).
            """
        },
    },

    "returns_html": {
        0: {
            "type": "array",
            "doc": "An array of layer names if successful."
        },
        1: {
            "type": "null",
            "doc": "If not successful, or on error."
        },
    },

    "id_com": 15,

    "params_com": {
        0: {
            "name": "vaSort",
            "opt_or_req": "Optional",
            "type": "tagVARIANT",
        },
    },

    "returns_com": "tagVARIANT",

}

