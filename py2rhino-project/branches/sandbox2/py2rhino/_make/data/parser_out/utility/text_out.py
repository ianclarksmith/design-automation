text_out = {
    "input_folder_name": "Utility_Methods",
    "input_file_name": "TextOut",
    "output_package_name": "utility",
    "output_module_name": "text_out",

    "doc_html": """
        Displays a text output window.
    """,

    "syntax_html": {
        0: ("strText", "strTitle"),
    },

    "params_html": {
        0: {
            "name": "strText",
            "py_name": "text",
            "opt_or_req": "Required",
            "type": "String",
            "name_prefix": "str",
            "name_main": "Text",
            "doc": """
        A text string to display.
            """
        },
        1: {
            "name": "strTitle",
            "py_name": "title",
            "opt_or_req": "Optional",
            "type": "String",
            "name_prefix": "str",
            "name_main": "Title",
            "doc": """
        A dialog box title.
            """
        },
    },

    "returns_html": {
        0: {
            "type": "null",
            "doc": "If successful or on failure."
        },
    },

    "id_com": 755,

    "params_com": {
        0: {
            "name": "vaText",
            "opt_or_req": "Required",
            "type": "tagVARIANT",
        },
        1: {
            "name": "vaTitle",
            "opt_or_req": "Optional",
            "type": "tagVARIANT",
        },
    },

    "returns_com": "tagVARIANT",

}

