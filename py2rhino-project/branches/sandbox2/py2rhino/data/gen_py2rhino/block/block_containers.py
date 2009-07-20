block_containers = {
    "module_name": "block",
    "class_name": "Block",
    "method_name": "block_containers",

    "doc_html": """
        Returns the names of the block definitions that contain a specified block definition.
    """,

    "syntax_html": """
        Rhino.BlockContainers (strBlock)
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
            "type": "array",
            "doc": "An array of block definition names if successful."
        },
        1: {
            "type": "null",
            "doc": "If not successful, or on error."
        },
    },

    "id_com": 412,

    "params_com": {
        0: {
            "name": "vaName",
            "opt_or_req": "Required",
            "type": "tagVARIANT",
        },
    },

    "returns_com": "tagVARIANT",

}

