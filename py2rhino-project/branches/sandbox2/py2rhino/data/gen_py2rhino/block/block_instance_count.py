block_instance_count = {
    "module_name": "block",
    "class_name": "Block",
    "method_name": "block_instance_count",

    "doc_html": """
        Counts the number of instances of the block in the document.  Nested instances are not included in the count.
    """,

    "syntax_html": """
        Rhino.BlockInstanceCount (strBlock)
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
            "doc": "The number of instances of the block in the document if successful."
        },
        1: {
            "type": "null",
            "doc": "If not successful, or on error."
        },
    },

    "id_com": 404,

    "params_com": {
        0: {
            "name": "vaName",
            "opt_or_req": "Required",
            "type": "tagVARIANT",
        },
    },

    "returns_com": "tagVARIANT",

}

