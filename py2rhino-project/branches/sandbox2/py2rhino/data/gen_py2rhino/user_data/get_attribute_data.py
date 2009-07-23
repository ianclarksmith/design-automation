get_attribute_data = {
    "input_folder_name": "User_Data_Methods",
    "input_file_name": "GetAttributeData",
    "output_package_name": "user_data",
    "output_module_name": "get_attribute_data",

    "doc_html": """
        Returns a RhinoScript user data item from an object's attributes.
    """,

    "syntax_html": {
        0: ("strObject", "strSection", "strEntry"),
    },

    "params_html": {
        0: {
            "name": "strObject",
            "opt_or_req": "Required",
            "type": "String",
            "name_prefix": "str",
            "name_main": "Object",
            "doc": """
        The object's identifier.
            """
        },
        1: {
            "name": "strSection",
            "opt_or_req": "Optional",
            "type": "String",
            "name_prefix": "str",
            "name_main": "Section",
            "doc": """
        The section name.  If omitted, all section names are returned.
            """
        },
        2: {
            "name": "strEntry",
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

    "id_com": 682,

    "params_com": {
        0: {
            "name": "vaObject",
            "opt_or_req": "Required",
            "type": "tagVARIANT",
        },
        1: {
            "name": "vaApp",
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

