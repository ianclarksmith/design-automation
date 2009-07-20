enable_redraw = {
    "input_folder_name": "Document_Methods",
    "input_file_name": "EnableRedraw",
    "output_package_name": "document",
    "output_module_name": "enable_redraw",

    "doc_html": """
        Enables or disables screen redrawing.
    """,

    "syntax_html": """
        Rhino.EnableRedraw ([blnRedraw])
    """,

    "params_html": {
        0: {
            "name": "Select",
            "opt_or_req": "Optional",
            "type": "Boolean",
            "type_string": "bln",
            "doc": """
        The screen redrawing state.  If omitted, screen redrawing is enabled (True).
            """
        },
    },

    "returns_html": {
        0: {
            "type": "boolean",
            "doc": "The previous screen redrawing state."
        },
    },

    "id_com": 317,

    "params_com": {
        0: {
            "name": "vaRedraw",
            "opt_or_req": "Optional",
            "type": "tagVARIANT",
        },
    },

    "returns_com": "tagVARIANT",

}

