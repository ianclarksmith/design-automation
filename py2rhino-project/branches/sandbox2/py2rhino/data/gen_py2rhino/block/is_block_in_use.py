is_block_in_use = {
    "module_name": "block",
    "class_name": "Block",
    "method_name": "is_block_in_use",

    "doc_html": """
        Verifies that a block definition is being used by an inserted instance.
    """,

    "syntax_html": """
        Rhino.IsBlockInUse (strBlock [, intWhere])
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
            "name": "Where",
            "opt_or_req": "Optional",
            "type": "Number",
            "type_string": "int",
            "doc": """
        Where to look, where:
		0 (Default)
		Check for top level references in active document
		1
		Check for top level and nested references in active document
		2
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

    "id_com": 406,

    "params_com": {
        0: {
            "name": "vaName",
            "opt_or_req": "Required",
            "type": "tagVARIANT",
        },
        1: {
            "name": "vaWhere",
            "opt_or_req": "Optional",
            "type": "tagVARIANT",
        },
    },

    "returns_com": "tagVARIANT",

}

