is_linetype_reference = {
    "input_folder_name": "Linetype_Methods",
    "input_file_name": "IsLinetypeReference",
    "output_package_name": "linetype",
    "output_module_name": "is_linetype_reference",

    "doc_html": """
        Verifies that an existing linetype is from a reference file.
    """,

    "syntax_html": """
        Rhino.IsLinetypeReference (strLinetype)
    """,

    "params_html": {
        0: {
            "name": "Linetype",
            "opt_or_req": "Required",
            "type": "String",
            "type_string": "str",
            "doc": """
        The name of an existing linetype.
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

    "id_com": 608,

    "params_com": {
        0: {
            "name": "vaName",
            "opt_or_req": "Required",
            "type": "tagVARIANT",
        },
    },

    "returns_com": "tagVARIANT",

}

