block_description = {
    "module_name": "block",
    "class_name": "Block",
    "method_name": "block_description",

    "doc_html": """
        Returns or sets the description of a block definition.
    """,

    "syntax_html": """
        Rhino.BlockDescription (strBlock [, strText])
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
        1: {
            "name": "Text",
            "opt_or_req": "Optional",
            "type": "String",
            "type_string": "str",
            "doc": """
        The new description.  If omitted, the current description is returned.
            """
        },
    },

    "returns_html": {
        0: {
            "type": "string",
            "doc": "If a description is not specified,  the current description if successful."
        },
        1: {
            "type": "string",
            "doc": "If a description is specified, the previous description if successful."
        },
        2: {
            "type": "null",
            "doc": "If not successful, or on error."
        },
    },

    "id_com": 400,

    "params_com": {
        0: {
            "name": "vaName",
            "opt_or_req": "Required",
            "type": "tagVARIANT",
        },
        1: {
            "name": "vaDesc",
            "opt_or_req": "Optional",
            "type": "tagVARIANT",
        },
    },

    "returns_com": "tagVARIANT",

}

