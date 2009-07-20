block_names = {
    "module_name": "block",
    "class_name": "Block",
    "method_name": "block_names",

    "doc_html": """
        Returns the names of all block definitions in the document.
    """,

    "syntax_html": """
        Rhino.BlockNames ([blnSort])
    """,

    "params_html": {
        0: {
            "name": "Sort",
            "opt_or_req": "Optional",
            "type": "Boolean",
            "type_string": "bln",
            "doc": """
        Return a sorted array of block definition names.
            """
        },
    },

    "returns_html": {
        0: {
            "type": "array",
            "doc": "An array of block definition names if successful."
        },
        1: {
            "type": "null",
            "doc": "If not successful, or on error."
        },
    },

    "id_com": 396,

    "params_com": {
        0: {
            "name": "vaSort",
            "opt_or_req": "Optional",
            "type": "tagVARIANT",
        },
    },

    "returns_com": "tagVARIANT",

}

