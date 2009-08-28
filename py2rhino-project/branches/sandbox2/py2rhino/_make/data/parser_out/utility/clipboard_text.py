clipboard_text = {
    "input_folder_name": "Utility_Methods",
    "input_file_name": "ClipboardText",
    "output_package_name": "utility",
    "output_module_name": "clipboard_text",

    "doc_html": """
        Returns or sets a text string to the Windows clipboard.
    """,

    "syntax_html": {
        0: ("strText"),
    },

    "params_html": {
        0: {
            "name": "strText",
            "py_name": "text",
            "opt_or_req": "Optional",
            "type": "String",
            "name_prefix": "str",
            "name_main": "Text",
            "doc": """
        A text string.
            """
        },
    },

    "returns_html": {
        0: {
            "type": "string",
            "doc": "If strText is not specified, the current text string from the Windows clipboard if successful."
        },
        1: {
            "type": "string",
            "doc": "If strText is specified, the previous text string from the Windows clipboard if successful."
        },
        2: {
            "type": "null",
            "doc": "If not successful or on error."
        },
    },

    "id_com": 245,

    "params_com": {
        0: {
            "name": "vaText",
            "opt_or_req": "Optional",
            "type": "tagVARIANT",
        },
    },

    "returns_com": "tagVARIANT",

}

