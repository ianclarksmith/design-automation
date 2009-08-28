open_file_name = {
    "input_folder_name": "User_Interface_Methods",
    "input_file_name": "OpenFileName",
    "output_package_name": "user_interface",
    "output_module_name": "open_file_name",

    "doc_html": """
        Displays a Windows file open dialog box allowing the user to select a file name. Note, this function does not open the file.
    """,

    "syntax_html": {
        0: ("strTitle", "strFilter", "strFolder", "strFilename", "strExtension"),
    },

    "params_html": {
        0: {
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
        1: {
            "name": "strFilter",
            "py_name": "filter",
            "opt_or_req": "Optional",
            "type": "String",
            "name_prefix": "str",
            "name_main": "Filter",
            "doc": """
        A filter string.  The filter string must be in the following form:  "Description1|Filter1|Description2|Filter2||", where "||" terminates filter string.  If omitted, the filter (*.*) is used.
            """
        },
        2: {
            "name": "strFolder",
            "py_name": "folder",
            "opt_or_req": "Optional",
            "type": "String",
            "name_prefix": "str",
            "name_main": "Folder",
            "doc": """
        A default folder.
            """
        },
        3: {
            "name": "strFilename",
            "py_name": "filename",
            "opt_or_req": "Optional",
            "type": "String",
            "name_prefix": "str",
            "name_main": "Filename",
            "doc": """
        A default file name.
            """
        },
        4: {
            "name": "strExtension",
            "py_name": "extension",
            "opt_or_req": "Optional",
            "type": "String",
            "name_prefix": "str",
            "name_main": "Extension",
            "doc": """
        A default file extension.
            """
        },
    },

    "returns_html": {
        0: {
            "type": "string",
            "doc": "The file name if successful."
        },
        1: {
            "type": "null",
            "doc": "If not successful, or on error."
        },
    },

    "id_com": 151,

    "params_com": {
        0: {
            "name": "vaTitle",
            "opt_or_req": "Optional",
            "type": "tagVARIANT",
        },
        1: {
            "name": "vaFilter",
            "opt_or_req": "Optional",
            "type": "tagVARIANT",
        },
        2: {
            "name": "vaPath",
            "opt_or_req": "Optional",
            "type": "tagVARIANT",
        },
        3: {
            "name": "vaFile",
            "opt_or_req": "Optional",
            "type": "tagVARIANT",
        },
        4: {
            "name": "vaExt",
            "opt_or_req": "Optional",
            "type": "tagVARIANT",
        },
    },

    "returns_com": "tagVARIANT",

}

