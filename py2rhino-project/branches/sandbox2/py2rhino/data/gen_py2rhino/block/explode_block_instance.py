explode_block_instance = {
    "module_name": "block",
    "class_name": "Block",
    "method_name": "explode_block_instance",

    "doc_html": """
        Explodes a block instance into it's geometric components.  The exploded objects are added to the document.
    """,

    "syntax_html": """
        Rhino.ExplodeBlockInstance (strObject)
    """,

    "params_html": {
        0: {
            "name": "Object",
            "opt_or_req": "Required",
            "type": "String",
            "type_string": "str",
            "doc": """
        The identifier of an existing block definition.
            """
        },
    },

    "returns_html": {
        0: {
            "type": "array",
            "doc": "An array of strings identifying the newly exploded objects if successful."
        },
        1: {
            "type": "null",
            "doc": "If not successful, or on error."
        },
    },

    "id_com": 419,

    "params_com": {
        0: {
            "name": "vaObject",
            "opt_or_req": "Required",
            "type": "tagVARIANT",
        },
    },

    "returns_com": "tagVARIANT",

}

