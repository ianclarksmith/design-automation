dim_style_arrow_size = {
    "module_name": "dimension",
    "class_name": "Dimension",
    "method_name": "dim_style_arrow_size",

    "doc_html": """
        Returns or changes the arrow size of a dimension style.
    """,

    "syntax_html": """
        Rhino.DimStyleArrowSize (strDimStyle [, dblSize])
    """,

    "params_html": {
        0: {
            "name": "DimStyle",
            "opt_or_req": "Required",
            "type": "String",
            "type_string": "str",
            "doc": """
        The name of an existing dimension style.
            """
        },
        1: {
            "name": "Size",
            "opt_or_req": "Optional",
            "type": "Number",
            "type_string": "dbl",
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

