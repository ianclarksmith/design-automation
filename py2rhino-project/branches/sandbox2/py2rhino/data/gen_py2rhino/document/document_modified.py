document_modified = {
    "input_folder_name": "Document_Methods",
    "input_file_name": "DocumentModified",
    "output_package_name": "document",
    "output_module_name": "document_modified",

    "doc_html": """
        Returns or sets the document's modified flag. The modified flag indicates whether or not any changes to the current document have been made.
		Note, setting the document modified flag to false will prevent the "Do you want to save this file..." from displaying when you close Rhino.
    """,

    "syntax_html": {
        0: ("blnModified"),
    },

    "params_html": {
        0: {
            "name": "blnModified",
            "opt_or_req": "Optional",
            "type": "Boolean",
            "name_prefix": "bln",
            "name_main": "Modified",
            "doc": """
        The modified state, either True or False.
            """
        },
    },

    "returns_html": {
        0: {
            "type": "boolean",
            "doc": "If no modified state is specified, the current modified state if successful."
        },
        1: {
            "type": "boolean",
            "doc": "If a modified state is specified, the previous modified state if successful."
        },
    },

    "id_com": 323,

    "params_com": {
        0: {
            "name": "vaModified",
            "opt_or_req": "Optional",
            "type": "tagVARIANT",
        },
    },

    "returns_com": "tagVARIANT",

}

