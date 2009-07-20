save_settings = {
    "module_name": "utility",
    "class_name": "Utility",
    "method_name": "save_settings",

    "doc_html": """
        Saves a string to a specified section in a Windows-style initialization file.  The initialization file must have the following form:
		[Section]
		Entry = String
		...
    """,

    "syntax_html": """
        Rhino.SaveSettings (strFilename [, strSection [, strEntry [, strString]]])
    """,

    "params_html": {
        0: {
            "name": "Filename",
            "opt_or_req": "Required",
            "type": "String",
            "type_string": "str",
            "doc": """
        The name of the initialization file.  If strFilename does not exist, the file will be created.  The specified directory must already exist.
            """
        },
        1: {
            "name": "Section",
            "opt_or_req": "Optional",
            "type": "String",
            "type_string": "str",
            "doc": """
        The section to which strString will be copied.  If strSection does not exist, it is created.
            """
        },
        2: {
            "name": "Entry",
            "opt_or_req": "Optional",
            "type": "String",
            "type_string": "str",
            "doc": """
        The name of the entry to be associated with strString.  If strEntry does not exist in the specified section, it is created.  If strEntry is nil, the entire section, including all entries within the section, is deleted.
            """
        },
        3: {
            "name": "String",
            "opt_or_req": "Optional",
            "type": "String",
            "type_string": "str",
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

