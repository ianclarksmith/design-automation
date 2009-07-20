is_detail = {
    "input_folder_name": "View_Methods",
    "input_file_name": "IsDetail",
    "output_package_name": "view",
    "output_module_name": "is_detail",

    "doc_html": """
        Verifies that a detail view exists on a page layout view.
    """,

    "syntax_html": """
        Rhino.IsDetail (strLayout, strDetail)
    """,

    "params_html": {
        0: {
            "name": "Layout",
            "opt_or_req": "Required",
            "type": "String",
            "type_string": "str",
            "doc": """
        The title or identifier of an existing page layout view.
            """
        },
        1: {
            "name": "Detail",
            "opt_or_req": "Required",
            "type": "String",
            "type_string": "str",
            "doc": """
        The title or identifier of an existing detail view.
            """
        },
    },

    "returns_html": {
        0: {
            "type": "null",
            "doc": "On error."
        },
    },

    "id_com": 921,

    "params_com": {
        0: {
            "name": "vaLayout",
            "opt_or_req": "Required",
            "type": "tagVARIANT",
        },
        1: {
            "name": "vaDetail",
            "opt_or_req": "Required",
            "type": "tagVARIANT",
        },
    },

    "returns_com": "tagVARIANT",

}

