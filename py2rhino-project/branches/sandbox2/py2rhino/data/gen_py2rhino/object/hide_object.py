hide_object = {
    "module_name": "object",
    "class_name": "Object",
    "method_name": "hide_object",

    "doc_html": """
        Hides a single object.  Hidden objects are not visible, cannot be snapped to, and cannot be selected.
    """,

    "syntax_html": """
        Rhino.HideObject (strObject)
    """,

    "params_html": {
        0: {
            "name": "Object",
            "opt_or_req": "Required",
            "type": "String",
            "type_string": "str",
            "doc": """
        The identifier of the object to hide.
            """
        },
    },

    "returns_html": {
        0: {
            "type": "boolean",
            "doc": "True or false indicating success or failure."
        },
        1: {
            "type": "null",
            "doc": "On error."
        },
    },

    "id_com": 187,

    "params_com": {
        0: {
            "name": "vaObject",
            "opt_or_req": "Required",
            "type": "tagVARIANT",
        },
    },

    "returns_com": "tagVARIANT",

}

