leader_text = {
    "input_folder_name": "Dimension_Methods",
    "input_file_name": "LeaderText",
    "output_package_name": "dimension",
    "output_module_name": "leader_text",

    "doc_html": """
        Returns or modifies the text string of a dimension leader object.
    """,

    "syntax_html": """
        Rhino.LeaderText (strObject [, strText])
    """,

    "params_html": {
        0: {
            "name": "Object",
            "opt_or_req": "Required",
            "type": "String",
            "type_string": "str",
            "doc": """
        The object's identifier.
            """
        },
        1: {
            "name": "Text",
            "opt_or_req": "Optional",
            "type": "String",
            "type_string": "str",
            "doc": """
        The new text string value.
            """
        },
    },

    "returns_html": {
        0: {
            "type": "string",
            "doc": "If strText is not specified, then the current text string if successful."
        },
        1: {
            "type": "string",
            "doc": "If strText is specified, then the previous text string if successful."
        },
        2: {
            "type": "null",
            "doc": "On error."
        },
    },

    "id_com": 895,

    "params_com": {
        0: {
            "name": "vaObject",
            "opt_or_req": "Required",
            "type": "tagVARIANT",
        },
        1: {
            "name": "vaText",
            "opt_or_req": "Optional",
            "type": "tagVARIANT",
        },
    },

    "returns_com": "tagVARIANT",

}

