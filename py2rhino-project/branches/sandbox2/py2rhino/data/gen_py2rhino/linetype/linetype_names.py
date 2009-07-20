linetype_names = {
    "input_folder_name": "Linetype_Methods",
    "input_file_name": "LinetypeNames",
    "output_package_name": "linetype",
    "output_module_name": "linetype_names",

    "doc_html": """
        Returns the names of all linetypes in the document.
    """,

    "syntax_html": """
        Rhino.LinetypeNames ([blnSort])
    """,

    "params_html": {
        0: {
            "name": "Sort",
            "opt_or_req": "Optional",
            "type": "Boolean",
            "type_string": "bln",
            "doc": """
        Return a sorted list of linetype names. The default is not to return a sorted list (False).
            """
        },
    },

    "returns_html": {
        0: {
            "type": "array",
            "doc": "An array of linetype names if successful."
        },
        1: {
            "type": "null",
            "doc": "If not successful, or on error."
        },
    },

    "id_com": 606,

    "params_com": {
        0: {
            "name": "vaSort",
            "opt_or_req": "Required",
            "type": "tagVARIANT",
        },
    },

    "returns_com": "tagVARIANT",

}

