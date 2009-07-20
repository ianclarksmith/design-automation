block_object_count = {
    "module_name": "block",
    "class_name": "Block",
    "method_name": "block_object_count",

    "doc_html": """
        Returns the number of objects that make up a block definition.
    """,

    "syntax_html": """
        Rhino.BlockObjectCount (strBlock)
    """,

    "params_html": {
        0: {
            "name": "Block",
            "opt_or_req": "Required",
            "type": "String",
            "type_string": "str",
            "doc": """
        The name of an existing block definition.
            """
        },
    },

    "returns_html": {
        0: {
            "type": "number",
            "doc": "The number of objects that make up the block definition if successful."
        },
        1: {
            "type": "null",
            "doc": "If not successful, or on error."
        },
    },

    "id_com": 416,

    "params_com": {
        0: {
            "name": "vaName",
            "opt_or_req": "Required",
            "type": "tagVARIANT",
        },
    },

    "returns_com": "tagVARIANT",

}

