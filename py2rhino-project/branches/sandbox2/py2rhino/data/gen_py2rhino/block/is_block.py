is_block = {
    "module_name": "block",
    "class_name": "Block",
    "method_name": "is_block",

    "doc_html": """
        Verifies the existence of a block definition in the document.
    """,

    "syntax_html": """
        Rhino.IsBlock (strBlock)
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
            "type": "boolean",
            "doc": "True or false indicating success or failure."
        },
        1: {
            "type": "null",
            "doc": "On error."
        },
    },

    "id_com": 398,

    "params_com": {
        0: {
            "name": "vaName",
            "opt_or_req": "Required",
            "type": "tagVARIANT",
        },
    },

    "returns_com": "tagVARIANT",

}

