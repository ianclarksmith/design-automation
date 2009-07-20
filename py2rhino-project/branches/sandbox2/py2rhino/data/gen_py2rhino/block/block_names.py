block_names = {
    "input_folder_name": "Block_Methods",
    "input_file_name": "BlockNames",
    "output_package_name": "block",
    "output_module_name": "block_names",

    "doc_html": """
        Returns the names of all block definitions in the document.
    """,

    "syntax_html": """
        Rhino.BlockNames ([blnSort])
    """,

    "params_html": {
        0: {
            "name": "Sort",
            "opt_or_req": "Optional",
            "type": "Boolean",
            "type_string": "bln",
            "doc": """
        Return a sorted array of block definition names.
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

    "id_com": 396,

    "params_com": {
        0: {
            "name": "vaSort",
            "opt_or_req": "Optional",
            "type": "tagVARIANT",
        },
    },

    "returns_com": "tagVARIANT",

}

