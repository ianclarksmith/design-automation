save_settings = {
    "input_folder_name": "Utility_Methods",
    "input_file_name": "SaveSettings",
    "output_package_name": "utility",
    "output_module_name": "save_settings",

    "doc_html": """
        Saves a string to a specified section in a Windows-style initialization file.  The initialization file must have the following form:
		[Section]
		Entry = String
		...
    """,

    "syntax_html": {
        0: ("strFilename", "strSection", "strEntry", "strString"),
    },

    "params_html": {
        0: {
            "name": "strFilename",
            "py_name": "filename",
            "opt_or_req": "Required",
            "type": "String",
            "name_prefix": "str",
            "name_main": "Filename",
            "doc": """
        The name of the initialization file.  If strFilename does not exist, the file will be created.  The specified directory must already exist.
            """
        },
        1: {
            "name": "strSection",
            "py_name": "section",
            "opt_or_req": "Optional",
            "type": "String",
            "name_prefix": "str",
            "name_main": "Section",
            "doc": """
        The section to which strString will be copied.  If strSection does not exist, it is created.
            """
        },
        2: {
            "name": "strEntry",
            "py_name": "entry",
            "opt_or_req": "Optional",
            "type": "String",
            "name_prefix": "str",
            "name_main": "Entry",
            "doc": """
        The name of the entry to be associated with strString.  If strEntry does not exist in the specified section, it is created.  If strEntry is nil, the entire section, including all entries within the section, is deleted.
            """
        },
        3: {
            "name": "strString",
            "py_name": "string",
            "opt_or_req": "Optional",
            "type": "String",
            "name_prefix": "str",
            "name_main": "String",
            "doc": """
        The string to be written to the file.  If omitted, the entry pointed to by strEntry is deleted.
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

    "id_com": 247,

    "params_com": {
        0: {
            "name": "vaFile",
            "opt_or_req": "Required",
            "type": "tagVARIANT",
        },
        1: {
            "name": "vaSection",
            "opt_or_req": "Optional",
            "type": "tagVARIANT",
        },
        2: {
            "name": "vaKey",
            "opt_or_req": "Optional",
            "type": "tagVARIANT",
        },
        3: {
            "name": "vaValue",
            "opt_or_req": "Optional",
            "type": "tagVARIANT",
        },
    },

    "returns_com": "tagVARIANT",

}

