dim_style_offset = {
    "input_folder_name": "Dimension_Methods",
    "input_file_name": "DimStyleOffset",
    "output_package_name": "dimension",
    "output_module_name": "dim_style_offset",

    "doc_html": """
        Returns or changes the extension line offset of a dimension style.
    """,

    "syntax_html": {
        0: ("strDimStyle", "dblOffset"),
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
            "name": "dblOffset",
            "py_name": "offset",
            "opt_or_req": "Optional",
            "type": "Number",
            "name_prefix": "dbl",
            "name_main": "Offset",
            "doc": """
        The new extension line offset.  If omitted, the current extension line offset is returned.
            """
        },
    },

    "returns_html": {
        0: {
            "type": "number",
            "doc": "If an offset is not specified, the current extension line offset if successful."
        },
        1: {
            "type": "number",
            "doc": "If an offset is specified, the previous extension line offset if successful."
        },
        2: {
            "type": "null",
            "doc": "If not successful, or on error."
        },
    },

    "id_com": 467,

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

