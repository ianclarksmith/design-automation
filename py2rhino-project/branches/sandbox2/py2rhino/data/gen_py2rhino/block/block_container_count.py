block_container_count = {
    "input_folder_name": "Block_Methods",
    "input_file_name": "BlockContainerCount",
    "output_package_name": "block",
    "output_module_name": "block_container_count",

    "doc_html": """
        Returns the number of block definitions that contain a specified block definition.
    """,

    "syntax_html": """
        Rhino.BlockContainerCount (strBlock)
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
            "doc": "The number of block definitions that contain the specified block definition if successful."
        },
        1: {
            "type": "null",
            "doc": "If not successful, or on error."
        },
    },

    "id_com": 411,

    "params_com": {
        0: {
            "name": "vaName",
            "opt_or_req": "Required",
            "type": "tagVARIANT",
        },
    },

    "returns_com": "tagVARIANT",

}

