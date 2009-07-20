text_dot_text = {
    "module_name": "geometry",
    "class_name": "Geometry",
    "method_name": "text_dot_text",

    "doc_html": """
        Returns or modifies the text string of an annotation text dot object.  Annotation dots can be created using Rhino's Dot command.
    """,

    "syntax_html": """
        Rhino.TextDotText (strObject [, strText])
    """,

    "params_html": {
        0: {
            "name": "Object",
            "opt_or_req": "Required",
            "type": "String",
            "type_string": "str",
            "doc": """
        The identifier of the object.
            """
        },
        1: {
            "name": "Text",
            "opt_or_req": "Optional",
            "type": "String",
            "type_string": "str",
            "doc": """
        A new character or text string.
            """
        },
    },

    "returns_html": {
        0: {
            "type": "string",
            "doc": "If a new text string is not specified,  the current string value if successful."
        },
        1: {
            "type": "string",
            "doc": "If a new text string is specified,  the previous string value if successful."
        },
        2: {
            "type": "null",
            "doc": "If not successful, or on error."
        },
    },

    "id_com": 421,

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

