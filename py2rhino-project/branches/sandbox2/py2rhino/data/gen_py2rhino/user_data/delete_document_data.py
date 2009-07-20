delete_document_data = {
    "input_folder_name": "User_Data_Methods",
    "input_file_name": "DeleteDocumentData",
    "output_package_name": "user_data",
    "output_module_name": "delete_document_data",

    "doc_html": """
        Removes RhinoScript user data items from the current document.
    """,

    "syntax_html": """
        Rhino.DeleteDocumentData ([strSection [, strEntry]])
    """,

    "params_html": {
        0: {
            "name": "Section",
            "opt_or_req": "Optional",
            "type": "String",
            "type_string": "str",
            "doc": """
        The section name.  If omitted, all sections and their corresponding entries are removed.
            """
        },
        1: {
            "name": "Entry",
            "opt_or_req": "Optional",
            "type": "String",
            "type_string": "str",
            "doc": """
        The entry name.  If omitted, all entries for strSection are removed.
            """
        },
    },

    "returns_html": {
        0: {
            "type": "boolean",
            "doc": "True or False indicating success or failure."
        },
        1: {
            "type": "null",
            "doc": "On error."
        },
    },

    "id_com": 237,

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

