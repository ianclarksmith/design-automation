get_settings = {
    "module_name": "utility",
    "class_name": "Utility",
    "method_name": "get_settings",

    "doc_html": """
        Returns a string from a specified section in a Windows-style initialization file.  The initialization file must have the following form:
		[Section]
		Entry = String
		...
    """,

    "syntax_html": """
        Rhino.GetSettings (strFilename [, strSection [, strEntry]])
    """,

    "params_html": {
        0: {
            "name": "Filename",
            "opt_or_req": "Required",
            "type": "String",
            "type_string": "str",
            "doc": """
        The name of the initialization file.
            """
        },
        1: {
            "name": "Section",
            "opt_or_req": "Optional",
            "type": "String",
            "type_string": "str",
            "doc": """
        The section containing the entry.
            """
        },
        2: {
            "name": "Entry",
            "opt_or_req": "Optional",
            "type": "String",
            "type_string": "str",
            "doc": """
        The entry whose associated string is to be returned.
            """
        },
    },

    "returns_html": {
        0: {
            "type": "array",
            "doc": "If strSection is not specified, a zero-based, one-dimensional array containing all section names from strFilename if successful."
        },
        1: {
            "type": "array",
            "doc": "If strEntry is not specified, a zero-based, one-dimensional array containing all entry names within strSection if successful."
        },
        2: {
            "type": "string",
            "doc": "If strSection and strEntry are returned, the value of strEntry if successful."
        },
        3: {
            "type": "null",
            "doc": "If not successful, or on error."
        },
    },

    "id_com": 246,

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
    },

    "returns_com": "tagVARIANT",

}

