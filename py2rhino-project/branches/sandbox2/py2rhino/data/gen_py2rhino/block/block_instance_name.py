block_instance_name = {
    "module_name": "block",
    "class_name": "Block",
    "method_name": "block_instance_name",

    "doc_html": """
        Returns the block name of a block instance.
    """,

    "syntax_html": """
        Rhino.BlockInstanceName (strObject)
    """,

    "params_html": {
        0: {
            "name": "Object",
            "opt_or_req": "Required",
            "type": "String",
            "type_string": "str",
            "doc": """
        The identifier of an existing block insertion object.
            """
        },
    },

    "returns_html": {
        0: {
            "type": "string",
            "doc": "The block name if successful."
        },
        1: {
            "type": "null",
            "doc": "If not successful, or on error."
        },
    },

    "id_com": 571,

    "params_com": {
        0: {
            "name": "vaObject",
            "opt_or_req": "Required",
            "type": "tagVARIANT",
        },
    },

    "returns_com": "tagVARIANT",

}

