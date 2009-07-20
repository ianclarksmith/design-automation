dim_style_offset = {
    "module_name": "dimension",
    "class_name": "Dimension",
    "method_name": "dim_style_offset",

    "doc_html": """
        Returns or changes the extension line offset of a dimension style.
    """,

    "syntax_html": """
        Rhino.DimStyleOffset (strDimStyle [, dblOffset])
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
            "name": "Offset",
            "opt_or_req": "Optional",
            "type": "Number",
            "type_string": "dbl",
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

