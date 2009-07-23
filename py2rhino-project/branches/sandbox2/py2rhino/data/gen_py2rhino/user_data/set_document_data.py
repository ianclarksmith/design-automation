set_document_data = {
    "input_folder_name": "User_Data_Methods",
    "input_file_name": "SetDocumentData",
    "output_package_name": "user_data",
    "output_module_name": "set_document_data",

    "doc_html": """
        Adds or sets a RhinoScript user data item to the current document.
    """,

    "syntax_html": {
        0: ("strSection", "strEntry", "strValue"),
    },

    "params_html": {
        0: {
            "name": "strSection",
            "opt_or_req": "Required",
            "type": "String",
            "name_prefix": "str",
            "name_main": "Section",
            "doc": """
        The section name.
            """
        },
        1: {
            "name": "strEntry",
            "opt_or_req": "Required",
            "type": "String",
            "name_prefix": "str",
            "name_main": "Entry",
            "doc": """
        The entry name.
            """
        },
        2: {
            "name": "strValue",
            "opt_or_req": "Required",
            "type": "String",
            "name_prefix": "str",
            "name_main": "Value",
            "doc": """
        The string value.
            """
        },
    },

    "returns_html": {
        0: {
            "type": "string",
            "doc": "The previous value if successful."
        },
        1: {
            "type": "null",
            "doc": "If no previous value exits, if not successful, or on error."
        },
    },

    "id_com": 243,

    "params_com": {
        0: {
            "name": "vaApp",
            "opt_or_req": "Required",
            "type": "tagVARIANT",
        },
        1: {
            "name": "vaKey",
            "opt_or_req": "Required",
            "type": "tagVARIANT",
        },
        2: {
            "name": "vaValue",
            "opt_or_req": "Required",
            "type": "tagVARIANT",
        },
    },

    "returns_com": "tagVARIANT",

}

