is_block_in_use = {
    "input_folder_name": "Block_Methods",
    "input_file_name": "IsBlockInUse",
    "output_package_name": "block",
    "output_module_name": "is_block_in_use",

    "doc_html": """
        Verifies that a block definition is being used by an inserted instance.
    """,

    "syntax_html": {
        0: ("strBlock", "intWhere"),
    },

    "params_html": {
        0: {
            "name": "strBlock",
            "py_name": "block",
            "opt_or_req": "Required",
            "type": "String",
            "name_prefix": "str",
            "name_main": "Block",
            "doc": """
        The name of an existing block definition.
            """
        },
        1: {
            "name": "intWhere",
            "py_name": "where",
            "opt_or_req": "Optional",
            "type": "Number",
            "name_prefix": "int",
            "name_main": "Where",
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

