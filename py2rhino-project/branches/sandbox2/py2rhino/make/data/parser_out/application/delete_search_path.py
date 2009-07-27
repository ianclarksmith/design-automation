delete_search_path = {
    "input_folder_name": "Application_Methods",
    "input_file_name": "DeleteSearchPath",
    "output_package_name": "application",
    "output_module_name": "delete_search_path",

    "doc_html": """
        Removes an existing path from Rhino's search path list. Search path items can be removed manually by using Rhino's Options command and modifying the contents of the Files tab. See "Options Files settings" in the Rhino help file for more details.
    """,

    "syntax_html": {
        0: ("strFolder"),
    },

    "params_html": {
        0: {
            "name": "strFolder",
            "py_name": "folder",
            "opt_or_req": "Required",
            "type": "String",
            "name_prefix": "str",
            "name_main": "Folder",
            "doc": """
        A valid folder, or path, to remove.
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

    "id_com": 512,

    "params_com": {
        0: {
            "name": "vaFolder",
            "opt_or_req": "Required",
            "type": "tagVARIANT",
        },
    },

    "returns_com": "tagVARIANT",

}

