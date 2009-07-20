dim_style_names = {
    "input_folder_name": "Dimension_Methods",
    "input_file_name": "DimStyleNames",
    "output_package_name": "dimension",
    "output_module_name": "dim_style_names",

    "doc_html": """
        Returns the names of all dimension styles in the document.
    """,

    "syntax_html": """
        Rhino.DimStyleNames ([blnSort])
    """,

    "params_html": {
        0: {
            "name": "Sort",
            "opt_or_req": "Optional",
            "type": "Boolean",
            "type_string": "bln",
            "doc": """
        Return a sorted list of dimension style names. The default is not to return a sorted list (False).
            """
        },
    },

    "returns_html": {
        0: {
            "type": "array",
            "doc": "An array of dimension style names if successful."
        },
        1: {
            "type": "null",
            "doc": "If not successful, or on error."
        },
    },

    "id_com": 452,

    "params_com": {
        0: {
            "name": "vaSort",
            "opt_or_req": "Optional",
            "type": "tagVARIANT",
        },
    },

    "returns_com": "tagVARIANT",

}

