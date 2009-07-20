is_layout_object = {
    "module_name": "object",
    "class_name": "Object",
    "method_name": "is_layout_object",

    "doc_html": """
        Verifies that an object is in either page layout space or model space.
    """,

    "syntax_html": """
        Rhino.IsLayoutObject (strObject)
    """,

    "params_html": {
        0: {
            "name": "Object",
            "opt_or_req": "Required",
            "type": "String",
            "type_string": "str",
            "doc": """
        The identifier of an object.
            """
        },
    },

    "returns_html": {
        0: {
            "type": "null",
            "doc": "On error."
        },
    },

    "id_com": 919,

    "params_com": {
        0: {
            "name": "vaObject",
            "opt_or_req": "Required",
            "type": "tagVARIANT",
        },
    },

    "returns_com": "tagVARIANT",

}

