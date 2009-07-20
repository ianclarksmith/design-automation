dimension_user_text = {
    "module_name": "dimension",
    "class_name": "Dimension",
    "method_name": "dimension_user_text",

    "doc_html": """
        Returns or modifies the user text string of a dimension object. The user text is the string that gets printed when the dimension is drawn. If it contains the token "<>", then the token is replaced with the measured value of the dimension, formatted according to the dimension style settings. Note,  "<>" is the default user text string for linear dimensions.
    """,

    "syntax_html": """
        Rhino.DimensionUserText (strObject [, strUserText])
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
            "name": "UserText",
            "opt_or_req": "Optional",
            "type": "String",
            "type_string": "str",
            "doc": """
        The new user text string value. To reset the use text string, use the string "<>".
            """
        },
    },

    "returns_html": {
        0: {
            "type": "string",
            "doc": "If strUserText is not specified, then the current user text string if successful."
        },
        1: {
            "type": "string",
            "doc": "If strUserText is specified, then the previous user text string if successful."
        },
        2: {
            "type": "null",
            "doc": "On error."
        },
    },

    "id_com": 563,

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

