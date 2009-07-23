get_document_data = {
    "input_folder_name": "User_Data_Methods",
    "input_file_name": "GetDocumentData",
    "output_package_name": "user_data",
    "output_module_name": "get_document_data",

    "doc_html": """
        Returns a RhinoScript user data item from the current document.
    """,

    "syntax_html": {
        0: ("strSection", "strEntry"),
    },

    "params_html": {
        0: {
            "name": "strSection",
            "py_name": "section",
            "opt_or_req": "Optional",
            "type": "String",
            "name_prefix": "str",
            "name_main": "Section",
            "doc": """
        The section name.  If omitted, all section names are returned.
            """
        },
        1: {
            "name": "strEntry",
            "py_name": "entry",
            "opt_or_req": "Optional",
            "type": "String",
            "name_prefix": "str",
            "name_main": "Entry",
            "doc": """
        The entry name.  If omitted, all entry names for strSection are returned.
            """
        },
    },

    "returns_html": {
        0: {
            "type": "array",
            "doc": "A zero-based, one-dimensional array of all section names if strSection is not specified."
        },
        1: {
            "type": "array",
            "doc": "A zero-based, one-dimensional array of all entry names for strSection if strEntry is not specified."
        },
        2: {
            "type": "string",
            "doc": "The value of the entry if both strSection and strEntry are specified."
        },
        3: {
            "type": "null",
            "doc": "If not successful, or on error."
        },
    },

    "id_com": 240,

    "params_com": {
        0: {
            "name": "vaApp",
            "opt_or_req": "Optional",
            "type": "tagVARIANT",
        },
        1: {
            "name": "vaKey",
            "opt_or_req": "Optional",
            "type": "tagVARIANT",
        },
    },

    "returns_com": "tagVARIANT",

}

