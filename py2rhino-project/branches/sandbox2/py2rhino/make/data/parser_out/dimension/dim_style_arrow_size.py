dim_style_arrow_size = {
    "input_folder_name": "Dimension_Methods",
    "input_file_name": "DimStyleArrowSize",
    "output_package_name": "dimension",
    "output_module_name": "dim_style_arrow_size",

    "doc_html": """
        Returns or changes the arrow size of a dimension style.
    """,

    "syntax_html": {
        0: ("strDimStyle", "dblSize"),
    },

    "params_html": {
        0: {
            "name": "strDimStyle",
            "py_name": "dim_style",
            "opt_or_req": "Required",
            "type": "String",
            "name_prefix": "str",
            "name_main": "DimStyle",
            "doc": """
        The name of an existing dimension style.
            """
        },
        1: {
            "name": "dblSize",
            "py_name": "size",
            "opt_or_req": "Optional",
            "type": "Number",
            "name_prefix": "dbl",
            "name_main": "Size",
            "doc": """
        The new arrow size.  If omitted, the current arrow size is returned.
            """
        },
    },

    "returns_html": {
        0: {
            "type": "number",
            "doc": "If a size value is not specified, the current arrow size if successful."
        },
        1: {
            "type": "number",
            "doc": "If a size value is specified, the previous arrow size if successful."
        },
        2: {
            "type": "null",
            "doc": "If not successful, or on error."
        },
    },

    "id_com": 468,

    "params_com": {
        0: {
            "name": "vaStyle",
            "opt_or_req": "Required",
            "type": "tagVARIANT",
        },
        1: {
            "name": "vaValue",
            "opt_or_req": "Optional",
            "type": "tagVARIANT",
        },
    },

    "returns_com": "tagVARIANT",

}

