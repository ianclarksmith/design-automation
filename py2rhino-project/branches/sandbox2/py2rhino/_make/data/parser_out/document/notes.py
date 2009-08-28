notes = {
    "input_folder_name": "Document_Methods",
    "input_file_name": "Notes",
    "output_package_name": "document",
    "output_module_name": "notes",

    "doc_html": """
        Returns or sets the document's notes.  Notes are generally created by using Rhino's Notes command.
    """,

    "syntax_html": {
        0: ("strNotes"),
    },

    "params_html": {
        0: {
            "name": "strNotes",
            "py_name": "notes",
            "opt_or_req": "Optional",
            "type": "String",
            "name_prefix": "str",
            "name_main": "Notes",
            "doc": """
        The notes.
            """
        },
    },

    "returns_html": {
        0: {
            "type": "string",
            "doc": "If strNotes is not specified, the current notes if successful."
        },
        1: {
            "type": "string",
            "doc": "If strNotes is specified, the previous notes if successful."
        },
        2: {
            "type": "null",
            "doc": "If not successful, or on error."
        },
    },

    "id_com": 274,

    "params_com": {
        0: {
            "name": "vaNotes",
            "opt_or_req": "Optional",
            "type": "tagVARIANT",
        },
    },

    "returns_com": "tagVARIANT",

}

