is_layout = {
    "input_folder_name": "View_Methods",
    "input_file_name": "IsLayout",
    "output_package_name": "view",
    "output_module_name": "is_layout",

    "doc_html": """
        Verifies that a view is a page layout view.
    """,

    "syntax_html": {
        0: ("strLayout"),
    },

    "params_html": {
        0: {
            "name": "strLayout",
            "py_name": "layout",
            "opt_or_req": "Required",
            "type": "String",
            "name_prefix": "str",
            "name_main": "Layout",
            "doc": """
        The title or identifier of an existing page layout view.
            """
        },
    },

    "returns_html": {
        0: {
            "type": "null",
            "doc": "On error."
        },
    },

    "id_com": 920,

    "params_com": {
        0: {
            "name": "vaLayout",
            "opt_or_req": "Required",
            "type": "tagVARIANT",
        },
    },

    "returns_com": "tagVARIANT",

}

